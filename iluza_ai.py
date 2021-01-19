# Iluza AI
# author Bulat

print("Welcome to:\nIluza")
words = ""
hello = "Hello, I am Iluza."
def sayai(words):
    name = "Iluza"
    if words == "":
        print("{}: {}".format(name, hello))
    else:
        print("{}: {}".format(name, words))
    request()
def request():
    user = input("You: ")
    ai(user)
def ai(file):
    if file == "":
        sayai(hello)
    elif file == "How are you?":
        words = "I am good! thank you."
    elif file == "Hello!":
        words = "How are you?"
    elif file == "I am good! thank you.":
        words = "Ok."
    sayai(words)
sayai(words)
