from flask import Flask, request, jsonify
import requests
import uuid
import pyodbc
import os
import json

app = Flask(__name__)

DAPR_HTTP_PORT = os.getenv("DAPR_HTTP_PORT", 3501)
STATE_STORE_NAME = "statestore"
SQL_CONN = os.getenv(
    "SQL_CONN",
    "DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost,1433;DATABASE=orders;UID=sa;PWD=YourStrong!Passw0rd;TrustServerCertificate=yes;"
)

@app.route('/createOrder', methods=['POST'])
def create_order():
    order = {"id": str(uuid.uuid4()), **request.json}
    try:
        # Write to SQL
        with pyodbc.connect(SQL_CONN) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Orders (Id, Data) VALUES (?, ?)",
                order["id"],
                json.dumps(order)
            )
            conn.commit()

        # Persist to Redis via Dapr state API
        requests.post(
            f"http://localhost:{DAPR_HTTP_PORT}/v1.0/state/{STATE_STORE_NAME}",
            json=[{"key": f"order-{order['id']}", "value": order}]
        )

        return jsonify(order), 201
    except Exception as err:
        return jsonify({"error": str(err)}), 500

if __name__ == "__main__":
    app.run(port=4000)
