<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HSI Smart Trader</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    body { font-family: Arial, sans-serif; padding: 20px; background-color: #f4f4f4; }
    h1 { color: #333; }
    #controls { margin-bottom: 20px; }
    button { margin-right: 10px; padding: 10px 20px; font-size: 16px; }
    #metrics { margin-top: 20px; font-size: 18px; }
    canvas { max-width: 100%; margin-top: 20px; }
    #summaryPopup { display: none; background: #fff; padding: 20px; border: 2px solid #444; position: fixed; top: 30%; left: 50%; transform: translate(-50%, -50%); z-index: 999; box-shadow: 0 0 10px rgba(0,0,0,0.3); }
    #overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 998; }
  </style>
</head>
<body>
  <h1>Hang Seng Index Smart Trader</h1>
  <div id="controls">
    <button onclick="startSimulation()">Start Simulation</button>
    <button onclick="startLive()">Start Live Trading</button>
    <button onclick="downloadCSV()">Download Log CSV</button>
  </div>
  <div id="metrics">
    <p><strong>Units Left:</strong> <span id="unitsLeft">100</span></p>
    <p><strong>Revenue:</strong> <span id="revenue">0.00</span></p>
  </div>
  <canvas id="revenueChart" height="100"></canvas>
  <canvas id="priceChart" height="100"></canvas>

  <div id="overlay"></div>
  <div id="summaryPopup">
    <h2>Trading Session Summary</h2>
    <p><strong>Total Revenue:</strong> <span id="finalRevenue"></span></p>
    <p><strong>Units Sold:</strong> <span id="finalUnits"></span></p>
    <button onclick="closePopup()">Close</button>
  </div>

  <script>
    let revenueChart, priceChart;
    let revenueData = [];
    let priceData = [];
    let labels = [];
    let latestLog = [];
    let tradingCompleted = false;

    function initCharts() {
      const ctx1 = document.getElementById('revenueChart').getContext('2d');
      revenueChart = new Chart(ctx1, {
        type: 'line',
        data: { labels: [], datasets: [{ label: 'Revenue', data: [], fill: false, borderColor: 'green' }] },
        options: { responsive: true }
      });

      const ctx2 = document.getElementById('priceChart').getContext('2d');
      priceChart = new Chart(ctx2, {
        type: 'line',
        data: { labels: [], datasets: [{ label: 'Price', data: [], fill: false, borderColor: 'blue' }] },
        options: { responsive: true }
      });
    }

    function updateCharts(log) {
      latestLog = log;
      revenueData = log.map(e => e.revenue);
      priceData = log.map(e => e.price);
      labels = log.map(e => e.time);

      revenueChart.data.labels = labels;
      revenueChart.data.datasets[0].data = revenueData;
      revenueChart.update();

      priceChart.data.labels = labels;
      priceChart.data.datasets[0].data = priceData;
      priceChart.update();
    }

    function pollStatus() {
      fetch('/status')
        .then(res => res.json())
        .then(data => {
          document.getElementById('unitsLeft').innerText = data.units_left;
          document.getElementById('revenue').innerText = data.revenue.toFixed(2);
          updateCharts(data.sell_log);

          if (!tradingCompleted && data.units_left === 0) {
            showSummary(data.revenue, 100);
            tradingCompleted = true;
          }
        });
    }

    function startSimulation() {
      fetch('/start_simulation')
        .then(res => res.json())
        .then(data => {
          console.log(data.status);
          tradingCompleted = false;
        });
    }

    function startLive() {
      fetch('/start_live')
        .then(res => res.json())
        .then(data => {
          console.log(data.status);
          tradingCompleted = false;
        });
    }

    function downloadCSV() {
      if (!latestLog.length) return;
      let csv = 'Time,Price,Units Sold,Revenue\n';
      latestLog.forEach(row => {
        csv += `${row.time},${row.price},${row.units},${row.revenue}\n`;
      });
      const blob = new Blob([csv], { type: 'text/csv' });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.setAttribute('hidden', '');
      a.setAttribute('href', url);
      a.setAttribute('download', 'trading_log.csv');
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }

    function showSummary(revenue, unitsSold) {
      document.getElementById('finalRevenue').innerText = revenue.toFixed(2);
      document.getElementById('finalUnits').innerText = unitsSold;
      document.getElementById('overlay').style.display = 'block';
      document.getElementById('summaryPopup').style.display = 'block';
    }

    function closePopup() {
      document.getElementById('overlay').style.display = 'none';
      document.getElementById('summaryPopup').style.display = 'none';
    }

    initCharts();
    setInterval(pollStatus, 2000);
  </script>
</body>
</html>
