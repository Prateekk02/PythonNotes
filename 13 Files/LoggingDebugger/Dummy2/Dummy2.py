import logging
logging.basicConfig(filename="Dummy2.log", level= logging.DEBUG, format='%(asctime)s, %(message)s')
logging.info("This is info")
logging.error("This is error")
logging.warning("This is warning")
logging.shutdown()