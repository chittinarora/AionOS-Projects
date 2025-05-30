from transformers import pipeline
import streamlit as st

# Initialize summarizer (this uses GPU if available)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")

st.title("Text Summarization Tool")

# Text input from user
user_input = st.text_area("Enter text to summarize", height=200)

if st.button("Summarize"):
    if user_input.strip() == "":
        st.warning("Please enter some text to summarize!")
    else:
        max_len = max(30, min(150, len(user_input) // 2))
        summary = summarizer(user_input, max_length=max_len, min_length=20, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
        