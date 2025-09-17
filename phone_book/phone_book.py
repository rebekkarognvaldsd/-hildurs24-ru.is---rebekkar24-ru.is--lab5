from injector import inject
from database.i_phone_book_repository import IPhoneBookRepository
from phone_book.i_phone_book import IPhoneBook
from phone_book.invalid_number_exception import InvalidNumberException
from phone_book.phone_book_entry import PhoneBookEntry
from phone_book.phone_number_validator import PhoneNumberValidator


class PhoneBook(IPhoneBook):
    @inject
    def __init__(
        self,
        phone_book_repository: IPhoneBookRepository,
        validator: PhoneNumberValidator,
    ):
        self.__repository = phone_book_repository
        self.__validator = validator

    def add(self, entry: PhoneBookEntry) -> None:
        if self.__validator.validate(entry.number):
            self.__repository.save_entry(entry)
        else:
            raise InvalidNumberException()

    def lookup(self, name: str) -> str:
        entry = self.__repository.get_entry(name)
        if entry:
            return entry.number
        else:
            raise KeyError()
