import streamlit as st
from document_processor import index_file, query_documents

# ========================================
# STREAMLIT UI
# ========================================

st.title("📄 Cloud RAG AI Chatbot with Ollama")
st.markdown("Ask anything about your uploaded documents via Ollama Cloud!")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    
    if uploaded_file and st.button("Process Document"):
        chunks = index_file(uploaded_file)
        st.success(f"Indexed {chunks} chunks ✅")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.spinner("Ollama Cloud thinking..."):
        try:
            answer = query_documents(prompt)
            st.session_state.messages.append({"role": "assistant", "content": answer})
            with st.chat_message("assistant"):
                st.write(answer)
        except Exception as e:
            st.error(f"Ollama API Error: {e}")
