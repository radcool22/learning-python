weight = int(input("What is your weight? "))
unit = input("(L)bs or (K)gs: ")

if unit.lower() == 'l':
    print("You are " + str(round(int(weight) * 0.45)) + " kilograms")
elif unit.lower() == "k":
    print("You are " + str(round(int(weight) / 0.45)) + " pounds")
else:
    print("Please enter a valid unit")