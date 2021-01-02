# password generator
# author Bulat

import random
import json

print("password generator and save")
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
dicw = {}
def main():
    l = int(input("password length: "))
    generate(l)
def save(x):
    inp_q = input("save ? (y/n) ")
    if inp_q == "y":
        n = input("web-site: ")
        dicw[n] = x
        with open("passwords.json", "a") as file:
            json.dump(dicw, file)
            del dicw[n]
        print("save!")
def generate(x):
    p = ""
    for i in range(x):
        p += random.choice(s)
    print("password is {}".format(p))
    save(p)
while True:
    main()
