import re
import random

def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey", "hola", "greetings"]
    goodbyes = ["bye", "goodbye", "see you", "exit"]
    thanks = ["thank you", "thanks", "appreciate it"]
    
    # Pattern matching responses
    if any(word in user_input for word in greetings):
        return random.choice(["Hello! 😊", "Hi there! 👋", "Hey! How can I assist you?"])

    elif any(word in user_input for word in goodbyes):
        return random.choice(["Goodbye! Have a great day! 😊", "See you soon! 👋", "Take care!"])

    elif any(word in user_input for word in thanks):
        return random.choice(["You're welcome! 😊", "Happy to help! 👍", "Anytime! 😃"])

    elif re.search(r"\bhow are you\b", user_input):
        return random.choice(["I'm just a bot, but I'm doing great! 😊", "Feeling fantastic! How about you?"])

    elif re.search(r"\bname\b", user_input):
        return "I'm ChatBuddy, your friendly assistant bot! 🤖"

    elif re.search(r"\b(what can you do|help)\b", user_input):
        return "I can chat with you, answer basic questions, and keep you entertained! 😊 Ask me anything!"

    elif re.search(r"\b(joke|funny)\b", user_input):
        jokes = [
            "Why don’t scientists trust atoms? Because they make up everything! 😂",
            "What do you call fake spaghetti? An impasta! 🍝🤣",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾😆"
        ]
        return random.choice(jokes)

    elif re.search(r"\b(weather|temperature)\b", user_input):
        return "I can't check the weather right now, but you can ask me anything else! ☁️🌞"

    else:
        return random.choice([
            "I'm not sure I understand. Can you rephrase? 🤔",
            "Hmm... I don't have an answer for that yet. Ask me something else! 😊",
            "Interesting! Tell me more. 🤖"
        ])

# Chat loop
print("🤖 ChatBuddy: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "goodbye"]:
        print("🤖 ChatBuddy:", chatbot_response(user_input))
        break
    else:
        print("🤖 ChatBuddy:", chatbot_response(user_input))
