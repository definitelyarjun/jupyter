# FastAPI Gemini AI Integration

A FastAPI-based REST API that integrates with Google's Gemini AI model to generate content.

## Features

- Basic API endpoints for testing and demonstration
- Gemini AI content generation endpoint
- Environment variable configuration for API keys
- Request/Response model validation using Pydantic

## Prerequisites

- Python 3.x
- FastAPI
- Pydantic
- python-dotenv
- requests

## Setup

1. Clone the repository
2. Install dependencies (Inside a virtual environment preferably):
```bash
pip install fastapi dotenv requests uvicorn
```
3. Create a `.env` file in the root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Running the Application

Start the server using uvicorn:

```bash
uvicorn main:app --reload
```

## API Endpoints

### GET /
- Query Parameters:
  - published (optional, boolean, default=True)
  - limit (optional, integer, default=10)
- Returns a welcome message

### GET /about/{id}
- Path Parameters:
  - id (integer)
- Returns a welcome message with the provided ID

### POST /generate
- Generates content using Gemini AI
- Request Body:
```json
{
    "contents": [
        {
            "parts": [
                {
                    "text": "Your prompt here"
                }
            ]
        }
    ]
}
```

## Error Handling

The application includes basic error handling for:
- Missing API keys
- Failed API requests
- Invalid request formats

## Security Notes

- Keep your Gemini API key secure
- Never commit the `.env` file to version control