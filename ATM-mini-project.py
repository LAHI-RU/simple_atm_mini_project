import time
print("Please Insert Your ATM CARD")
time.sleep(2)
print("Loading.....")
time.sleep(3)
password = 225577
pin_code = int(input("Please Enter Your PIN "))
balance = 0
if pin_code == password:
    pass
print("Enter Press 1 for Balance ")
print("Enter Press 2 for Withdraw the Cash ")
print("Enter Press 3 for Deposit the Cash ")
print("Enter Press 4 for EXIT ")

try:
    option = int(input("Please Enter Your Choice: "))

except Exception as e:
    print("Please Enter Valid Option")
    if option == 1:
        print(f"Your Current Balance is = {balance}")

    if option == 2:
        withdraw_amount = int(input("Please Enter Your Withdraw Amount: "))
        balance = balance - withdraw_amount
        print(f"{withdraw_amount} is debited from your account")
        print(f"Your Current Balance is = {balance}")

    if option == 3:
        deposit_amount = int(input("Please Enter Your Deposit Amount: "))
        balance = balance + deposit_amount
        print(f"Your Updated Balance is = {balance}")

    if option == 4:
        print("Thank You! ")
        exit()


