from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")


class BookSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True


"""
The parameter attribute in the RequestBook class in Python
specifies that the parameter
attribute should be a BookSchema object. The BookSchema
object is a Pydantic model that represents a book.
"""


class RequestBook(BaseModel):
    parameter: BookSchema = Field(...)


class Response(BaseModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
