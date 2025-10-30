import streamlit as st
import requests

# ======================
# 🧠 Configuration
# ======================
import os
API_KEY = os.getenv("GROQ_API_KEY")

API_URL = "https://api.groq.com/openai/v1/chat/completions"

# ======================
# ✨ Helper Function
# ======================
def rewrite_text(text, tone):
    prompt = f"Rewrite this text in a {tone.lower()} tone:\n\n{text}"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
    "model": "llama-3.1-8b-instant",
    "messages": [
        {"role": "system", "content": "You are a helpful text rewriting assistant."},
        {"role": "user", "content": prompt}
    ]
}


    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code != 200:
        return f"⚠️ Error: {response.text}"
    
    result = response.json()
    return result["choices"][0]["message"]["content"]

# ======================
# 🌐 Streamlit UI
# ======================
st.set_page_config(page_title="AI Text Rewriter", page_icon="🪄")

st.title("🪄 AI Text Rewriter (Groq)")

st.write("Paste any text and choose a tone — AI will rewrite it instantly!")

text = st.text_area("Enter your text:", height=150)
tone = st.selectbox("Choose a tone:", ["Professional", "Friendly", "Funny", "Formal", "Casual", "Romantic"])

if st.button("✨ Rewrite Text"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Rewriting with Groq..."):
            result = rewrite_text(text, tone)
            st.success("✅ Done!")
            st.text_area("Rewritten Text:", result, height=150)
