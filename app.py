import streamlit as st
from pdf_processing import extract_text_from_file
from mcq_generation import generate_mcq

st.title("MCQ Generator")

option = st.radio("Choose an option:", ("Upload PDF", "Type a Topic"))

if option == "Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        text = extract_text_from_file(uploaded_file)
        st.subheader("Extracted Text:")
        st.write(text)

        if text:
            mcq = generate_mcq(text, api=None) 
            st.subheader("Generated MCQs:")
            st.write(mcq)

elif option == "Type a Topic":
    topic = st.text_input("Enter a topic to generate MCQs:")

    if topic:
        mcq = generate_mcq(topic, api=None)
        st.subheader("Generated MCQs:")
        st.write(mcq)
