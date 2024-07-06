import time
from colorama import init, Fore, Style

# Initialize colorama
init()

password = 225577
balance = 1000

def check_balance():
    print(Fore.CYAN + f"Your Current Balance is = {balance}" + Style.RESET_ALL)
    time.sleep(2)

def withdraw_cash():
    global balance
    withdraw_amount = int(input(Fore.YELLOW + "Please Enter Your Withdraw Amount: " + Style.RESET_ALL))
    if withdraw_amount > balance:
        print(Fore.RED + "Insufficient Balance" + Style.RESET_ALL)
    else:
        balance -= withdraw_amount
        print(Fore.GREEN + f"{withdraw_amount} is debited from your account" + Style.RESET_ALL)
        print(Fore.CYAN + f"Your Current Balance is = {balance}" + Style.RESET_ALL)
    time.sleep(2)

def deposit_cash():
    global balance
    deposit_amount = int(input(Fore.YELLOW + "Please Enter Your Deposit Amount: " + Style.RESET_ALL))
    balance += deposit_amount
    print(Fore.CYAN + f"Your Updated Balance is = {balance}" + Style.RESET_ALL)
    time.sleep(2)

def exit_app():
    print(Fore.MAGENTA + "Thank You! Have a nice day!" + Style.RESET_ALL)
    time.sleep(2)
    exit()

def main_menu():
    while True:
        print(Fore.BLUE + "+++++++++++++++++++++++++++++++++")
        print("+ Press 1 for Balance           +")
        print("+ Press 2 for Withdraw the Cash +")
        print("+ Press 3 for Deposit the Cash  +")
        print("+ Press 4 for EXIT              +")
        print("+++++++++++++++++++++++++++++++++" + Style.RESET_ALL)

        try:
            option = int(input(Fore.GREEN + "Please Enter Your Choice: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Please Enter a Valid Option" + Style.RESET_ALL)
            time.sleep(2)
            continue

        if option == 1:
            check_balance()
        elif option == 2:
            withdraw_cash()
        elif option == 3:
            deposit_cash()
        elif option == 4:
            exit_app()
        else:
            print(Fore.RED + "Please Enter a Valid Option" + Style.RESET_ALL)
            time.sleep(2)

def main():
    print(Fore.CYAN + "Please Insert Your ATM CARD" + Style.RESET_ALL)
    time.sleep(2)
    print(Fore.YELLOW + "Loading....." + Style.RESET_ALL)
    time.sleep(3)

    pin_code = int(input(Fore.GREEN + "\t🔒Please Enter Your PIN :- " + Style.RESET_ALL))

    if pin_code != password:
        print(Fore.RED + "Wrong Pin, Please Try Again🛑" + Style.RESET_ALL)
        exit()
    else:
        main_menu()

if __name__ == "__main__":
    main()
