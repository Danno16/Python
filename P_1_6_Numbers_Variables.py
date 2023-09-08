from PC_1_1_Tools import *
from math import *
def lesson_6():

    def title():
        new_page()
        print("\n                                -----------------------------    Lesson 6 - Use Numbers\ Store in Variables    -----------------------------\n")

    def definition():
        title()
        print( "In this Exercise, We are going To:"
               "\n                      ---     Calculations with Variables"
               "\n                      ---     Covert numbers into Strings and printing Numbers with Text  "
               "\n                      ---     Using the POW, Max,Min, and Round commands"
               "\n                      ---     Using the floor. ceiling, and square root commands  "
               "\n                      ---     Using the Max/Min command   "
               )
        end()




    def EX1():
        title()
        print("                                    ****  Exercise 1 -  Calculations with Variables    ****  ")
        print(
            "\n         CODE                                                     Description of outcome                                                           Output")
        print(
            "`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
        print(
            " print(2)                             Prints the Sum                                                                                                " + str(
                2))
        print(
            " print(2.55252)                  Prints the Sum                                                                                                " + str(
                22.55252))
        print(
            " print(2+5)                         Prints the Sum                                                                                                " + str(
                5 + 2))
        print(
            " print(2-5)                          Prints the Sum                                                                                                " + str(
                2 - 5))
        print(
            " print(2*525214)                Prints the Sum                                                                                                " + str(
                22 * 525214))
        print(
            " print(2/5)                          Prints the Sum                                                                                                 " + str(
                2 / 5))
        print(
            " print(2 -3 *12 /5)              Example of  complex compulations                                                                 " + str(
                2 - 3 * 12 / 5))
        print(
            " print(2 -3 * (12 /5))           You can changes the order of operations                                                       " + str(
                2 - 3 * (12 / 5)))
        print(
            " print(10 % 3)                   Module operator divides 10 by 3 and will display the remainder                   " + str(
                10 % 3))


    def EX2():
        title()
        print("\n                                    ****  Exercise 2 -  Calculations with  inputs and stored  in Variables     **** \n ")

        print("\n Now were going to use the same formulas using values we input and store in variables {first_num} and {second_num}:")

        try:
            first_num = int(input("\nEnter First Number:  "))
            second_num = int(input("Enter Second Number:  "))
            print("\n       CODE                                                     Description of outcome                                                                                 Output")
            print(
                "`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")


            print("first_num = input(\"Enter First Number\")                Stores inputed value  in variable of {first_num}                                  - first_num = " + str(first_num))
            print("second_num = input(\"Enter Secondt Number\")    Stores inputed value  in variable of{second_num}                             - second_num = " + str(second_num))
            print("print(first_num + second_num)                               Prints the first_num PLUS second_num                                             " + str(int(first_num + second_num)))
            print("print(first_num - second_num)                                Prints the first_num SUBTRACT second_num                                   " + str(int(first_num - second_num)))
            print("print(first_num * second_num)                                Prints the first_num MULTIPLY second_num                                     " + str(first_num * second_num))
            print("print(first_num / second_num)                                Prints the first_num DIVIDED BY second_num                                  " + str(first_num / second_num))
            print("print(first_num + second_num + second_num)      Prints the first_num PLUS second_num  PLUS second_num           " + str(int(first_num + second_num + second_num)))
        except ValueError:
            print("\nYou did not use a valid number. I put a command called try/except so it did not error, Otherwise it wold have:"
                  "\n             ---     Error out"
                  "\n             ---     Stop the program"
                  "\n\n   Try/Except will be covered in lesson 24. ")
            input("\nPress <Enter> to try again.")
            EX2()

    def EX3():
        title()
        print("                                    ****  Exercise 3 -  Formulas options that are not in basic Python     **** \n ")



    def EX4():
        title()
        print("                                    ****  Exercise 4 -  Getting input from Users     **** \n ")


    def end():
        print("\n                                         -----------------------------    Lesson Main Menu  -----------------------------")
        a = input("\n Please Select:  "
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run all Lessons "
                  "\n  (1)    Exercise 1 -  Calculations with Variables "
                  "\n  (2)    Exercise 2 -  Calculations with  inputs and stored  in Variables  "

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

