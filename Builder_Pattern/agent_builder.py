
from abstract_agent import AbstractAgent
from agent import Agent


class AgentBuilder(AbstractAgent):
    def __init__(self):
        self._name = ""
        self._systemprompt = ""
        self._llm = None
        self._tools = []
    
    def add_name(self, name):
        self._name = name

    def add_systemprompt(self, systemprompt):
        self._systemprompt = systemprompt

    def add_llm(self, llm):
        self._llm = llm
    
    def add_tools(self, tools):
        self._tools = tools
    
    def get_result(self):
        return Agent(
            name=self._name,
            systemprompt=self._systemprompt,
            llm=self._llm,
            tools=self._tools
        )
