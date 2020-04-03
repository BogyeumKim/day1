import  random


count = 0

befroe = ''
winner = ''
while True:
    user = int(input("0,1,2"))
    com = random.randrange(0,3)

    if com<user:
        com = com+3

    gap = com-user


        if gap ==2:
            winner ='V'

        elif gap ==1:
            winner = 'C'
        elif gap == 0 :
            winner= 'D'
            continue


    # if gap==2:
    #     winner = 'V'
    # else:
    #     winner = 'C'


    if befroe!= winner:
        befroe= winner
        count =1

    else :
        count = count+1

    if count==3:
        break
