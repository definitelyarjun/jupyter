import os
from fastapi import FastAPI, Depends
from typing import Optional
import requests
from dotenv import load_dotenv
import schemas
from models import ChatHistory
import db
from sqlalchemy.orm import Session

app = FastAPI()
load_dotenv()
db.create_table()

@app.get('/')
def intro(published: Optional[bool] = True, limit: int =10):
    if published:
       return {"data": f'Welcome to API Testing displaying {limit} values'}
    return {"data": 'Welcome to API Testing, no values displayed'}                                                                        

@app.get('/about/{id}')
def intro(id: int):
    return {"data": f'Welcome to API Testing {id}'}

@app.post('/generate')
def generate_response(model_request: schemas.ContentPart, db_session: Session = Depends(db.get_db)):
    #Manging API Key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        return {"error": "API key not found in environment variables"}

    #Model response
    response = requests.post(f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}', json=model_request.model_dump())
    user_query = model_request.model_dump() #for database usage
    if response.status_code == 200:
        gemini_response = response.json()
        new_entry = ChatHistory(query = user_query['contents'][0]['parts'][0]['text'], response = gemini_response['candidates'][0]['content']['parts'][0]['text'])
        db_session.add(new_entry)
        db_session.commit()
        db_session.refresh(new_entry)
        return gemini_response['candidates'][0]['content']['parts'][0]['text']
    return {"error": "Failed to generate content", "status_code": response.status_code, "details": response.text}
    
    
   