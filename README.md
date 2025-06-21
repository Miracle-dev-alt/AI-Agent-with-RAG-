# LocalAIAgentWithRAG

A Retrieval-Augmented Generation (RAG) AI agent that runs entirely on your local machine using Ollama models.

## Overview

This project demonstrates how to build a question-answering system that retrieves relevant information from a database of restaurant reviews before generating responses. By running locally with Ollama, it offers:

- 🚀 Fast responses without internet latency
- 🔒 Privacy-focused architecture with no data sent to external APIs
- 💰 Cost-free alternative to cloud-based LLM services

## Prerequisites

- [Ollama](https://ollama.ai/) installed on your system
- Python 3.8+
- Required Ollama models:
  - `llama3.2` (for text generation)
  - `mxbai-embed-large` (for embeddings)

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Make sure Ollama is running in the background

## Usage

1. First, prepare the vector database by running:
   ```
   python vector.py
   ```
   This will process the restaurant reviews and create embeddings.

2. Start the interactive question-answering system:
   ```
   python main.py
   ```
   
3. Type your questions about the restaurant when prompted. The system will find relevant reviews and generate an informed response.
   
4. Enter `q` when you want to quit the application.

## Example Interaction

Here's what the interaction looks like when you run the system:

```
-------------------------------
Ask your question (q to quit): What do people say about the pizza crust?


Based on the reviews, people have varied opinions about the pizza crust:

Many positive reviews mention the crust being "perfectly crispy on the outside and chewy inside" with some describing it as having "that perfect combination of crispy and chewy with a slight sourdough tang."

Several reviews praise the thin crust options, with comments like "cracker-thin, crispy all the way through, yet somehow still has a nice chew" and "their crust has the perfect crispness all the way through - no soggy middle!"

There are also specialty crusts mentioned, including "excellent gluten-free option" with a "cauliflower crust that doesn't fall apart," and "Detroit-style square pizza" with "crispy cheese edges, fluffy interior."

However, some negative reviews mention issues like "doughy and undercooked" centers, "tough leathery crust," or being "burned on the bottom." A few customers complained about the crust being "stale-tasting" or having a "refrigerator taste."

Overall, when the crust is done well, it seems to be a highlight of the restaurant's pizza.

-------------------------------
Ask your question (q to quit): Are there any good vegan options?


Based on the reviews, there are indeed excellent vegan options at this restaurant:

One reviewer specifically called it a "hidden gem for vegans" and mentioned that the restaurant makes their own cashew cheese "that actually melts properly" and uses fresh, seasonal vegetable toppings. They noted that even their non-vegan friends loved it.

Another positive mention was about their "great gluten-free option" with a cauliflower crust, which might appeal to some vegan customers looking for alternative crusts.

However, there was one negative review about their vegan cheese option, describing it as "terrible" with "no meltability, a grainy texture, and tasted strongly of coconut which clashed with the tomato sauce." This reviewer suggested that if the restaurant can't do vegan cheese well, they should "offer cheese-free options that are properly balanced."

Overall, it seems the restaurant does offer good vegan options that most customers enjoy, though the quality of their vegan cheese might be inconsistent or divisive.

-------------------------------
Ask your question (q to quit): q
```

## How it Works

1. **Vectorization**: The system converts restaurant reviews into vector embeddings using Ollama's `mxbai-embed-large` model
2. **Retrieval**: When you ask a question, the system finds the most relevant reviews using similarity search
3. **Generation**: The retrieved reviews are passed to the LLM (llama3.2) along with your question to generate an informed response

## Project Structure

- `main.py` - The interactive question-answering loop
- `vector.py` - Creates and manages the vector database
- `realistic_restaurant_reviews.csv` - Dataset of restaurant reviews
- `requirements.txt` - Required Python packages

## Limitations

- Quality depends on the Ollama models you have installed
- Limited to knowledge within the restaurant reviews dataset
- No memory of previous interactions in the conversation

