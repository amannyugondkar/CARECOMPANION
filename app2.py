import streamlit as st
from login import login_page  # Import the login function from login.py
from io import BytesIO
import zipfile
import requests
from pathlib import Path
from functions.KeywordExtraction import MedicalKeywordProcessor

# 🚀 Set page configuration
st.set_page_config(page_title="Care Companion", page_icon="💙", layout="wide")

# 🔐 Check if user is logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    login_page()  
    st.stop()  

# 🎨 Sidebar Navigation
st.sidebar.title("🔹 Care Companion")
page = st.sidebar.radio("Select a Feature", ["Home 🏠", "Unstructured to Structured 🔄", "Keyword Extraction 🔍", "Text Summarization & Translation 📜🌐", "Chatbot 🤖"])

# 🏠 Home Page
if page == "Home 🏠":
    st.title("🏥 Welcome to Care Companion!")
    st.subheader("Your AI-powered assistant for medical text processing. 🚀")
    st.write("Empowering healthcare with AI-driven solutions for better insights and analysis.")

    st.markdown("### 🔥 Why Care Companion?")
    st.write("""
    ✅ Extract *meaningful information* from raw text  
    ✅ Find *important keywords* in large medical documents  
    ✅ Summarize *long reports* into easy-to-read summaries  
    ✅ Chat with AI for quick medical insights! 🤖  
    """)
    st.info("💡 Knowledge Box: AI is transforming healthcare, reducing paperwork, and enhancing diagnostics!")
    st.image("https://source.unsplash.com/800x400/?medical,AI", caption="AI in Healthcare", use_column_width=True)

# 📜 Feature 2 & 3 Combined: Text Summarization & Translation
elif page == "Text Summarization & Translation 📜🌐":
    st.title("📜🌐 Medical Text Summarization & Translation")

    # Input text area for user input
    text_input = st.text_area("📝 Enter medical text to summarize:", height=200)

    if st.button("Generate Summary"):
        if text_input:
            from functions.Summarization import MedicalSummary
            summarizer = MedicalSummary()
            summary = summarizer.summarize_text(text_input)
            st.session_state.current_summary = summary
            st.success("✅ Summary generated successfully!")
            st.write("### Summary:")
            st.write(summary)
        else:
            st.error("❌ No input provided. Please enter medical text.")

    # Translation Section
    st.write("\n")
    st.write("🌐 Translate the generated summary into different languages.")

    target_language = st.selectbox(
        "Select target language",
        ['gujarati', 'hindi', 'marathi'],
        format_func=lambda x: x.capitalize()
    )

    if st.button("Translate Summary"):
        if 'current_summary' in st.session_state and st.session_state.current_summary:
            from functions.Translation import translate_medical_summary
            translation_result = translate_medical_summary(
                st.session_state.current_summary,
                target_language
            )
            if translation_result['status'] == 'success':
                st.success("✅ Translation completed!")
                st.write("### Original Summary:")
                st.write(translation_result['original'])
                st.write("### Translated Summary:")
                st.write(translation_result['translated'])
            else:
                st.error("❌ Translation failed. Please try again.")
        else:
            st.error("❌ No summary available to translate. Please generate a summary first.")

    st.info("💡 Tip: Translate summaries into Gujarati, Hindi, or Marathi for better understanding!")

# 🤖 Chatbot Feature
elif page == "Chatbot 🤖":
    st.title("🗣️ Care Companion Chatbot")
    st.write("💬 Ask me anything related to medical insights and reports!")

    # Chat history
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # User input
    user_input = st.text_input("🧑 You:")

    if user_input:
        from functions.Chatbot import CareCompanionChatbot
        chatbot = CareCompanionChatbot()
        response = chatbot.get_response(user_input)
        st.session_state['chat_history'].append((user_input, response))

    # Display chat history
    for user_msg, bot_response in st.session_state['chat_history']:
        st.markdown(f"**🧑 You:** {user_msg}")
        st.markdown(f"**🤖 CareBot:** {bot_response}")

    st.info("💡 Tip: The chatbot can answer medical queries, summarize reports, and suggest keywords!")

# 🎨 Footer
st.sidebar.markdown("---")
st.sidebar.write("💙 *Care Companion - AI for Healthcare!* 🚀")
