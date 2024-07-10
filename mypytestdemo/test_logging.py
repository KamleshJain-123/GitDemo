import logging

def test_logging():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)

    logger.debug("debug")
    logger.info("inforrmation")
    logger.warning("warnning")
    logger.error("error")
    logger.critical("critical")
