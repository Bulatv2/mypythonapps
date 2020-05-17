# Bashe Game v1.0
# Игра Баше v1.0
# Bulat Valiakhmetov
# 16.5.2020
print('Game Bashe. There are 11 items. Rivals go in turn, for each move \n any of the players can take 1, 2 or 3 items. \n Loses the one who is forced to take the last item.')
print('Игра Баше. 11 предметов. Соперники ходят по очереди, за каждый ход \n любой  из играющих может взять 1, 2 или 3 предмета. \n Проигрывает тот, кто вынужден \n взять последний предмет.')
n = 11
# 11 things
c = 0
# for first step to know win algotithm 
u = 0
a = 0
# u - user take flag, a - app take flag
while n >= 4:
    i = int(input('Enter: number 1, 2 or 3: '))
    n -= i
    u += 1
    print('Total left: ', n)
    if n != 1:
        if n == 10 and i == 1:
            c = 1
            n -= c
            a = 1
            u = 0
        elif n == 9 and i == 2:
            c = 1
            n -= c
            a = 1
            u = 0
        elif n ==8 and i == 3:
            c = 3
            n -= c
            a = 1
            u = 0
        else:
            c = 4 - i
            n -= c
            a = 1
            u = 0
        print('The computer took: ', c)
        print('Total left: ', n)
if n == 1 and u == 1:
    print('You won!')
elif n == 1 and a == 1:
    print('You lost!')
