from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel
import requests
from dotenv import load_dotenv
import os

app = FastAPI()

@app.get('/')
def intro(published: Optional[bool] = True, limit: int =10):
    if published:
       return {"data": f'Welcome to API Testing displaying {limit} values'}
    return {"data": 'Welcome to API Testing, no values displayed'}                                                                        


@app.get('/about/{id}')
def intro(id: int):
    return {"data": f'Welcome to API Testing {id}'}

class TextPart(BaseModel):
    text: str

class Parts(BaseModel):
    parts: List[TextPart]

class ContentPart(BaseModel):
    contents: List[Parts]

@app.post('/generate')
def generate_response(model_request: ContentPart):
    # Manging API Key 
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        return {"error": "API key not found in environment variables"}
    request_url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}'
    ##
    # Model response
    response = requests.post(request_url, json=model_request.model_dump())
    if response.status_code == 200:
        gemini_response = response.json()
        return gemini_response['candidates'][0]['content']['parts'][0]['text']
    return {"error": "Failed to generate content", "status_code": response.status_code, "details": response.text}