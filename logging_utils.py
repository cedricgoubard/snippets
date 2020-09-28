"""
Logging functions
-----------------

A few functions to simplify the use of python's logging module.
"""
import logging


def setup_loggers(file_path=None):
    logger = logging.getLogger("keleven")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

    if file_path:
        handler = logging.FileHandler(file_path)
    else:
        handler = logging.StreamHandler()
    
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
