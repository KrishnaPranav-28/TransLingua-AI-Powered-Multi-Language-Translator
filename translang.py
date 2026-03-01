import streamlit as st
from googletrans import Translator
from dotenv import load_dotenv
import os

# Load environment variables (optional, for future API keys)
load_dotenv()

# Define the translation function using googletrans
def translate_text(text, source, target):
    lang_map = {
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Chinese": "zh-cn"
    }
    translator = Translator()
    result = translator.translate(text, src=lang_map[source], dest=lang_map[target])
    return result.text

# Streamlit UI
st.title("🌍 AI-Powered Language Translator")
st.caption("Translate text between multiple languages using Google Gemini")

text = st.text_area("📝 Enter text to translate:")

source_language = st.selectbox(
    "🌍 Select source language:",
    ["English", "Spanish", "French", "German", "Chinese"]
)

target_language = st.selectbox(
    "🌐 Select target language:",
    ["English", "Spanish", "French", "German", "Chinese"]
)

# Translate button
if st.button("🔄 Translate"):
    if text and source_language and target_language:
        try:
            translated_text = translate_text(
                text, source_language, target_language
            )
            st.subheader("✨ Translated Text:")
            st.success(translated_text)   # ✅ shows the translated text clearly
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
    else:
        st.warning("⚠️ Please fill in all fields.")