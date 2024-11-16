import logging

def setup_logging():
    logging.basicConfig(filename='trapmind.log', level=logging.INFO,
                        format='%(asctime)s - %(message)s')

def log_event(message):
    logging.info(message)
