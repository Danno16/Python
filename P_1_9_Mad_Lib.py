from PC_1_1_Tools import *
def lesson_9():

    def title():
        new_page()
        print("\n                                -----------------------------    Lesson 9> Mad Lib using Variables  -----------------------------\n")

    def definition():
        title()
        print( "  Now were going to have a little fun by building a simple mad lib."
                "\n   I don't believe there is anything have not covered in previous lessons. \n\n\n\n\n\n")

        end()

    def EX1():
        title()
        print("\n\n\n\n\n\n\n\n\n\n\n\n   Provide the following inputs to see the example: ")

        name = input("\n\n\n\n What is your Name: ")
        color = input("\n What is your favorite  color: ")
        animal = input("\n What is your favorite  Animal: ")
        number = input("\n What is your favorite  Number: ")
        girl = input("\n What is your favorite  Girl's Name: ")
        boy = input("\n What is your favorite  Boy's Name: ")

        print("\n\n\n\n Here is the Output:")
        print(
            "\nThere once was a kid named  " + name + ". " + name +" bought " + number  + " " + color + " ballons."
            "\n Then " + name + " saw some friends named " + girl + " and " + boy + " walking their " + animal + ".")
        end()

    def EX1_code():
        title()

        print("   Here is the code we are using:\n")
        print("                      name = input(\"\\n What is your Name: \")     ")
        print("                      color = input(\"\\n What is your favorite  color: \")    ")
        print("                      animal = input(\"\\n What is your favorite  Animal: \")    ")
        print("                      number = input(\"\\n What is your favorite  Number: \")    ")
        print("                      girl = input(\"\\n What is your favorite  Girl's Name: \")    ")
        print("                      boy = input(\"\\n What is your favorite  Boy's Name: \")    \n")
        print("         print(\"There once was a kid named  \" + name + \". \" + name +\"  bought \" + number  + \" \" + color + \" ballons.\"")
        print("         print(\" Then \" + name + \" saw some friends named \" + girl + \" and \" + boy + \" walking their \" + animal + \".\")")
        end()
    def end():

        print("\n                                -----------------------------    Lesson Main Menu  -----------------------------")
        a = input("\n Please Select: \n "
                  "\n  (D)   Description of Lesson "
                  "\n  (1)  Exercise 1 -  Run the mad Lib "
                  "\n  (c)  View the code for Exercise 1. \n\n  "

                  "\n           <Enter>  for main menu: ")

        if str(a) == "d":
            definition()
        if str(a) == "D":
            definition()

        if str(a) == "c":
            EX1_code()
        if str(a) == "C":
            EX1_code()


        if str(a) == "1":
            EX1()
            end()


        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()

