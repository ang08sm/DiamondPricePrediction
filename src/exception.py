import sys
import os
import logging  # Import logging module

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import logger  

def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in script [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):

    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    logging.info("Logging has started")  

    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Division by zero occurred")
        raise CustomException(e, sys)