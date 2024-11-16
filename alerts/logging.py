import logging

# Setup logging to capture events
logging.basicConfig(filename='honeypot_events.log', level=logging.DEBUG)

def log_event(message: str):
    """
    Log significant events such as detected attacks or system anomalies.
    """
    logging.debug(f"Event logged: {message}")
