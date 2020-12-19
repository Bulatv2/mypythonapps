# mytaskmanager 0.1
# autor Bulat Valiakhmetov
# 17.12.2020

print("mytaskmanager \n")
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
    print("{} done!".format(tasklist[0]))
    del tasklist[0]
def show():
    for i in range(len(tasklist)):
        print(tasklist[i])
while True:
    entcommand()
