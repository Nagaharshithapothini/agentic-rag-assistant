# Agentic RAG Assistant

An enterprise-style **Agentic Retrieval-Augmented Generation (RAG) application** built using **LangGraph, LangChain, FastAPI, vector search, and Large Language Models (LLMs)**.

The project demonstrates how an AI assistant can retrieve relevant information from a knowledge base, maintain workflow state, generate grounded responses, and expose the functionality through a REST API.

## Project Overview

Traditional LLM applications can generate responses based only on information learned during model training. This can create limitations when users need answers based on private, domain-specific, or frequently changing information.

This project implements a **Retrieval-Augmented Generation architecture** where relevant information is retrieved from a vector database and provided to the language model as context before the final response is generated.

The workflow is managed using **LangGraph**, allowing the application to represent AI processing as a stateful sequence of nodes.

## Architecture

```text
User Question
      |
      v
FastAPI Endpoint
      |
      v
LangGraph Workflow
      |
      v
Retrieval Node
      |
      v
Vector Database
      |
      v
Relevant Documents
      |
      v
Context Construction
      |
      v
Generation Node
      |
      v
Large Language Model
      |
      v
Grounded Response
      |
      v
API Response
```

## Key Features

* Agentic workflow using LangGraph
* Retrieval-Augmented Generation
* Semantic search using embeddings
* Vector database integration
* Context-aware LLM responses
* Stateful workflow management
* Modular Python architecture
* FastAPI REST API
* Pydantic request validation
* Swagger/OpenAPI documentation
* Environment-variable based API-key management
* Docker-ready application structure
* Unit testing support with PyTest

## Technologies Used

| Category          | Technologies               |
| ----------------- | -------------------------- |
| Programming       | Python                     |
| Generative AI     | Large Language Models, RAG |
| Agent Framework   | LangGraph                  |
| LLM Framework     | LangChain                  |
| API Development   | FastAPI, Pydantic          |
| Embeddings        | OpenAI Embeddings          |
| Vector Database   | ChromaDB                   |
| Testing           | PyTest                     |
| Deployment        | Docker                     |
| API Documentation | Swagger / OpenAPI          |

## Project Structure

```text
agentic-rag-assistant/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── agent.py
│   ├── rag.py
│   ├── tools.py
│   ├── vector_store.py
│   └── config.py
│
├── data/
│   └── sample_documents.txt
│
├── tests/
│   └── test_agent.py
│
├── requirements.txt
├── .env.example
├── .gitignore
├── Dockerfile
└── README.md
```

## Application Workflow

The application processes a user question through several stages.

### 1. User Request

The user submits a question through the FastAPI `/ask` endpoint.

Example:

```json
{
  "question": "What is Retrieval-Augmented Generation?"
}
```

### 2. LangGraph State

LangGraph maintains application state containing the question, retrieved context, and generated answer.

```python
class AgentState(TypedDict):
    question: str
    context: str
    answer: str
```

### 3. Retrieval

The retrieval node searches the vector database for documents semantically related to the user's question.

```python
documents = vector_store.similarity_search(
    query,
    k=3
)
```

The most relevant documents are combined into a context that is passed to the language model.

### 4. Response Generation

The generation node combines the retrieved context with the original question and sends the resulting prompt to the LLM.

```text
Retrieved Context
       +
User Question
       |
       v
Language Model
       |
       v
Grounded Response
```

### 5. API Response

The generated answer is returned to the user through the FastAPI endpoint.

Example:

```json
{
  "question": "What is RAG?",
  "answer": "Retrieval-Augmented Generation combines information retrieval with a language model to generate responses grounded in retrieved information."
}
```

## Installation

### Prerequisites

Install the following before running the project:

* Python 3.10+
* Git
* pip
* OpenAI-compatible API credentials

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/agentic-rag-assistant.git
```

Move into the project directory:

```bash
cd agentic-rag-assistant
```

Create a Python virtual environment:

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the root directory.

```text
OPENAI_API_KEY=your_api_key_here
```

Do not commit the `.env` file to GitHub.

The `.gitignore` file should contain:

```text
.env
venv/
__pycache__/
.pytest_cache/
*.pyc
```

## Running the Application

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The application will run locally at:

```text
http://127.0.0.1:8000
```

## Swagger API Documentation

FastAPI automatically provides interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

The Swagger interface can be used to test the API directly from the browser.

## API Endpoints

### Health / Home Endpoint

```http
GET /
```

Example response:

```json
{
  "message": "Agentic RAG Assistant API"
}
```

### Ask Question

```http
POST /ask
```

Request:

```json
{
  "question": "How does LangGraph support AI agents?"
}
```

Example response:

```json
{
  "question": "How does LangGraph support AI agents?",
  "answer": "LangGraph can be used to build stateful AI workflows containing multiple processing nodes and transitions."
}
```

## Vector Search

The application converts documents into numerical embeddings and stores them in a vector database.

When a question is submitted, the same embedding process is applied to the query.

Semantic similarity is then used to locate the most relevant documents.

```text
Documents
   |
   v
Embedding Model
   |
   v
Vectors
   |
   v
Vector Database


User Query
   |
   v
Query Embedding
   |
   v
Similarity Search
   |
   v
Top-K Documents
```

## LangGraph Workflow

The current workflow contains two primary nodes:

```text
START
  |
  v
Retrieve Context
  |
  v
Generate Answer
  |
  v
END
```

The modular design allows additional agent capabilities to be introduced later.

Possible future nodes include:

```text
Question
   |
   v
Intent Classification
   |
   +-------------------+
   |                   |
   v                   v
Knowledge Search    Tool Execution
   |                   |
   +---------+---------+
             |
             v
        Validation
             |
             v
       Answer Generation
```

## Testing

Run the tests using:

```bash
pytest
```

Tests can be added for:

* API endpoint validation
* Retrieval functionality
* Empty-query handling
* Vector search
* Workflow execution
* Response generation
* Invalid request handling

## Docker

Build the Docker image:

```bash
docker build -t agentic-rag-assistant .
```

Run the container:

```bash
docker run -p 8000:8000 --env-file .env agentic-rag-assistant
```

Then open:

```text
http://localhost:8000/docs
```

## Example Use Cases

This architecture can be extended for enterprise applications such as:

* Internal knowledge assistants
* Policy and procedure search
* Technical documentation assistants
* Customer-support knowledge systems
* Financial document analysis
* Research assistants
* Employee knowledge portals
* Contract and document intelligence
* Natural-language enterprise search

## Future Enhancements

Planned improvements include:

* PDF document ingestion
* Multiple document formats
* Metadata-based filtering
* Hybrid semantic and keyword search
* Cross-encoder reranking
* Conversation memory
* Tool calling
* Conditional LangGraph routing
* Human-in-the-loop approval
* Query rewriting
* Retrieval evaluation
* LLM response evaluation
* Hallucination detection
* Authentication and authorization
* PostgreSQL/pgvector integration
* Pinecone integration
* Cloud deployment
* CI/CD with GitHub Actions
* Monitoring and observability

## Learning Objectives

This project demonstrates practical concepts used in modern AI engineering, including:

* Retrieval-Augmented Generation
* LLM application development
* Agentic workflow orchestration
* Semantic retrieval
* Embeddings
* Vector databases
* REST API development
* Modular Python application design
* Prompt construction
* Context grounding
* Containerization
* AI application testing

## Disclaimer

This repository is a portfolio and learning project designed to demonstrate modern Generative AI and Agentic AI engineering concepts.

The sample documents and data included in the repository are synthetic and do not contain proprietary or confidential enterprise information.

## Author

**Naga Harshitha Pothini**

Senior AI Engineer | Generative AI | Agentic AI | Machine Learning | Data Engineering
