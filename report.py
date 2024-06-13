import json
from analyzer import analyze_plan

def generate_report(analysis_report):
    report = []
    report.append("Terraform Plan Analysis Report")
    report.append("==============================")
    
    report.append(f"Total Resources: {analysis_report['Total Resources']}")
    report.append(f"Resources to be Created: {analysis_report['Resources to be Created']}")
    report.append(f"Resources to be Read: {analysis_report['Resources to be Read']}")
    report.append(f"Resources to be Updated: {analysis_report['Resources to be Updated']}")
    report.append(f"Resources to be Deleted: {analysis_report['Resources to be Deleted']}")
    report.append(f"No Operation Resources: {analysis_report['No Operation Resources']}")
    report.append(f"Resources with Delete and Create: {analysis_report['Resources with Delete and Create']}")
    report.append(f"Resources with Create and Delete: {analysis_report['Resources with Create and Delete']}")
    
    report.append("\nDetailed Changes:")
    for change_type, resources in analysis_report['Detailed Changes'].items():
        if change_type != 'total_resources':
            report.append(f"\n{change_type.replace('_', ' ').capitalize()}: {len(resources)}")
            for resource in resources:
                report.append(f"  - {resource['address']}")
    
    return "\n".join(report)

if __name__ == '__main__':
    plan_file = 'plan.json'
    analysis_report = analyze_plan(plan_file)
    detailed_report = generate_report(analysis_report)
    
    with open('analysis_report.txt', 'w') as file:
        file.write(detailed_report)
    
    print("Detailed report generated: analysis_report.txt")
