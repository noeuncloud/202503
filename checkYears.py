while True:
    print("======Check Year Program======")
    print("       1.Check Leap Year")
    print("       2.Check total day")
    print("       3.Exit")
    print("===============================")

    select = int(input("Select : "))

    if select == 1:
        year = int(input("Enter year to check : "))
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            print(year,"is leap year.\n")
        else:
            print(year,"is not leap year.\n")

    elif select == 2:
        print("Enter month and date")
        month = int(input("Month : "))
        date = int(input("Date : "))
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        total_days = 0
        for i in range(1, month):
            total_days += days_in_month[i - 1]
        total_days += date
        print("2028.%d.%d is %dth day in 2028.\n" % (month, date, total_days))

    elif select == 3:
        print("Thanks for using program.")
        break
    
    else:
        print("잘못된 메뉴 선택입니다. 다시 시도해주세요.\n")


