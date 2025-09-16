from abc import ABC, abstractmethod
from typing import Optional

from phone_book.phone_book_entry import PhoneBookEntry


class IPhoneBookRepository(ABC):
    @abstractmethod
    def save_entry(self, entry: PhoneBookEntry) -> None:
        pass 

    @abstractmethod
    def get_entry(self, name: str) -> Optional[PhoneBookEntry]:
        pass