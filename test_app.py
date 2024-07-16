import os
import pytest
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from app import app, db, QuestionAnswer

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_ask_endpoint(client):
    response = client.post('/ask', json={'question': 'What is the capital of France?'})
    data = response.get_json()
    assert response.status_code == 200
    assert 'answer' in data
    assert data['answer'] == 'Paris'

if __name__ == "__main__":
    pytest.main()
