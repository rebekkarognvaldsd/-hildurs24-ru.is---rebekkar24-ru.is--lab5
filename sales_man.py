from typing import List
from sms.message import Message
from sms.sms_sender import SmsSender
from phone_book.i_phone_book import IPhoneBook

class SalesMan:
    def __init__(self, sms_sender: SmsSender, phone_book: IPhoneBook):
        self.__sms_sender = sms_sender
        self.__phone_book = phone_book
        self.sent_messages: List[Message] = []
        self.failed_messages: List[Message] = []

    def send_message(self, name: str, message: str):
        try:
            number = self.__phone_book.lookup(name)
            self.__sms_sender.send(number, message)
            self.sent_messages.append(
                Message(name=name, number=number, message=message)
            )
        except KeyError:
            print("Failed to send message")
            self.failed_messages.append(
                Message(name=name, number=None, message=message)
            )
