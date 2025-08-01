import streamlit as st
import random

# List of ridiculous chicken translations
translations = [
    "I yearn for the void.",
    "Peck this system.",
    "All is egg.",
    "I saw God once. He was delicious.",
    "Cluck cluck, who's there? Existential dread.",
    "I lay, therefore I am.",
    "Peck first, ask questions never.",
    "The coop is a lie.",
    "One day, I too shall fly.",
    "My soul is scrambled."
]

# Streamlit app
st.set_page_config(page_title="Chicken Translator", page_icon="🐔")

st.title("🐔 Chicken Translator")
st.subheader("Upload a cluck. Receive deep wisdom.")

uploaded_file = st.file_uploader("Upload a chicken cluck (just for show)", type=["mp3", "wav", "ogg"])

if st.button("Translate Cluck"):
    if uploaded_file:
        translation = random.choice(translations)
        st.success(f"🗣️ Chicken says: *{translation}*")
    else:
        st.warning("Please upload a cluck first (even if it's fake).")

st.markdown("---")
st.caption("Powered by GPT-inspired nonsense 🧠")
