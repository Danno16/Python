from PC_1_1_Tools import *
from math import *
def lesson_1():

    def title():
        new_page()
        print("                                -----------------------------    Lesson 1 - How to Print in Python    -----------------------------")

    def definition():
        title()
        print("Welcome to Python.  In our first lesson, we are going to start off easy by doing some simple print"
              " commands.  We are going to:\n")
        print("                        Print a couple of Sentences.")
        print("                        Print a Triangle.")
        print("  \n\nAbout using this Lesson Plan.  At the bottom of the screen, we will have options to review "
              "the description of the lesson, Running all the lessons included in that lesson, or you can select,"
              "what lesson you want to run."
              "\nThe last option is to press <Enter> to return to the main menu.  Hope you have fun!!!.")
        end()


    def EX1():
        title()
        print("                                                             ****  Exercise 1 -  Simple Print Commands  **** \n ")
        print("In order to print something on the screen you have to use the following command: "
              "\nCode we used:"
              "\n       print(\"Hello World\")")
        print("\n Here is the Output:"
              "\n               Hello World")
        print(
            "\nNow Lets try it again.  Lets print - \'How are you doing?\"."
            "\nCode we used:"
            "\n         print(\"How are you doing?\")")
        print("\n Here is the Output:"
              "\n               How are you doing?")

    def EX2():
        title()
        print("                                                             ****  Exercise 2 -  Complex Print Commands  **** \n ")
        print(
            "           Now were going to try something a little more complex.  Were going to make a half triangle using the following code:")

        print("print(\"      /|\")")
        print("print(\"     / |\")")
        print("print(\"    /  |\")")
        print("print(\"   /   |\")")
        print("print(\"  /    |\")")
        print("print(\" /     |\")")
        print("print(\"/___|\")")

        print("\n     Here is the Output:")
        print("      /|")
        print("     / |")
        print("    /  |")
        print("   /   |")
        print("  /    |")
        print(" /     |")
        print("/___|\n")





    def end():
        print("\n                                         -----------------------------    Lesson Main Menu  -----------------------------")
        a = input("\n Please Select:  "
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run Lessons "
                  "\n  (1)    Exercise 1 -  Simple Print Commands"
                  "\n  (2)    Exercise 2 -  Complex Print Commands "

                  "\n           <Enter>  for main menu: ")

        if str(a) == "d":
            definition()

        if str(a) == "D":
            definition()

        if str(a) == "r":
            EX1()
            continue_lesson()
            EX2()
            enter_lesson_menu()
            title()
            end()

        if str(a) == "R":
            EX1()
            continue_lesson()
            EX2()
            enter_lesson_menu()
            end()

        if str(a) == "D":
            definition()

        if str(a) == "1":
            EX1()
            end()

            end()
        if str(a) == "2":
            EX2()
            enter_lesson_menu()
            title()
            end()

        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()

