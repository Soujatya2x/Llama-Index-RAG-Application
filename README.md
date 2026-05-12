# 🦙 LlamaIndex RAG Application

> A lightweight Retrieval-Augmented Generation (RAG) pipeline that ingests documents from a local directory, chunks them using a sentence splitter, embeds them with a local HuggingFace model, and persists the vector index for fast, offline retrieval — no repeated embedding needed.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![LlamaIndex](https://img.shields.io/badge/LlamaIndex-RAG-blueviolet?style=flat-square)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-yellow?style=flat-square&logo=huggingface)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

---

## 🧠 Overview

This project implements a simple but production-ready RAG pipeline using **LlamaIndex**. Documents are loaded from a `data/` directory, split into sentence-level chunks, embedded locally using `all-MiniLM-L6-v2`, and stored in a persistent vector index. Once indexed, retrieval is fast and does not require re-embedding — making it efficient for repeated queries.

---

## ✨ Features

- 📂 **Flexible ingestion** — reads `.txt` and `.pdf` files from any directory
- ✂️ **Sentence-level chunking** — uses LlamaIndex's `SentenceSplitter` for semantic coherence
- 🔒 **100% local embeddings** — powered by `sentence-transformers/all-MiniLM-L6-v2` via HuggingFace (no API key needed for embedding)
- 💾 **Persistent vector store** — index is saved to disk; retrieval skips re-embedding entirely
- ⚡ **Fast retrieval** — `retrieve.py` fetches context directly from stored index
- 🤖 **Groq LLM integration** — uses Groq's API for fast inference on retrieved context

---

## 🛠️ Tech Stack

| Component     | Technology                              |
|---------------|-----------------------------------------|
| RAG Framework | [LlamaIndex](https://www.llamaindex.ai) |
| Embeddings    | HuggingFace `all-MiniLM-L6-v2`         |
| LLM Inference | [Groq](https://groq.com)               |
| Language      | Python 3.9+                             |

---

## 📁 Project Structure

```
LlamaIndex-RAG-Application/
├── data/               # Place your .txt or .pdf documents here
├── storage/            # Auto-generated persistent vector index
├── main.py             # Ingests documents and builds the index
├── retrieve.py         # Queries the stored index
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Soujatya2x/Llama-Index-RAG-Application.git
cd Llama-Index-RAG-Application
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your Groq API key

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> Get your free API key at [console.groq.com](https://console.groq.com)

---

## 💻 Usage

### Step 1 — Add your documents

Place any `.txt` or `.pdf` files inside the `data/` directory:

```
data/
├── my_document.pdf
├── notes.txt
└── report.pdf
```

### Step 2 — Build the index

```bash
python main.py
```

This will chunk, embed, and persist the vector index to the `storage/` directory.

### Step 3 — Retrieve and query

```bash
python retrieve.py
```

Retrieval loads from the persisted index — no re-embedding required.

---

## ⚙️ Configuration

You can adjust the following parameters in `main.py`:

| Parameter         | Default            | Description                        |
|-------------------|--------------------|------------------------------------|
| `chunk_size`      | `512`              | Token size per chunk               |
| `chunk_overlap`   | `50`               | Overlap between consecutive chunks |
| `embed_model`     | `all-MiniLM-L6-v2` | HuggingFace embedding model        |
| `data_dir`        | `./data`           | Directory to load documents from   |
| `persist_dir`     | `./storage`        | Directory to save the index        |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">Built with 🦙 LlamaIndex + ⚡ Groq + 🤗 HuggingFace</p>
