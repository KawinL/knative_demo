import time
import os
import logging
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


TIME_TO_DIE = os.environ.get('TIME_TO_DIE', 1)
I_HAVE_TO_DIE = os.environ.get('I_HAVE_TO_DIE', "yes")


def main():
    logger.info("I'm alive")

    time_to_die = int(TIME_TO_DIE)

    while True:
        time.sleep(1)
        time_to_die -= 1
        logger.info("I'm alive for %s seconds", time_to_die)
        if time_to_die == 0 and I_HAVE_TO_DIE == "yes":
            if random.random() < 0.1:
                raise Exception("I'm dead")
            else:
                time_to_die = int(TIME_TO_DIE)
                logger.info("I'm servived")
        

if __name__ == "__main__":
    main()



