from pydantic import BaseModel
from typing import List

class TextPart(BaseModel):
    text: str

class Parts(BaseModel):
    parts: List[TextPart]

class ContentPart(BaseModel):
    contents: List[Parts]