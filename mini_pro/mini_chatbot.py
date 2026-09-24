from ollama import chat 
print("WELCOME VANDY!!! HOPING TO HAVE A GREAT CONVERSATION....")
system_msg = "you are a journalist,answer like a news reader,in just one line "
while True:
    question= input("Ask a question")
    if question == "":
        print("Luna🌙:Please type something!!!")
    if question.lower().strip() == "exit":
        print("Luna🌙: See you soon vandy...please come back soon!🤧🤧🤧")
        break
    try:
        response = chat(
            model = "llama3.2",
            messages = [
                {
                    "role": "user",
                    "content": question
                },
                {
                    "role" : "system",
                    "content" : system_msg
                }
            ]
        )
        print(f"Luna🌙:{response['message']['content']}")
    except Exception as e:
        print(f"Luna🌙:Something went wrong....{e}")
