from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

# Create a temporary dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Sales': [12, 19, 3, 5, 2, 3]
}
df = pd.DataFrame(data)

# HTML template with embedded dataset
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Chart Example</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        .chart-container {
            width: 50%;
            margin: auto;
        }
    </style>
</head>
<body>
    <h1>Sales Data</h1>
    <div class="chart-container">
        <canvas id="myChart"></canvas>
    </div>
    <script>
        const ctx = document.getElementById('myChart').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: {{ labels|safe }},
                datasets: [{
                    label: 'Sales',
                    data: {{ data|safe }},
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    labels = df['Month'].tolist()
    data = df['Sales'].tolist()
    return render_template_string(html_template, labels=labels, data=data)

if __name__ == '__main__':
    app.run(debug=True)