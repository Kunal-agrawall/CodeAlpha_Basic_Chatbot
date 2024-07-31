import spacy
from random import choice

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Predefined responses
responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Hey! How's it going?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "default": ["I'm not sure I understand. Can you please elaborate?", "Could you please rephrase that?", "I'm here to help, but I need more information."]
}

# Function to classify user input
def classify_text(text):
    doc = nlp(text.lower())
    if any(token.lemma_ in ["hello", "hi", "hey"] for token in doc):
        return "greeting"
    elif any(token.lemma_ in ["bye", "goodbye", "see you"] for token in doc):
        return "goodbye"
    elif any(token.lemma_ in ["thank", "thanks"] for token in doc):
        return "thanks"
    else:
        return "default"

# Chatbot function
def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response_type = classify_text(user_input)
        response = choice(responses[response_type])
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
