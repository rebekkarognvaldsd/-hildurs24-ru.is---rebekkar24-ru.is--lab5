from abc import ABC, abstractmethod

from phone_book.phone_book_entry import PhoneBookEntry


class IPhoneBook(ABC):
    @abstractmethod
    def add(self, entry: PhoneBookEntry) -> None:
        pass

    @abstractmethod
    def lookup(self, name: str) -> str:
        pass
