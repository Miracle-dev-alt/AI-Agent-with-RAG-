# AI Agent with RAG - Local Ollama vs Cloud Gemini

A Retrieval-Augmented Generation (RAG) AI agent that can answer questions about a pizza restaurant based on customer reviews. Choose between running locally with Ollama or using Google's Gemini API in the cloud.

## 🎯 Choose Your Implementation

This project offers two implementations:

### 🏠 **Local Ollama Version** (`main.py`)
- **Privacy-focused**: Runs entirely on your local machine
- **Cost-free**: No API costs or usage limits
- **Offline capable**: Works without internet connection
- **Customizable**: Use any Ollama model you prefer

### ☁️ **Cloud Gemini Version** (`gemini.py`)
- **Powerful**: Uses Google's latest Gemini 1.5 Flash model
- **Fast**: Optimized for speed and accuracy
- **Reliable**: Managed cloud infrastructure
- **Scalable**: No local resource limitations

## 📋 Prerequisites

### For Local Ollama Version:
- [Ollama](https://ollama.ai/) installed on your system
- Python 3.8+
- Required Ollama models:
  - `deepseek-r1:1.5b` (for text generation)
  - `mxbai-embed-large` (for embeddings)

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
   ollama pull deepseek-r1:1.5b
   ollama pull mxbai-embed-large
   ```

2. **Install Python Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Local AI Agent:**
   ```bash
   python main.py
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

1. **Start the application** using either `python main.py` (Ollama) or `python gemini.py` (Gemini)
2. **Ask questions** about the pizza restaurant when prompted
3. **Get AI responses** based on customer reviews
4. **Type 'q'** to quit

### Example Questions:
- "What do customers say about the pizza quality?"
- "What are the most common complaints?"
- "How is the customer service?"
- "What are the best-rated menu items?"
- "What are the delivery times like?"

## 🔧 How It Works

Both implementations follow the same RAG (Retrieval-Augmented Generation) process:

1. **Data Loading**: Restaurant reviews from `realistic_restaurant_reviews.csv`
2. **Vector Embeddings**: Reviews converted to numerical vectors
3. **Vector Database**: Embeddings stored in Chroma for fast retrieval
4. **RAG Process**: 
   - Find relevant reviews using similarity search
   - Pass reviews + question to AI model
   - Generate contextual response

## 📁 Project Structure

```
LocalAIAgentWithRAG/
├── main.py                    # Local Ollama implementation
├── gemini.py                  # Cloud Gemini implementation
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

Edit `main.py` to use different models:
```python
# Change the model name
model = OllamaLLM(model="llama3.2")  # or any other model

# Change the embedding model in vector.py
embeddings = OllamaEmbeddings(model="nomic-embed-text")
```

### Customizing Gemini Models

Edit `gemini.py` to use different Gemini models:
```python
# Use different Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")  # or gemini-1.0-pro
```

## 🔍 Troubleshooting

### Ollama Issues:
- **Model not found**: Run `ollama pull model_name`
- **Ollama not running**: Start Ollama service
- **Slow responses**: Try smaller models or better hardware

### Gemini Issues:
- **API key error**: Check your `GOOGLE_API_KEY` environment variable
- **Quota exceeded**: Check usage in Google AI Studio dashboard
- **Import errors**: Run `pip install -r requirements.txt`

### General Issues:
- **Vector database errors**: Delete the `chrome_langchain_db` or `chroma_gemini_db` folders to rebuild
- **CSV file missing**: Ensure `realistic_restaurant_reviews.csv` is in the project directory

## 🎯 Which Should You Choose?

### Choose **Ollama (Local)** if you:
- Value privacy and data control
- Want to avoid ongoing costs
- Have decent local hardware
- Need offline functionality
- Want to experiment with different models

### Choose **Gemini (Cloud)** if you:
- Want the best performance and accuracy
- Don't mind cloud-based processing
- Prefer simpler setup
- Have budget for API costs
- Need reliable, managed infrastructure

## 📈 Performance Tips

### For Ollama:
- Use SSD storage for faster vector operations
- Allocate sufficient RAM (8GB+ recommended)
- Consider using smaller models for faster responses

### For Gemini:
- Monitor API usage to control costs
- Use appropriate models for your use case
- Implement caching for repeated queries

## 🤝 Contributing

Feel free to contribute improvements, bug fixes, or additional features to either implementation!

## 📄 License

This project is open source and available under the MIT License. 