<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Analysis Report</title>
    <!-- Bootstrap CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0c6b7;
        }
        .container {
            background: #fff;
            padding: 15px;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(188, 8, 8, 0.1);
            margin-top: 25px;
        }
        .summary p {
            font-size: 18px;
            margin-bottom: 15px;
        }
        .create {
            color: #28a745;
        }
        .update {
            color: #ffc107;
        }
        .delete {
            color: #dc3545;
        }
        .resources {
            display: none;
            animation: fadeIn 0.5s;
        }
        .toggle-btn {
            cursor: pointer;
            color: #040c16;
        }
        .toggle-btn:hover {
            text-decoration: underline;
        }
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .mb-4 {
            align-items: center;
            color: #040b64;
            box-shadow: 0 0 30px rgba(188, 8, 8, 0.1);
            background: #fff;
            padding: 5px;
            border-radius: 5px;
        }
        .mb-3 {
            color: #040b64;
            box-shadow: 0 0 30px rgba(188, 8, 8, 0.1);
            background: #fff;
            padding: 5px;
            border-radius: 5px;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center mb-4">Terraform Plan Analysis Report</h1>
        <div class="summary mb-4">
            <p>Total Resources: <strong>{{ report['Total Resources'] }}</strong></p>
            <p>Resources to be Created: <span class="create">{{ report['Resources to be Created'] }}</span></p>
            <p>Resources to be Updated: <span class="update">{{ report['Resources to be Updated'] }}</span></p>
            <p>Resources to be Deleted: <span class="delete">{{ report['Resources to be Deleted'] }}</span></p>
        </div>

        <div class="details">
            <h2 class="mb-4">Detailed Changes</h2>
            {% for change_type, resources in report['Detailed Changes'].items() %}
                {% if change_type != 'total_resources' %}
                    <div class="card mb-3">
                        <div class="card-header">
                            <h3 class="m-0">{{ change_type.capitalize() }}: {{ resources|length }}</h3>
                            <button class="btn btn-sm btn-info toggle-btn" onclick="toggleResources('{{ change_type }}')">
                                <i class="fas fa-chevron-down"></i> <b>Show/Hide</b>
                            </button>
                        </div>
                        <ul class="resources list-group list-group-flush" id="{{ change_type }}">
                            {% for resource in resources %}
                                <li class="list-group-item {{ change_type }}">
                                    <i class="fas fa-{{ 'plus-circle' if change_type == 'create' else 'edit' if change_type == 'update' else 'trash-alt' }}"></i>
                                    {{ resource['address'] }}
                                </li>
                            {% endfor %}
                        </ul>
                    </div>
                {% endif %}
            {% endfor %}
        </div>
    </div>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <script>
        function toggleResources(type) {
            var resources = document.getElementById(type);
            if (resources.style.display === "none" || resources.style.display === "") {
                resources.style.display = "block";
            } else {
                resources.style.display = "none";
            }
        }
    </script>
</body>
</html>
