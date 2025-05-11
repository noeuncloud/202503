balance = 0

for month in range (1, 36, 2) :
    balance =balance + 50000
    print("%2d month, " %month
          + "current ; " + str(balance) +"won")

print("\nTotal Balance : "+ str(balance))
