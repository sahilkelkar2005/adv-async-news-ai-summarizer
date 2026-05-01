import streamlit as st
import threading
import uuid
import time
from src.queue_system import task_queue, result_dict
from src.worker import start_worker

# Start worker threads once
if "worker_started" not in st.session_state:
    for _ in range(2):
        thread = threading.Thread(target=start_worker)
        thread.daemon = True
        thread.start()

    st.session_state.worker_started = True

st.title("📰 Advanced Async News Summarizer")

# Store request id
if "request_id" not in st.session_state:
    st.session_state.request_id = None

text = st.text_area("Enter news text")

if st.button("Summarize"):
    if text.strip() == "":
        st.warning("Enter text first")
    else:
        request_id = str(uuid.uuid4())
        st.session_state.request_id = request_id

        task_queue.put({
            "id": request_id,
            "text": text
        })

        st.info(f"Request ID: {request_id}")
        st.info("Processing asynchronously...")

# AUTO-REFRESH RESULT (THIS FIXES YOUR ISSUE)
if st.session_state.request_id:
    request_id = st.session_state.request_id

    if request_id in result_dict:
        st.success("Summary:")
        st.write(result_dict[request_id])
    else:
        st.warning("Still processing... auto refreshing")
        time.sleep(2)
        st.rerun()