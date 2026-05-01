from src.queue_system import task_queue, result_dict
from src.summarizer import summarize

def start_worker():
    print("✅ Worker started...")

    while True:
        task = task_queue.get()
        print("📩 Task received:", task)

        request_id = task["id"]
        text = task["text"]

        try:
            result = summarize([text])
            print("✅ Result generated")

            result_dict[request_id] = result

        except Exception as e:
            print("❌ ERROR:", e)
            result_dict[request_id] = f"Error: {str(e)}"

        task_queue.task_done()