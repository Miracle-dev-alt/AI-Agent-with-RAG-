import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_core.documents import Document
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Check for API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key or api_key == "your_gemini_api_key_here":
    print("❌ Error: Gemini API key not found!")
    print("Please run 'python setup_gemini.py' to set up your API key.")
    print("Or set the GOOGLE_API_KEY environment variable.")
    exit(1)

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Load and prepare the data
df = pd.read_csv("realistic_restaurant_reviews.csv")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

db_location = "./chroma_gemini_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)
        
vector_store = Chroma(
    collection_name="restaurant_reviews_gemini",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)
    
retriever = vector_store.as_retriever(
    search_kwargs={"k": 8}
)

# Create the prompt template
template = """
You are an expert in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}

Please provide a helpful and accurate response based on the reviews provided.
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def main():
    print("🍕 Pizza Restaurant AI Assistant (Powered by Gemini)")
    print("=" * 50)
    print("This assistant can answer questions about the restaurant based on customer reviews.")
    print("Type 'q' to quit.\n")
    
    while True:
        print("\n" + "-" * 50)
        question = input("Ask your question: ")
        print("\n")
        
        if question.lower() == 'q':
            print("Thank you for using the Pizza Restaurant AI Assistant!")
            break
        
        try:
            # Retrieve relevant reviews
            reviews = retriever.invoke(question)
            
            # Generate response using Gemini
            result = chain.invoke({"reviews": reviews, "question": question})
            print("🤖 AI Response:")
            print(result.content)
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please check your API key and try again.")

if __name__ == "__main__":
    main()
