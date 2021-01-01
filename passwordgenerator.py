# password generator
# autor Bulat
import random
import json
print("password generator and save")
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
p = ""
dicw = {}
def main():
    ffi()
def save():
    n = input("web-site: ")
    dicw[n] = p
    with open("passwords.json", "a") as file:
        json.dump(dicw, file)
        del dicw[n]
        print("save!")
def ffi():
    l = int(input("password length: "))
    generate(l)
def generate(x):
    global p
    for i in range(x):
        p += random.choice(s)
    print("password is {}".format(p))
    n = input("save password (y/n)? ")
    if n == "y":
        save()
    elif n == "n":
        main()
while True:
    main()
