from PC_1_1_Tools import *
def lesson_16():

    def title():
        new_page()
        print("\n                                   -----------------------------------    Lesson - 16  Building a better Calculator   -----------------------------\n")

    def definition():
        title()
        print("                                                                                  *****   Description of lesson  *****")
        print("We are building a calculator...  This is a little more smart than the one we built in previous exercises")
        print("                  *  We are using elif which means else/ if.  ")
        print("                         It is used for a filtering mechanism so it can detect if the oporator is valid or invalid  ")
        print("                  *  We are using FLOATs so we can use Decimals")
        print("                  *  We are converting the inputs to a float so it can accept decimals \n")
        end()

    def code():
        title()
        print("                                                                                *****   Running the code the Code  *****")
        print("Enter 2 numbers following by the operator [+, -, *, /]\n")
        num1 = float(input("Enter 1st Number: "))
        num2 = float(input("Enter 2nd Number: "))
        op = input("Enter operator :")
        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "x":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
        else:
            print("invalid operator")

        end()

    def print_code():
        title()
        print("                                                                                            *****   Here is the Code used  *****")
        print("         num1 = float(input(\"Enter 1st Number: \"))")
        print("         num2 = float(input(\"Enter 2nd Number: \"))   ")
        print("         op = input(\"Enter operator :\")    ")
        print("         if op == \"+\":    ")
        print("             print(num1 + num2)   ")
        print("         elif op == \"-\":   ")
        print("             print(num1 - num2)   ")
        print("         elif op == \"*\":   ")
        print("             print(num1 * num2)   ")
        print("         elif op == \"x\":    ")
        print("             print(num1 * num2)   ")
        print("         elif op == \"/\":    ")
        print("             print(num1 / num2)   ")
        print("         else:     ")
        print("             print(\"invalid operator\")    ")
        continue_lesson()
        end()


    def end():
        a = input("\n Please Select: "
            " \n           (R) to Run the program "
            "  \n           (P) to See the code used to build the program."
            "\n           (D) Description of the lesson\n "
            "\n           <Enter>  for main menu: ")
        if str(a) == "r":
            code()
        if str(a) == "R":
            code()

        if str(a) == "p":
            print_code()
        if str(a) == "P":
            print_code()

        if str(a) == "d":
            lesson_16()
        if str(a) == "D":
            lesson_16()

        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()

