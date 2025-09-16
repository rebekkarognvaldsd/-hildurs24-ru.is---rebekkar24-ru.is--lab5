from pydantic import BaseModel


class PhoneBookEntry(BaseModel):
    number: str
    name: str

