from queue import Queue

# Task queue (Producer → Consumer)
task_queue = Queue()

# Result storage (UUID → result)
result_dict = {}

# Stats (for UI)
stats = {
    "cache_hits": 0,
    "cache_misses": 0,
    "requests_processed": 0
}