import json
from typing import Optional
from database.i_phone_book_repository import IPhoneBookRepository
from phone_book.phone_book_entry import PhoneBookEntry

class PhoneBookFileRepository(IPhoneBookRepository):
    def __init__(self, file_path: str) -> None:
        self.__file_path = file_path
        self.__entries = {}
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for entry_data in data:
                    entry = PhoneBookEntry(**entry_data)
                    self.__entries[entry.name] = entry
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

    def save_entry(self, entry: PhoneBookEntry) -> None:
        self.__entries[entry.name] = entry
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            data = [entry.dict() for entry in self.__entries.values()]
            json.dump(data, file, indent=4)

    def get_entry(self, name: str) -> Optional[PhoneBookEntry]:
        return self.__entries.get(name)
