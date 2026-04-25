import streamlit as st

from src.pdf_loader import load_pdf
from src.chunker import chunk_text
from src.embeddings import load_model, get_embeddings
from src.vectorstore import create_index
from src.retriever import retrieve
from src.llm import generate_answer

st.title("PDF Chatbot (RAG)")

if "ready" not in st.session_state:
    st.session_state.ready = False

if st.button("Process PDF"):
    text = load_pdf("data/sample.pdf")
    chunks = chunk_text(text)

    model = load_model()
    embeddings = get_embeddings(model, chunks)

    index = create_index(embeddings)

    st.session_state.model = model
    st.session_state.index = index
    st.session_state.chunks = chunks
    st.session_state.ready = True

    st.success("PDF processed!")

query = st.text_input("Ask a question")

if query and st.session_state.ready:
    context = retrieve(
        query,
        st.session_state.model,
        st.session_state.index,
        st.session_state.chunks
    )

    answer = generate_answer(query, context)

    st.write(answer)