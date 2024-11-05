import time
import logging


class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        logging.info("Timer Started")
        logging.info(f"Timer is called by {__name__} module")
        return self

    def __exit__(self, execution_type=None, execution_value=None, execution_traceback=None):
        self.end_time = time.time()
        logging.info("Timer Stopped")
