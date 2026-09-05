# 📚 AI PDF Chatbot with RAG

An AI-powered PDF chatbot that allows users to upload a PDF and ask questions about its content.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from the uploaded PDF and generate answers using an LLM.

## 🚀 Features

- 📄 Upload PDF documents
- ✂️ Split PDF text into chunks
- 🔢 Generate embeddings
- 🗄️ Store embeddings using ChromaDB
- 🔍 Perform semantic search
- 🤖 Generate AI-powered answers
- 💬 Interactive chat interface
- 📊 Display document and conversation statistics
- 🗑️ Clear chat history
- 🎨 Simple and user-friendly Streamlit interface

## 🛠️ Technologies Used

- Python
- Streamlit
- ChromaDB
- Embeddings
- OpenRouter LLM
- PyPDF
- RAG (Retrieval-Augmented Generation)

## 📂 Project Structure

```text
AI-PDF-Chatbot/
│
├── utils/
│   ├── pdf_reader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_db.py
│   ├── retriever.py
│   ├── prompt_builder.py
│   └── openrouter_llm.py
│
├── data/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```
## **⚙️ How It Works**

1. Upload a PDF document.
2. Extract text from the PDF.
3. Split the text into smaller chunks.
4. Generate embeddings for the chunks.
5. Store the embeddings in ChromaDB.
6. Convert the user's question into an embedding.
7. Retrieve relevant chunks using semantic search.
8. Build a prompt using the retrieved information.
9. Send the prompt to the LLM.
10 .Display the generated answer in the chat interface.
```
## **🔧 Installation**

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-PDF-Chatbot

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt
🔐 Environment Variables

Create a .env file in the project directory:

OPENROUTER_API_KEY=your_api_key_here
```

##**▶️ Run the Application**

Run the Streamlit application:

streamlit run app.py

The application will open in your browser.
```

**💡 Example Questions**

After uploading a PDF, you can ask:

What is this document about?
Summarize the main points.
Explain the important topics.
What are the key concepts discussed?
Find information about a specific topic.
```

**🔒 Privacy**

The uploaded PDF is processed locally by the application. API credentials are stored using environment variables and should not be committed to GitHub.
```

**👩‍💻 Author**

Sukanya Chalalgulla
```

**📄 License**

This project is created for educational and learning purposes.   
