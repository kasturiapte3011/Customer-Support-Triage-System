import streamlit as st
import requests

API_URL = "http://api:8000/ingest/chat"

st.set_page_config(page_title="Customer Support", page_icon="💬")

st.title("Customer Support")

st.write("Describe your issue below.")

message = st.text_area("Your message")

if st.button("Submit"):
    if not message.strip():
        st.error("Message cannot be empty")
    else:
        response = requests.post(
            API_URL,
            json={"message": message}
        )

        if response.status_code == 200:
            st.success(response.json()["message"])
        else:
            st.error("Something went wrong. Please try again.")
