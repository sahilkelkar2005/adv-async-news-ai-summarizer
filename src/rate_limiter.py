import time
import threading

class TokenBucket:
    def __init__(self, rate=5, capacity=5):
        self.tokens = capacity
        self.capacity = capacity
        self.rate = rate
        self.last_refill = time.time()
        self.lock = threading.Lock()

    def consume(self):
        with self.lock:
            now = time.time()
            elapsed = now - self.last_refill

            self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
            self.last_refill = now

            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False