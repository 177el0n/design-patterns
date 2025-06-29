from abc import ABC, abstractmethod

class HelloWorld(ABC):

    @abstractmethod
    def hello(self):
        pass
