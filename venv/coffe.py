from random import randrange


value = randrange(0,4)

current = 0

while True:
    input('마음에 준비를 하시고 Enter')


    print(current,value)

    if current == value:
        print('당첨')

    else:
        print('꽝')
    break

    current = current +1
