# mytimemanager 0.1
# autor Bulat Valiakhmetov
# 17.12.2020

print("mytimemanager \n")
print(" a - add task \n s - show task \n t - take task \n")
tasklist = []
def entcommand():
    x = input("command ")
    if x == "a":
        add()
    elif x == "s":
        show()
    elif x == "t":
        take()
def add():
    y = input("task: ")
    save(y)
def save(x):
    tasklist.append(x)
def take():
    del tasklist[0]
    print("done!")
def show():
    print(tasklist)
while True:
    entcommand()
