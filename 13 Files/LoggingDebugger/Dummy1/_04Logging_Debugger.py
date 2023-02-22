import logging
logging.basicConfig(filename='dummy1.log', level=logging.INFO)
logging.info("This is information")
logging.info("This is information2")
logging.debug("This is debug")
logging.warning("This is warning")
logging.critical("This is critical")
logging.error("This is error")
logging.shutdown()
