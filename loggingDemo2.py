import logging

logging.basicConfig(filename="C://Users/HP/Google Drive/Learning/Selenium/seleniumLogs/test1.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is debug message")
logger.info("This is info message")

logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")
