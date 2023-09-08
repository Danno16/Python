from PC_1_1_Tools import *

def lesson_21():
    def title():
        new_page()
        print(
            "\n                                   -----------------------------------   Lesson 21 -  EXPONENT FUNCTION  -----------------------------\n")

    def definition():
        title()
        print("An Exponent function allows us to take a certain number and raise it to a specific power.")
        print("         - An Example:  3^4 = 81.")
        print("         - In pyton the \"**\" represents the power of.")
        end()



    def example_1_code():
        title()
        print("             Example 1 -  Using LOOP to raise to the power of with input      \n")
        print("We are asking for user input to provide a number then raising to the power of")


        print("           1        def raise_to_power(base_num, power_num):")
        print("           2        result = 1")
        print("           3              for i in range(power_num):")
        print("           4        result = result * base_num   ")
        print("           5        return result")

        print("           6        a = int(input(\"Enter number:  \"))    ")
        print("           7        b = int(input(\"Enter Exponent:  \"))  ")

        print("           8        print(raise_to_power(a, b))\n")




    def example_1():
        title()
        print("                                              Example 1 -  Using LOOP to raise to the power of with input     \n")
        def raise_to_power(base_num, power_num):
            result = 1
            for i in range(power_num):
                result = result * base_num
            return result

        a = int(input("Enter number:  "))
        b = int(input("Enter Exponent:  "))

        print(raise_to_power(a, b))
        print("  \n")


    def example_2_code():
        title()
        print("                                              Example 1 -  Using LOOP to raise to the power of with input     \n")
        def raise_to_power(base_num, power_num):
            result = 1
            for i in range(power_num):
                result = result * base_num
            return result

        a = int(input("Enter number:  "))
        b = int(input("Enter Exponent:  "))

        print(raise_to_power(a, b))

        print("  This is how we coded this exercise.\n\n")

    def end():
        a = input("\n Please Select: To see the code behind the example put \"C\" before the number: \n"
                  "\n (D) Description of Lesson "

                  "\n (C1) / (1) Example 1 -  Using LOOP to raise to the power of with input  \n"
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

        if str(a) == "d":
            definition()
        if str(a) == "D":
            definition()

        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()