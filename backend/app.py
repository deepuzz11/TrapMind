from flask import Flask, render_template
from database import get_attack_data
from alerts import send_alert
import logging

app = Flask(__name__)

@app.route('/')
def index():
    attack_data = get_attack_data()
    return render_template('index.html', attack_data=attack_data)

@app.route('/alert')
def alert():
    send_alert("Significant attack detected!")
    return "Alert Sent"

if __name__ == "__main__":
    app.run(debug=True)
