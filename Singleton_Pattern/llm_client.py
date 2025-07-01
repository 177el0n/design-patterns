from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

class LLMClient(object):
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not LLMClient._initialized:
            self.client = ChatOpenAI(
                model="gpt-3.5-turbo",
                temperature=0.7,
                max_tokens=1000,
                top_p=1.0,
            )
            LLMClient._initialized = True
    
    def invoke(self, messages):

        input = {
            "messages": messages
        }
        result = self.client.invoke(input)
        return result
