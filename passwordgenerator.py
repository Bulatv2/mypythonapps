import random

print("password generator and save")
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
p = ""
l = int(input("length: "))
def generate(x):
    global p
    for i in range(x):
        p += random.choice(s)
generate(l)
print("password is {}".format(p))
