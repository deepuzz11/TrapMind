import logging
import os
from datetime import datetime

# Setup logging to capture all data interactions
logging.basicConfig(filename='honeypot_data.log', level=logging.INFO)

def capture_command(command: str):
    """
    Captures commands issued by an attacker and logs them with timestamps.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"{timestamp} - Command Captured: {command}")

def capture_network_traffic(data: str):
    """
    Captures network traffic data (e.g., IP, ports, request type) and logs it.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"{timestamp} - Network Traffic: {data}")

def capture_file_access(file_path: str, access_type: str):
    """
    Captures file access data (e.g., read, write, delete operations) and logs it.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"{timestamp} - File Accessed: {file_path}, Type: {access_type}")
