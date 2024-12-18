# import logging method

import logging

#creating and configure logger
logging.basicConfig(filename="newFile.log", format= "%(asctime)s %(message)s",filemode="w")

#creating a object 
logger = logging.getLogger()

#setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#Test message 
logger.debug("Harmless debug message")
logger.info("Just a information")
logger.warning("Its a warning")
logger.error("Did you try to Divide by Zero")
logger.critical("Internet is down")
