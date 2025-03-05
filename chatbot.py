import nltk
from nltk.chat.util import Chat, reflections

# Ensure you have the necessary NLTK resources
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r'hi|hello|hey',
        ['Hello!', 'Hi there!', 'Hey! How can I help you?']
    ],
    [
        r'how are you?',
        ['I am just a computer program, but thanks for asking!', 'Doing well, how about you?']
    ],
    [
        r'what is your name?',
        ['I am a chatbot created using NLTK.', 'You can call me Chatbot!']
    ],
    [
        r'what can you do?',
        ['I can chat with you and answer your questions!', 'I can provide information and have a conversation.']
    ],
    [
        r'quit|exit',
        ['Goodbye! Have a great day!', 'See you later!']
    ],
    [
        r'(.*)',
        ['I am sorry, I do not understand that.', 'Can you please rephrase?']
    ]
]
# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the chatbot
print("Hi! I'm a chatbot. Type 'quit' or 'exit' to stop the conversation.")
chatbot.converse()
