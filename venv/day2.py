import time


#총수입 = 수입-지출
price = 5.0
people = 120
before = 0

while True:

#수입 = 티켓가격 * 관객수
    income = price * people
#지출 = 고정비용(180) + (관객수 * 0.4)
    outcome = 180 + (people*0.04)

    total = income - outcome


    if total> before:
        before = total

    else:

        break


    print(before,price,total)

    price=price-0.1
    people=people+15