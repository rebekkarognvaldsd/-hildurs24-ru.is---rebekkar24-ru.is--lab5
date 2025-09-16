from phone_book.invalid_number_exception import InvalidNumberException
from phone_book.phone_book_entry import PhoneBookEntry
from phone_book.i_phone_book import IPhoneBook
from phone_book.phone_number_validator import PhoneNumberValidator


class PhoneBookFake(IPhoneBook):
    def __init__(self, validator: PhoneNumberValidator):
        self.__validator = validator
        self.__phone_numbers = {}

    def add(self, entry: PhoneBookEntry) -> None:
        if self.__validator.validate(entry.number):
            self.__phone_numbers[entry.name] = entry.number
        else:
            raise InvalidNumberException()

    def lookup(self, name: str) -> str:
        return self.__phone_numbers[name]
