from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os
from sqlalchemy.orm import Session
from models import SessionLocal, QuestionAnswer, create_tables

# Load environment variables from .env file
load_dotenv()

# Create Flask application
app = Flask(__name__)

# Set OpenAI API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')
print(f"Loaded OpenAI API key: {api_key}")
openai.api_key = api_key

# Create database tables
create_tables()

@app.route('/')
def index():
    return "Flask server is running. Use POST /ask to ask questions."

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')
    
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    
    answer = None
    try:
        print(f"Received question: {question}")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        print(f"Response from OpenAI: {response}")
        
        if response['choices']:
            answer = response['choices'][0]['message']['content'].strip()
            print(f"Answer from OpenAI: {answer}")

    except Exception as e:
        print(f"Error: {e}")
        answer = f"Error: {e}"
    
    # Save question and answer (or error) to the database
    try:
        db: Session = SessionLocal()
        qa = QuestionAnswer(question=question, answer=answer)
        db.add(qa)
        db.commit()
        db.refresh(qa)
        print(f"Saved to database: {qa}")
    except Exception as db_error:
        print(f"Database error: {db_error}")
    
    return jsonify({'question': question, 'answer': answer})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
