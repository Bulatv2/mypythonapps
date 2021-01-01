# mytaskmanager 0.1
# autor Bulat

print("mytaskmanager \n")
print(" a - add task \n s - show task \n t - take task \n h - help\n")
tasklist = []
def main():
    x = input("command ")
    if x == "a":
        add()
    elif x == "s":
        show()
    elif x == "t":
        take()
    elif x == "h":
        help()
    elif x == "q":
        quit()
def add():
    y = input("task: ")
    save(y)
def save(x):
    tasklist.append(x)
def take():
    print("{} done!".format(tasklist[0]))
    del tasklist[0]
def show():
    print("to do :")
    for i in range(len(tasklist)):
        print(tasklist[i])
def help():
    print("this is taskmanager.")
while True:
    main()
