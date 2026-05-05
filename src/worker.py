import threading
import hashlib
import time
from src.queue_system import task_queue, result_dict, stats
from src.cache import LRUCache
from src.rate_limiter import TokenBucket
from src.circuit_breaker import CircuitBreaker
from src.summarizer import summarize

cache = LRUCache(50)
rate_limiter = TokenBucket(rate=2, capacity=2)
circuit_breaker = CircuitBreaker()

def worker():
    while True:
        task_id, text = task_queue.get()

        try:
            # HASH for cache
            key = hashlib.sha256(text.encode()).hexdigest()

            # CACHE CHECK
            cached = cache.get(key)
            if cached:
                stats["cache_hits"] += 1
                result_dict[task_id] = cached
                continue

            stats["cache_misses"] += 1

            # RATE LIMIT
            while not rate_limiter.consume():
                time.sleep(0.5)

            # CIRCUIT BREAKER
            if not circuit_breaker.allow_request():
                result_dict[task_id] = "Service temporarily unavailable"
                continue

            # API CALL
            result = summarize(text)

            cache.put(key, result)
            circuit_breaker.record_success()

            result_dict[task_id] = result
            stats["requests_processed"] += 1

        except Exception:
            circuit_breaker.record_failure()
            result_dict[task_id] = "Error processing request"

        task_queue.task_done()

def start_workers(n=2):
    for _ in range(n):
        t = threading.Thread(target=worker, daemon=True)
        t.start()