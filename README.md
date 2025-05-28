# ⚡FastAPI Gemini AI Integration

A FastAPI-based REST API that seamlessly integrates with Google's Gemini AI model for content generation.

## Features

- Basic API endpoints for testing and demonstration
- Gemini AI content generation endpoint
- Environment variable configuration for API keys
- Request/Response model validation using Pydantic
- Built-in error handling and validation

## Prerequisites

- Python 3.x
- FastAPI
- dotenv
- requests

## Setup

1. Clone the repository
2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi dotenv requests uvicorn
```

4. Create a `.env` file in the root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Running the Application

Start the server using uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### GET / 
- Query Parameters:
  - `published` (optional, boolean, default=True)
  - `limit` (optional, integer, default=10)
- Returns a welcome message with configurable display options

### GET /about/{id}
- Path Parameters:
  - `id` (integer)
- Returns a personalized welcome message with the provided ID

### POST /generate
- Generates content using Gemini AI
- Request Body Schema:
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

The application includes robust error handling for:
- Missing API keys
- Failed API requests
- Invalid request formats
- Server-side errors

## Security Notes

- Never expose your Gemini API key in your code
- Add `.env` to your `.gitignore` file
- Use environment variables for all sensitive data

## Project Structure

```
├── main.py           # FastAPI application and route handlers
├── schemas.py        # Pydantic models for request/response validation
├── .env             # Environment variables (create this file)
└── README.md        # Project documentation
```