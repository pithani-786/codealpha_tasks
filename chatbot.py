def chatbot():
    print("Bot: Hello! I'm a simple chatbot. Type something to begin (type 'bye' to exit).")
    
    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for easy comparison
        
        if user_input == "hello":
            print("Bot: hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "what's your name":
            print("Bot: I'm just a chatbot created by Python")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

# Start the chatbot
chatbot()
