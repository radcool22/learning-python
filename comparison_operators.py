temperature = input('What is the temperature right now? ')

if int(temperature) > 30:
    print("It's a hot day")
elif int(temperature) < 10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")

name = input('What is your name? ')

if len(name) < 3:
    print("Your name must be more than 3 characters long")
elif len(name) > 50:
    print("Your name must be less than 50 characters long")
else:
    print("Looks good!")