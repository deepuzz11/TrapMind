# TrapMind - AI-Powered Dynamic Honeypot System

**TrapMind** is an AI-powered dynamic honeypot system designed to simulate vulnerabilities and attract attackers. The system adapts to attacker behavior, simulating vulnerabilities, logging interactions, and providing real-time alerts. It aims to enhance threat detection and analysis by analyzing attack patterns using machine learning.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Machine Learning Integration](#machine-learning-integration)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Structure

```
TrapMind/
│
├── backend/
│   ├── app.py              # Main application file using Flask to handle web requests and manage the honeypot environment
│   ├── models.py           # Define machine learning models for analyzing attacker behavior
│   ├── data_capture.py     # Logs interactions with the honeypot, capturing commands, network traffic, and file accesses
│   └── vulnerability_simulation.py  # Simulates various vulnerabilities to attract attackers
│
├── frontend/
│   ├── index.html          # Dashboard interface for visualizing real-time data
│   ├── styles.css          # Styles for the dashboard
│   └── dashboard.js        # JavaScript to handle dynamic data visualization and interactions on the dashboard
│
├── database/
│   ├── database.py         # Manages database connections and queries (using MySQL or MongoDB)
│   └── schema.sql          # SQL schema to set up the database structure (for MySQL)
│
├── ml/
│   ├── train_model.py      # Script to train machine learning models on captured data to identify attack patterns
│   └── predict_behavior.py  # Code for real-time prediction of attacker behavior based on trained models
│
├── alerts/
│   ├── alerts.py           # Handles incident alerts and notifications for security teams
│   └── logging.py          # Utility for logging events and errors throughout the application
│
├── tests/
│   └── test_app.py         # Unit tests to ensure the functionality of various components
│
├── requirements.txt        # List of dependencies for the project
└── README.md               # Documentation file (this file)
```

## Features

- **Vulnerability Simulation**: Simulates a variety of common vulnerabilities such as SQL Injection, XSS, Buffer Overflow, and more, to attract attackers.
- **Dynamic Honeypot**: Uses machine learning to adapt and change its simulated vulnerabilities based on attacker behavior.
- **Data Capture**: Logs all interactions, including commands, network traffic, and file accesses for analysis.
- **Machine Learning**: Analyzes attacker behavior patterns and provides predictions for real-time threat detection.
- **Real-Time Alerts**: Sends alerts to the security team when significant attacks or anomalies are detected.
- **Dashboard Interface**: Provides a web-based dashboard to visualize captured data and received alerts.
- **Logging and Monitoring**: Comprehensive logging of events and system errors for debugging and analysis.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/TrapMind.git
   cd TrapMind
   ```

2. **Install dependencies:**
   Make sure you have `pip` installed and then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database:**
   If using MySQL:
   - Create a MySQL database and run the schema to set up the tables:
   ```bash
   mysql -u yourusername -p yourdatabase < database/schema.sql
   ```

4. **Run the application:**
   For the backend, navigate to the `backend/` directory and run the Flask app:
   ```bash
   python app.py
   ```
   The application should now be accessible at `http://127.0.0.1:5000`.

5. **Frontend:**
   Open `frontend/index.html` in your browser to visualize the honeypot data and interact with the dashboard.

## Usage

1. **Simulate Vulnerabilities**: The `vulnerability_simulation.py` script will randomly simulate various vulnerabilities that attract attackers. These vulnerabilities can be customized or extended as needed.
   
2. **Capture Data**: All interactions with the honeypot (commands, traffic, etc.) will be logged by the `data_capture.py` module. The captured data is then stored in a database for analysis.

3. **Machine Learning**: The `train_model.py` script is used to train machine learning models using the captured data. These models can then be used for predicting attacker behavior in real time through `predict_behavior.py`.

4. **Alerts and Logging**: The `alerts.py` module sends notifications to security teams whenever an attack pattern is detected. These are logged in `logging.py`.

## Machine Learning Integration

The system integrates machine learning to identify and predict attacker behavior based on past interactions. The `train_model.py` script trains models using captured data, while `predict_behavior.py` applies the trained models to detect threats in real-time.

## Testing

Unit tests are available in the `tests/test_app.py` file. To run the tests:

```bash
pytest tests/test_app.py
```

Ensure the system is set up and running before performing tests.

## Technologies Used

- **Flask**: Web framework for backend implementation.
- **TensorFlow / Scikit-learn**: Machine learning models for attack detection.
- **MySQL / MongoDB**: Database for storing captured interactions and threat data.
- **HTML/CSS/JavaScript**: Frontend technologies for the dashboard.
- **Python**: Primary language for backend and machine learning components.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by modern cybersecurity practices involving honeypots and AI-based attack detection.
- Special thanks to the machine learning libraries used, such as TensorFlow and Scikit-learn, for their powerful models and algorithms.
