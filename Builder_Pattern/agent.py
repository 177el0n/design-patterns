from dataclasses import dataclass, field
from typing import Any, List

from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

@dataclass
class Agent:
    name: str = ""
    systemprompt: str = ""
    llm: Any = field(default=None)
    tools: List[Any] = field(default_factory=list)

    def __post_init__(self):
        self.agent = create_react_agent(
            self.llm,
            self.tools,
            prompt=self.systemprompt,
        )

    def act(self, state):
        result = self.agent.invoke(state)
        result["messages"][-1] = HumanMessage(
            content=result["messages"][-1].content,
            name=f"{self.name}"
        )
        update = {
            "messages": result["messages"]
        }
        return update
