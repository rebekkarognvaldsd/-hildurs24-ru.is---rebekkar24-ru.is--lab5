import sqlite3
from injector import inject
from typing import Optional
from database.i_phone_book_repository import IPhoneBookRepository
from phone_book.phone_book_entry import PhoneBookEntry

class PhoneBookSqliteRepository(IPhoneBookRepository):
    @inject
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.__connection = connection
        cursor = self.__connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS phone_book (
                name TEXT PRIMARY KEY,
                number TEXT
            )
        """)
        self.__connection.commit()

    def save_entry(self, entry: PhoneBookEntry) -> None:
        cursor = self.__connection.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO phone_book (name, number) VALUES (?, ?)
        """, (entry.name, entry.number))
        self.__connection.commit()

    def get_entry(self, name: str) -> Optional[PhoneBookEntry]:
        cursor = self.__connection.cursor()
        cursor.execute("""
            SELECT name, number FROM phone_book WHERE name = ?
        """, (name,))
        result = cursor.fetchone()
        if result:
            return PhoneBookEntry(name=result[0], number=result[1])
        else:
            return None
