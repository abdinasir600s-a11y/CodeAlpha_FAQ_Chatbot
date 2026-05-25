from html import escape

import streamlit as st

from chatbot import get_bot_response
from faq_data import FAQ_DATA


SAMPLE_QUESTIONS = [
    "What documents are required for admission?",
    "How can I apply for a scholarship?",
    "When is the application deadline?",
    "Can international students apply?",
    "Do I need English proficiency proof?",
    "How can I check my application status?",
]


def add_custom_styles():
    """Add simple CSS for a clean light Streamlit interface."""
    st.markdown(
        """
        <style>
        :root {
            --app-bg: #f8fafc;
            --card-bg: #ffffff;
            --app-text: #0f172a;
            --muted-text: #475569;
            --soft-border: #e2e8f0;
            --button-blue: #2563eb;
            --button-hover: #1d4ed8;
        }

        html,
        body,
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        .stApp {
            background: var(--app-bg) !important;
            color: var(--app-text) !important;
            font-family: "Inter", "Segoe UI", Arial, sans-serif;
        }

        header[data-testid="stHeader"] {
            background: var(--app-bg) !important;
            border-bottom: 1px solid var(--soft-border);
        }

        header[data-testid="stHeader"] button,
        header[data-testid="stHeader"] a,
        [data-testid="stToolbar"] {
            display: none !important;
        }

        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"] {
            color: var(--app-text) !important;
        }

        .main .block-container {
            max-width: 980px;
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }

        .app-header {
            background: var(--card-bg);
            border: 1px solid var(--soft-border);
            border-radius: 8px;
            margin-bottom: 1rem;
            padding: 1rem;
        }

        .app-header h1 {
            color: var(--app-text);
            font-size: 2rem;
            margin-bottom: 0.25rem;
        }

        .subtitle {
            color: var(--button-blue);
            font-size: 1.05rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .description {
            color: var(--muted-text);
            font-size: 1rem;
        }

        div[data-testid="stForm"] {
            background: var(--card-bg);
            border: 1px solid var(--soft-border);
            border-radius: 8px;
            margin-bottom: 1rem;
            padding: 1rem 1rem 0.35rem 1rem;
        }

        div[data-testid="stForm"] label {
            color: var(--app-text) !important;
            font-weight: 600;
        }

        .stTextInput input {
            background: var(--card-bg);
            border: 1px solid var(--soft-border);
            border-radius: 6px;
            color: var(--app-text);
        }

        .stTextInput input::placeholder {
            color: #94a3b8;
            opacity: 1;
        }

        .stTextInput input:focus {
            border-color: var(--button-blue);
            box-shadow: 0 0 0 1px var(--button-blue);
        }

        div[data-testid="stFormSubmitButton"] button,
        div[data-testid="stButton"] button {
            background: var(--button-blue);
            border: 1px solid var(--button-blue);
            border-radius: 6px;
            color: #ffffff;
            font-weight: 700;
            min-height: 2.6rem;
        }

        div[data-testid="stFormSubmitButton"] button *,
        div[data-testid="stButton"] button * {
            color: #ffffff !important;
        }

        div[data-testid="stFormSubmitButton"] button:hover,
        div[data-testid="stButton"] button:hover {
            background: var(--button-hover);
            border-color: var(--button-hover);
            color: #ffffff;
        }

        div[data-testid="stFormSubmitButton"] button:focus,
        div[data-testid="stButton"] button:focus {
            box-shadow: 0 0 0 2px rgba(96, 165, 250, 0.45);
            color: #ffffff;
        }

        .chat-card {
            background: var(--card-bg);
            border: 1px solid var(--soft-border);
            border-radius: 8px;
            margin: 0.85rem 0;
            padding: 1rem;
        }

        .user-question {
            color: var(--button-hover);
            font-weight: 600;
            margin-bottom: 0.75rem;
        }

        .bot-answer {
            color: var(--app-text);
            line-height: 1.55;
            margin-bottom: 0.9rem;
        }

        .meta-row {
            border-top: 1px solid var(--soft-border);
            color: var(--muted-text);
            font-size: 0.92rem;
            padding-top: 0.7rem;
        }

        .status {
            border-radius: 6px;
            display: inline-block;
            font-size: 0.82rem;
            font-weight: 700;
            margin-bottom: 0.75rem;
            padding: 0.25rem 0.55rem;
        }

        .status-confident {
            background: #dcfce7;
            border: 1px solid #bbf7d0;
            color: #166534;
        }

        .status-fallback {
            background: #fef3c7;
            border: 1px solid #fde68a;
            color: #92400e;
        }

        section[data-testid="stSidebar"],
        section[data-testid="stSidebar"] > div,
        div[data-testid="stSidebar"] {
            background: var(--app-bg) !important;
            border-right: 1px solid var(--soft-border);
            color: var(--app-text) !important;
        }

        section[data-testid="stSidebar"] * {
            color: var(--app-text);
        }

        section[data-testid="stSidebar"] button,
        section[data-testid="stSidebar"] button * {
            color: #ffffff !important;
        }

        div[data-testid="stSidebar"] h1,
        div[data-testid="stSidebar"] h2,
        div[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: var(--app-text);
        }

        div[data-testid="stSidebar"] p,
        div[data-testid="stSidebar"] li,
        div[data-testid="stSidebar"] .stMarkdown,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] li,
        section[data-testid="stSidebar"] .stMarkdown {
            color: var(--muted-text);
        }

        section[data-testid="stSidebar"] hr {
            border-color: var(--soft-border);
        }

        .sidebar-note {
            background: var(--card-bg);
            border: 1px solid var(--soft-border);
            border-radius: 8px;
            color: var(--app-text);
            margin-bottom: 1rem;
            margin-top: 0.8rem;
            padding: 0.75rem;
        }

        .history-title {
            color: var(--app-text);
            margin-top: 0.5rem;
        }

        div[data-testid="stAlert"] {
            background: var(--card-bg);
            border: 1px solid var(--soft-border);
            color: var(--app-text) !important;
        }

        div[data-testid="stAlert"] * {
            color: var(--app-text) !important;
        }

        div[data-testid="stAlert"][kind="warning"] {
            background: #fffbeb;
            border: 1px solid #fde68a;
        }

        div[data-testid="stAlert"][kind="warning"] * {
            color: #713f12 !important;
        }

        div[data-testid="stAlert"][kind="info"] {
            background: #eff6ff;
            border: 1px solid #bfdbfe;
        }

        div[data-testid="stAlert"][kind="info"] * {
            color: #1e3a8a !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def initialize_session_state():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def save_chat(user_question, bot_response):
    st.session_state.chat_history.insert(
        0,
        {
            "question": user_question,
            "response": bot_response,
        },
    )


def show_sidebar():
    with st.sidebar:
        st.header("Sample Questions")

        for question in SAMPLE_QUESTIONS:
            st.write(f"- {question}")

        st.divider()
        st.markdown(
            f"""
            <div class="sidebar-note">
                FAQ dataset contains <strong>{len(FAQ_DATA)}</strong>
                admission questions.
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.success("Chat history cleared.")


def show_header():
    st.markdown(
        """
        <div class="app-header">
            <h1>CodeAlpha FAQ Chatbot</h1>
            <div class="subtitle">
                Artificial Intelligence Internship - Task 2
            </div>
            <div class="description">
                Ask university admission related questions and get answers using
                an NLP-based FAQ matching chatbot.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def build_meta_details(response, status_text):
    if response["is_confident"]:
        matched_question = escape(response["matched_question"])
        category = escape(response["category"])

        return (
            f"<strong>Matched FAQ:</strong> {matched_question}<br>"
            f"<strong>Category:</strong> {category}<br>"
            f"<strong>Confidence Score:</strong> {response['confidence_score']:.2f}<br>"
            f"<strong>Status:</strong> {status_text}"
        )

    return (
        f"<strong>Confidence Score:</strong> {response['confidence_score']:.2f}<br>"
        f"<strong>Status:</strong> {status_text}"
    )


def show_chat_card(chat_item):
    response = chat_item["response"]
    status_class = "status-confident" if response["is_confident"] else "status-fallback"
    status_text = (
        "Confident answer"
        if response["is_confident"]
        else "No confident FAQ match found"
    )
    question = escape(chat_item["question"])
    answer = escape(response["answer"])
    meta_details = build_meta_details(response, status_text)

    chat_card_html = (
        '<div class="chat-card">'
        f'<div class="user-question">You: {question}</div>'
        f'<div class="status {status_class}">{status_text}</div>'
        f'<div class="bot-answer">Chatbot: {answer}</div>'
        f'<div class="meta-row">{meta_details}</div>'
        "</div>"
    )

    st.markdown(chat_card_html, unsafe_allow_html=True)


def run_app():
    st.set_page_config(
        page_title="CodeAlpha FAQ Chatbot",
        page_icon="chat",
        layout="wide",
    )

    add_custom_styles()
    initialize_session_state()
    show_sidebar()
    show_header()

    with st.form("question_form", clear_on_submit=True):
        user_question = st.text_input(
            "Ask a university admission question",
            placeholder="Example: What documents are required for admission?",
        )
        submitted = st.form_submit_button("Ask Chatbot", use_container_width=True)

    if submitted:
        if not user_question.strip():
            st.warning("Please enter a question before asking the chatbot.")
        else:
            bot_response = get_bot_response(user_question)
            save_chat(user_question, bot_response)

    st.markdown('<h3 class="history-title">Chat History</h3>', unsafe_allow_html=True)

    if st.session_state.chat_history:
        for chat_item in st.session_state.chat_history:
            show_chat_card(chat_item)
    else:
        st.info("Ask a question to start the chat.")
