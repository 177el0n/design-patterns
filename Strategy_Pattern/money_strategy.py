from abc import ABC, abstractmethod

class MoneyStrategy(ABC):
    @abstractmethod
    def how_mach(amount: int) -> int:
        pass
