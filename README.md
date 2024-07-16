# INSAIT Backend Project

This project is a simple Flask server that exposes an endpoint to ask a question. The server sends the question to the OpenAI API, receives the answer, and saves both the question and the answer in a PostgreSQL database. The server and the database are dockerized and run with Docker Compose.

## Requirements

- Flask Server
- OpenAI API Integration
- PostgreSQL Database
- Alembic for database migrations
- Docker and Docker Compose
- Testing with pytest

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/RoiAzrai/INSAIT_Backend_Project.git
    cd INSAIT_Backend_Project
    ```

2. Create a `.env` file with the following content:
    ```
    OPENAI_API_KEY=your_openai_api_key
    DATABASE_URL=postgresql://postgres:yourpassword@db:5432/mydatabase
    ```

3. Build and start the containers using Docker Compose:
    ```bash
    docker-compose up --build
    ```

4. The server should now be running on `http://127.0.0.1:5000`.

## Usage

To ask a question, send a POST request to the `/ask` endpoint with a JSON payload containing the question:

```bash
curl -X POST http://127.0.0.1:5000/ask -H "Content-Type: application/json" -d "{\"question\": \"What is the capital of France?\"}"
