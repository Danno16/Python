from PC_1_1_Tools import *
from math import *
def lesson_2():

    def title():
        new_page()
        print("\n                                -----------------------------    Lesson 2 - Variable and Data Types    -----------------------------\n")

    def definition():
        title()
        print("Think of a variable as a box where you can store stuff.  You can store:\n")
        print("                        Strings - Alpha and Numeric")
        print("                        Numbers -  Numeric")
        print("                        Boolean - True False")
        print("\n    There are other values but we'll leave it for now.")

        end()


    def EX1():
        title()
        print(
            "\n  --------------------------------    Exercise  1 - Examples of Variables  --------------------------------")

        print(
            "\nNow Lets sets some variables.  We'll set the variables: (name = \"dan\"),  (age = \"10\") and (isMale = false).")
        print("    - Now notice we use quotation marks (\") around the name and age. ")
        print("    - Quotation marks is how we set the variable as a string.  ")
        print("    - Notice the variable called isMale = false  This is how we set as a booleen value.  ")
        print("\n Lets look at how we actually code. ")
        print("           name = \"dan\"  # String")
        print("           age = \"20\"  # String")
        print("           isMale = False  # Boolean Vale\n\n\n")


    def EX2():
        title()

        name = "dan"  # String
        age = "10"  # String
        isMale = False  # Boolean Vale

        print(
            "\n                                    ****  Exercise 2 -  Using Variables in a Sentence  **** \n ")
        print(" Okay now lets acually us these variables in a sentence.  Here is the code were going to use ")
        print("           name = \"dan\"  # String")
        print("           age = \"10\"  # String")
        print(
            "  Note - Notice the format to combine text with a variable.  The text is wrapped with quotations marks then (+) adds in the variables")
        print("\n  The text is wrapped with quotations marks then (+) adds in the variables")
        print("           print(\"There once name named \" + name + \",\")")
        print("           print(\"He was  \" + age + \" years old. \")")
        print("           print(\"He really liked the name \" + name + \",)")
        print("           print(\"but he did not like to be \" + age + \" years old.\")")
        print("\n Here is the output:\n ")
        print("There once name named " + name + ",")
        print("He was  " + age + " years old.  ")
        print("He really liked the name " + name + ",")
        print("but he did not like to be " + age + " years old.\n\n")



    def EX3():
        title()
        print(
            "\n                                    ****  Exercise 3 -  Multiple Lines on the same Print Statement  **** \n ")
        print("Normally you print one line at a time.  Example:"
              "\n           print(\"The Dog ran after the duck,\")"
              "\n           print(\"the Dog's owner called him back.\")")
        print("\nOutput:")
        print("The Dog ran after the duck,")
        print("the Dog's owner called him back.\n")
        continue_lesson()
        title()
        print(
            "\n                                    ****  Exercise 3 -  Multiple Lines on the same Print Statement  **** \n ")
        print("\nNow you can print more than one line using the same print statement.  Example:"
              "\n           print(\"The Dog ran after the duck,\""
              "\n           \"\\n the Dog's owner called him back.\")")
        print("\nOutput:")
        print("The Dog ran after the duck,"
              "\n the Dog's owner called him back.")

    def end():
        print("\n                                         -----------------------------    Lesson Main Menu  -----------------------------")
        a = input("\n Please Select:  "
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run Lessons "
                  "\n  (1)    Exercise 1 - Using \"\\n\" to insert a line"
                  "\n  (2)    Exercise 2 -  Using Variables in a Sentence "


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
            enter_lesson_menu()
            title()
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

