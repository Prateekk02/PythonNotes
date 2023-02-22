import logging
logging.basicConfig(filename='Dummy3.log', level=logging.DEBUG, format='%(asctime)s %(name)s %(message)s')
logging.info("This is my info logging")
logging.error("This is my error msg")
logging.critical("This is critical")
logging.shutdown()