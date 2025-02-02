# GraphRAG-LLM

GraphRAG-LLM is an AI-powered customer support application that leverages LangChain, Neo4j, and Google Generative AI to provide reliable and efficient customer support. The application consists of a FastAPI backend and a Streamlit frontend.

## Features

- AI-Powered Assistance
- 24/7 Support
- Customer Support
- Query Resolution

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/GraphRAG-LLM.git
    cd GraphRAG-LLM
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    ```sh
    export NEO4J_URI="your_neo4j_uri"
    export NEO4J_USERNAME="your_neo4j_username"
    export NEO4J_PASSWORD="your_neo4j_password"
    export GROQ_API_KEY="your_groq_api_key"
    export GEMINI_API_KEY="your_gemini_api_key"
    ```

## Running the Application

### Backend

1. Navigate to the backend directory:
    ```sh
    cd backend
    ```

2. Run the FastAPI application:
    ```sh
    uvicorn backend:app --host 127.0.0.1 --port 9999
    ```

### Frontend

1. Navigate to the frontend directory:
    ```sh
    cd frontend
    ```

2. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:8501` to access the Streamlit frontend.
2. Interact with the chatbot by entering your queries in the input box.
3. The chatbot will respond with AI-generated answers based on the context and data retrieved from the Neo4j graph database.

## Project Structure

- `backend.py`: FastAPI backend implementation.
- `app.py`: Streamlit frontend implementation.
- `Graprag.py`: Core logic for processing questions and retrieving data.

## License

This project is licensed under the MIT License.