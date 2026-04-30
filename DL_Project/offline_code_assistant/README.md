# 🧠 Offline Codebase Assistant (LangChain + Ollama)

## 📌 Overview

This project is an **offline AI-powered codebase assistant** that allows you to query and understand your local code files using natural language.

Unlike traditional chatbots, this system:

* Reads your **local codebase**
* Retrieves relevant code snippets
* Generates answers based **only on your code**

It works completely **offline**, using a local LLM via Ollama.

---

## 🚀 Features

* 🔍 Query your codebase using natural language
* 📂 Supports local `.py` files
* 🧠 Retrieval-Augmented Generation (RAG) pipeline
* ⚡ Works fully offline (no API required)
* 📁 Displays source file references
* 🧾 Shows retrieved code snippets for transparency

---

## 🏗️ Project Structure

```
offline_code_assistant/
│
├── venv/                  # Virtual environment
│
├── data/                  # Your codebase (input files)
│   └── test.py
│
├── src/                   # Application source code
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── qa_chain.py
│   └── main.py
```

---

## ⚙️ Tech Stack

* Python
* LangChain (community modules)
* FAISS (vector database)
* Sentence Transformers (embeddings)
* Ollama (local LLM runtime)
* TinyLlama / Phi (lightweight models)

---

## 🧠 How It Works

1. 📂 Load Python files from `data/`
2. ✂️ Split code into smaller chunks
3. 🔢 Convert chunks into embeddings
4. 🗃️ Store in FAISS vector database
5. 🔍 Retrieve relevant code for a query
6. 🤖 Generate answer using local LLM

---

## 🔧 Setup Instructions

### 1. Clone / Create Project

```bash
mkdir offline_code_assistant
cd offline_code_assistant
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
pip install langchain langchain-community faiss-cpu sentence-transformers
```

---

### 4. Install Ollama

Install:
👉 https://ollama.com/

Then pull a lightweight model:

```bash
ollama pull tinyllama
```

---

### 5. Add Code Files

Place your Python files inside:

```
/data
```

Example:

```python
def add(a, b):
    return a + b
```

---

### 6. Run the Project

```bash
cd src
python main.py
```

---

## 💬 Example Queries

```
what does add function do?
explain test.py code
which file contains multiplication logic?
```

---

## 🧪 Sample Output

```
💡 Answer:
The function 'add' takes two inputs and returns their sum.

📁 Sources: data/test.py

🔎 Retrieved Code:
def add(a, b):
    return a + b
```

---

## ⚠️ Limitations

* Uses lightweight models → limited reasoning
* Works best with **specific queries**
* Currently supports only `.py` files
* No UI (CLI-based interaction)

---

## 🚀 Future Improvements

* 🔍 Function-level parsing (AST-based)
* 💬 Streamlit UI (chat interface)
* 📊 Multi-language support (Java, JS)
* ⚡ Faster retrieval optimization
* 🧠 Better local models

---

## 🎯 Key Learning

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Offline AI system design
* Vector databases (FAISS)
* Local LLM integration

---

## 👨‍💻 Author

Built as a beginner-friendly LangChain + Offline AI project.

---

## ⭐ Tip

For better results:

* Ask **specific questions**
* Use meaningful file names
* Add more code files to improve context
