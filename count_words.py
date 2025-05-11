import easygui

sentence = easygui.enterbox("Write a sentence")
easygui.msgbox("You wrote ' %s '" %sentence)
words = sentence.split()
chosen = easygui.choicebox("choose your word to study", choices = words)
easygui.msgbox("Today's word :\n%s" %chosen)