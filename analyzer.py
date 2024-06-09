import json
from parserplan import parse_plan

def analyze_plan(file_path):
    analysis = parse_plan(file_path)
    
    total_resources = analysis['total_resources']
    created_resources = len(analysis['create'])
    updated_resources = len(analysis['update'])
    deleted_resources = len(analysis['delete'])
    
    report = {
        'Total Resources': total_resources,
        'Resources to be Created': created_resources,
        'Resources to be Updated': updated_resources,
        'Resources to be Deleted': deleted_resources,
        'Detailed Changes': analysis
    }
    
    return report

if __name__ == '__main__':
    plan_file = 'plan.json'
    analysis_report = analyze_plan(plan_file)
    print(json.dumps(analysis_report, indent=4))