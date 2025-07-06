import threading
from fibonacci_number import FibonacciNumber
from worker import worker

def main():

    number_list = []
    threads = []
    processing = FibonacciNumber()

    for i in range(5):
        thread = threading.Thread(target=worker, name=f"worker-{i}", args=(processing, number_list))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Final list of fibonacci numbers: {number_list}")

if __name__ == "__main__":
    main()
