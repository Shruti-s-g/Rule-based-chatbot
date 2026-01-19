import datetime 
import time
name=input("Enter your name:")
presentHour=datetime.datetime.now().hour

if 5<=presentHour<=11:
    print("Good morning,",name)
elif 12<=presentHour<=17:
    print("Good afternoon",name)
elif 17<=presentHour<=20:
    print("Good evening",name)   
else:
    print("Good night",name)        

print("Welcome to rule-based chatbot")
print("You can ask me basic questions,Type 'bye' to exit from the bot")

#Chatbot Memory Creation[dictionary of responses]

responses={
    "hello":"Hi,welcome.How can I help you?",
    "how are you":"I am very fine.Thank you",
    "who are you":"I am smart AI chatbot",
    "motivate me":"Keep going.Every bug of your project makes you a better developer",
    "happy":"Great to hear that",
}

#Method/Function to get response of ChatBot
def getResponseBot(userQuestion):
    userQuestion=userQuestion.lower()
    for i in responses:
        if i in userQuestion:
            return responses[i]
   
    return "I am not able to tell that yet"    

#Take user input


while True:
    userInput=input("Please ask your question:")
    reply=getResponseBot(userInput)
    print("Bot Response:",reply)

    if "bye" in userInput.lower():
        break