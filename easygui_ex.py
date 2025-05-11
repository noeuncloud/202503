import easygui

selected_language = easygui.buttonbox("What is your favorite programming language?",
                                      choices = ['C','Java','Python'])
easygui.msgbox("You picked" +selected language)
