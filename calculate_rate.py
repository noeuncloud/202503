name = input("Write your name : ")
voice = int(input("Enter the amount of call times(s) : "))
data = float(input("Enter the amount of data usage(MB) : "))

total = 12100+(voice*1.98) +(data*55)
print(name,"'s chare for using : ",total)
