import streamlit as st
from src.summarizer import summarize

st.set_page_config(page_title="News AI Summarizer")

st.title("📰 News AI Summarizer")

user_input = st.text_area("Enter news text:")

if st.button("Summarize"):
    if user_input.strip():
        class Doc:
            def __init__(self, text):
                self.page_content = text

        docs = [Doc(user_input)]

        with st.spinner("Summarizing..."):
            result = summarize(docs)

        st.subheader("Summary")
        st.write(result)
    else:
        st.warning("Please enter some text.")