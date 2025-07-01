import os
import pandas as pd
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever, df
import time

try:
    model = OllamaLLM(
        model="qwen3:4b",      
        temperature=0.1,          
        top_p=0.9,               
        num_ctx=8192             
    )
    print("✅ Initialized Qwen3:4b model")
except Exception as e:
    print("⚠️  Qwen3:4b not available, trying smaller version")
    try:
        model = OllamaLLM(
            model="qwen2.5", 
            temperature=0.1, 
            num_ctx=8192
        )
        print("✅ Using Qwen2.5 model")
    except Exception as e2:
        print("⚠️  Falling back to basic Qwen model")
        model = OllamaLLM(model="qwen2.5", temperature=0.1, num_ctx=4096)

# Enhanced prompt template with better context and instructions
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
- Use bullet points or numbered lists when appropriate

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
        metadata = review.metadata
        rating = metadata.get('rating', 'N/A')
        date = metadata.get('date', 'N/A')
        
        formatted.append(f"Review {i} (Rating: {rating}/5, Date: {date}):\n{review.page_content}\n")
    
    return "\n".join(formatted)

def get_help_examples():
    """Return example questions users can ask"""
    return """
🤖 Example Questions You Can Ask:

📊 General Analysis:
  • "What do customers say about the pizza quality?"
  • "What are the most common complaints?"
  • "What's the overall customer satisfaction?"

🍕 Food & Menu:
  • "Which menu items are most praised?"
  • "What are customers saying about the taste?"
  • "Are there any food quality issues?"

🚚 Service & Delivery:
  • "How is the customer service?"
  • "What are the delivery times like?"
  • "Any issues with order accuracy?"

🏪 Restaurant Experience:
  • "What's the general atmosphere like?"
  • "How clean is the restaurant?"
  • "What about pricing and value?"

🔍 Specific Issues:
  • "Are there any recurring problems?"
  • "What do customers say about staff?"
  • "Any mentions of wait times?"
"""

def main():
    print("🍕 Enhanced Local Pizza Restaurant AI Assistant")
    print("🤖 Powered by Qwen3:4b with Nomic-Embed-Text RAG")
    print("=" * 70)
    
    # Display review statistics
    try:
        stats = get_review_stats()
        print(f"📊 Database Info:")
        print(f"   • Total Reviews: {stats['total_reviews']}")
        print(f"   • Average Rating: {stats['average_rating']:.1f}/5")
        print(f"   • Rating Distribution: {dict(stats['rating_distribution'])}")
    except Exception as e:
        print(f"⚠️  Could not load statistics: {e}")
    
    print("\n🤖 This assistant analyzes customer reviews to answer your questions.")
    print("💡 Type 'help' to see example questions or 'q' to quit.\n")
    
    while True:
        print("\n" + "="*50)
        question = input("🤔 Ask your question: ").strip()
        
        if question.lower() == "q":
            print("👋 Goodbye! Thanks for using the AI assistant!")
            break
        elif question.lower() == "help":
            print(get_help_examples())
            continue
        elif not question:
            print("❓ Please enter a question or type 'help' for examples.")
            continue
        
        print("\n🔍 Searching relevant reviews...")
        start_time = time.time()
        
        try:
            # Get relevant reviews
            reviews = retriever.invoke(question)
            
            if not reviews:
                print("❌ No relevant reviews found for your question.")
                continue
            
            # Format reviews for better context
            formatted_reviews = format_reviews_for_context(reviews)
            
            print(f"📚 Found {len(reviews)} relevant reviews")
            print("🤖 Generating response...\n")
            
            # Generate response
            result = chain.invoke({
                "reviews": formatted_reviews, 
                "question": question
            })
            
            # Display response with formatting
            print("🎯 AI RESPONSE:")
            print("-" * 40)
            print(result)
            
            # Show processing time
            processing_time = time.time() - start_time
            print(f"\n⏱️  Response generated in {processing_time:.2f} seconds")
            
        except Exception as e:
            print(f"❌ Error processing your question: {e}")
            print("Please try rephrasing your question or check if Ollama is running.")

if __name__ == "__main__":
    main()