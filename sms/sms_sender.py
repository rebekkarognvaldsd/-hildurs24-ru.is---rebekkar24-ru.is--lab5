class SmsSender:
    def send(self, number: str, message: str):
        print(f'sending "{message}" to {number}')