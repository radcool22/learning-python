has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("You are eligible for a loan")

if has_high_income or has_good_credit:
    print("You are eligible for a loan")

if has_good_credit and not has_criminal_record:
    print("You are eligible for a loan")