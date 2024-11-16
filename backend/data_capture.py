import random
import logging

# Function to capture attack data
def capture_attack_data():
    attack_types = ["SQL Injection", "XSS", "Buffer Overflow", "Privilege Escalation"]
    attack_details = {
        "timestamp": "2024-11-16T12:34:56Z",
        "attack_type": random.choice(attack_types),
        "details": "Simulated attack attempt"
    }
    logging.info(f"Captured attack data: {attack_details}")
    return attack_details
