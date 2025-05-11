balance = 0

month = 1

while month<36 :
    balance = balance + 50000
    print("%2d month, "%month
          + "current : "+str(balance) + "won")
    month +=2

print("\nTotal Balance : "+str(balance))
