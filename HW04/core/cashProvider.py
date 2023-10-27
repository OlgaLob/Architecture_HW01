from HW04.models.ticket import Ticket
from HW04.services.bankRepo import BankRepo


class CashProvider:
    def __init__(self):
        self.bancRepo = BankRepo()
        self.cardNumber = 0
        self.isAuthorized = False

    def buy(self, ticket: Ticket):
        if self.isAuthorized:
            return self.bancRepo.request(ticket.getPrice(), self.cardNumber)
        return False

    def authorization(self, client):
        self.cardNumber = client.getCardNumber()
        self.isAuthorized = True

        print(self.cardNumber, self.isAuthorized)
