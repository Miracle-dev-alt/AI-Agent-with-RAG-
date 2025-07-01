from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

# Load the CSV data
df = pd.read_csv("realistic_restaurant_reviews.csv")
print(f"✅ Loaded {len(df)} restaurant reviews")


embeddings = OllamaEmbeddings(
    model="nomic-embed-text:v1.5",   
    show_progress=True,         
    num_thread=4               
)
print("✅ Using nomic-embed-text embedding model")

db_location = "./chroma_ollama_db"
add_documents = not os.path.exists(db_location)

print("🔄 Setting up vector database...")
if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
      
        document = Document(
            page_content=f"Title: {row['Title']}\nReview: {row['Review']}",
            metadata={
                "rating": row["Rating"], 
                "date": row["Date"],
                "review_id": i,
                "title": row["Title"]
            },
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)
    
    print(f"📝 Created {len(documents)} documents for embedding...")

      
vector_store = Chroma(
    collection_name="restaurant_reviews_ollama_v2",  
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    print("🚀 Adding documents to vector store (this may take a moment)...")
    vector_store.add_documents(documents=documents, ids=ids)
    print("✅ Vector database setup complete!")
else:
    print("✅ Using existing vector database")
    

retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "k": 5,  
        "score_threshold": 0.3  # Only retrieve reasonably similar documents
    }
)