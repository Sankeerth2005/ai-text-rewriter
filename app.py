'''import streamlit as st
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
   
result = rewrite_text(text,             st.text_area("Rewritten Text:", result, height=150)'''

import streamlit as st
import requests
import os
from datetime import datetime

# ======================
# 🧠 Configuration
# ======================
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
st.set_page_config(page_title="AI Text Rewriter", page_icon="🪄", layout="wide")

# Sidebar
st.sidebar.title("⚙️ Settings")
st.sidebar.markdown("Select your preferred tone and theme.")
tone = st.sidebar.selectbox("🗣️ Choose a tone", [
    "✨ Professional", "😄 Friendly", "😂 Funny", "🎓 Formal", "💬 Casual", "❤️ Romantic"
])
st.sidebar.markdown("---")
st.sidebar.write("Made with ❤️ by Sankeerth")

# Main Layout
st.title("🪄 AI Text Rewriter")
st.write("Give your writing a fresh tone — from professional to playful, instantly!")

# Input area
text = st.text_area("📝 Enter your text below:", height=180, placeholder="Type or paste your text here...")

# Word count
if text:
    st.caption(f"📏 Word count: {len(text.split())}")

# Rewrite button
if st.button("✨ Rewrite Text", use_container_width=True):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Rewriting with Groq magic 🧠..."):
            result = rewrite_text(text, tone)
            if "⚠️" in result:
                st.error(result)
            else:
                st.success("✅ Text rewritten successfully!")
                st.text_area("🔁 Rewritten Text:", result, height=180)
                st.download_button("💾 Download as .txt", data=result, file_name="rewritten_text.txt")

                # Save to session history
                if "history" not in st.session_state:
                    st.session_state.history = []
                st.session_state.history.append({
                    "timestamp": datetime.now().strftime("%H:%M:%S"),
                    "tone": tone,
                    "input": text,
                    "output": result
                })

# Show history
if "history" in st.session_state and st.session_state.history:
    with st.expander("🕒 View Rewrite History"):
        for h in reversed(st.session_state.history[-5:]):
            st.markdown(f"**[{h['timestamp']}] {h['tone']}**")
            st.markdown(f"📝 *Original:* {h['input']}")
            st.markdown(f"🔁 *Rewritten:* {h['output']}")
            st.markdown("---")

