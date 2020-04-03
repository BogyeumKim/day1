import random

    min = 1
    max = 100

    while True:
        current = random.randrange(min, max)
        ##current = int((min+max) /2)

        print(current)

        answer = input("H,L,C")

    print(answer)

    if answer== 'C':
        print('정답')
    elif answer=='H':
        min = current
    elif answer=='L':
        max = current

