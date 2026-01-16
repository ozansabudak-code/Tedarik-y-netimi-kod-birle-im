def respond_to_greeting(message):
    greetings = ["merhaba", "selam", "hello"]
    for greeting in greetings:
        if greeting in message.lower():
            return f"{greeting.capitalize()}! How can I assist you today."
    return "Hello!"
