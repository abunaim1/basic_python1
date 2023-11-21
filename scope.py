balance = 3000
def buy_things(item, price):
    # local variable scope
    # i can access global variable without using global keyword
    # but if i want to modify global variable, i have to use the global keyword
    global balance
    print(f'previous balance value: ', balance)
    balance = balance - price
    print(f'balance after buying {item}: ', balance)

buy_things('Sunglass', 1000)