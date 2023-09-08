from PC_1_1_Tools import *

def lesson_24():

    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 24 - Using Try / Except     -----------------------------\n")

    def definition():
            title()
            print(" The try block lets you test a block of code for errors. The except block lets you handle the error. "
                    "\nThe else block lets you execute code when there is no error. "
                    "\nThe finally block lets you execute code, regardless of the result of the try- and except block")
            print(
                "\n* There are situation where the program will error out when we don't want it to.  Such as if a letter is inputed instead of a number")
            print("The format looks like the following:\n"
                  "\n                     1       try:"
                  "\n                     2           print(\"Enter 2 numbers following by the operator [+, -, *, /]\\n\")"
                  "\n                     3           num1 = float(input(\"Enter 1st Number: \"))"
                  "\n                     4       except ValueError:"
                  "\n                     5           print(\"This is not a Valid Number\\n\")")

            end()

    def run_all():
        print("Run All")
        continue_lesson()
        end()

    def EX1():
        title()
        print(
            "\                                  -----------------------------------   Exercise 1 - TRY/EXCEPT  -----------------------------\n")
        print("We are using the try / excepts.  Please enter both positive (numbers) and negative (non-numbers)(:\n")

        try:
            number = int(input("\n1> Enter number -  Use Numeric:   "))
            print("                         Output - " + str(number) + " is a valid number")
        except:
            print("                         Output - Ivalid number")

        try:
            number = int(input("\n1> Lets stry again, Enter number -  Use NON - Numeric:   "))
            print("                         Output - " + str(number) + " is a valid number")
        except:
            print("                         Output - Ivalid number")

        try:
            number = int(input("\n1> One last time - Enter number or non number, your choice:   "))
            print("                         Output - " + str(number) + " is a valid number")
        except:
            print("                         Output - Ivalid number")

        g = input("\nDo you want to try again? (Y/N):")
        if(g) == "y":
             EX1()
        elif(g) == "Y":
             EX1()
        else:
            lesson_24()


        continue_lesson()
        end()

    def EX1_code():
        title()
        print(
            "\                                   -----------------------------------   Exercise 1 Code - TRY/EXCEPT  -----------------------------\n")
        print("The following is a try / except example that will bypass an error.  If we did not have this code,"
              "\nit would error out and stop the program.:\n")
        print("         try:")
        print("                number = int(input(\"enter number:\"))")
        print("                print(\"                         Output - \" + str(number) + \" is a valid number\")")
        print("         except:")
        print("                 print(\"invalid number\")\n\n")
        continue_lesson()
        end()


    def EX2():
        title()
        print(
            "\                                   -----------------------------------   Exercise 2 - TRY/EXCEPT as a Calculator   -----------------------------\n")
        print(
            "\nNow were going to try it with that Calculator we built eariler.  In This example enter valid or invalid information.")
        count = 0
        n = input("How many times do you want to try this example?")
        for  count  in range(int(n)):

            try:
                print("Try # - " + str(count) + ":      Enter 2 numbers following by the operator [+, -, *, /]\n")
                num1 = float(input("Enter 1st Number: "))
            except ValueError:
                print("This is not a Valid Number\n")

            try:
                num2 = float(input("Enter 2st Number: "))
            except ValueError:
                print("This is not a Valid Number\n")

            op = input("Enter operator :")

            try:
                if op == "+":
                    print(num1 + num2)
                    print("")
                elif op == "-":
                    print(num1 - num2)
                    print("")
                elif op == "*":
                    print(num1 * num2)
                    print("")
                elif op == "x":
                    print(num1 * num2)
                    print("")
                elif op == "/":
                    print(num1 / num2)
                    print("")
                else:
                    print("\ninvalid operator\n")
            except ValueError:
                print("\nYou did not enter numbers\n")
            except NameError:
                print("\nYou did not enter valid information\n")
        else:
            continue_lesson()
            definition()
            end()


    def EX2_code():
        title()
        print(
            "\                                   -----------------------------------   Exercise 2 Code  - TRY/EXCEPT as a Calculator   -----------------------------\n")
        print("                                             1           n = input(\"How many times do you want to try this example?\")  ")

        print("                                             2           count = 0        ")
        print("                                             3           for count in range(5):        ")
        print("                                             4              try:        ")
        print("                                             5                   print(\"Try # - \" + str(count) + \":      Enter 2 numbers following by the operator [+, -, *, /]\\n\")        ")
        print("                                             6                    num1 = float(input(\"Enter 1st Number: \"))        ")
        print("                                             7               except ValueError:        ")
        print("                                             8                   print(\"This is not a Valid Number\\n\")        ")

        print("                                             9                try:        ")
        print("                                             10                  num2 = float(input(\"Enter 2st Number: \"))        ")
        print("                                             11               except ValueError:        ")
        print("                                             12                   print(\"This is not a Valid Number\\n\")        ")

        print("                                             13               op = input(\"Enter operator :\")        ")

        print("                                             14               try:        ")
        print("                                             15                   if op == "+":        ")
        print("                                             16                       print(num1 + num2)        ")
        print("                                             17                       print("")        ")
        print("                                             18                   elif op == \"-\":        ")
        print("                                             19                       print(num1 - num2)        ")
        print("                                             20                       print("")        ")
        print("                                             21                   elif op == \"*\":        ")
        print("                                             22                      print(num1 * num2)        ")

        print("                                             23                   elif op == \"x\":        ")
        print("                                             24                       print(num1 * num2)        ")

        print("                                             25                   elif op == \"/\":        ")
        print("                                             26                        print(num1 / num2)        ")

        print("                                             27                   else:        ")
        print("                                             28                       print(\"\\ninvalid operator\")        ")
        print("                                             29              except ValueError:  ")
        print("                                             30                   print(\"\\nYou did not enter numbers\")        ")
        print("                                             31               except NameError:  ")
        print("                                             32                   print(\"\\nYou did not enter valid information\")  \n      ")

        continue_lesson()
        definition()
        end()




    def end():
        a = input("\n Please Select: To see the code behind the example put \"C\" before the number\n"
                  "\n (D)   Description of Lesson "
                  "\n (R)   Run all the Examples "
                  "\n (C1) / (1) Example 1 -  Using Try / Except        "
                  "\n (C2) / (2) Example 2 -  TRY/EXCEPT as a Calculator                     "

                  "\n           <Enter>  for main menu: ")

        if str(a) == "r":
            EX1()
            run_all()()
            definition()

        if str(a) == "r":
            EX1()
            run_all()()
            definition()

        if str(a) == "1":
            EX1()
            continue_lesson()
            definition()

        if str(a) == "c1":
            EX1_code()
            continue_lesson()
            definition()

        if str(a) == "2":
            EX2()
            continue_lesson()
            definition()

        if str(a) == "c2":
            EX2_code()
            continue_lesson()
            definition()

        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()