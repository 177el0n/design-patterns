from abstract_agent import AbstractAgent


class Director:

    def __init__(self, builder: AbstractAgent):
        self._builder = builder

    def construct(self, llm, tools=[]):
        self._builder.add_name("researcher")
        self._builder.add_systemprompt(
            """
            あなたは優秀な調査員です。
            必要な情報を適宜ツールを使用しながら回答を作成してください。
            """
            )
        self._builder.add_llm(llm)
        self._builder.add_tools(tools=tools)
        return self._builder.get_result()
