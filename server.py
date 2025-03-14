from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)
conn = mysql.connector.connect(host="localhost", user="root", password="password", database="ids_db")
cursor = conn.cursor(dictionary=True)

@app.route('/logs', methods=['GET'])
def get_logs():
    cursor.execute("SELECT * FROM intrusions ORDER BY timestamp DESC LIMIT 100")
    logs = cursor.fetchall()
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)
