from flask import Flask, render_template, request
from analyzer import analyze_plan
from parserplan import generate_plan
from report import generate_report

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file.save('plan.json')
        plan_data = generate_plan('plan.json')
        analysis_result = analyze_plan(plan_data)
        report = generate_report(analysis_result,'templates/report.html')
        return render_template('report.html', report=report)
    
if __name__ == '__main__':
    app.run(debug=True)