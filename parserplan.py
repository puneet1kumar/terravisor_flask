import json

def parse_plan(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    resources = data.get('resource_changes', [])
    analysis = {
        'create': [],
        'update': [],
        'delete': [],
        'total_resources': len(resources)
    }

    for resource in resources:
        change = resource['change']['actions'][0]
        if change == 'create':
            analysis['create'].append(resource)
        elif change == 'update':
            analysis['update'].append(resource)
        elif change == 'delete':
            analysis['delete'].append(resource)

    return analysis