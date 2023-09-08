from PC_1_1_Tools import *
def lesson_8():

    def title():
        new_page()
        print("\n                                -----------------------------    Lesson 8>  Building a Calculator   -----------------------------\n")

    def definition():
        title()
        print( "In this Exercise, We are going to have Python preform mathmatical operations. \n "
               "We are introducing:\n "
               "\n                    Converting strings to  integers."
               "\n                    Converting back to strings"
               "\n                    Using \" Float\"\n\n\n ")
        end()

    def EX1():
        title()
        print("\n                                    ****  Exercise 1 -  Building a Calculator without Float (have to use WHOLE numbers)     **** \n ")
        print("             Exercise 1 Building a Calculator    ****  IT WILL ERROR IF WE DON'T USE WHOLE Numbers  *** \n"
                "\n     We are going to ask for 2 whole numbers then python will Add, Subtract, Multiply, and Devide the numbers")
        try:
            num1 = input("\nEnter First Number   -     (Has to be a WHOLE number): ")  # Input Number with variable "num1"
            num2 = input("Enter Second Number  - (Has to be a WHOLE number):   ")  # Input Number with variable "num2"
            result_add = int(num1) + int(num2)  # Converts to integers and adds together
            result_sub = int(num1) - int(num2)  # Converts to integers and adds together
            result_mult = int(num1) * int(num2)  # Converts to integers and adds together
            result_div = int(num1) / int(num2)  # Converts to integers and adds together

            print("\n" + num1 + " + " + num2 + " = " + str(result_add))
            print(num1 + " - " + num2 + " = " + str(result_sub))
            print(num1 + " * " + num2 + " = " + str(result_mult))
            print(num1 + " / " + num2 + " = " + str(result_div))

        except ValueError:
            print("\n\nYou did not use WHOLE Number.  I put a command called try/except so it did not error, Otherwise it wold have:"
                  "\n             ---     Error out"
                  "\n             ---     Stop the program"
                  "\n\n   Try/Except will be covered in lesson 24. ")
            input("\nPress <Enter> to try again.")
            EX1()


        end

    def EX1_code():
        title()

        print("\n                                    ****  Exercise 1 - Code: Building a Calculator without Float (have to use WHOLE numbers)     **** \n ")

        print(
            "Here is the code we are going to use:  The only things you may not recognize is turning string into integer.")
        print(" int(num1) changes the number from a string to a number so we can do calculations.\n")
        print(
            "                 num1 = input(\"Enter First Number: \")                               ---          Input Number with variable \"num1\"")
        print(
            "                 num2 = input(\"Enter Second Number: \")                          ---          Input Number with variable \"num2\"")
        print(
            "                 result_add = int(num1) + int(num2)                                  ---          Converts to integers and ADDS variables")
        print(
            "                 result_sub = int(num1) - int(num2)                                   ---          Converts to integers and SUBTRACTS variables")
        print(
            "                 result_mult = int(num1) * int(num2)                                  ---          Converts to integers and MULTIPLY variables")
        print(
            "                 result_div = int(num1) / int(num2)                                     ---         Converts to integers and DIVIDES variables\n")

        print(
            "                 print(num1 + \" + \" + num2 + \" = \" + str(result_add))         ---         prints: first variable")
        print(
            "                 print(num1 + \" - \" + num2 + \" = \" + str(result_sub))          ---         plus operator (+,- ,* , /) ")
        print(
            "                 print(num1 + \" * \" + num2 + \" = \" + str(result_mult))         ---         second variable ")
        print(
            "                 print(num1 + \" / \" + num2 + \" = \" + str(result_div))           ---         the equals sign")
        print(
            "                                                                                                            ---        Converts {result_add} to string and prints it out.")
        input("Press <Enter> for Lesson Main Menu:   ")
        title()
        end()


    def EX2():
        title()
        print("\n                                    ****  Exercise 2 -  Building a Calculator with Float (Now we can use decimals)     **** \n ")
        print("             In Exercise 1, we did not use a float so it wold error if we used decimals. \n"
                "\n     We are going to ask for 2 numbers then python will Add, Subtract, Multiply, and Devide the numbers")
        try:
            num1 = input("Enter First Number       - Now you can use decimals: ")  # Input Number with variable "num1"
            num2 = input("Enter Second Number  - Now you can use decimals: ")  # Input Number with variable "num2"
            result_add = float(num1) + float(num2)  # Converts to integers and adds together
            result_sub = float(num1) - float(num2)  # Converts to integers and adds together
            result_mult = float(num1) * float(num2)  # Converts to integers and adds together
            result_div = float(num1) / float(num2)  # Converts to integers and adds together

            print(num1 + " + " + num2 + " = " + str(result_add))
            print(num1 + " - " + num2 + " = " + str(result_sub))
            print(num1 + " * " + num2 + " = " + str(result_mult))
            print(num1 + " / " + num2 + " = " + str(result_div))

        except ValueError:
            print("\nYou did not use a valid number. I put a command called try/except so it did not error, Otherwise it wold have:"
                  "\n             ---     Error out"
                  "\n             ---     Stop the program"
                  "\n\n   Try/Except will be covered in lesson 24. ")
            input("\nPress <Enter> to try again.")

        end()
    def EX2_code():
        title()
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n                           -------------------      Building a Calculator now we can use decimals using FLOAT decimal      -----------------------")
        print(" \n              ****  Example of using FLOAT (allows for decimals), Variables, and formulas  **** ")
        print("   As you can see, we are using  FLOAT allows for decimal.  Here is the code were going to use:\n")

        print(
            "                num1 = input(\"Enter First Number: \")                                ---          Input Number with variable \"num1\"")
        print(
            "                num2 = input(\"Enter Second Number: \")                           ---          Input Number with variable \"num2\"")
        print(
            "                result_add = float(num1) + float(num2)                             ---          Converts to Integer and adds together")
        print(
            "                result_sub = float(num1) - float(num2)                              ---          Converts to integers and adds together")
        print(
            "                result_mult = float(num1) * float(num2)                             ---          Converts to integers and adds together")
        print(
            "                result_div = float(num1) / float(num2)                                 ---          Converts to integers and adds together\n")

        print(
            "                print(num1 + \" + \" + num2 + \" = \" + str(result_add))         ---         prints: first variable\")")
        print(
            "                print(num1 + \" - \" + num2 + \" = \" + str(result_sub))          ---         plus operator (+,- ,* , / \")")
        print(
            "                print(num1 + \" * \" + num2 + \" = \" + str(result_mult))         ---         second variable \")")
        print(
            "                print(num1 + \" / \" + num2 + \" = \" + str(result_div))           ---         the equals sign\")")
        print(
            "                                                                                                           ---        Converts {result_add} to string and prints it out.")
        input("Press <Enter> for Lesson Main Menu:   ")
        title()
        end()






    def end():
        print("\n                                         -----------------------------    Lesson Main Menu  -----------------------------\n")
        a = input("\n Please Select:  "
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run all Lessons "
                  "\n  (1)    Exercise 1 -  Building a Calculator without Float (have to use WHOLE numbers)   "
                  "\n  (2)    Exercise 2 -  Building a Calculator with Float (Now we can use decimals)       "
                  "\n  (C1)  Exercise 1 - Code: Building a Calculator without Float (have to use WHOLE numbers) "
                  "\n  (C2)  Exercise 2  - Code:  Building a Calculator with Float (Now we can use decimals)        "

                  "\n           <Enter>  for main menu: ")

        if str(a) == "d":
            definition()

        if str(a) == "D":
            definition()

        if str(a) == "r":
            EX1()
            continue_lesson()
            EX2()
            end()

        if str(a) == "R":
            EX1()
            continue_lesson()
            EX2()
            end()


        if str(a) == "1":
            EX1()
            end()
        if str(a) == "2":
            EX2()
            end()
        if str(a) == "c1":
            EX1_code()
            end()
        if str(a) == "C1":
            EX1_code()
            end()
        if str(a) == "c2":
            EX2_code()
            end()
        if str(a) == "C2":
            EX2_code()
            end()


        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()

