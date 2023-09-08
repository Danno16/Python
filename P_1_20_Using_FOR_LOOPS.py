from PC_1_1_Tools import *


def lesson_20():
    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 20 - Using FOR LOOPS  -----------------------------\n")

    def definition():
        title()
        print(
            " *A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).")
        print(
            "* This is less like the for keyword in other programming languages, and works more like an iterator method   ")
        print("             as found in other object-orientated programming languages.")
        print(" *With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.")
        print("\n  * Writing a for loop: ")
        print(
            "           - Step 1 - It starts with the for keyword, followed by a value name that we assign to the item of the sequence.")
        print(
            "           - Step 2 - Then, the in keyword is followed by the name of the sequence that we want to iterate.")
        print("           - Step 3 - The initializer section ends with “ : ”.")
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
        example_5()
        continue_lesson()
        example_6()
        continue_lesson()
        end()

    def example_1():
        title()
        print(
            "\                                                   Example 1 -  Using LOOP using  INPUTed Text     \n")
        print("Now INPUT a name a name and we'll use the Loop to print letter by letter")

        name = input("\n\nEnter name you want to use in a FOR LOOP:  ")

        for i in (name):
            print(i)

    def example_1_code():
        title()
        print(
            "\                                                    Code used for -- Example 1 -  Using LOOP using  INPUTed Text     \n")
        print("           1     print(\"Now INPUT a name a name and we'll use the Loop to print letter by letter\")")
        print("           2     name = input(\"\\n\\nEnter name you want to use in a FOR LOOP:  \")")
        print("           3     for i in (name):")
        print("           4          print(i)\n")
        print("  This is how we coded this exercise.\n\n")

    def example_2():
        title()
        print(
            "\n                                               Example 2 - Using LOOP in ARRAY      \n")
        print("\nHere is the ARRAY we are working with:")
        cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pinto", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150",
                "F250"]
        print(cars)

        a = input("\nPress <Enter> to us FOR LOOP to display the ARRAY item by item:  ")
        print("\nAs you can see, we used the FOR LOOP to display the ARRAY item by item:\n")
        b = 0
        for i in (cars):
            b = b + 1
            print(str(b) + " - " + i)
        print("\nNOTE - I added the count number.\n")

    def example_2_code():
        title()
        print(
            "\n                                                Code used for -- Example 2 - Using LOOP in ARRAY      \n")
        print("           1     print(\"\\nHere is the ARRAY we are working with:\")")
        print(
            "           2     cars = [\"Mustang\", \"Camaro\", \"Challenger\", \"Pinto\", \"Pinto\", \"Pinto\", \"Pizza Car\", \"Shoe Car\", \"Ram\", \"F150\", \"F250\"]  ")
        print("           3     print(cars)  ")

        print("           4     a = input(\"\\nPress <Enter> to us FOR LOOP to display the ARRAY item by item:  \")")
        print(
            "           5     print(\"\\nAs you can see, we used the FOR LOOP to display the ARRAY item by item:\\n\") ")
        print("           6     b = 0  ")
        print("           7     for i in (cars):   ")
        print("           8         b=b+1 ")
        print("           9     print(str(b) +\" - \"+ i)   ")
        print("         10     print(\"\\nNOTE - I added the count number.\n\")  ")

    def example_3():
        title()
        print(
            "                                     Example 3 - Using LOOP with input value to set the end of the RANGE     \n")

        print("We are going to use a range.  Input a number and we will count using the range function. \n")
        a = int(input("ENTER how big you want to range to be?:  ")) + 1
        for i in range(int(a)):
            print(i)

        print("\n As you can the range counted between 1 and " + str(a - 1) + "\n")

    def example_3_code():
        title()
        print(
            "                                     Code used for -- Example 3 - Using LOOP with input value to set the end of the RANGE     \n")

        print(
            "           1      print(\"We are going to use a range.  Input a number and we will count using the range function. \\n\")")
        print("           2      a = int(input(\"ENTER how big you want to range to be?:  \")) + 1  ")
        print("           3            for i in range(int(a)):  ")
        print("           4                 print(i)")

        print("           5      print(\"\\n As you can the range counted between 1 and \" + str(a-1) + \"\\n\")  \n\n")

    def example_4():
        title()
        print(
            "                                     Example 4 - Using LOOP with input value to set the beginning and ending RANGE     \n")
        a = int(input("Enter the LOWEST number of the RANGE:  "))
        b = int(input("Enter the HIGHEST number of the RANGE:   ")) + 1
        for i in range(a, b):
            print(i)

    def example_4_code():
        title()
        print(
            "                                     Example 4 - Using LOOP with input value to set the beginning and ending RANGE     \n")
        print("           1        a = int(input(\"Enter the LOWEST number of the RANGE:  \")) ")
        print("           2        b = int(input(\"Enter the HIGHEST number of the RANGE:   \")) + 1    ")
        print("           3        for i in range(a, b):")
        print("           4             print(i)\n\n")

    def example_5():
        title()
        print("                                     Example 5 - Using LOOP with  RANGE and LEN commands     ")
        cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pinto", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150",
                "F250"]

        print(
            "\nWe are using a LOOP to print the ARRAY we are using the (len) command to determine the length of the array. \n")
        continue_lesson()
        for i in range(len(cars)):
            print(cars[i])
        print(
            "\n Even though the it looks the same as example 2, in this example we set the ending variable of the if statement using the length (len) command.")
        print("\n you will not this when you/if you review the code..\n")

    def example_5_code():
        title()
        print(
            "                                              Example 5 - Using LOOP with  RANGE and LEN commands     ")
        print(
            "           1     cars = [\"Mustang\", \"Camaro\", \"Challenger\", \"Pinto\", \"Pinto\", \"Pinto\", \"Pizza Car\", \"Shoe Car\", \"Ram\", \"F150\", \"F250\"]  ")

        print(
            "           2     print(\"\\nWe are using a LOOP to print the ARRAY we are using the (len) command to determine the length of the array. \\n\")   ")
        print("           3     continue_lesson()  ")
        print("           4     for i in range(len(cars)):   ")
        print("           5        print(cars[i]) \n\n")

    def example_6():
        title()
        print(
            "\                          Example 6 - Using Loop in to print out part of the array using INPUTED beginning and ending RANGE      \n")
        cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pinto", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150",
                "F250"]
        print("Now lets try with an inputed RANGE\n\n\n\n")
        number = len(cars)

        a = int(input("\nEnter the BEGINNING number of the range . Has to be less than " + str(number) + ":  "))
        b = int(input("\nEnter the ENDING number of the range. Has to be less than " + str(number) + ":  ")) + 1

        for i in range(a, b):
            print(str(i) + " - " + cars[i])
        print("\n")

    def example_6_code():
        title()
        print(
            "\                                         Example 6 - Using Loop in to print out part of the array using INPUTED beginning and ending RANGE     \n")
        print(
            "           1     cars = [\"Mustang\", \"Camaro\", \"Challenger\", \"Pinto\", \"Pinto\", \"Pinto\", \"Pizza Car\", \"Shoe Car\", \"Ram\", \"F150\", \"F250\"]  ")
        print("           2     print(\"Now lets try with an inputed RANGE\\n\\n\\n\\n\")        ")
        print("           3     number = len(cars) ")

        print(
            "           4     a = int(input(\"\\nEnter the BEGINNING number of the range . Has to be less than \" + str(number) + \":  \"))  ")
        print(
            "           5     b = int(input(\"\\nEnter the ENDING number of the range. Has to be less than \" + str(number) + \":  \")) + 1   ")

        print("           6     for i in range(a, b): ")
        print("           7        print(str(i) + \" - \" +  cars[i])  ")
        print("           8     print(\"\\n\")   \n\n")

    def end():
        a = input("\n Please Select: To see the code behind the example put \"C\" before the number"
                  "\n (R)Decription of Lesson "
                  "\n (R) Run all the Examples "
                  "\n (C1) / (1) Example 1 -  Using LOOP using  INPUTed Text            "
                  "\n (C2) / (2) Example 2 - Using  LOOP  in ARRAY                          "
                  "\n (C3) / (3) Example 3 - Using LOOP with input value to set the end of the RANGE          "
                  "\n (C4) / (4) Example 4 - Using Loop in INPUTED Numbers or RANGE             "
                  "\n (C5) / (5) Example 5 - Using LOOP with  RANGE and LEN commands       "
                  "\n (C6) / (6) Example 6 - Using Loop in to print out part of the array using INPUTED beginning and ending RANGE  \n"


                  "\n (D) Description "
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

