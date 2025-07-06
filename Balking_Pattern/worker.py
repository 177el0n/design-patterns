import random
import time

def worker(processing, number_list):

    time.sleep(random.randint(1, 3))
    processing.add(number_list)
