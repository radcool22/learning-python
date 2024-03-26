names = ['John', 'Bob', 'Kabir', 'Sarah', 'Mary']
print(names[2:-1]) # Will print the terms from the third term till the last term

numbers = [1, 2, 3, 4, 5]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)