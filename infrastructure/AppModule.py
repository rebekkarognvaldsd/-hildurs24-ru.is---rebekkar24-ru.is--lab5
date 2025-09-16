from injector import provider, singleton, Binder
from sqlite3 import Connection
import sqlite3
from phone_book.i_phone_book import IPhoneBook
from phone_book.phone_book import PhoneBook
from phone_book.phone_book_fake import PhoneBookFake
from database.i_phone_book_repository import IPhoneBookRepository
from database.phone_book_file_repository import PhoneBookFileRepository
from database.phone_book_sqlite_repository import PhoneBookSqliteRepository

class AppModule():

    def __init__(self, environment: str):
        self.__environment = environment

    @provider
    def provide_sqlite3_connection(self) -> Connection:
        return sqlite3.connect("phone_book.db")


    def configure(self, binder: Binder):
        binder.bind(IPhoneBook,
                    to=(PhoneBookFake if self.__environment == "developement" else PhoneBook))

    @provider
    def provide_phonebook_repository(self, connection: Connection): # Connection er sqlite
        if self.__environment == Environment.STAGING:
            return PhoneBookFileRepository("phone_book.json")
        elif environment == Environment.PRODUCTION:
            # connection = sqlite3.connect("phone_book.db")
            repository = PhoneBookSqliteRepository(connection)

    # def configure(self, binder: Binder):
    #     binder.bind(IPhoneBookRepository,
    #                 to=(PhoneBookFileRepository if self.__environment == "staging" else PhoneBookSqliteRepository))

