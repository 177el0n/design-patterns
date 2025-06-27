from langgraph.graph import MessagesState, StateGraph, START, END


from agent_builder import AgentBuilder
from director import Director

def main():
    builder = AgentBuilder()
    director = Director(builder)
    agent = director.construct(llm)
    
    user_prompt = str(input())
    workflow = StateGraph(MessagesState)
    workflow.add_node("agent", agent.act)
    workflow.add_edge(START, "agent")
    workflow.add_edge("agent", END)

    graph = workflow.compile()
    result = graph.invoke(
        {
            "messages": [("user", user_prompt)]
        }
    )
    print(result)

if __name__ == "__main__":
    main()
