# A RAG (Retrieval Augmented Generation) app in Python 

Here I am building a python RAG apication that can let you query/chat with your PDFs using generative AI.

This project contains covers:
* Run RAG apps locally (with Ollama).
* Update a vector DB with new items. 
* Use RAG with PDFs (or any other files).
* Test the quality of AI generated responses.


Sample data:
* [AWS Lambda documentation](https://docs.aws.amazon.com/pdfs/serverless/latest/devguide/serverless-core.pdf)
* [Alice in Wonderland](https://raw.githubusercontent.com/pixegami/langchain-rag-tutorial/main/data/books/alice_in_wonderland.md)


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
We'll also need to set up an OpenAI account (and set the OpenAI key in your environment variable) for this to work.



I am following [pixegami](https://www.youtube.com/@pixegami). For the basic tutorial and seutp.