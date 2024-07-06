import time
print("Please Insert Your ATM CARD")
time.sleep(2)
print("Loading.....")
time.sleep(3)

password = 225577
balance = 1000

pin_code = int(input("\t🔒Please Enter Your PIN :- "))

if pin_code != password:
    print("Wrong Pin, Please Try Again🛑")
    exit()

while True:
    print("Press 1 for Balance")
    print("Press 2 for Withdraw the Cash")
    print("Enter Press 3 for Deposit the Cash")
    print("Enter Press 4 for EXIT")

    try:
        option = int(input("Please Enter Your Choice: "))
    except ValueError:
        print("Please Enter a Valid Option")
        print("===================================================")
        continue

    if option == 1:
        print(f"Your Current Balance is = {balance}")
        print("===================================================")
    elif option == 2:
        withdraw_amount = int(input("Please Enter Your Withdraw Amount: "))
        if withdraw_amount > balance:
            print("Insufficient Balance")
        else:
            balance -= withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"Your Current Balance is = {balance}")
        print("===================================================")
    elif option == 3:
        deposit_amount = int(input("Please Enter Your Deposit Amount: "))
        balance += deposit_amount
        print(f"Your Updated Balance is = {balance}")
        print("===================================================")
    elif option == 4:
        print("Thank You! ")
        break
    else:
        print("Please Enter a Valid Option")
        print("===================================================")
