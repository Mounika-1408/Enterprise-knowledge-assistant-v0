# 🏢 Enterprise Knowledge Assistant

An AI-powered Enterprise Knowledge Assistant built using LangChain, ChromaDB, HuggingFace Embeddings, and Groq Llama 3.3.

The assistant enables employees to search across an enterprise knowledge base containing multiple departments and multiple document formats.

---

## 🚀 Features

- Multi-format document support
  - PDF
  - DOCX
  - TXT
  - CSV
- Automatic knowledge base indexing
- Semantic search using ChromaDB
- HuggingFace Embeddings
- Retrieval-Augmented Generation (RAG)
- Enterprise metadata
  - Department
  - Document Name
  - Page Number
- Continuous question answering
- Persistent Vector Database
- Modular project architecture

---

## 🛠️ Tech Stack

- Python
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq API
- Llama 3.3 70B Versatile

---

## 📂 Project Structure

```
enterprise_knowledge_assistant/
│
├── knowledge_base/
│   ├── HR/
│   ├── Finance/
│   ├── IT/
│   └── Legal/
│
├── document_loader.py
├── vector_store.py
├── llm.py
├── prompt.py
├── assistant.py
├── main.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python main.py
```

---

## 💬 Example Questions

- What is the leave policy?
- How do I reset my password?
- What is the reimbursement process?
- Explain the security policy.
- What documents are available in HR?
- What is the employee onboarding process?

---

## 📌 Future Improvements

- Department Filtering
- Conversation Memory
- Streamlit Web Interface
- Multi-user Authentication
- Source Highlighting
- Document Upload Support

---

## 👩‍💻 Author

**Mounika Gopidinni**

Applied AI Engineer