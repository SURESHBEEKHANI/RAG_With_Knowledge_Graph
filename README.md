# RAG_With_Knowledge_Graph

**RAG_With_Knowledge_Graph** is an advanced AI-driven customer support system that integrates LangChain, Neo4j, and Google Generative AI to deliver efficient and dependable customer assistance. The application features a FastAPI backend and a Streamlit frontend.

## Key Features

- AI-Powered Assistance
- 24/7 Support Availability
- Comprehensive Customer Query Resolution

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/SURESHBEEKHANI/RAG_With_Knowledge_Graph.git
   cd RAG_With_Knowledge_Graph
   ```

2. Set up a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Use `venv\Scripts\activate` on Windows
   ```

3. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure environment variables:
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

2. Launch the FastAPI application:
   ```sh
   uvicorn backend:app --host 127.0.0.1 --port 9999
   ```

### Frontend

1. Navigate to the frontend directory:
   ```sh
   cd ../frontend
   ```

2. Start the Streamlit application:
   ```sh
   streamlit run app.py
   ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8501` to access the Streamlit frontend.
2. Interact with the chatbot by entering your queries into the input box.
3. The chatbot will respond with AI-generated answers based on context and data retrieved from the Neo4j graph database.

## Project Structure

- `backend.py`: Implementation of the FastAPI backend.
- `app.py`: Implementation of the Streamlit frontend.
- `Graprag.py`: Core logic for query processing and data retrieval.

## Video Demonstration

Watch our project demonstration video:

[![Customer Support LangChain](notebook/Customer Suppport Langchan .mp4)]

## License

This project is licensed under the MIT License.
