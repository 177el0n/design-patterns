from abc import ABC, abstractmethod

class AbstractAgent(ABC):

    @abstractmethod
    def add_name(self, name):
        pass

    @abstractmethod
    def add_systemprompt(self, systemprompt):
        pass

    @abstractmethod
    def add_llm(self, llm):
        pass

    @abstractmethod
    def add_tools(self, tools):
        pass

    @abstractmethod
    def get_result(self):
        pass
