import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)

logging.warning("This is a warning message")
logging.info("This is Info message")
logging.error("Error message")
