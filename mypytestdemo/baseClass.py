import inspect
import logging

class baseClass:
    def getlogger(self):
        logname = inspect.stack()[1][3]  # for log correct method name in log file
        logger = logging.getLogger(logname)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

