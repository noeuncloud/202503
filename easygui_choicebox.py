import easygui
subjects = ["Understanding Computer Science","English reading","Writing"]
reply = easygui.choicebox("Which subject do you want to tack?",choices=subjects)
easygui.msgbox(reply+"is chosen.")
