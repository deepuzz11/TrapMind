from flask import Flask, render_template, jsonify
import data_capture
import vulnerability_simulation
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_attack_data')
def get_attack_data():
    # Retrieve attack data from the simulated vulnerability
    attack_data = data_capture.capture_attack_data()
    return jsonify(attack_data)

@app.route('/simulate_vulnerability')
def simulate_vulnerability():
    # Simulate a vulnerability and return details
    vulnerability = vulnerability_simulation.simulate_vulnerability()
    logging.info(f"Simulated Vulnerability: {vulnerability}")
    return jsonify({"vulnerability": vulnerability})

if __name__ == '__main__':
    app.run(debug=True)
