import logging
import random
import time

logger = logging.getLogger(__name__)
FORMAT = '%(levelname)s - %(message)s'

handler = logging.FileHandler(filename='battery_temperature.log', mode='w')
handler.setLevel(logging.WARNING)
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)

startat = time.time()
while True:
    temp = random.randint(20,40)
    message = f"{temp} C"
    print(f"At {time.ctime()} the temp was {message}")
# DEBUG = TEMPERATURE_IN_CELSIUS < 20
# WARNING = TEMPERATURE_IN_CELSIUS >= 30 AND TEMPERATURE_IN_CELSIUS <= 35
# CRITICAL = TEMPERATURE_IN_CELSIUS > 35
    if 20 < temp < 30:
        logger.debug(message)
    elif 30 <= temp <= 35:
        logger.warning(message)
    else:
        logger.critical(message)
    if time.time() - startat < 60:
        time.sleep(10)
    else:
        break
