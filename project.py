print("Welcome to Python ATM!")

pin = int(input("Enter Pin: "))
balance = float(input("Enter Your Balance: "))

print("ATM Setup Complete!")

entered_pin = int(input("Enter Your PIN: "))

if entered_pin != pin:
    print("Invalid pin! Access Denied")
else:
    while True:
        print("------------ATM Menu------------")
        print("1.Check Balance \n 2.Deposit Money \n 3.Withdraw Money \n 4.Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            print(f"Current balance: Rs.{balance}")

        elif choice == 2:
            amount = float(input("Enter Deposit Amount: "))
            if amount>0:
                balance+=amount
                print(f"Rs.{amount} deposited succesfully!")
            else:
                print("Invalid deposit Amount!")

        elif choice == 3:
            amount = float(input("Enter Withdrawal Amount: "))
            if amount<=0:
                print("Enter Valid Amount!")
            elif amount>balance:
                print("Insufficient Funds!")
            else:
                balance-=amount
                print(f"Rs.{amount} withdrawn succesfully!")

        elif choice == 4:
            print("Thank you for using python ATM!")
            break

        else:
            print("Invalid Choice! Please Try again.")