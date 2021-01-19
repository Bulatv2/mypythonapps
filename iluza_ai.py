# Iluza AI
# author Bulat

print("Welcome to:\nIluza")
answer = ""
hello = "Hello, I am Iluza."
def sayai(answer):
    name = "Iluza"
    if answer == "":
        print("{}:{}".format(name, hello))
    else:
        print("{}:{}".format(name, answer))
    request()
def request():
    user = input("You: ")
    ai(user)
def ai(file):
    if file == "":
        sayai(hello)
    elif file == "Hello! how are you?":
        words = "I am fine! thank you."
    elif file == "Hello!":
        words = "How are you?"
    elif file == "I am ":
        words = "Nice to meet you."
    sayai(words)
def main():
    if answer == "":
        sayai(hello)
while True:
    main()
