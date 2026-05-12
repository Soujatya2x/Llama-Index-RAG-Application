from llama_index.core import SimpleDirectoryReader
from llama_index.core.text_splitter import SentenceSplitter
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

##load files from a directory
documents=SimpleDirectoryReader("./data").load_data()
print(f"Loaded {len(documents)} documents")

##define a sentence-based text splitter
text_splitter=SentenceSplitter(chunk_size=512, chunk_overlap=50)

##applly text splitting to documents
#nodes=text_splitter.split_documents(documents)
nodes=text_splitter.get_nodes_from_documents(documents)

'''In LlamaIndex, a node is just a chunk of text cut from your original document, 
with some extra metadata attached.'''

print(f"split into {len(nodes)} chunks")

##index documents with embeddings
#configuring local embedding model
Settings.embed_model=HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    device="cpu",
)
#create an index
index=VectorStoreIndex(nodes)

#persist in the index(optional)
index.storage_context.persist(persist_dir="./storage")


