
import nltk
from nltk.chat.util import Chat, reflections

# Define the conversation rules
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created with NLTK.",]
    ],
    [
        r"how are you",
        ["I'm doing well, thank you!",]
    ],
    [
        r"(.*) (weather|temperature) in (.*)",
        ["I'm sorry, I cannot provide real-time weather information.",]
    ],
    [
        r"quit",
        ["Goodbye!", "Have a great day!"]
    ],
]

# Create and start the chatbot
def chatbot():
    print("AI: Hi, I'm a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()