import datetime

def get_response(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I help you today?"
    elif 'name' in user_input:
        return "I'm your friendly chatbot."
    elif 'time' in user_input:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."
    elif 'date' in user_input:
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%B %d, %Y')}."
    elif 'how are you' in user_input:
        return "I'm doing great! Thanks for asking."
    elif user_input in ['bye', 'exit', 'quit']:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I didn't understand that."

print("Chatbot: Hello! Type something to begin. (Type 'bye' to exit)")

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Chatbot:", response)
    
    if user_input.lower() in ['bye', 'exit', 'quit']:
        break
