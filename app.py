import os
import streamlit as st
from utils.pdf_reader import read_pdf
from utils.chunking import create_chunks
from utils.embeddings import generate_embeddings
from utils.vector_db import store_in_chromadb
from utils.vector_db import show_database
from utils.retriever import semantic_search
from utils.prompt_builder import build_prompt
from utils.openrouter_llm import generate_answer

# Page configuration
st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 5px solid #1f77b4;
    }
    .bot-message {
        background-color: #f5f5f5;
        border-left: 5px solid #ff7f0e;
    }
    .stButton button {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "collection" not in st.session_state:
    st.session_state.collection = None
if "processed" not in st.session_state:
    st.session_state.processed = False
if "chunks" not in st.session_state:
    st.session_state.chunks = None

# Header
st.markdown('<div class="main-header">📚 AI PDF Chatbot with RAG</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📄 PDF Upload & Processing")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type="pdf",
        help="Upload a PDF document to chat with"
    )
    
    # Process button
    if uploaded_file is not None:
        if st.button("🔄 Process PDF", type="primary"):
            with st.spinner("Processing PDF..."):
                try:
                    # Save uploaded file temporarily
                    temp_path = f"data/{uploaded_file.name}"
                    os.makedirs("data", exist_ok=True)
                    
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getvalue())
                    
                    # Step 1: Read PDF
                    text = read_pdf(temp_path)
                    st.info(f"✅ PDF read successfully: {len(text)} characters")
                    
                    # Step 2: Create chunks
                    chunks = create_chunks(text)
                    st.session_state.chunks = chunks
                    st.info(f"✅ Created {len(chunks)} chunks")
                    
                    # Step 3: Generate embeddings
                    embeddings = generate_embeddings(chunks)
                    st.info(f"✅ Generated embeddings")
                    
                    # Step 4: Store in ChromaDB
                    collection = store_in_chromadb(chunks, embeddings)
                    st.session_state.collection = collection
                    st.session_state.processed = True
                    
                    # Show database info
                    st.success(f"✅ PDF processed successfully!")
                    
                    # Display database stats
                    with st.expander("📊 Database Information"):
                        show_database(collection)
                    
                    # Clear previous messages
                    st.session_state.messages = []
                    
                except Exception as e:
                    st.error(f"❌ Error processing PDF: {str(e)}")
    
    # Show processing status
    if st.session_state.processed:
        st.success("✅ PDF is ready for questions!")
        if st.session_state.chunks:
            st.info(f"📊 {len(st.session_state.chunks)} chunks available")
    
    st.divider()
    
    # Instructions
    with st.expander("ℹ️ How to use"):
        st.markdown("""
        1. **Upload a PDF** using the file uploader
        2. Click **Process PDF** to index the document
        3. Ask questions about the PDF in the chat
        4. The system will retrieve relevant sections and generate answers
        
        **Sample questions:**
        - What is this document about?
        - Summarize the main points
        - Find information about [specific topic]
        """)

# Main chat area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("💬 Chat with your PDF")
    
    # Display chat history
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(
                    f'<div class="chat-message user-message">'
                    f'<strong>👤 You:</strong><br>{message["content"]}'
                    f'</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'<div class="chat-message bot-message">'
                    f'<strong>🤖 Bot:</strong><br>{message["content"]}'
                    f'</div>',
                    unsafe_allow_html=True
                )
    
    # Chat input
    if st.session_state.processed:
        question = st.chat_input("Ask a question about the PDF...")
        
        if question:
            # Add user message to history
            st.session_state.messages.append({"role": "user", "content": question})
            
            with st.spinner("🤔 Thinking..."):
                try:
                    # Step 6: Semantic Search
                    retrieved_chunks = semantic_search(
                        st.session_state.collection,
                        question
                    )
                    
                    # Step 7: Build Prompt
                    prompt = build_prompt(question, retrieved_chunks)
                    
                    # Step 8: Generate Answer
                    answer = generate_answer(prompt)
                    
                    # Add bot response to history
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                    
                    # Rerun to update chat display
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Error generating answer: {str(e)}")
    else:
        st.info("📄 Please upload and process a PDF file to start chatting.")

with col2:
    st.subheader("📊 Quick Stats")
    
    if st.session_state.processed:
        if st.session_state.chunks:
            st.metric("Total Chunks", len(st.session_state.chunks))
        st.metric("Messages", len(st.session_state.messages))
        
        # Show recent context
        if st.session_state.messages:
            with st.expander("🔄 Recent Conversation"):
                recent_messages = st.session_state.messages[-4:]
                for msg in recent_messages:
                    if msg["role"] == "user":
                        st.markdown(f"**👤 You:** {msg['content'][:50]}...")
                    else:
                        st.markdown(f"**🤖 Bot:** {msg['content'][:50]}...")
    else:
        st.info("No PDF processed yet")
    
    # Clear chat button
    if st.session_state.messages:
        if st.button("🗑️ Clear Chat History", type="secondary"):
            st.session_state.messages = []
            st.rerun()

# Footer
st.divider()
st.caption("🔒 Your PDF is processed locally. No data is stored on external servers.")