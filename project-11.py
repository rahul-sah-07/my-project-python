# openAI Chat App
# use in python library pip install openai 


import openai

API_KEY = "YOUR_OPENAI_API_KEY"
openai.api_key = API_KEY
model_name = "gpt-3.5-turbo"

def chat_with_ai():
    print("OpenAI Chat App Started")
    print("Type 'exit' to quit\n")
    chat_history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chat Ended")
            break
        chat_history.append({"role": "user", "content": user_input})
        try:
            res = openai.ChatCompletion.create(
                model=model_name,
                messages=chat_history
            )
            ai_msg = res.choices[0].message["content"]
        except Exception as e:
            print("API Error:", e)
            continue
        chat_history.append({"role": "assistant", "content": ai_msg})
        print("AI:", ai_msg, "\n")

if __name__ == "__main__":
    chat_with_ai()
