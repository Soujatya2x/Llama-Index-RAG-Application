# LlamaIndex RAG Application

>A simple RAG application that reads documents from a directory, makes chunks from sentences, embeds locally, and creates a persistent storage

<!-- ![Demo](demo.png) -->

## Features
- reads any text or pdf file from a directory
- uses sentence splitter for chunking
- performs vector embedding with local sentence transformer model (all-MiniLM-L6 V2)
- creates a persistent storage
- retreival only requires to fetch context from stored data.

## Tech Stack
- LlamaIndex, HuggingFace, Groq

## Getting Started
\```bash
git clone https://github.com/Soujatya2x/Llama-Index-RAG-Application.git
pip install requirements.txt

\```

## Usage
\```bash
put documents in data directory
python main.py
python retrieve.py
\```

## License
MIT
