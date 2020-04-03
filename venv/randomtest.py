import random

win_count=0
before=''
result =''

while True:

    com = random.randrange(0, 3)

    user = int(input("무엇을 낼것인가요"))

    if com-user<0:
        com = com+3

    if com-user ==2 :
        win_count = win_count+1
        print('승리')
        result=win_count

        if result==3:
            break

    elif com-user ==0 :
        print('무승부')

    else:
        print('패배')

        win_count=1
        win_count = win_count + 1
        result = win_count

        if result==3:
            break








