import time
import random

def consumer(q):

    print("Consumer started")
    while True:
        data = q.get()
        if data is None:
            break

        print(f"Consumed: {data}({q.qsize()})")
        consumed_data = data ** 2
        time.sleep(random.randint(1, 5))
        print(f"Processed: {consumed_data}({q.qsize()})")
