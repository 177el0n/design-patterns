import time
import random

def producer(q, count):

    print("Producer started")
    for i in range(count):
        data = i

        time.sleep(random.randint(1, 5))

        q.put(data)
        print(f"Produced: {data}({q.qsize()})")
    q.put(None)
    print("Producer finished")
