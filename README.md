# A RAG (Retrieval Augmented Generation) app in Python 

https://www.youtube.com/watch?v=2TJxpyO3ei4


Here I am building a python RAG apication that can let you query/chat with your PDFs using generative AI.

This project contains covers:
* Run RAG apps locally (with Ollama).
* Update a vector DB with new items. 
* Use RAG with PDFs (or any other files).
* Test the quality of AI generated responses.


Sample data:
* [Alice in Wonderland](https://raw.githubusercontent.com/pixegami/langchain-rag-tutorial/main/data/books/alice_in_wonderland.md)
* Calculus made easy
* Monopoly


Install dependencies.
```
pip install -r requirements.txt
```
Create the Chroma DB.
```
python create_database.py
```
Query the Chroma DB.
```
python query_data.py "How does Alice meet the Mad Hatter?"
```

Using Ollama locally. We need to install Ollama locally, visit `https://ollama.com`
```
curl -fsSL https://ollama.com/install.sh | sh
```
To install available opensource models:
```
ollama pull llama2
ollala pull mistral
```
To serve the model as a REST API on local host:
```
ollama serve
```
We also need to update the model name in embeddings in get_embedding_function.py .

First we need to store the data in db and update when necessary. Start with populating db
```
python populate_database.py
```

Example usage:
```
python query_data.py "How many clues can I give in Codenames?"
```
To run test cases:
```
pytest test_rag.py 
```

I am following [pixegami](https://www.youtube.com/@pixegami). For the basic tutorial and seutp.