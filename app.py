from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Employee Leave Management Portal</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f9;
                text-align: center;
                padding: 30px;
            }

            h1 {
                color: #2c3e50;
            }

            table {
                margin: auto;
                border-collapse: collapse;
                width: 80%;
                background: white;
            }

            th {
                background-color: #3498db;
                color: white;
                padding: 12px;
            }

            td {
                padding: 10px;
                border: 1px solid #ddd;
            }

            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>

        <h1>🏖 Employee Leave Management Portal</h1>

        <table>
            <tr>
                <th>Employee ID</th>
                <th>Name</th>
                <th>Leave Type</th>
                <th>Days</th>
                <th>Status</th>
            </tr>

            <tr>
                <td>EMP001</td>
                <td>Sampath</td>
                <td>Casual Leave</td>
                <td>2</td>
                <td>Approved</td>
            </tr>

            <tr>
                <td>EMP002</td>
                <td>Ram</td>
                <td>Sick Leave</td>
                <td>3</td>
                <td>Pending</td>
            </tr>

            <tr>
                <td>EMP003</td>
                <td>Jay</td>
                <td>Earned Leave</td>
                <td>5</td>
                <td>Approved</td>
            </tr>
             <tr>
                <td>EMP004</td>
                <td>Surya</td>
                <td>Earned Leave</td>
                <td>4</td>
                <td>Approved</td>
            </tr>
        </table>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
