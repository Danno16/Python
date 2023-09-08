from PC_1_1_Tools import *

def lesson_22():
    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 22 - 2D LISTS AND NESTED LOOPS   -----------------------------\n")

    def definition():
        title()
        print(" 2D array in Python is a nested data structure, meaning it is a set of arrays inside another array.\n "
              "The 2D array is mostly used to represent data in a tabular or two-dimensional format.\n")
        print("A nested loop is a loop inside the body of the outer loop. The inner or outer loop can be any type, \n"
                 "such as a while loop or for loop. For example, the outer for loop can contain a while loop and \n"
                 "vice versa. The outer loop can contain more than one inner loop.")
        end()

    def run_all():
        example_1()
        continue_lesson()
        example_2()
        continue_lesson()
        example_3()
        continue_lesson()
        example_4()
        continue_lesson()


    def example_1():
        title()
        print("                                                   Example 1 - How to pull data from a 2d list  \n")
        print("Now were going to pull a piece of data within the 2d List. Here is the list:\n")
        print("number_grid = [")
        print("    [1, 2, 3],")
        print("    [4, 5, 6,],")
        print("    [7, 8, 9],")
        print("    [0]")
        print("]\n")
        print(
            "Were going to use the code  - print(number_grid[2][1]),  Which means 2nd position in column and 1 over in the row:  ")

        number_grid = [
            [1, 2, 3],
            [4, 5, 6, ],
            [7, 8, 9],
            [0]
        ]

        print("The ouput is: " + str(number_grid[2][1]))

    def example_1_code():
        title()
        print("                                                   Code for --  Example 1 - How to pull data from a 2d list  \n")
        print("Code for Exercise 1:\n")
        print("                 1    number_grid = [")
        print("                 2    [1, 2, 3],")
        print("                 3    [4, 5, 6,],")
        print("                 4    [7, 8, 9],")
        print("                 5    [0]")
        print("                 6   print(\"The ouput is: \" + str(number_grid[2][1]))\n\n")


    def example_2():
        title()
        print("                                                   Example 2 - How to pull data from a 2d list  \n")
        print("Now were going to pull a piece of data within the 2d List. Here is the list:\n")
        print("number_grid = [")
        print("    [1, 2, 3],")
        print("    [4, 5, 6,],")
        print("    [7, 8, 9],")
        print("    [0]")
        print("]\n")
        print(
            "Were going to use the code  - print(number_grid[2][0]),  Which means 1st position in column and 0 over in the row:  ")

        number_grid = [
            [1, 2, 3],
            [4, 5, 6, ],
            [7, 8, 9],
            [0]
        ]

        print("The ouput is: " + str(number_grid[1][0]))

    def example_2_code():
        title()
        print("                                                   Code 2 for --  Example 2 - How to pull data from a 2d list  \n")
        print("Code for Exercise 2:\n")
        print("                 1    number_grid = [")
        print("                 2    [1, 2, 3],")
        print("                 3    [4, 5, 6,],")
        print("                 4    [7, 8, 9],")
        print("                 5    [0]")
        print("                 6   print(\"The ouput is: \" + str(number_grid[2][1]))\n\n")


    def example_3():
        title()
        print("                                                   Example 3 - Using a Nested LOOP to pull data in a  2d List  \n")
        print("Here is loop that will display all the rows.  Here is the code\n")
        print("             for row in number_grid:")
        print("                 for col in row:")
        print("                     print(col)")
        number_grid = [
            [1, 2, 3],
            [4, 5, 6, ],
            [7, 8, 9],
            [0]
        ]
        for row in number_grid:
            for col in row:
                print(col)
    def example_3_code():
        title()
        print("                                                   Code for --  Example 3 - Using a Nested LOOP to pull data in a  2d List  \n")
        print("             1       for row in number_grid:")
        print("             2          for col in row:")
        print("             3               print(col)")

    def example_4():
        title()
        print("                                                   Example 4 - How to pull data from a 2d list using input values  \n")
        print("Now were going to pull a piece of data within the 2d List using input values.\n")
        print("number_grid = [")
        print("    [1, 2, 3],")
        print("    [4, 5, 6,],")
        print("    [7, 8, 9],")
        print("    [0]")
        print("]\n")

        number_grid = [
            [1, 2, 3],
            [4, 5, 6, ],
            [7, 8, 9],
            [0]
        ]
        a = int(input("Enter ROW number (0 - 3);"))
        b = int(input("Enter COLUMN number (0 - 2);"))
        try:
            print("The ouput is: " + str(number_grid[a][b]))

        except:
            print("Invalid Number ")


        c = input("Do you want to try again? (Y/N):")
        if(c) == "y":
             example_4()
        elif(c) == "Y":
             example_4()
        else:
            lesson_22()


    def example_4_code():
        title()
        print("                                                   Code for --  Example 4 - How to pull data from a 2d list using input values  \n")
        print("Now were going to pull a piece of data within the 2d List using input values.")
        print("         - NOTE Wer are going to use TRY/EXCEPT which we have not covered yet.")
        print("              * We will cover TRY/EXCEPT in later lessons.\n")
        print("                         1       number_grid = [")
        print("                         2           [1, 2, 3],")
        print("                         3           [4, 5, 6,],")
        print("                         4           [7, 8, 9],")
        print("                         5           [0]")
        print("                         6       ]")
        print("                         7       a = int(input(\"Enter ROW number (0 - 3);\"))   ")
        print("                         8       b = int(input( \"Enter COLUMN number (0 - 2);\"))  ")
        print("                         9       try:   ")
        print("                         10           print(\"The ouput is: \" + str(number_grid[a][b]))  ")
        print("                         11       except:   ")
        print("                         12       print(\"Invalid Number \")  \n")

    def example_5():
        title()

    def example_5_code():
        title()

    def example_6():
        title()

    def example_6_code():
        title()

    def end():
        a = input("\n Please Select: To see the code behind the example put \"C\" before the number\n"
                  "\n (R)Decription of Lesson "
                  "\n (R) Run all the Examples "
                  "\n (C1) / (1) Example 1 - Replacing Vowels with input Value      "
                  "\n (C2) / (2) Example 2 - How to pull data from a 2d list                          "
                  "\n (C3) / (3) Example 3 - Using a Nested LOOP to pull data in a  2d List     "
                  "\n (C4) / (4) Example 4 - How to pull data from a 2d list using input values             "


                  "\n (D) Description\n "
                  "\n           <Enter>  for main menu: ")

        if str(a) == "1":
            example_1()
            continue_lesson()
            definition()

        if str(a) == "c1":
            example_1_code()
            continue_lesson()
            definition()

        if str(a) == "C1":
            example_1_code()
            continue_lesson()
            definition()

        if str(a) == "2":
            example_2()
            continue_lesson()
            end()

        if str(a) == "c2":
            example_2_code()
            continue_lesson()
            definition()

        if str(a) == "C2":
            example_2_code()
            continue_lesson()
            definition()

        if str(a) == "3":
            example_3()
            continue_lesson()
            end()

        if str(a) == "c3":
            example_3_code()
            continue_lesson()
            definition()

        if str(a) == "C3":
            example_3_code()
            continue_lesson()
            definition()

        if str(a) == "4":
            example_4()
            continue_lesson()
            end()

        if str(a) == "c4":
            example_4_code()
            continue_lesson()
            definition()

        if str(a) == "C4":
            example_4_code()
            continue_lesson()
            definition()

        if str(a) == "5":
            example_5()
            continue_lesson()
            end()

        if str(a) == "c5":
            example_5_code()
            continue_lesson()
            definition()

        if str(a) == "C5":
            example_5_code()
            continue_lesson()
            definition()

        if str(a) == "6":
            example_6()
            continue_lesson()
            end()

        if str(a) == "c6":
            example_6_code()
            continue_lesson()
            definition()

        if str(a) == "C6":
            example_6_code()
            continue_lesson()
            definition()

        if str(a) == "r":
            run_all()
        if str(a) == "R":
            run_all()

        if str(a) == "d":
            definition()
        if str(a) == "D":
            definition()
        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()