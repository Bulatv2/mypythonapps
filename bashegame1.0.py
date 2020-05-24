# Bashe Game v1.0
# Игра Баше v1.0
# Bulat Valiakhmetov
# 16.5.2020

import random
print('Game Bashe. There are 11 items. Rivals go in turn, for each move \n any of the players can take 1, 2 or 3 items. \n Loses the one who is forced to take the last item.')
print('Игра Баше. 11 предметов. Соперники ходят по очереди, за каждый ход \n любой  из играющих может взять 1, 2 или 3 предмета. \n Проигрывает тот, кто вынужден \n взять последний предмет.')
k = 11
# 11 things. The game can have 7, 11, 15, 19, 21, ... things.
c = 0
# how much things should take, how much take and for win algorithm for app
u = 0
a = 0
# u - user last take flag == 1, a - app last take flag == 1
while k > 1:
    userwr = int(input('Enter: number 1, 2 or 3: '))
    k -= userwr
    u = 1
    print('Total left: ', k)
    if k >= 1:
        # first step to know how to get win algorithm for app
        if a != 1 and userwr == 1:
            c = 4 - userwr
            # how to count for app
            c = 1
            k -= c
            # app's step
            a = 1
            u = 0
        elif a != 1 and userwr == 2:
            c = random.randint(1, 3) 
            k -= c
            # app's step
            a = 1
            u = 0
        elif a != 1 and userwr == 3:
            c = 3
            k -= c
            # app's step
            a = 1
            u = 0
        elif k >= 4:
            c = 4 - userwr
            k -= c
            # app's step
            a = 1
            u = 0
        elif k == 3:
            c = 2
            k -= c
            # app's step
            a = 1
            u = 0
        elif k == 2:
            c = 1
            k -= c
            # app's step
            a = 1
            u = 0
        elif k == 1:
            continue
    print('The app took: ', c)
    print('Total left: ', k)
print()
if k == 1 and u == 1:
    print('You won!')
elif k == 1 and a == 1:
    print('You lost!')
