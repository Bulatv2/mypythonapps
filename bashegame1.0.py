# Bashe Game
# author Bulat

import random

print('Game Bashe. There are 11 items. Rivals go in turn, for each move \nany of the players can take 1, 2 or 3 items. \nLoses the one who is forced to take the last item.')
print('Игра Баше. 11 предметов. Соперники ходят по очереди, за каждый ход \nлюбой  из играющих может взять 1, 2 или 3 предмета. \nПроигрывает тот, кто вынужден \nвзять последний предмет.')

things = 11 # 11 things. The game can have 7, 11, 15, 19, 21, ... things.
first = 0

def main():
    global things
    user = int(input('Enter: number 1, 2 or 3: '))
    things -= user
    logic(user)
def printr(take):
    global things
    global first
    if things == 0:
        print("You win!")
        things = 11
        first = 0
    elif things == 1:
        print("You lost! Total left {}".format(things))
        things = 11
        first = 0
    else:
        print("The app took {}. Total left {}".format(take, things))
def logic(usertake):
    global things
    global first
    if things > 1:
        if first == 0:
            if usertake == 1:
                first = 1
                take = 1
                things -= take
                printr(take)
            elif usertake == 2:
                first = 1
                take = random.randint(1, 3)
                things -= take
                printr(take)
            elif usertake == 3:
                first = 1
                take = 3
                things -= take
                printr(take)
        else:
           take = winalgorithm(usertake)
           things -= take
           printr(take)
    elif things == 1:
        take = things - 1
        printr(take)
def winalgorithm(usertake):
    take = 4 - usertake
    return take
while True:
    main()
