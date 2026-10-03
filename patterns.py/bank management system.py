balance=100000
def deposit(amount):
    global balance
    balance+=amount
    print("depsosit",amount)
    print("updated amount",balance)
def withdraw(amount):
    global balance
    if amount<=balance:
        balance-=amount
    else:
        print("insufficient balance")
    print("withdraw amount",amount)
    print("updated balance:",balance)
def check_bal():
    print("current bank balance:",balance)
while True:
    print("1.deposit")
    print("2.withdraw")
    print("3.check_balance")
    print("4.Exit")
    choice=int(input("enter your option"))
    if choice==1:
        amount=int(input("enter the deposit amount:"))
        deposit(amount)
    elif choice==2:
        amount=int(input("enter the withdraw amont"))
        withdraw(amount)
    elif choice==3:
        check_bal()
    elif choice==4:
        print("thank you for visting")
        break
    else:
        print("please enter the valid option")
