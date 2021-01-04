# mytaskmanager
# author Bulat

import json
print("mytaskmanager \n")
print(" a - add task \n s - show task \n t - take task \n d - done task \n h - help\n")
tasklist = []
progresslist = []
donelist = []
def main():
    x = input("command ")
    if x == "a":
        add()
    elif x == "s":
        show()
    elif x == "t":
        take()
    elif x == "d":
        done()
    elif x == "h":
        help()
    elif x == "q":
        quit()
def add():
    y = input("task: ")
    save(y)
    tsave(y)
def save(x):
    tasklist.append(x)
def take():
    progresslist.append(tasklist[0])
    del tasklist[0]
    print("ok")
def done():
    donelist.append(progresslist[0])
    del progresslist[0]
    print("{} is done".format(donelist[0]))
def show():
    if len(tasklist) == 0 and len(donelist) == 0:
        with open("tasks.txt", "r") as file:
            for line in file:
                print(line)
    else:
        print("to do:")
        for i in range(len(tasklist)):
            print(tasklist[i])
        if len(progresslist) != 0:
            print("doing:")
            for i in range(len(progresslist)):
                print(progresslist[i])
                if len(donelist) != 0:
                    print("done:")
                    for i in range(len(donelist)):
                        print(donelist[i]) 
def help():
    print("this is taskmanager.")
def tsave(x):
    with open("tasks.txt", "a") as file:
        file.write("{}\n".format(x))
while True:
    main()

