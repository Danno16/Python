from PC_1_1_Tools import *
from math import *
def lesson_7():

    def title():
        new_page()
        print("\n                                -----------------------------    Lesson 7 -  More About Numbers   -----------------------------\n")

    def definition():
        title()
        print( "In this Exercise, We are going To:"
               "\n                      ---     Storing Numbers into Variables"
               "\n                      ---     Covert numbers into Strings and printing Numbers with Text  "
               "\n                      ---     Using the POW, Max,Min, and Round commands"
               "\n                      ---     Using the floor. ceiling, and square root commands  "
               "\n                      ---     Using the Max/Min command   "
               )
        end()

    def EX1():
        title()
        print("\n                                    ****  Exercise 1 -  Storing Numbers into Variables and Covert numbers into Strings   **** \n ")
        print(
            "\n\n\n\n\n\n\n\n\n                                  -------      Lesson 7 - More about numbers  ---------\n")
        print(" In order to use a number with a text, you have to convert to a string. The following is an example:\n")
        print("     CODE                                                     Description of outcome                                                    Output")
        print(
            "`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
        first_num = 10

        print(
            "         first_num = 10                               - Stores the value of 10 in the variable first_num                     " + str(
                first_num))
        print(
            "         print(str(first_num))                       - Convert the number to a string.                                             " + str(
                first_num))
        print(
            "         print(\"Albert\" + str(first_num))       - prints \"Albert\" plus  value iin the variable {first_num}           Albert" + str(
                first_num))


    def EX2():
        title()
        print("\n                                    ****  Exercise 2 -  Using the POW, Max,Min, and Round commands     **** \n ")
        print(
            "     CODE                                                     Description of outcome                                                    Output")
        print(
            "`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
        print(
            " print(pow(13,17))                                   Prints 13 to the power of 17                                     " + str(
                pow(13, 17)))
        print(
            " print(max(13,17,23,52,3))                      Prints the largest number                                         " + str(
                max(13, 17, 23, 52, 3)))
        print(
            " print(min(13,17,23,52,3))                       Prints the smallest number                                      " + str(
                min(13, 17, 23, 52, 3)))
        print(
            " print(round(23.525))                              Rounds the number                                                  " + str(
                round(23.525)))
        print(
            " print(round(21,28725))                          Rounds the number                                                  " + str(
                round(21, 28725)))


    def EX3():
        title()
        print("                                    ****  Exercise 3 -  Formulas options that are not in basic Python     **** \n ")
        print(" Now were going to use formulas options that are not in basic Python. ")
        print(" In order to do this, we must import additional functions by using the following code:\n ")
        print(" from math import *\n ")
        print(
            "     CODE                                                     Description of outcome                                            Output")
        print(
            "`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")

        print(
            " print(floor(3.7))                                       Chops off the decimal                                              " + str(
                floor(3.7)))
        print(
            " print(ceil(3.7))                                         Rounds a number UP to the nearest integet           " + str(
                ceil(3.7)))
        print(
            " print(sqrt(36))                                         Gives  us the square root of a number                    " + str(
                sqrt(36)))


    def EX4():
        title()
        print("                                    ****  Exercise 4 -  Getting input from Users     **** \n ")
        print(
            "----------------------------------------------------------------------------------------------------------------------------------")
        print("\nWe are going to do another example of using input statements to auto populate a sentence.")
        print("First we'll do 2 inputs, name and age using the following commands:\n")

        print(
            "         name = input(\"What is your full  Name: \")                                     ------      Input Text with variable \"name\"")
        print(
            "         Age = input(\"What is your Age: \")                                                  ------      Input Text with variable \"Age\"")
        print(
            "         print(\"\\n\\nHi \" + name + \" you are \" + Age + \" years old\")             ------      Output with the two variables")

        print(
            "\n                              -------------------------------- Getting input from Users  --------------------------------          ")
        print(
            "----------------------------------------------------------------------------------------------------------------------------------")
        print("")
        name = input("\nWhat is your full  Name: ")  # Input Text with variable "name"
        Age = input("What is your Age: ")  # Input Text with variable "Age"

        print("\n\nHi " + name + " you are " + Age + " years old")  # Output with the two variables




    def end():
        print("\n                                         -----------------------------    Lesson Main Menu  -----------------------------")
        a = input("\n Please Select:  "
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run all Lessons "
                  "\n  (1)    Exercise 1 -  Storing Numbers into Variables and Covert numbers into Strings. "
                  "\n  (2)    Exercise 2 -  Using the POW, Max, Min, and Round commands )  "
                  "\n  (3)    Exercise 3 -  Formulas options that are not in basic Python  ) "
                  "\n  (4)    Exercise 4 -  Getting input from Users)        "

                  "\n           <Enter>  for main menu: ")

        if str(a) == "d":
            definition()

        if str(a) == "D":
            definition()

        if str(a) == "r":
            EX1()
            continue_lesson()
            EX2()
            continue_lesson()
            EX3()
            continue_lesson()
            EX4()
            input("\nPress <Enter> to go to Lesson Main Menu")
            end()

        if str(a) == "R":
            EX1()
            continue_lesson()
            EX2()
            continue_lesson()
            EX3()
            continue_lesson()
            EX4()
            input("\nPress <Enter> to go to Lesson Main Menu")
            end()


        if str(a) == "1":
            EX1()
            end()
        if str(a) == "2":
            EX2()
            end()
        if str(a) == "3":
            EX3()
            end()
        if str(a) == "4":
            EX4()
            input("\nPress <Enter> to go to Lesson Main Menu")
            title()
            end()



        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()

