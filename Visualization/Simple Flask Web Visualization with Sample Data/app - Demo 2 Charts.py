from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

# Create temporary datasets
data1 = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Sales': [12, 19, 3, 5, 2, 3]
}
data2 = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Revenue': [1200, 1900, 300, 500, 200, 300]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# HTML template with embedded datasets
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
    <h1>Sales and Revenue Data</h1>
    <div class="chart-container">
        <canvas id="chart1"></canvas>
    </div>
    <div class="chart-container">
        <canvas id="chart2"></canvas>
    </div>
    <script>
        const ctx1 = document.getElementById('chart1').getContext('2d');
        const chart1 = new Chart(ctx1, {
            type: 'bar',
            data: {
                labels: {{ labels1|safe }},
                datasets: [{
                    label: 'Sales',
                    data: {{ data1|safe }},
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

        const ctx2 = document.getElementById('chart2').getContext('2d');
        const chart2 = new Chart(ctx2, {
            type: 'line',
            data: {
                labels: {{ labels2|safe }},
                datasets: [{
                    label: 'Revenue',
                    data: {{ data2|safe }},
                    borderColor: 'rgba(75, 192, 192, 1)',
                    fill: false,
                    tension: 0.1
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
    labels1 = df1['Month'].tolist()
    data1 = df1['Sales'].tolist()
    labels2 = df2['Month'].tolist()
    data2 = df2['Revenue'].tolist()
    return render_template_string(html_template, labels1=labels1, data1=data1, labels2=labels2, data2=data2)

if __name__ == '__main__':
    app.run(debug=True)
