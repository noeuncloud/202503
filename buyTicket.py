import easygui

easygui.msgbox("Welcome to buy lunch ticket! \n" \
"(Lunch : 11:00 - 15:00)")

koreandish=3500
westerndish=4000
chinesedish=3000
japanesedish=4500
total=0

while True:
    choice = easygui.buttonbox("Choose lunch menu to buy",
                  choices=["Korean dish","Western dish","Chinese dish","Japanese dish","Exit"])

    if choice=="Korean dish":
        a = int(easygui.enterbox("Korean dish is %d won.\nHow many tickets do you want to buy?" %koreandish))
        total = total + koreandish * a

    elif choice=="Western dish":
        b = int(easygui.enterbox("Western dish is %d won.\nHow many tickets do you want to buy?" %westerndish))
        total = total + westerndish * b

    elif choice=="Chinese dish":
        c = int(easygui.enterbox("Chinese dish is %d won.\nHow many tickets do you want to buy?" %chinesedish))
        total = total + chinesedish * c

    elif choice=="Japanese dish":
        d = int(easygui.enterbox("Japanese dish is %d won.\nHow many tickets do you want to buy?" %japanesedish))
        total = total + japanesedish * d

    elif choice=="Exit":
        easygui.msgbox("Total amount to pay : %d \nThanks for using!" %total)
        break
