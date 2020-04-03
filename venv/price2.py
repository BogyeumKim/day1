price = 5
people = 120
before = 0

while True:

    income = price * people
    outcome = 180+(people*0.04)

    total=income-outcome
    print('total:','before:',before,'price',price)
    if total > before:
        before= total
        break
    else:
        break





