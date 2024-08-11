import random
#setting up a response dictionary.
responses = {
    "hi": ["hello!", "hi there!", "heyy!"],
    "hello":["hello!", "hi there!", "heyy!"],
    "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "whats your name": ["I'm a chatbot!", "You can call me ChatBot."],
    "what do you do": ["I'm here to chat with you!", "I'm a conversational agent."],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!",
    "I'm not good at jokes, but here's one: Why was the math book sad? Because it had too many problems."],
    "who created you": ["I was created by a team of developers.", "My creators prefer to be anonymous."],
    "what is the weather today": ["I'm sorry, I can't provide real-time information.",
    "You can check the weather on a weather website or an app."],
    "how old are you": ["I don't have an age. I'm just a program!", "I exist in the realm of ones and zeros, so I don't age."],
    "what is the meaning of life": ["The meaning of life is a philosophical question that has puzzled humans for centuries.",
    "I think the meaning of life is subjective and varies from person to person."],
    "had your breakfast": ["I'm sorry, but even fools know bots cannot eat breakfast.",
    "I can only eat the ones and zeros you feed me while programming."]
}

#function to return response.
def chatbot(user_input):
    if user_input.lower() in responses:
        return random.choice(responses[user_input.lower()])
    else:
        return "Sorry, I don't understand. Can you rephrase that?"

def main():
    print("Welcome to the ChatBot!")
    #enter user input, type "exit" to end conversation.
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
