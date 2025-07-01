# AI Agent with RAG - Local Ollama vs Cloud Gemini

A Retrieval-Augmented Generation (RAG) AI agent that can answer questions about a pizza restaurant based on customer reviews. Choose between running locally with Ollama ## 🚀 Recent Improvements (v2.0)

### Enhanced Ollama Implementation:
- **Upgraded Model**: Now uses Qwen2.5:34b (superior reasoning and multilingual capabilities)
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
- **Powerful AI**: Uses Qwen2.5:34b for superior reasoning and analysis
- **Advanced Embeddings**: Nomic-embed-text for excellent document retrieval
- **Customizable**: Use any Ollama model you prefer

### ☁️ **Cloud Gemini Version** (`gemini.py`)
- **Powerful**: Uses Google's advanced Gemini 1.5 Pro model
- **Enhanced RAG**: Improved retrieval with better embeddings (text-embedding-004)
- **Smart Analysis**: Advanced prompt engineering for better responses
- **User-friendly**: Interactive interface with help system and statistics
- **Reliable**: Managed cloud infrastructure with error handling

## 📋 Prerequisites

### For Local Ollama Version:
- [Ollama](https://ollama.ai/) installed on your system
- Python 3.8+
- Required Ollama models:
  - `qwen2.5:34b` (for text generation and analysis)
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
   ollama pull qwen2.5:34b
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

## 🛠️ Advanced Configuration

### Customizing Ollama Models

Edit `local.py` to use different models:
```python
# Change the language model
model = OllamaLLM(
    model="llama3.2",  # or any other model
    temperature=0.1,
    num_ctx=8192
)

# Change the embedding model in vector.py
embeddings = OllamaEmbeddings(
    model="mxbai-embed-large",  # or other embedding models
    show_progress=True
)
```

### Customizing Gemini Models

Edit `gemini.py` to use different Gemini models:
```python
# Use different Gemini model (current: gemini-1.5-pro)
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Faster but less capable
    temperature=0.1,
    max_tokens=2048
)

# Use different embedding model (current: text-embedding-004)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",  # Older but still good
    task_type="retrieval_document"
)
```

## 🔍 Troubleshooting

### Ollama Issues:
- **Model not found**: Run `ollama pull qwen2.5:34b` and `ollama pull nomic-embed-text`
- **Ollama not running**: Start Ollama service
- **Slow responses**: Qwen2.5:34b requires significant RAM (16GB+ recommended)
- **Memory issues**: Try smaller models like `qwen2.5:14b` or `qwen2.5:7b`

### Gemini Issues:
- **API key error**: Check your `GOOGLE_API_KEY` environment variable
- **Quota exceeded**: Check usage in Google AI Studio dashboard
- **Import errors**: Run `pip install -r requirements.txt`

### General Issues:
- **Vector database errors**: Delete the `chroma_ollama_db` or `chroma_gemini_db` folders to rebuild
- **CSV file missing**: Ensure `realistic_restaurant_reviews.csv` is in the project directory
- **Performance issues**: The new Gemini 1.5 Pro model provides better quality responses than Flash
- **Large model requirements**: Qwen2.5:34b needs substantial RAM and processing power

## 🎯 Which Should You Choose?

### Choose **Ollama (Local)** if you:
- Value privacy and data control
- Want to avoid ongoing costs
- Have powerful local hardware (16GB+ RAM for Qwen2.5:34b)
- Need offline functionality
- Want to experiment with different models
- Prefer the advanced reasoning capabilities of Qwen2.5:34b

### Choose **Gemini (Cloud)** if you:
- Want the best performance and accuracy (now with Gemini 1.5 Pro)
- Don't mind cloud-based processing
- Prefer enhanced user interface with statistics and help system
- Have budget for API costs (still very affordable)
- Need reliable, managed infrastructure with better error handling

## � Recent Improvements (v2.0)

### Enhanced Gemini Implementation:
- **Upgraded Model**: Now uses Gemini 1.5 Pro (better reasoning, longer context)
- **Better Embeddings**: Latest `text-embedding-004` model for improved similarity search
- **Smart Retrieval**: Score-based filtering to retrieve only relevant reviews
- **Rich Context**: Enhanced document formatting with structured metadata
- **Advanced Prompting**: Improved prompt engineering for more detailed responses
- **User Experience**: Interactive help system, statistics display, and better error handling
- **Performance**: Optimized parameters for consistent, high-quality responses

## �📈 Performance Tips

### For Ollama:
- Use SSD storage for faster vector operations
- Allocate sufficient RAM (16GB+ for Qwen2.5:34b, 8GB+ for smaller models)
- Consider using GPU acceleration if available
- Monitor system resources during operation
- Use smaller models (qwen2.5:14b or qwen2.5:7b) if experiencing performance issues

### For Gemini:
- Monitor API usage to control costs
- Use appropriate models for your use case
- Implement caching for repeated queries

## 🤝 Contributing

Feel free to contribute improvements, bug fixes, or additional features to either implementation!

## 📄 License

This project is open source and available under the MIT License. 