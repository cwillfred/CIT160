loan=int(input("How large is the loan? "))
credit=int(input("How good is your credit history? "))
income=int(input("How high is your income? "))
down=int(input("How large is your down payment? "))

should_loan = False

if loan >= 5:
    if credit >= 7 and income >= 7:
        should_loan = True
    elif credit >= 7 or income >= 7:
        if down >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else:
    if credit < 4:
        should_loan = False
    else:
        if income >= 7 or down >= 7:
            should_loan = True
        elif income >= 4 and down >= 4:
            should_loan = True
        else:
            should_loan = False

if should_loan:
    print("The decision is yes. This is a good loan.")
else:
    print("The decision is no. You should not loan this money.")
