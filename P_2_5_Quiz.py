from PC_1_1_Tools import *
from math import *


def terms_page():
    def title():
        new_page()
        print("                                                            ---------------   Coding Terms   ----------------"      )
    title()
    print("\n               *    Polymorphism  "
          "\n                       - same block of code "
          "\n                       - same name "
          "\n                              ---      Motorcycle  --> 2 wheels "
          "\n                              ---      Car  --> 4 wheels "
          "\n                              ---      Tricycle  --> 3 wheels "
          "\n             *   Lists"
          "\n                           - Lists are used to store multiple items in a single variable. "
          "\n                           - Lists are one of 4 built-in data types in Python used to store collections of data., "
          "\n                           - The other 3 are Tuple, Set, and Dictionary, all with different qualities and usage"
          "\n             *   Tuples"
          "\n                             - Tuples are used to store multiple items in a single variable. "
          "\n                             - Tuple is one of 4 built-in data types in Python used to store collections of data."
          "\n                             - ,The other 3 are List, Set, and Dictionary, all with different qualities and usage. "
          "\n                             - A tuple is a collection which is ordered and unchangeable.\n"
          )
    continue_lesson()
    title()
    print(
        "             *   Functions:"
        "\n                                - The following are the different types of Python Functions"
        "\n                                         --  Built-in Functions            "
        "\n                                         --  Recursion Functions            "
        "\n                                         --  Lambda Functions            "
        "\n                                         --  User-defined Functions         "
        "\n\n             *   Built in Functions"
        "                           - str(), int(), and etc"
        "\n\n             *   Python Recursion Functions           "
        "\n                     \"Recursive functions are functions that calls itself. It is always made up of 2 portions,"
        "\n                       the base case and the recursive case. The base case is the condition to stop the recursion. "
        "\n                       The recursive case is the part where the function calls on itsel \""
        "\n\n             *   Python Lambda Functions      "
        "\n                         \"A lambda function is a small anonymous function. A lambda function can take any number of arguments, "
        "\n                               but can only have one expression\"      "
        "\n\n             *   Python User-defined Functions  "
        "\n                         \"Functions that we define ourselves to do certain specific task are referred as"
        "\n                           user-defined functions. The way in which we define and call functions in Python are "
        "\n                           already discussed. Functions that readily come with Python are called built-in functions\"  \n    "
    )
    continue_lesson()
    title()

    print("           *   Expression:"
          "\n                     - \" combination of operators and operands. An example of expression can be : x = x + 1 0 x = x + 10 x=x+10." \
          "\n                            In this expression, the first 1 0 10 10 is added to the variable x. " \
          "\n                               After the addition is performed, the result is assigned to the variable x\"."
          "\n\n            *    Return Statement:"
          "\n                      - \"A special statement that you can use inside a function or method to send the function's result back to the caller. "
          "\n                           A return statement consists of the return keyword followed by an optional return value. The return value of a Python "
          "\n                             function can be any Python object.\""
          "\n\n             *   If Statement:"
          "\n                      -  \"Python if statement is one of the most commonly used conditional statements in programming languages. "
          "\n                            It decides whether certain statements need to be executed or not. It checks for a given condition, if the condition "
          "\n                            is true, then the set of code present inside the ” if ” block will be executed otherwise no   "
          "\n\n             *   IF STATEMENT and Comparison: "
          "\n                     - \"You can compare strings in Python using the equality ( == ) and comparison ( < , > , != , <= , >= ) operators. "
          "\n                         \"There are no special methods to compare two strings\". \n"
          )

    input("\nPress Enter to go back to Programming Notes :   ")
    import P_2_1_Coder_Information_Menu
    P_2_1_Coder_Information_Menu.Coder_main_menu_1()




