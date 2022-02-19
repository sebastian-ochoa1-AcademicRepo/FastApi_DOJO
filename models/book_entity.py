from typing import Optional
from pydantic import BaseModel


class BookEntity(BaseModel):
    isbn: str
    name: str
    synopsis: str
    author: str
    category: str
    edition: int
    
class BookEntityUpdate(BaseModel):
    name: Optional[str]
    synopsis: Optional[str]
    author: Optional[str]
    category: Optional[str]
    edition: Optional[int]