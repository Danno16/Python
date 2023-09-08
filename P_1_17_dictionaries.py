from PC_1_1_Tools import *
def lesson_17():
    monthConversion = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December",
        "jan": "January",
        "feb": "February",
        "mar": "March",
        "apr": "April",
        "may": "May",
        "jun": "June",
        "jul": "July",
        "aug": "August",
        "sep": "September",
        "oct": "October",
        "nov": "November",
        "dec": "December",
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }

    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson - 17  Using Dictionaries   -----------------------------\n")

    def definition():
        title()
        print(
            "             *  A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated valu]")
        print(
            "             *  Dictionaries are Python's implementation of a data structure that is more generally known as an associative array.")
        print(
            "             *  A dictionary is a collection which is ordered*, changeable and do not allow duplicates.")
        print("             *  Dictionaries are used to store data values in key:value pairs. ")
        print(
            "             *  Dictionaries allow us to associate a value to a unique key, and then to quickly access this value.")
        print(
            "             *  It's a good idea to use them whenever we want to find (lookup for) a certain Python object.")
        print("             *  List  are much slower than dictionaries")
        end()

    def print_code_dictionary():
        title()
        print("                                 monthConversion = {")
        print("                                \"Jan\": \"January\",  ")
        print("                                \"Feb\": \"February\",  ")
        print("                                \"Mar\": \"March\",  ")
        print("                                \"Apr\": \"April\",  ")
        print("                                \"May\": \"May\",  ")
        print("                                \"Jun\": \"June\",  ")
        print("                                \"Jul\": \"July\",  ")
        print("                                \"Aug\": \"August\",  ")
        print("                                \"Sep\": \"September\",  ")
        print("                                \"Oct\": \"October\",  ")
        print("                                \"Nov\": \"November\",  ")
        print("                                \"Dec\": \"December\",  ")
        print(
            "  Page 1 of the list - The Above list is used to convert the 3 letters to the Full Month (Notice -  the fist letter is all UPPER case).\n")
        continue_lesson()
        title()
        print("                                \" jan\": \"January\",  ")
        print("                                \"feb\": \"February\",  ")
        print("                                \"mar\": \"March\",  ")
        print("                                \"apr\": \"April\",  ")
        print("                                \"may\": \"May\",  ")
        print("                                \"jun\": \"June\",  ")
        print("                                \"jul\": \"July\",  ")
        print("                                \"aug\": \"August\",  ")
        print("                                \"sep\": \"September\",  ")
        print("                                \"oct\": \"October\",  ")
        print("                                \"nov\": \"November\",  ")
        print("                                \"dec\": \"December\",  ")
        print(
            "  Page 2 of the list - The Above list is used to convert the 3 letters to the Full Month (Notice -  the fist letter is all LOWER case).\n")
        continue_lesson()
        title()
        print("                                \"1\": \"January\",  ")
        print("                                \" 2\": \"February\",  ")
        print("                                \"3\": \"March\",  ")
        print("                                \"4\": \"April\",  ")
        print("                                \"5\": \"May\",  ")
        print("                                \"6\": \"June\",  ")
        print("                                \"7\": \"July\",  ")
        print("                                \"8\": \"August\",  ")
        print("                                \"9\": \"September\",  ")
        print("                                \"10\": \"October\",  ")
        print("                                \"11\": \"November\",  ")
        print("                                \"12\": \"December\",  ")
        print("                                 }")
        print(" Page 3 of the list - The Above list is used to convert the NUMERIC to the month.\n")
        continue_lesson()

    def run_lesson():
        title()
        print("First we have to create a list:  Here is the format to enter a list:")
        continue_lesson()
        print_code_dictionary()
        title()
        print(
            "Then we are going to hard code a command using a UPPER case as the first letter. The month we are going to enter is \"Nov\".")
        print("                   CODE -            print(monthConversion[\"Nov\"])")
        print("                   OUTPUT-        " + monthConversion["Nov"])

        print("\nNext we are going hard code using all LOWER case. The month we are going to enter is \"aug\".")
        print("                   CODE -            print(monthConversion[\"aug\"])")
        print("                   OUTPUT-        " + monthConversion["aug"])

        print("\nLast we are going hard code a command using a  NUMERIC. The month we are going to enter is \"2\".")
        print("                   CODE -            print(monthConversion[\"2\"])")
        print("                   OUTPUT-        " + monthConversion["2"] + "\n\n")
        continue_lesson()

        title()
        print(
            "\nNow were going to us the [.get.] Command  By using [.get.] Command it won't error out even if the element KEY DOES NOT exist.)")
        print("First we'll try a valid entery.  We'll use \"Mar\"")
        print("\n                     CODE -       print(monthConversion.get(\"Mar\", \"Not a Valid Month\"))")
        print("                     OUTPUT -   " + monthConversion.get("Mar", "Not a Valid Month"))

        print(
            "\nLets try another condition.  We'll use another valid entry of  \"12\".")
        print("\n                     CODE -       print(monthConversion.get(\"12\", \"Not a Valid Month\"))")
        print("                     OUTPUT -   " + monthConversion.get("12", "Not a Valid Month"))
        print("\nNow lets try a negative condition.   We'll use the entry of  \"dan\".")
        print("\n                      CODE -       print(monthConversion.get(\"dan\", \"Not a Valid Month\"))")
        print("                      OUTPUT -   " + monthConversion.get("dan", "Not a Valid Month") + "\n")

        continue_lesson()
        title()

        print("\nNow lets continue the fun.  Lets hard code numbers.  First were going to enter 5:")
        print("\n                      CODE -       print(monthConversion.get(\"5\", \"Not a Valid Month\"))")
        print("                      OUTPUT -   " + monthConversion.get("5", "Not a Valid Month"))

        print("\nNow lets try Number 2: ")
        print("\n                      CODE -       print(monthConversion.get(\"2\", \"Not a Valid Month\"))")
        print("                      OUTPUT -   " + monthConversion.get("2", "Not a Valid Month"))

        print("\nLast lets try Number 22. (Negative condition: ")
        print("\n                      CODE -       print(monthConversion.get(\"22\", \"Not a Valid Month\"))")
        print("                      OUTPUT -   " + monthConversion.get("22", "Not a Valid Month") + "\n")

        continue_lesson()
        code_1()

    def code_1():
        print(
            "\nLets us abbreviated inputs.  Enter Jan to Dec, or 1 to 12, and Etc.  You can also use negative conditions")
        a = input("Enter abbreviated Month:  Enter \"X\"  to go back to main menu:  ")
        print(monthConversion.get((a), "Not a Valid Month") + "\n")
        if a == "x":
            lesson_17()
        elif a == "X":
            lesson_17()
        else:
            code_1()

    def see_code():
        print(
            "      print(\"\\nLets us abbreviated inputs.  Enter Jan to Dec, or 1 to 12, and Etc.  You can also use negative conditions\") - Simple print statement  ")
        print(
            "      a = input(\"Enter abbreviated Month:  Enter \"X\"  to go back to main menu:  \")       - input used for month conversion or to go to menu ")
        print(
            "      print(monthConversion.get((a), \"Not a Valid Month\") + \"\\n\")  -  Code used or month conversions or \"Not a Valid Month\"")
        print(
            "\n      if a == \"x\":                                                                                    - if the input is lower case \"x\", it will run function called \"lesson_h() \" ")
        print("            lesson_17() ")
        print(
            "     elif a == \"X\":                                                                                  - if the input is lower case \"X\", it will run function called \"lesson_h() \" ")
        print("         lesson_17() ")
        print(
            "     else:                                                                                                 - if neither condition apply it will run function called \"code_1() \" ")
        print("         code_1()\n\n\n ")
        continue_lesson()
        lesson_17()

    def end():
        a = input("\n Please Select: "
                  "\n           (R) This gives a step by step of the commands entered and what that code does.."
                  "\n           (C) This gives an example of the we built to show the power of using dictionaries."
                  "\n           (D) Description of Python Dictionary."
                  "\n           (L) To see the layout of the dictionary\n"

                  "\n           <Enter>  for main menu: ")
        if str(a) == "d":
            lesson_17()
        if str(a) == "D":
            lesson_17()

        if str(a) == "l":
            print_code_dictionary()
            definition()
        if str(a) == "L":
            print_code_dictionary()
            definition()

        if str(a) == "r":
            run_lesson()
        if str(a) == "R":
            run_lesson()

        if str(a) == "c":
            title()
            code_1()
        if str(a) == "C":
            title()
            code_1()

        if str(a) == "s":
            title()
            see_code()
        if str(a) == "s":
            title()
            see_code()
        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()

