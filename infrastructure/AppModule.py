from injector import provider, singleton, Binder, Module
from sqlite3 import Connection
import sqlite3
from phone_book.i_phone_book import IPhoneBook
from phone_book.phone_book import PhoneBook
from phone_book.phone_book_fake import PhoneBookFake
from database.phone_book_file_repository import PhoneBookFileRepository
from database.phone_book_sqlite_repository import PhoneBookSqliteRepository
from environment import Environment
from database.i_phone_book_repository import IPhoneBookRepository

class AppModule(Module):

    def __init__(self, environment: str):
        self.__environment = environment

    @provider
    @singleton
    def provide_sqlite3_connection(self) -> Connection:
        return sqlite3.connect("phone_book.db")


    def configure(self, binder: Binder):
        binder.bind(IPhoneBook,
                    to=(PhoneBookFake if self.__environment == Environment.DEVELOPMENT else PhoneBook), scope=singleton)

    @provider
    @singleton
    def provide_phonebook_repository(self, connection: Connection) -> IPhoneBookRepository: # Connection er sqlite
        if self.__environment == Environment.STAGING:
            return PhoneBookFileRepository("phone_book.json")
        elif self.__environment == Environment.PRODUCTION:
            return PhoneBookSqliteRepository(connection)



