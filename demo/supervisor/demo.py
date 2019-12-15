import datetime
import time
import logging
logging.basicConfig(filename='demo.log',level=logging.DEBUG)
while True:
    time.sleep(3)
    logging.info("now time:{}".format(datetime.datetime.now()))
