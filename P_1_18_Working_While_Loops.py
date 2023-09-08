from PC_1_1_Tools import *
def lesson_18():

    def title():
        new_page()
        print("\n                                   -----------------------------------    Lesson - 18  Working with While Loops   -----------------------------\n")

    def definition():
        title()
        print("         *  A Python WHILE loop is used to run a block code until a certain condition is met. ")
        print("         *  The syntax of while loop is: while condition: # body of while loop.")
        print(
            "         * A while loop evaluates the condition. If the condition evaluates to True , the code inside the while loop is executed.")
        print("               - . If the condition evaluates to True , the code inside the while loop is executed.")
        print("         * Difference between a while loop and a for loop is:")
        print(
            "                  - while loops to run the same task multiple times and for loops to loop once over list data.")
        print(
            "          * While loop is basically a Structure in python which allows us to loop thru and execute a block of code multiple times\n")
        print("Were going to make a simple program that prints what you want and how many times\n")
        end()

    def code():
        title()
        print("Were going to make a simple program that prints what you want and how many times\n")

        b = input("What do you want to print? : ")
        c = input("how many times do you want to print it? : ")
        i = 1
        while i <= int(c):
            print((b) + "  " + str(i))
            i += 1

        print("\nDone with loop\n")
        a = input("Do you want to do it again (Y)es or <Enter> for Lesson Menu)?  ")
        if a == "Y":
            code()
        elif a == "y":
            code()
        else:
            lesson_18()

    def print_code():
        title()
        print("                                                                                            *****   Here is the Code used  *****\n")
        print("                 b = input(\"What do you want to print? : \")   ")
        print("                 c = input(\"how many times do you want to print it? : \")  ")
        print("                 i = 1  ")
        print("                 while i <= int(c):  ")
        print("                     print((b) + "  " + str(i))  ")
        print("                     i += 1 \n\n\n ")
        continue_lesson()
        print("\n\n\n")
        end()


    def end():
        a = input("\n Please Select: "
            " \n           (R) to Run an Example.. "
            "  \n           (P) to See the code."
            "\n           (D) Description "
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
            lesson_18()
        if str(a) == "D":
            lesson_18()
        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()

