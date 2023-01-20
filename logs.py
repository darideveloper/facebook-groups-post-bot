import os
import logging

# logs to file
logging.basicConfig(filename='.log', format='%(asctime)s - %(filename)s (%(lineno)s) - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
