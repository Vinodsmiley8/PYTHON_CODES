# Create a basic chatbot using natural language processing
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['hi|hello', ['Hi there!', 'Hello!', 'Hey!']],
    ['how are you', ['I am good, thank you.', 'I am doing well. How about you?']],
    ['(.*)(good|well)', ['That\'s great!', 'Good to hear that.']],
    ['bye|goodbye', ['Goodbye!', 'Bye!', 'See you later!']],
]

chatbot = Chat(pairs, reflections)
chatbot.converse()