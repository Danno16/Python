from PC_1_1_Tools import *
from math import *
def lesson_3():

    def title():
        new_page()
        print("\n                                -----------------------------    Lesson 3 - Additional Print Options   -----------------------------\n")

    def definition():
        title()
        print("\nOkay there are additional features in printing.  If you use:")
        print("                      -  \\n = it will insert a line.")
        print(
            "                      -  \\ = you can print key items that you wouldn't normally be able to print like \", \\ and etc."
            "\n                      ---      You can also do multiple lines on the same print statement (You Will see Examples Below)  ")

        end()


    def EX1():
        title()
        print(
            "\n  -------------------------------- Exercise  1 - Using \"\\n\" to insert a line--------------------------------")
        print("\nOkay there are additional features in printing.  If you use:")
        print("                      -  \\n = it will insert a line.")
        print("\nLets give some examples so hopefully it will make more since."
              "\n\n       If we enter the command line: "
              "\n           print(\"The dog ran up the hill and found a bone.\")"
              "\n\n       It will produce the following results:"
              "\n                   The dog ran up the hill and found a bone.\n\n")
        continue_lesson()
        title()
        print("\n  -------------------------------- Exercise  1 (Page 2) - Using \"\\n\" to insert a line--------------------------------")
        print("\n\n Now if we add the \\n it will insert a line."
              " \n\n       If we enter the command line:"
              " \n           print(\"The dog ran up the hill \\n and found a bone.\""
              "\n\n       It will produce the following results:"
              "\n                   The dog ran up the hill\n                   and found a bone.\n\n")
        continue_lesson()
        title()
        print("\n  -------------------------------- Exercise  1 (Page 3) - Using \"\\n\" to insert a line--------------------------------")
        print(" We can also enter multiple \\n\\n to add more than one line Insert.\n"
              "\n           Example: using 1 Line Insert:"
              " \n              print(\"The dog ran up the hill \\n and found a bone.\""
              "\n                       The dog ran up the hill\n                   and found a bone."

              "\n\n       Example: using 2 Line Inserts:"
              " \n              print(\"The dog ran up the hill \\n\\n and found a bone.\""
              "\n                       The dog ran up the hill\n\n                   and found a bone."

              "\n\n       Example: using 3 Line Inserts:"
              " \n              print(\"The dog ran up the hill \\n\\n\\n and found a bone.\""
              "\n                       The dog ran up the hill\n\n\n                       and found a bone."
              "\n\n  As you can see we can add as many \\n as we like to add more line inserts."
              )

    def EX2():
        title()
        print(
            "\n                                    ****  Exercise 2 -  Using  \\  So you can print key items  **** \n ")

        print(
            "\n So in lesson 1, we printed half a triangle.  Now we will print a full one. Now python will not print \\ because as ")
        print("mentioned it is used for a print feature. So in order to print \\ we have to use \\\\.")
        print("\n Here is the code we are using:")
        print("      print(\"      /\\\\\"")
        print("      print(\"     /  \\\\\"")
        print("      print(\"    /    \\\\\"")
        print("      print(\"   /      \\\\\"")
        print("      print(\"  /        \\\\\"")
        print("      print(\" /          \\\\\"")
        print("      print(\"/______\\\\\"")

        input("\n\nPress <Enter> to Continue: ")
        title()
        print(
            "\n                                    ****  Exercise 2 (Page 2) -  Using  \\  So you can print key items  **** \n ")
        print("\nHere is the output.  It prints a full triangle.\n")
        print("      /\\")
        print("     /  \\")
        print("    /    \\")
        print("   /      \\")
        print("  /        \\")
        print(" /          \\")
        print("/______\\\n")




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
                  "\n  (1)    Exercise 1 - Using \"\\n\" to insert a line"
                  "\n  (2)    Exercise 2 - Using  \\  So you can print key items "
                  "\n  (3)    Exercise 3 - Multiple Lines on the same Print Statement   "

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
            end()

        if str(a) == "R":
            EX1()
            continue_lesson()
            EX2()
            continue_lesson()
            EX3()
            end()

        if str(a) == "D":
            definition()

        if str(a) == "1":
            EX1()
            continue_lesson()
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

