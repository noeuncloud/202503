balance = 100000
print("You have " +str(balance) +"won.")
amount = int(input("Write amount to deposit : "))

if amount <= balance :
    balance = balance - amount
    print("Current balance : ",balance)
else :
    print("Lack of balance")
