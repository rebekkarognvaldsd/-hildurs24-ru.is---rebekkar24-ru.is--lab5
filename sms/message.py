from typing import Optional

from pydantic import BaseModel


class Message(BaseModel):
    name: str
    number: Optional[str]
    message: str
