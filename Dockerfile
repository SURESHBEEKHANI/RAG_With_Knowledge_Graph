# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV NEO4J_URI=$NEO4J_URI
ENV NEO4J_USERNAME=$NEO4J_USERNAME
ENV NEO4J_PASSWORD=$NEO4J_PASSWORD
ENV GROQ_API_KEY=$GROQ_API_KEY
ENV GEMINI_API_KEY=$GEMINI_API_KEY

# Expose port 9999 for the FastAPI backend
EXPOSE 9999

# Expose port 8501 for the Streamlit frontend
EXPOSE 8501

# Run the backend and frontend concurrently
CMD ["sh", "-c", "uvicorn backend:app --host 0.0.0.0 --port 9999 & streamlit run app.py"]
