import logging

logging.basicConfig(filename="C://Users/HP/Google Drive/Learning/Selenium/seleniumLogs/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

logging.debug("This is debug message")
logging.info("This is info message")

logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")
