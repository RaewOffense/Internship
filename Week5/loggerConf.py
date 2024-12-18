import logging
import logging.config

logging.config.fileConfig ("newFile.conf")

logger = logging.getLogger("simple message")

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')