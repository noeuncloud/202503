import random
import easygui

answer = random.randint(1,100)
prediction = 0
times = easygui.buttonbox("Choose times for challenge",choices = ['5','6','7'])
times = int(times)

while prediction != answer and times >0 :
    prediction = easygui.integerbox("Enter your prediction number : ")

    if prediction < answer :
        easygui.msgbox("Lower than answer")
    elif prediction > answer :
        easygui.msgbox("Higher than answer")

    times = times-1
    print("You only have", times,"times Left\n")

if prediction == answer :
    easygui.msgbox("Answer!")
else :
    easygui.msgbox("No more chace. Answer is ", str(answer))
