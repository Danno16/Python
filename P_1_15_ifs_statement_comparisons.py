from PC_1_1_Tools import *
def lesson_15():
    def definition():
        new_page()
        print(
            "\n\n\n\n\n                                   -----------------------------------    15>    IF STATEMENT and Comparisions    -----------------------------\n")
        print(" We can do comparisions in a function, you can use a varity of operator signs:")
        print("          * == means equals")
        print("          * != means not equals")
        print("          * > means greater than")
        print("          * <  means Less than")
        print("          * >= means greater than or equals")
        print("          * <=  means Less than or equals")
        end()

    def EX1():
        new_page()
        print(
            "\n\n\n                                   -----------------------------------    Exercise 1 -   IF STATEMENT and Comparisions Find Highest Number    -----------------------------\n")
        print("Here is an example of a simple comparison statement:")

        print("         def max_num\(num1, num2, num3\):")
        print("             if num1 >= num2 and num1 >= num3:")
        print("                 return num1")
        print("             if num2 >= num1 and num2 >= num3:")
        print("                 return num2")
        print("             else:")
        print("                 return num3")

        print("\n             print(max_num(30, 40, 5))\n")

        def max_num(num1, num2, num3):
            if num1 >= num2 and num1 >= num3:
                return num1
            if num2 >= num1 and num2 >= num3:
                return num2
            else:
                return num3

        print("So as you an see we are using 30, 40, and 5.  When we run the code the output is - " + str(max_num(30, 40, 5)) + " - Which is the highest number.")

    def EX2():
        new_page()
        print(
            "\n\n\n                                   -----------------------------------    Exercise 2- IF STATEMENT and Comparisions Find Lowest Number    -----------------------------")
        print("Here is an example of a simple comparison statement:\n")

        print("def max_num\(num1, num2, num3\):")
        print("    if num1 <= num2 and num1 <= num3:")
        print("        return num1")
        print("    if num2 <= num1 and num2 <= num3:")
        print("        return num2")
        print("    else:")
        print("       return num3")
        print(" (max_num(30, 40, 5))\n")

        def min_num(num1, num2, num3):
            if num1 <= num2 and num1 <= num3:
                return num1
            if num2 <= num1 and num2 <= num3:
                return num2
            else:
                return num3

        print("So as you can see we are using 30, 40, and 5.  When we run the code the output is - " + str(min_num(30, 40, 5)) + " - which is the lowest number.")

    def EX3():
        new_page()
        print("\n\n\n                                   -----------------------------------    Exercise 3 -  IF STATEMENT and Comparisions with input    -----------------------------\n")

        def max_num1(num1, num2, num3):
            if num1 >= num2 and num1 >= num3:
                return num1
            if num2 >= num1 and num2 >= num3:
                return num2
            else:
                return num3

        def min_num1(num1, num2, num3):
            if num1 <= num2 and num1 <= num3:
                return num1
            if num2 <= num1 and num2 <= num3:
                return num2
            else:
                return num3

        print("Now its time to have some fun.")
        print("Lets do the same operation but you provide the data used\n")
        first_num = int(input("Enter FIRST number:  "))
        second_num = int(input("Enter SECOND number:  "))
        third_num =int( input("Enter THIRD  number:  "))

        print("\n\nThe LOWEST number you entered is = " + str(min_num1(first_num, second_num, third_num)))
        print("\nThe HIGHEST number you entered is = " + str(max_num1(first_num, second_num, third_num)))

    def end():
        a = input("\n      (D)    Description of the lesson "
            "\n      (R)    Run all Exercises"
            "\n      (1)  Exercise 1 - IF STATEMENT and Comparisions Find Highest Number   "
            "\n      (2)  Exercise 2-  IF STATEMENT and Comparisions Find Lowest Number "
            "\n      (3)  Exercise 3 - IF STATEMENT and Comparisions with input "
            "\n\n     Please Select:  "         )
        if str(a) == "D":
            definition()
        if str(a) == "d":
            definition()
        if str(a) == "r":
            EX1()
            continue_lesson()
            EX2()
            continue_lesson()
            EX3()
            end()
        if str(a) == "d":
            definition()

        if str(a) == "1":
            EX1()
            end()
        if str(a) == "2":
            EX2()
            end()
        if str(a) == "3":
            EX3()
            end()



        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1
    definition()

