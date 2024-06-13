import json

def parse_plan(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    resources = data.get('resource_changes', [])
    analysis = {
        'no-op': [],
        'create': [],
        'read': [],
        'update': [],
        'delete': [],
        'delete_create': [],  # This is for ["delete", "create"]
        'create_delete': [],  # This is for ["create", "delete"]
        'total_resources': len(resources)
    }

    for resource in resources:
        change = resource['change']['actions']
        if change == ["no-op"]:
            analysis['no-op'].append(resource)
        elif change == ["create"]:
            analysis['create'].append(resource)
        elif change == ["read"]:
            analysis['read'].append(resource)
        elif change == ["update"]:
            analysis['update'].append(resource)
        elif change == ["delete"]:
            analysis['delete'].append(resource)
        elif change == ["delete", "create"]:
            analysis['delete_create'].append(resource)
        elif change == ["create", "delete"]:
            analysis['create_delete'].append(resource)

    return analysis
