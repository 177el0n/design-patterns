import threading
import time
import random

class FibonacciNumber:

    def __init__(self):
        self._lock = threading.Lock()

    def add(self, list_of_numbers):

        thread_name = threading.current_thread().name
        print(f"current thread: {thread_name}")

        if not self._lock.acquire(blocking=False):
            print(f"{thread_name} is balking")
            return
        
        try:
            print(f"{thread_name} is calculating fibonacci numbers")
            if len(list_of_numbers) < 2:
                if len(list_of_numbers) == 0:
                    primary_number = 1
                    list_of_numbers.append(primary_number)
                primary_number = list_of_numbers[-1]
                list_of_numbers.append(primary_number)
            left = list_of_numbers[-2]
            right = list_of_numbers[-1]
            next_number = left + right
            list_of_numbers.append(next_number)

            time.sleep(random.randint(1, 3))

            print(f"{thread_name} added {next_number} to the list")
        finally:
            self._lock.release()
            print(f"{thread_name} released the lock")
