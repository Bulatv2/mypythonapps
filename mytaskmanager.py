# mytaskmanager
# author Bulat

print("mytaskmanager \n")
print(" a - add task \n s - show task \n t - take task \n d - done task \n h - help\n")
tasklist = []
def main():
    cd = input("command ")
    if cd == "a":
        add()
    elif cd == "s":
        show()
    elif cd == "t":
        take()
    elif cd == "h":
        help()
    elif cd == "q":
        quit()
def add():
    task = input("task: ")
    save(task)
def save(task):
    tasklist.append(task)
def take():
    print("{} is done.".format(tasklist[0]))
    del tasklist[0]
def show():
    print("to do:")
    for i in range(len(tasklist)):
        print(tasklist[i])
def help():
    print("this is taskmanager.")
while True:
    main()
