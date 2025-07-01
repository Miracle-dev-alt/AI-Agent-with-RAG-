# AI Agent with RAG - Local Ollama vs Cloud Gemini

A Retrieval-Augmented Generation (RAG) AI agent that can answer questions about a pizza restaurant based on customer reviews. Choose between running locally with Ollama ## 🚀 Recent Improvements (v2.0)

### Enhanced Ollama Implementation:
- **Upgraded Model**: Now uses Qwen3:4b (superior reasoning and multilingual capabilities)
- **Optimized Embeddings**: Nomic-embed-text for excellent document similarity matching
- **Smart Retrieval**: Score-based filtering to retrieve only relevant reviews
- **Rich Context**: Enhanced document formatting with structured metadata
- **Advanced Prompting**: Improved prompt engineering for more detailed responses
- **User Experience**: Interactive help system, statistics display, and better error handling
- **Performance**: Optimized parameters for consistent, high-quality responses

### Enhanced Gemini Implementation:using Google's Gemini API in the cloud.

## 🎯 Choose Your Implementation

This project offers two implementations:

### 🏠 **Local Ollama Version** (`local.py`)
- **Privacy-focused**: Runs entirely on your local machine
- **Cost-free**: No API costs or usage limits
- **Offline capable**: Works without internet connection
- **Powerful AI**: Uses Qwen3:4b for superior reasoning and analysis
- **Advanced Embeddings**: Nomic-embed-text for excellent document retrieval
- **Customizable**: Use any Ollama model you prefer

### ☁️ **Cloud Gemini Version** (`gemini.py`)
- **Powerful**: Uses Google's advanced Gemini 1.5 
- **Enhanced RAG**: Improved retrieval with better embeddings (text-embedding-004)
- **Smart Analysis**: Advanced prompt engineering for better responses
- **User-friendly**: Interactive interface with help system and statistics
- **Reliable**: Managed cloud infrastructure with error handling

## 📋 Prerequisites

### For Local Ollama Version:
- [Ollama](https://ollama.ai/) installed on your system
- Python 3.8+
- Required Ollama models:
  - `qwen3:4b` (for text generation and analysis)
  - `nomic-embed-text` (for embeddings)

### For Cloud Gemini Version:
- Python 3.8+
- Google AI Studio account
- Gemini API key

## 🚀 Quick Start

### Option 1: Local Ollama (Recommended for Privacy)

1. **Install Ollama and Models:**
   ```bash
   # Install Ollama (follow instructions at https://ollama.ai/)
   # Then pull the required models:
   ollama pull qwen3:4b
   ollama pull nomic-embed-text
   ```

2. **Install Python Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Local AI Agent:**
   ```bash
   python local.py
   ```

### Option 2: Cloud Gemini (Recommended for Performance)

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get Your Gemini API Key:**
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Click "Create API Key"
   - Copy the generated API key

3. **Set Up API Key:**
   ```bash
   # Option A: Set environment variable
   # Windows:
   set GOOGLE_API_KEY=your_api_key_here
   # Linux/Mac:
   export GOOGLE_API_KEY=your_api_key_here
   
   # Option B: Create .env file
   echo GOOGLE_API_KEY=your_api_key_here > .env
   ```

4. **Run the Cloud AI Agent:**
   ```bash
   python gemini.py
   ```

## 🍕 How to Use

Both versions work the same way:

1. **Start the application** using either `python local.py` (Ollama) or `python gemini.py` (Gemini)
2. **View database statistics** showing total reviews and rating distribution
3. **Ask questions** about the pizza restaurant when prompted
4. **Get AI responses** based on customer reviews with detailed analysis
5. **Type 'help'** to see example questions
6. **Type 'q'** to quit

### Example Questions:
- "What do customers say about the pizza quality?"
- "What are the most common complaints?"
- "How is the customer service?"
- "What are the best-rated menu items?"
- "What are the delivery times like?"
- "Which menu items are most praised?"
- "What's the general atmosphere like?"
- "Are there any recurring issues mentioned?"

## 🔧 How It Works

Both implementations follow the same RAG (Retrieval-Augmented Generation) process:

1. **Data Loading**: Restaurant reviews from `realistic_restaurant_reviews.csv`
2. **Vector Embeddings**: Reviews converted to numerical vectors using advanced models:
   - Ollama: `nomic-embed-text` (excellent for document similarity)
   - Gemini: `text-embedding-004` (latest Google embedding model)
3. **Vector Database**: Embeddings stored in Chroma for fast similarity search
4. **Enhanced RAG Process**: 
   - Find relevant reviews using similarity search with score thresholds
   - Format reviews with metadata (ratings, dates)
   - Pass structured context + question to AI model
   - Generate contextual response with advanced prompt engineering

## 📁 Project Structure

```
LocalAIAgentWithRAG/
├── local.py                   # Local Ollama implementation  
├── gemini.py                  # Enhanced Cloud Gemini implementation (Gemini 1.5 Pro)
├── vector.py                  # Vector database setup (Ollama)
├── realistic_restaurant_reviews.csv  # Sample data
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## ⚖️ Comparison: Ollama vs Gemini

| Feature | Ollama (Local) | Gemini (Cloud) |
|---------|----------------|----------------|
| **Privacy** | ✅ Complete | ❌ Data sent to Google |
| **Cost** | ✅ Free | 💰 Pay per use |
| **Speed** | ⚡ Depends on hardware | ⚡ Fast cloud processing |
| **Internet** | ❌ Not required | ✅ Required |
| **Setup** | 🔧 More complex | 🔧 Simpler |
| **Models** | 🎛️ Customizable | 🎛️ Fixed to Gemini |
| **Scalability** | 📊 Limited by hardware | 📊 Unlimited |


## 🤝 Contributing

Feel free to contribute improvements, bug fixes, or additional features to either implementation!

## 📄 License

This project is open source and available under the MIT License. 