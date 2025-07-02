import queue
import threading
from producer import producer
from consumer import consumer

def main():
    
    shared_queue = queue.Queue(maxsize=3)

    producer_thread = threading.Thread(target=producer, args=(shared_queue, 15))
    consumer_thread = threading.Thread(target=consumer, args=(shared_queue,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print("All tasks completed.")

if __name__ == "__main__":
    main()
