import streamlit as st
from src.summarizer import summarize

st.set_page_config(page_title="News AI Summarizer")

st.title("📰 News AI Summarizer")

text = st.text_area("Enter news text")

if st.button("Summarize"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        with st.spinner("Summarizing..."):
            result = summarize([text])
            st.success("Summary:")
            st.write(result)