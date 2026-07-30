import streamlit as st

from src.rag_pipeline import answer_question
from src.upload import save_uploaded_files
from src.add_document import add_document
from pathlib import Path

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Engineering AI Copilot",
    page_icon="⚙️",
    layout="wide"
)

st.sidebar.title("⚙️ Engineering AI Copilot")

st.sidebar.markdown("---")

st.sidebar.subheader("✨ Features")

st.sidebar.write("• Semantic Search")
st.sidebar.write("• Multi-PDF Support")
st.sidebar.write("• Source Citations")
st.sidebar.write("• Conversation Memory")

st.sidebar.subheader("📄 Loaded Documents")

docs = sorted(Path("data/documents").glob("*.pdf"))

for doc in docs:
    display_name = (Path(doc.name).stem.replace("_", " "))
    st.sidebar.write(f"• {display_name}")

st.title("⚙️ Engineering AI Copilot")
st.markdown("""
    Ask questions about your engineering reference documents using AI-powered semantic search.

    Upload engineering PDFs, then ask technical questions and receive answers with source citations.
""")

# --------------------------------------------------
# Upload PDFs
# --------------------------------------------------
st.sidebar.markdown("---")

uploaded_files = st.sidebar.file_uploader(
    "Upload Engineering PDFs",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:

    if st.sidebar.button("📚 Add PDFs"):

        saved = save_uploaded_files(uploaded_files)

        with st.spinner("Indexing new documents..."):

            for pdf in saved:
                add_document(pdf)

        st.success("Documents added successfully!")

        for pdf in saved:
            st.write(f"✅ {pdf.name}")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.caption(
    "Built with Streamlit, OpenAI, and ChromaDB."
)

# --------------------------------------------------
# Chat History
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input("Ask an engineering question...")

if question and question.strip():

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer, sources, distances = answer_question(question, st.session_state.messages)

        st.markdown(answer)

        # Show retrieved sources
        if sources:

            st.markdown("#### Sources")

            shown = {}

            for source, distance in zip(sources, distances):

                filename = source["source"]

                if filename not in shown:
                    shown[filename] = distance
                else:
                    shown[filename] = min(
                        shown[filename],
                        distance
                    )

            for filename, distance in sorted(
                shown.items(),
                key=lambda x: x[1]
            ):

                st.caption(
                    f"📄 {filename}"
                )

    # Save assistant response to chat history
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )