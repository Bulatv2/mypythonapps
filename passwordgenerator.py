# password generator
# author Bulat

import random
import json

print("password generator and save")
s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2 = "abcdefghijklmnopqrstuvwxyz"
s3 = "0123456789"
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
    p1 = random.choice(s1)
    p2 = ""
    p3 = random.choice(s3)
    for i in range(x-2):
        p2 += random.choice(s2)
    p = p1 + p2 + p3
    print("password is {}".format(p))
    save(p)
while True:
    main()
