class BankRepo:

    def __init__(self):
        self.bank_data = {}
        self.bank_data = {1234567898765432: 10000}

    def request(self, bill, cardNumber):
        if bill < self.bank_data[cardNumber]:
            self.bank_data[cardNumber] = self.bank_data[cardNumber] - bill
            return True
        else:
            return False
