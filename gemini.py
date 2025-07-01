import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_core.documents import Document
import pandas as pd


load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")
if not api_key or api_key == "your_gemini_api_key_here":
    print("❌ Error: Gemini API key not found!")
    print("Please run 'python setup_gemini.py' to set up your API key.")
    print("Or set the GOOGLE_API_KEY environment variable.")
    exit(1)


model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


try:
    df = pd.read_csv("realistic_restaurant_reviews.csv")
    print(f"✅ Loaded {len(df)} restaurant reviews")
except FileNotFoundError:
    print("❌ Error: realistic_restaurant_reviews.csv not found!")
    print("Please ensure the CSV file is in the current directory.")
    exit(1)

# Initialize embeddings with better model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",  
    task_type="retrieval_document"     
)

db_location = "./chroma_gemini_db"
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
    collection_name="restaurant_reviews_gemini_v2",  
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
        "score_threshold": 0.3  
    }
)


template = """You are an expert AI assistant specializing in analyzing restaurant reviews and providing helpful insights about a pizza restaurant.

CONTEXT - Recent Customer Reviews:
{reviews}

CUSTOMER QUESTION: {question}

INSTRUCTIONS:
- Analyze the provided reviews carefully and provide a comprehensive, helpful response
- If the question asks about specific aspects (food quality, service, delivery, etc.), focus on those areas
- Include specific examples from reviews when relevant
- Mention ratings or patterns you notice across multiple reviews
- If you don't have enough information in the reviews to fully answer the question, say so
- Be objective and balanced in your response
- Format your response in a clear, easy-to-read manner

RESPONSE:"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def get_review_stats():
    """Get basic statistics about the reviews"""
    total_reviews = len(df)
    avg_rating = df['Rating'].mean()
    rating_distribution = df['Rating'].value_counts().sort_index()
    
    return {
        'total_reviews': total_reviews,
        'average_rating': avg_rating,
        'rating_distribution': rating_distribution
    }

def format_reviews_for_context(reviews):
    """Format retrieved reviews for better context"""
    formatted = []
    for i, review in enumerate(reviews, 1):
        content = review.page_content
        metadata = review.metadata
        rating = metadata.get('rating', 'N/A')
        date = metadata.get('date', 'N/A')
        
        formatted.append(f"Review {i} (Rating: {rating}/5, Date: {date}):\n{content}\n")
    
    return "\n".join(formatted)

def main():
    print("🍕 Advanced Pizza Restaurant AI Assistant")
    print("💎 Powered by Gemini 1.5 Pro with Enhanced RAG")
    print("=" * 60)
    
    # Display review statistics
    stats = get_review_stats()
    print(f"📊 Database Info:")
    print(f"   • Total Reviews: {stats['total_reviews']}")
    print(f"   • Average Rating: {stats['average_rating']:.1f}/5")
    print(f"   • Rating Distribution: {dict(stats['rating_distribution'])}")
    
    print("\n🤖 This assistant analyzes customer reviews to answer your questions.")
    print("💡 Try asking about: food quality, service, delivery, prices, atmosphere, etc.")
    print("❓ Type 'help' for example questions or 'q' to quit.\n")
    
    while True:
        print("\n" + "─" * 60)
        question = input("🔍 Ask your question: ").strip()
        print()
        
        if question.lower() == 'q':
            print("👋 Thank you for using the Pizza Restaurant AI Assistant!")
            break
        elif question.lower() == 'help':
            print("💡 Example questions you can ask:")
            print("   • What do customers say about the pizza quality?")
            print("   • How is the customer service?")
            print("   • What are the most common complaints?")
            print("   • What are the delivery times like?")
            print("   • Which menu items are most praised?")
            print("   • What's the general atmosphere like?")
            print("   • Are there any recurring issues mentioned?")
            continue
        elif not question:
            print("⚠️  Please enter a question or 'q' to quit.")
            continue
        
        try:
            print("🔄 Searching through reviews...")
            
            # Retrieve relevant reviews
            reviews = retriever.invoke(question)
            
            if not reviews:
                print("❌ No relevant reviews found for your question.")
                print("💡 Try rephrasing your question or asking about a different topic.")
                continue
            
            print(f"✅ Found {len(reviews)} relevant reviews")
            
            # Format reviews for better context
            formatted_reviews = format_reviews_for_context(reviews)
            
            # Generate response using Gemini
            print("🧠 Generating AI response...")
            result = chain.invoke({
                "reviews": formatted_reviews, 
                "question": question
            })
            
            print("🤖 AI Analysis:")
            print("─" * 40)
            print(result.content)
            
        except Exception as e:
            print(f"❌ Error occurred: {str(e)}")
            if "API key" in str(e).lower():
                print("🔑 Please check your GOOGLE_API_KEY environment variable.")
            elif "quota" in str(e).lower() or "limit" in str(e).lower():
                print("📊 You may have reached your API usage limit. Please try again later.")
            else:
                print("🔧 Please check your internet connection and try again.")

if __name__ == "__main__":
    main()
