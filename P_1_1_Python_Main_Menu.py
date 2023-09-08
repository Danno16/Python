'''===================================================================================
                                                                    Imported Files
=================================================================================='''


import P_1_1_How_to_Print
import P_1_2_Variable_and_Data_Type
import P_1_3_Additional_print_Options
import P_1_4_Concatenate
import P_1_5_functions
import P_1_6_Numbers_Variables
import P_1_7_More_about_numbers
import P_1_8_Building_a_Calculator
import P_1_9_Mad_Lib
import P_1_10_Working_with_Lists
import P_1_11_Working_with_Tuples
import P_1_12_Working_with_Function
import P_1_13_Return_statement
import P_1_14_if_statement
import P_1_15_ifs_statement_comparisons
import P_1_16_better_calculator
import P_1_17_dictionaries
import P_1_18_Working_While_Loops
import P_1_19_Building_Guessing_Game
import P_1_20_Using_FOR_LOOPS
import P_1_21_EXPONENT_FUNCTION
import P_1_22_2d_Lists_Nested_Loops
import P_1_23_Building_a_Translator
import P_1_24_Try_Except
import P_1_25_Reading_Files
import P_1_26_Lesson_26_Modules_and_PiP
import P_1_27_Lesson_27_Classes_objects
import P_1_28_Lesson_28_Multiple_Choice_Quiz
import P_1_29_Lesson_29_Object_Function
import P_1_30_Lesson_30_Inheritance
import P_2_1_Coder_Information_Menu



def main_menu_1():            #                Main Menu Screen
    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------           LESSON PROGRAMS           --------------------------------    \n")
    print(
        "Lesson 1 - How to Print in Python                                        Lesson 16 - Building a better Calculator                            ")
    print("Lesson 2 - Variable and Data Types                                    Lesson 17 - Using Dictionaries")
    print(
        "Lesson 3 - Additional Print options                                       Lesson 18 - Working with While Loops ")
    print("Lesson 4 - How to Concatenate Text and Numbers            Lesson 19 - Building a guessing Game")
    print("Lesson 5 - Use of Functions                                                 Lesson 20 - Using FOR LOOPS")
    print("Lesson 6 - Use Numbers\ Store in Variables                       Lesson 21 -  EXPONENT FUNCTION ")
    print(
        "Lesson 7 - More about Numbers                                          Lesson 22 -  2D LISTS AND NESTED LOOPS")
    print(
        "Lesson 8 - Building a Calculator                                           Lesson 23 -  BUILDING A TRANSLATOR ")
    print("Lesson 9 - Building a Mad Lib                                              Lesson 24  - Using Try / Except")
    print("Lesson 10 - Working with LISTS                                          Lesson 25  - Working with Files")
    print("Lesson 11 - Working with TUPLES                                      Lesson 26  - Modules and PIP")
    print("Lesson 12 - Working with FUNCTIONS                               Lesson 27  - Classes and Objects ")
    print("Lesson 13 - RETURN Statement                                          Lesson 28  - Trivia Pursuit")
    print("Lesson 14 - IF Statement                                                      Lesson 29 - Object Function")
    print("Lesson 15 - IF STATEMENT and Comparison                    Lesson 30  - Inheritance")

    a = input("\nSelect Lesson Number, (P) for Programming Notes, or <Enter> to Return to Main Menu :  ")

    if a == "1":
        P_1_1_How_to_Print.lesson_1()
    if a == "2":
        P_1_2_Variable_and_Data_Type.lesson_2()
    if a == "3":
        P_1_3_Additional_print_Options.lesson_3()
    if a == "4":
        P_1_4_Concatenate.lesson_4()
    if a == "5":
        P_1_5_functions.lesson_5()
    if a == "6":
        P_1_6_Numbers_Variables.lesson_6()
    if a == "7":
        P_1_7_More_about_numbers.lesson_7()
    if a == "8":
        P_1_8_Building_a_Calculator.lesson_8()
    if a == "9":
        P_1_9_Mad_Lib.lesson_9()
    if a == "10":
       P_1_10_Working_with_Lists.lesson_10()
    if a == "11":
       P_1_11_Working_with_Tuples.lesson_11()
    if a == "12":
       P_1_12_Working_with_Function.lesson_12()
    if a == "13":
       P_1_13_Return_statement.lesson_13()
    if a == "14":
       P_1_14_if_statement.lesson_14()
    if a == "15":
       P_1_15_ifs_statement_comparisons.lesson_15()
    if a == "16":
       P_1_16_better_calculator.lesson_16()
    if a == "17":
       P_1_17_dictionaries.lesson_17()
    if a == "18":
       P_1_18_Working_While_Loops.lesson_18()
    if a == "19":
       P_1_19_Building_Guessing_Game.lesson_19()
    if a == "20":
       P_1_20_Using_FOR_LOOPS.lesson_20()
    if a == "21":
       P_1_21_EXPONENT_FUNCTION.lesson_21()
    if a == "22":
       P_1_22_2d_Lists_Nested_Loops.lesson_22()
    if a == "23":
       P_1_23_Building_a_Translator.lesson_23()
    if a == "24":
       P_1_24_Try_Except.lesson_24()
    if a == "25":
       P_1_25_Reading_Files.lesson_25()
    if a == "26":
        P_1_26_Lesson_26_Modules_and_PiP.lesson_26()
    if a == "27":
        P_1_27_Lesson_27_Classes_objects.lesson_27()
    if a == "28":
        P_1_28_Lesson_28_Multiple_Choice_Quiz.lesson_28()
    if a == "29":
        P_1_29_Lesson_29_Object_Function.lesson_29()
    if a == "30":
        P_1_30_Lesson_30_Inheritance.lesson_30()
    if a == "p":
        P_2_1_Coder_Information_Menu.Coder_main_menu_1()
    if a == "P":
        P_2_1_Coder_Information_Menu.Coder_main_menu_1()
    else:
        main_menu_1()

main_menu_1()


