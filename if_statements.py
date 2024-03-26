is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')
else:
    print("It's a lovely day")

print("Enjoy your day")

good_credit = False
price = 1000000

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print("You need to put down " + str(round(down_payment)) + " dollars in down payment")