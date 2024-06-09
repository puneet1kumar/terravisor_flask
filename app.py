from flask import Flask, render_template, request
from analyzer import analyze_plan

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'plan' not in request.files:
        return "No file part"
    
    file = request.files['plan']
    if file.filename == '':
        return "No selected file"
    
    file.save('plan.json')
    analysis_report = analyze_plan('plan.json')
    
    return render_template('report.html', report=analysis_report)

if __name__ == '__main__':
    app.run(debug=True)
