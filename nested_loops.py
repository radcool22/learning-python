for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [5, 2, 5, 2, 2]

for x in numbers:
    print("x" * x)  # Simple version using one for loop

for x in numbers:
    output=''
    for x in range(x):  # Detailed version using a nested loop
        output += 'x'
    print(output)