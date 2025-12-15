# 🤖 Agentic AI Quiz Master (RAG)

An intelligent, interactive Quiz Generator built with Python. This tool reads a PDF document, understands the content using Vector Search (RAG), and generates custom Multiple Choice Questions (MCQs) for the user to practice.

## ✨ Features

* **RAG (Retrieval-Augmented Generation):** Uses your own custom data (`climates.pdf`) to generate questions.
* **Vector Database:** Stores document embeddings in Qdrant for semantic search.
* **AI-Powered:** Uses OpenAI's `gpt-4o-mini` to generate logically sound questions and validate answers.
* **Interactive CLI:** A simple command-line interface that tracks your score in real-time.
* **Context-Aware:** Generates questions based specifically on the topic you choose (e.g., "Rain", "Desert").

## 🛠️ Tech Stack

* **Language:** Python 3.12+
* **AI Models:** OpenAI (`gpt-4o-mini`, `text-embedding-3-large`)
* **Framework:** LangChain
* **Database:** Qdrant (Vector Store)
* **Format:** JSON (Structured Output)

## 🚀 Prerequisites

Before you begin, ensure you have the following:

1.  **Python** installed on your machine.
2.  **Docker** installed (to run the Qdrant database).
3.  An **OpenAI API Key**.

## 📦 Installation

1.  **Clone or Set up the project:**
    ```bash
    mkdir quiz_taker
    cd quiz_taker
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    
    # Windows
    venv\Scripts\activate
    
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install langchain-openai langchain-qdrant langchain-community qdrant-client openai python-dotenv pypdf
    ```

4.  **Set up Environment Variables:**
    Create a `.env` file in the root folder and add your API key:
    ```env
    OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxx
    ```

5.  **Start Qdrant (Vector DB):**
    Run this Docker command to start the database locally:
    ```bash
    docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
    ```

## 🏃‍♂️ Usage

### Step 1: Index Your Data (Run Once)
This script loads `climates.pdf`, splits it into chunks, and saves the embeddings to Qdrant.
```bash
python index.py