from abc import ABC, abstractmethod
from typing import List
from HW04.models.ticket import Ticket


class ITicketRepo(ABC):

    @abstractmethod
    def readAll(self, routeNumber: int) -> List[Ticket]:
        pass