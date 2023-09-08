from PC_1_1_Tools import *
from math import *
def lesson_4():

    def title():
        new_page()
        print("\n                                -----------------------------    Lesson 4 - Concatenate numbers and Text    -----------------------------\n")

    def definition():
        title()
        print( "Concatenating two strings refers to the merging of both the strings together. Concatenation of “Tutorials” and “Point” "
               " will result in \“TutorialsPoint\”."
               "\n    We will be discussing different methods of concatenating two strings in Python."
               "\n      Using ‘+’ operator"
               "\n      Two strings can be concatenated in Python by simply using the ‘+’ operator between them."
               "\n      More than two strings can be concatenated using ‘+’ operator"
               "\n\nWe can perform string concatenation using following ways:"
               "\n                     sing + operator.        "
               "\n                     ---     Using join() method."
               "\n                     ---     Using % operator."
               "\n                     ---     Using format() function."
               "\n                     ---     Using f-string (Literal String Interpolation)"
               )
        end()




    def EX1():
        title()
        print(
            "\n                                    ****  Exercise 1 -  Concatenate Text and Variables  **** \n ")
        print(
            "We touched upon this in Lesson - 2,  but we'll go over it again.  To combine Text or Variables we use the plus sign (+).")
        print("\nLets set the variable of {first_name} as \"Spider\" and the variable {last name} to \"man\".")
        print("                 first_name = \"Spider \"")
        print("                 last_name = \"man\"")
        first_name = "Spider "
        last_name = "man"
        print("\n So to combine variables first_name and last_name we use {+}.  Here is the code were using:")
        print("                 print(first_name + last_name)")
        print("\nHere is the ouput:")
        print("                           " + first_name + last_name)

        end()

    def EX2():
        title()
        first_name = "Spider "
        last_name = "man"
        print(
            "\n                                    ****  Exercise 2 -  Concatenate Text and Variables **** \n ")

        print("\nNow were going to do a combination of concatenation: following by the output:\n")
        print(
            "      Code:  print(\"A \" + first_name + \"is scary.\"" + "                                                  Output:   A " + first_name + " is scary.")
        print(
            "      Code:  print(\"Super\" + last_name) " + "                                                              Output:    Super" + last_name)
        print(
            "      Code:  print(\"The Hulk is stronger than \" + first_name + last_name)         Output:    The Hulk is stronger than " + first_name + last_name)


    def EX3():
        title()
        print(
            "\n                                    ****  Exercise 3 -  Concatenate Text and Input Variables  **** \n ")
        first_name = input("Enter a Name:  ")
        last_name = input("Enter a Last Name:  ")
        print("        first_name = input(\"Enter a Name:  \"")
        print("        last_name = input(\"Enter a Last Name:\"")
        title()
        print(
            "\n                                    ****  Exercise 3 -  Concatenate Text and Input Variables  **** \n ")

        print("\nNow were going to do a combination of concatenation using the values you input, : following by the output:\n")
        print("      first_name = input(\"Enter a Name:  \" ")
        print("      last_name = input(\"Enter a Last Name:\"  ")
        print("      print(first_name)                                                                                                  Output: " + first_name )
        print("      print(lastt_name)     :                                                                                           Output: " + last_name)

        print(
            "      Code:  print(\"A \" + first_name + \"is scary.\"" + "                                                         Output:   A " + first_name + " is scary.")
        print(
            "      Code:  print(\"Super\" + last_name) " + "                                                                     Output:    Super" + last_name)
        print(
            "      Code:  print(\"The Hulk is stronger than \" + first_name + \" \" +  last_name)        Output:    The Hulk is stronger than " + first_name +" " + last_name)

    def end():
        print("\n                                         -----------------------------    Lesson Main Menu  -----------------------------")
        a = input("\n Please Select:  "
                  "\n  (D)   Description of Lesson "
                  "\n  (1)    Exercise 1 -  Concatenate Text and Variables"
                  "\n  (2)    Exercise 2 -  Concatenate Text and Variables "
                  "\n  (3)    Exercise 3 -  Concatenate Text and Input Variables   "

                  "\n           <Enter>  for main menu: ")

        if str(a) == "d":
            definition()

        if str(a) == "D":
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

