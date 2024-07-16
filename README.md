

# INSAIT Backend Project

## Overview
This project is a Flask-based backend application that integrates with the OpenAI API to handle user queries, process them through the OpenAI API, and store both the queries and responses in a PostgreSQL database. The application is containerized using Docker and managed with Docker Compose.

## Features
- **Flask Server**: A RESTful API endpoint to handle user queries.
- **OpenAI Integration**: Sends user queries to the OpenAI API and receives responses.
- **PostgreSQL Database**: Stores queries and responses.
- **Alembic**: Manages database migrations.
- **Docker**: Containerizes the application.
- **Docker Compose**: Manages multi-container Docker applications.
- **Testing**: Ensures functionality using pytest.

## Requirements
- Python 3.10
- Docker
- Docker Compose

## Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/RoiAzrai/INSAIT_Backend_Project.git
    cd INSAIT_Backend_Project
    ```

2. **Set up environment variables**
    - Create a `.env` file in the project root with the following content:
      ```env
      OPENAI_API_KEY=your_openai_api_key
      DATABASE_URL=postgresql://postgres:password@db:5432/mydatabase
      ```

3. **Build and run the Docker containers**
    ```sh
    docker-compose up --build
    ```

## Running Tests

- Activate the virtual environment:
    ```sh
    source openai-env/bin/activate # On Windows use `openai-env\Scripts\activate`
    ```

- Run tests using pytest:
    ```sh
    pytest test_app.py
    ```

## Project Structure
```plaintext
INSAIT_Backend_Project/
│
├── alembic/                 # Alembic migrations
├── app.py                   # Flask application
├── Dockerfile               # Dockerfile for Flask application
├── docker-compose.yml       # Docker Compose configuration
├── models.py                # SQLAlchemy models and database setup
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
├── test_app.py              # Pytest test file
```

## Usage
- To send a query to the OpenAI API:
    ```sh
    curl -X POST http://127.0.0.1:5000/ask -H "Content-Type: application/json" -d '{"question": "What is the capital of France?"}'
    ```

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-foo`)
3. Commit your changes (`git commit -m 'Add some foo'`)
4. Push to the branch (`git push origin feature-foo`)
5. Create a new Pull Request

## License
[MIT](https://choosealicense.com/licenses/mit/)

