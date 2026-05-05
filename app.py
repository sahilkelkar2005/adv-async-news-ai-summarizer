import streamlit as st
import uuid
from src.queue_system import task_queue, result_dict, stats
from src.worker import start_workers

# Page config
st.set_page_config(page_title="Advanced Async News Summarizer")

# Start workers ONLY ONCE
if "workers_started" not in st.session_state:
    start_workers(2)
    st.session_state.workers_started = True

st.title("📰 Advanced Async News Summarizer")

# Store request id
if "request_id" not in st.session_state:
    st.session_state.request_id = None

# Input
text = st.text_area("Enter news text")

# Submit
if st.button("Summarize"):
    if text.strip() == "":
        st.warning("Enter text first")
    else:
        request_id = str(uuid.uuid4())
        st.session_state.request_id = request_id

        # NEW FORMAT (tuple instead of dict)
        task_queue.put((request_id, text))

        st.info(f"Request ID: {request_id}")
        st.info("Processing asynchronously...")

# Result checking (NO infinite rerun loop)
if st.session_state.request_id:
    request_id = st.session_state.request_id

    if request_id in result_dict:
        st.success("Summary:")
        st.write(result_dict[request_id])
    else:
        st.warning("Still processing... click button again to refresh")

# 🔥 SYSTEM STATS (important for marks)
st.sidebar.title("📊 System Stats")
st.sidebar.write(f"Cache Hits: {stats['cache_hits']}")
st.sidebar.write(f"Cache Misses: {stats['cache_misses']}")
st.sidebar.write(f"Requests Processed: {stats['requests_processed']}")
st.sidebar.write(f"Queue Size: {task_queue.qsize()}")