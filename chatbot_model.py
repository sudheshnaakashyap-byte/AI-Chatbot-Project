import random

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hi" or user_input == "hello":
        return "Hello! How can I help you?"
    
    elif "how are you" in user_input:
        return "I am fine! 😊"
    
    elif "what is ai" in user_input:
        return "AI stands for Artificial Intelligence."
    
    elif "what is python" in user_input:
        return "Python is a programming language."
    
    elif user_input == "thank you":
        return "You’re welcome 😊"
    
    elif user_input == "bye":
        return "Goodbye!"
    
    else:
        return "Sorry, I don't understand."