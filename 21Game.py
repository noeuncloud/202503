import random
import easygui

# 사용자 이름 입력 받기
name = easygui.enterbox("What is your name?")
easygui.msgbox("OK, " + name + "\nLet's play the 21 game")

# 컴퓨터와 사용자 카드 뽑기
computer_card = random.randint(1, 21)
user_first_card = random.randint(1, 13)

choice = easygui.buttonbox("Your first card is " + str(user_first_card)+"\nDo you want more?", choices=['yes', 'no'])

# 사용자가 yes를 선택한 경우 
if choice == 'yes':
    user_second_card = random.randint(1, 13)
    user_total = user_first_card + user_second_card

    easygui.msgbox("Your second card is " + str(user_second_card)+"\nCheck your result")
   

    if user_total > 21:
        easygui.msgbox("Your final result is " + str(user_total) +".It is over 21, so you lose.\nComputer's card was " + str(computer_card))
    elif user_total > computer_card:
        easygui.msgbox("Your final result is " + str(user_total)+"\nComputer's card was " + str(computer_card)+"\nYou win!")
    elif user_total == computer_card:
         easygui.msgbox("Your final result is " + str(user_total)+"\nComputer's card was " + str(computer_card)+"\nIt's a tie!")
    else:
        easygui.msgbox("Your final result is" + str(user_total)+"\nComputer's card was " + str(computer_card)+"\nYou lose!")

# 사용자가 no를 선택한 경우
elif choice == 'no':
    user_total = user_first_card
    easygui.msgbox("OK, check your result")

    if user_total > computer_card:
        easygui.msgbox("Your final result is " + str(user_total)+"\nComputer's card was " + str(computer_card)+"\nYou win!")
    elif user_total == computer_card:
        easygui.msgbox("Your final result is " + str(user_total)+"\nComputer's card was " + str(computer_card)+"\nIt's a tie!")
    else:
        easygui.msgbox("Your final result is " + str(user_total)+"\nComputer's card was " + str(computer_card)+"\nYou lose!")