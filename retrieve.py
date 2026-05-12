from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
from llama_index.core import Settings
import os
from dotenv import load_dotenv

load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")

llm=Groq(model="openai/gpt-oss-120b", api_key=groq_api_key, temperature=0.7, max_tokens=512)
Settings.llm=llm
Settings.embed_model=HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    device="cpu",
)
#load from same directory
storage_context = StorageContext.from_defaults(
    persist_dir="./storage"
)
index= load_index_from_storage(storage_context)

query_engine= RetrieverQueryEngine.from_args(
    index.as_retriever()
)
query=input("what's in your mind: ")
response=query_engine.query(query)
print(response)