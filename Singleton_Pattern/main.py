from llm_client import LLMClient

def main():
    while True:
        print("If you want to exit, type 'exit'.")
        user_prompt = input("Please enter your prompt: ")
        if user_prompt.strip().lower() == 'exit':
            print("Exiting the program.")
            break
        llm_client = LLMClient()
        result = llm_client.invoke(
            [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user","content": user_prompt}
            ]
        )
        print(result.content)

if __name__ == "__main__":
    main()
