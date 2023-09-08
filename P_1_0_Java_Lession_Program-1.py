from PC_1_1_Tools import *
from PC_1_1_1_Class_file import Car
from PC_1_1_1_Class_file import Question

def continue_lesson():
    input(" press <Enter> to Continue: "
          "")

def new_page():ttrttt

    for i in range (20):
        print("")

from PC_1_1_1_Class_file import student_object
from PC_1_1_1_Class_file import chef_class1
from PC_1_1_1_Class_file import chef_class2

def main_menu_1():
    menu = [lesson_1, lesson_2, lesson_3, lesson_4, lesson_5, lesson_6,
            lesson_7, lesson_8, lesson_9, lesson_10, lesson_11, lesson_12, lesson_13, lesson_14, lesson_15,
            lesson_16, lesson_17, lesson_18, lesson_19, lesson_20, lesson_21, lesson_22, lesson_23, lesson_24,
            lesson_25, lesson_26, lesson_27, lesson_28, lesson_29, lesson_30]

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------           LESSON PROGRAMS           --------------------------------    \n")
    print("Lesson 1 - How to Print                                                        Lesson 16 - Building a better Calculator                            ")
    print("Lesson 2 - Variable and Data Types                                    Lesson 17 - Using Dictionaries")
    print("Lesson 3 - Additional Print options                                       Lesson 18 - Working with While Loops ")
    print("Lesson 4 - How to Concatenate Text and Numbers            Lesson 19 - Building a guessing Game")
    print("Lesson 5 - Use of Functions                                                 Lesson 20 - Using FOR LOOPS")
    print("Lesson 6 - Use Numbers\ Store in Variables                       Lesson 21 -  EXPONENT FUNCTION ")
    print("Lesson 7 - More about Numbers                                          Lesson 22 -  2D LISTS AND NESTED LOOPS")
    print("Lesson 8 - Building a Calculator                                           Lesson 23 -  BUILDING A TRANSLATOR ")
    print("Lesson 9 - Building a Mad Lib                                              Lesson 24  - Using Try / Except")
    print("Lesson 10 - Working with LISTS                                          Lesson 25  - Working with Files")
    print("Lesson 11 - Working with TUPLES                                      Lesson 26  - Modules and PIP")
    print("Lesson 12 - Working with FUNCTIONS                               Lesson 27  - Classes and Objects ")
    print("Lesson 13 - RETURN Statement                                          Lesson 28  - Trivia Pursuit")
    print("Lesson 14 - IF Statement                                                      Lesson 29 - Object Function")
    print("Lesson 15 - IF STATEMENT and Comparison                    Lesson 30  - Inheritance")

    try:
        a = input("\n\nChoose Lesson or (P) for programming Notes (T)  for Terminology:  ")
        if str(a) == "p":
            version_control()
        if str(a) == "P":
            version_control()
        if str(a) == "t":
            terms()
        if str(a) == "T":
            terms()
        else:
            menu [int(a)-1]()


    except ValueError:
        print("\n Not a valid entry")
        main_menu_1()





def lesson_1():
    print("\n\n\n\n\n\n\n\n\n                                                            -----   Lesson 1 -  How to Print    --------\n")

    print("In order to print something on the screen you have to use the following command: print(\"Hello World\")")
    print("\nHello World")
    input("\n\nPress <Enter> to Continue: ")

    print("\n\n\n\n                                                            -----   How to Print    --------\n")
    print("\nNow Lets try it again.  Lets print - How are you doing? -  using the following command: print(\"How are you doing?\")")
    print("\nHow are you doing?")
    input("\n\nPress <Enter> to Continue: ")
    print("\n\n\n\n                                                            -----   How to Print    --------\n")
    print("Now were going to try something a little more complex.  Were going to make a half triangle using the following code:")

    print("print(\"      /|\")")
    print("print(\"     / |\")")
    print("print(\"    /  |/\")")
    print("print(\"   /   |/\")")
    print("print(\"  /    |/\")")
    print("print(\" /     |/\")")
    print("print(\"/___|/\")")

    input("\n\nPress <Enter> to run the code: ")

    print("      /|")
    print("     / |")
    print("    /  |")
    print("   /   |")
    print("  /    |")
    print(" /     |")
    print("/___|")
    print("Here is the output - Really Cool Huh?")

    a = input("\n\nThis is the end of this lesson - Do you want to redo The lesson? (y) or push <ENTER>: ")
    if str(a) == "y":
        lesson_1()
    else:
        main_menu_1()


#---------------------------------------------------------------------------------------------------

def lesson_2():
    print("\n\n\n\n\n\n\n\n\n\n   -------------------------------- Lesson 2 -Variable and Data Types --------------------------------")
    print("Think of a variable as a box where you can store stuff.  You can store:\n")
    print("                        Strings - Alpha and Numeric")
    print("                        Numbers -  Numeric")
    print("                        Boolean - True False")
    print("\n    There are other values but we'll leave it for now")

    input("\n\nPress <Enter> to Continue: ")
    print("\n\n\n\n\n\n\n\n\n\n   -------------------------------- Lesson 2 -Variable and Data Types --------------------------------")
    print("Now Lets sets some variables.  We'll set the variables: (name = \"dan\"),  (age = \"10\") and (isMale = false).")
    print("    - Now notice we use quotation marks (\") around the name and age. ")
    print( "    - Quotation marks is how we set the variable as a string.  ")
    print( "    - Notice the varialbe called isMale = false  This is how we set as a booleen value.  ")
    input("\n\nPress <Enter> to Continue: ")

    print("\n\n\n\n\n\n\n\n\n\n   -------------------------------- Lesson 2 -Variable and Data Types --------------------------------")
    print(" Lets look at how we actually code. ")
    print("           name = \"dan\"  # String")
    print("           age = \"20\"  # String")
    print("           isMale = False  # Bulion Vale")

    name = "dan"  # String
    age = "10"  # String
    isMale = False  # Bulion Vale


    print("\n\n\n\n\n\n\n\n\n\n   -------------------------------- Lesson 2 -Variable and Data Types --------------------------------")
    print(" Okay now lets acually us these variables in a sentence.  Here is the code were going to use ")
    print("           name = \"dan\"  # String")
    print("           age = \"10\"  # String")
    print("  Note - Notice the format to combine text with a variable.  The text is wrapped with quotations marks then (+) adds in the variables")
    print("\n  The text is wrapped with quotations marks then (+) adds in the variables")
    print("           print(\"There once name named \" + name + \",\")")
    print("           print(\"He was  \" + age + \" years old. \")")
    print("           print(\"He really liked the name \" + name + \",)")
    print("           print(\"but he did not like to be \" + age + \" years old.\")")

    input("\n\nPress <Enter> to Continue>: ")

    print("\n\n\n\n\n\n\n\n\n\n   -------------------------------- Lesson 2 -Variable and Data Types --------------------------------")
    print("\n Here is the output:\n ")
    print("There once name named " + name + ",")
    print("He was  " + age + " years old.  ")
    print("He really liked the name " + name + ",")
    print("but he did not like to be " + age + " years old.")

    a = input("\n\nThis is the end of this lesson - Do you want to redo The lesson? (y) or push <ENTER>: ")
    if str(a) == "y":
        lesson_2()
    else:
        main_menu_1()



def lesson_3():
    print("\n\n\n\n\n\n\n\n\n\n    -------------------------------- Lesson 3 - Additional Print options--------------------------------")
    print("\nOkay there are additional features in printing.  If you use:")
    print("                      -  \\n = it will insert a line.")
    print("                      -  \\ = you can print key items that you wouldn't normally be able to print like \" \\ and etc.")

    input("\n\nPress <Enter> to Continue: ")
    print("\n\n\n\n\n   -------------------------------- Lesson 3 - Additional Print options--------------------------------")
    print("\n So in lesson 1, we printed half a triangle.  Now we will print a full one. Now python will not print \\ because as ")
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
    print("\n\n\n\n\n   -------------------------------- Lesson 3 - Additional Print options--------------------------------")
    print("\nHere is the output.  It prints a full triangle.\n")
    print("      /\\")
    print("     /  \\")
    print("    /    \\")
    print("   /      \\")
    print("  /        \\")
    print(" /          \\")
    print("/______\\")
    print("\n This is the end of this lesson.")
    a = input("\n\nThis is the end of this lesson - Do you want to redo The lesson? (y) or push <ENTER>: ")
    if str(a) == "y":
        lesson_3()
    else:
        main_menu_1()


def lesson_4():
    print("\n\n\n\n\n\n\n\n\n                                  -------      Concatenate Text and Variables    ---------\n")
    print("We touched upon this in Lesson - 2,  but we'll go over it again.  To combine Text or Variables we use the  plus sign (+).")
    print("\nLets set the variable of {first_name} as \"Spider\" and the variable {last name} to \"man\".")
    print("                 first_name = \"Spider \"")
    print("                 last_name = \"man\"")
    input("\n\nPress <Enter> to Continue: ")


    print("\n\n\n\n\n\n\n\n\n                                  -------      Concatenate Text and Variables    ---------")
    first_name = "Spider "
    last_name = "man"
    print(" So to combine variables first_name and last_name we use {+}.  Here is the code were using:")
    print("                 print(first_name + last_name)")
    print("\nHer is the ouput:")
    print("                           " + first_name + last_name)

    input("\n\nPress <Enter> to Continue: ")

    print("\n\n\n\n\n\n\n\n\n                                  -------      Concatenate Text and Variables    ---------")
    print("\nNow were going to do a combination of concatenation: following by the output:\n")
    print("      Code:  print(\"A \" + first_name + \"is scary.\"" + "                                                  Output:   A " + first_name + "is scary.")
    print("      Code:  print(\"Super\" + last_name) " + "                                                              Output:    Super" + last_name)
    print("      Code:  print(\"The Hulk is stronger than \" + first_name + last_name)         Output:    The Hulk is stronger than " + first_name + last_name)



    a = input("\n\nThis is the end of this lesson - Do you want to redo The lesson? (y) or push <ENTER>: ")
    if str(a) == "y":
        lesson_4()
    else:
        main_menu_1()


def lesson_5():
    print("\n\n\n\n\n\n\n\n\n                                  -------      Use of Functions    ---------\n")
    print("We are going to concentrate are some of the functions that are available in python.")
    print("We are going to show the code for the function and description then the output.")
    print("We are going to use 2 Variables {first_name} and {last_name}\n")
    print("first_name = \"Albert\"")
    print("first_name = \"Einstein\"")
    first_name = "Albert"
    last_name = "Einstein"
    input("\n\nPress <Enter> to Continue: ")

    print("\n\n\n\n\n\n\n\n          CODE                                                     Description                                                            Output")
    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print("  print(first_name.upper())                       Makes it all UPPER Case                                                       " + (first_name.upper()))
    print("  print(first_name.lower())                        Makes it all lower Case                                                           " + (first_name.lower()))
    print("  print(first_name.isupper())                    Checks to see if all UPPER Case                                           " + str(first_name.isupper()))
    print("  print(first_name.islower())                     Checks to see if all LOWER Case                                          " + str(first_name.islower()))
    print("  print(first_name.upper().isupper())       Makes it all Upper Case then sees if it is all upper  case       " + str(first_name.upper().isupper()))
    print("  print(first_name.lower().islower())        Makes it all LOWER Case then sees if it is all upper  case.   " + str(first_name.lower().islower()))
    print("  print(len(first_name))                            Lengh of the string (were using the first name                         " + str(len(first_name)))
    print("  print(len(first_name + Last_name))      Lengh of the string with concatenation                                     " +  str(len(first_name + last_name)))
    print("  print(first_name[0])                               1st Letter of the string                                                               " + (first_name[0]))
    print("  print(first_name[2])                               3d Letter of the string                                                                " + (first_name[2]))
    print("  print(first_name[4])                               5th  Letter of the string                                                              " + (first_name[4]))
    print("  print(first_name.index(\"A\"))                Tells me what position the letter \"A\" is                                      " + str(first_name.index("A")))
    print("  print(first_name.index(\"e\"))                 Tells me what position the letter \"e\" is                                      " + str(first_name.index("e")))
    print("  print(first_name.replace(\"S\", \"P\"))    Replaces the b with a P                                                              " + first_name.replace("b", " - Pop - "))

    a = input("\n\nThis is the end of this lesson - Do you want to redo The lesson? (y) or push <ENTER>: ")
    if str(a) == "y":
        lesson_5()
    else:
        main_menu_1()


def lesson_6():
    print("\n\n\n\n\n\n\n\n\n                                  -------      Use Numbers   ---------\n")
    print("\n\n\n\n\n\n\n\n          CODE                                                     Description of outcome                                                           Output")
    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print(" print(2)                             Prints the Sum                                                                                                " + str(2))
    print(" print(2.55252)                  Prints the Sum                                                                                                " + str(22.55252))
    print(" print(2+5)                         Prints the Sum                                                                                                " + str(5+2))
    print(" print(2-5)                          Prints the Sum                                                                                                " + str(2-5))
    print(" print(2*525214)                Prints the Sum                                                                                                " + str(22*525214))
    print(" print(2/5)                          Prints the Sum                                                                                                 " + str(2/5))
    print(" print(2 -3 *12 /5)              Example of  complex compulations                                                                 "+ str(2 -3 * 12 /5))
    print(" print(2 -3 * (12 /5))           You can changes the order of operations                                                       "+ str(2 -3 * (12 /5)))
    print(" print(10 % 3)                   Module operator divides 10 by 3 and will display the remainder                   " + str(10%3))
    input("\n\nPress <Enter> to Continue: ")


    print("\n\n\n\n\n\n\n\n\n                                  -------      Calculations with Variables  ---------\n")
    print("Now were going to use Variables\n ")

    print("      CODE                                                     Description of outcome                                                           Output")
    print(
        "`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    first_num = 10
    second_num = 20
    print("first_num = 10                                                          Stores the number 10 in variable of {first_num}                                  - No output")
    print("second_num = 20                                                    Stores the number 20 in variable of {second_num}                            - No output")
    print("print(first_num + second_num)                               Prints the first_num PLUS second_num                                             " + str(first_num + second_num))
    print("print(first_num - second_num)                                Prints the first_num SUBTRACT second_num                                   " + str(first_num - second_num))
    print("print(first_num * second_num)                                Prints the first_num MULTIPLY second_num                                     " + str(first_num * second_num))
    print("print(first_num / second_num)                                Prints the first_num DIVIDED BY second_num                                  " + str(first_num / second_num))
    print("print(first_num + second_num + second_num)      Prints the first_num PLUS second_num  PLUS second_num           " + str(first_num + second_num+ second_num))
    input("\n\nPress <Enter> to Continue: ")



    print("\n\n\n\n\n\n\n\n\n                                                             -------      Calculations with  inputs and stored  in Variables  ---------\n")
    print("\n\n\n\n\n Now were going to use the same formulas using values we input and store in variables {first_num} and {second_num}:")
    first_num = int(input("\nEnter First Number:  "))
    second_num = int(input("\nEnter Second Number:  "))


    print("\n\n\n\n\n\n\n\n\n       CODE                                                     Description of outcome                                                           Output")
    print(
        "`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")


    print("first_num = input(\"Enter First Number\")                Stores inputed value  in variable of {first_num}                                  - first_num = " + str(first_num))
    print("second_num = input(\"Enter Secondt Number\")    Stores inputed value  in variable of{second_num}                             - second_num = " + str(second_num))
    print("print(first_num + second_num)                               Prints the first_num PLUS second_num                                             " + str(int(first_num + second_num)))
    print("print(first_num - second_num)                                Prints the first_num SUBTRACT second_num                                   " + str(int(first_num - second_num)))
    print("print(first_num * second_num)                                Prints the first_num MULTIPLY second_num                                     " + str(first_num * second_num))
    print("print(first_num / second_num)                                Prints the first_num DIVIDED BY second_num                                  " + str(first_num / second_num))
    print("print(first_num + second_num + second_num)      Prints the first_num PLUS second_num  PLUS second_num           " + str(int(first_num + second_num + second_num)))
    print("This is the end of this less")
    a = input("\n\nThis is the end of this lesson - Do you want to redo The lesson? (y) or push <ENTER>: ")
    if str(a) == "y":
        lesson_6()
    else:
        main_menu_1()


def lesson_7():

    print("\n\n\n\n\n\n\n\n\n                                  -------      Lesson 7 - More about numbers  ---------\n")
    print(" In order to use a number with a text, you have to convert to a string. The following is an example:\n")
    print("     CODE                                                     Description of outcome                                                    Output")
    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    first_num = 10

    print("         first_num = 10                               - Stores the value of 10 in the variable first_num                     "  + str(first_num))
    print("         print(str(first_num))                       - Convert the number to a string.                                             " + str(first_num))
    print("         print(\"Albert\" + str(first_num))       - prints \"Albert\" plus  value iin the variable {first_num}           Albert" + str(first_num))
    input("\n\nPress <Enter> to Continue: ")


    print("\n\n\n\n\n\n\n\n\n\n Now were going to use number functions:\n")

    print("     CODE                                                     Description of outcome                                                    Output")
    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print(" print(pow(13,17))                                   Prints 13 to the power of 17                                     " + str(pow(13,17)))
    print(" print(max(13,17,23,52,3))                      Prints the largest number                                         " + str(max(13,17,23,52,3)))
    print(" print(min(13,17,23,52,3))                       Prints the smallest number                                      " + str(min(13,17,23,52,3)))
    print(" print(round(23.525))                              Rounds the number                                                  " + str(round(23.525)))
    print(" print(round(21,28725))                          Rounds the number                                                  " + str(round(21,28725)))

    input("\n\nPress <Enter> to Continue: ")
    print("\n\n\n\n\n\n\n\n\n\n Now were going to use formulas options that are not in basic Python. ")
    print(" In order to do this, we must import additional functions by using the following code:\n ")
    print(" from math import *:\n ")
    print("     CODE                                                     Description of outcome                                            Output")
    print("`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")

    print(" print(floor(3.7))                                       Chops off the decimal                                              " + str(floor(3.7)))
    print(" print(ceil(3.7))                                         Rounds a number UP to the nearest integet           " + str(ceil(3.7)))
    print(" print(sqrt(36))                                         Gives  us the square root of a number                    " + str(sqrt(36)))

    print("\n\n\n\n\n\n\n\n\n\n                                -------------------------------- Getting input from Users  --------------------------------          ")
    print("----------------------------------------------------------------------------------------------------------------------------------")
    print("\nWe are going to do another example of using input statements to auto populate a sentence.")
    print("First we'll do 2 inputs, name and age using the following commands:\n")

    print("         name = input(\"What is your full  Name: \")                                     ------      Input Text with variable \"name\"")
    print("         Age = input(\"What is your Age: \")                                                  ------      Input Text with variable \"Age\"")
    print("         print(\"\\n\\nHi \" + name + \" you are \" + Age + \" years old\")             ------      Output with the two variables")

    input("\n\nPress <Enter> to Continue: ")
    print("\n\n\n\n\n\n\n\n\n\n                                -------------------------------- Getting input from Users  --------------------------------          ")
    print("----------------------------------------------------------------------------------------------------------------------------------")
    print("")
    name = input("\nWhat is your full  Name: ")  # Input Text with variable "name"
    Age = input("What is your Age: ")  # Input Text with variable "Age"

    print("\n\nHi " + name + " you are " + Age + " years old")  # Output with the two variables
    input("\npress <Enter> Calculator using Integer")


    a = input("\n\nThis is the end of this lesson - Do you want to redo The lesson? (y) or push <ENTER>: ")
    if str(a) == "y":
        lesson_7()
    else:
        main_menu_1()




def lesson_8():
    print("\n\n\n\n\n\n\n\n\n\n -------------------------------- Building a Calculator it will error if use decimal--------------------------------")


    print("\n               ****  Example of using INTEGERS, Variables, and formulas (Does not allow for decimals)")
    print("Here is the code we are going to use:  The only things you may not recognize is turning string into integer.")
    print(" int(num1) changes the number from a string to a number so we can do calculations.\n")
    print("                 num1 = input(\"Enter First Number: \")                               ---          Input Number with variable \"num1\"")
    print("                 num2 = input(\"Enter Second Number: \")                          ---          Input Number with variable \"num2\"")
    print("                 result_add = int(num1) + int(num2)                                  ---          Converts to integers and ADDS variables")
    print("                 result_sub = int(num1) - int(num2)                                   ---          Converts to integers and SUBTRACTS variables")
    print("                 result_mult = int(num1) * int(num2)                                  ---          Converts to integers and MULTIPLY variables")
    print("                 result_div = int(num1) / int(num2)                                     ---         Converts to integers and DIVIDES variables\n")

    print("                 print(num1 + \" + \" + num2 + \" = \" + str(result_add))         ---         prints: first variable")
    print("                 print(num1 + \" - \" + num2 + \" = \" + str(result_sub))          ---         plus operator (+,- ,* , /) ")
    print("                 print(num1 + \" * \" + num2 + \" = \" + str(result_mult))         ---         second variable ")
    print("                 print(num1 + \" / \" + num2 + \" = \" + str(result_div))           ---         the equals sign")
    print("                                                                                                            ---        Converts {result_add} to string and prints it out.")

    input("\nPress <Enter> to run code:  ")


    num1 = input("\nEnter First Number   -     (Has to be a WHOLE number): ")  # Input Number with variable "num1"
    num2 = input("Enter Second Number  - (Has to be a WHOLE number):   ")  # Input Number with variable "num2"
    result_add = int(num1) + int(num2)  # Converts to integers and adds together
    result_sub = int(num1) - int(num2)  # Converts to integers and adds together
    result_mult = int(num1) * int(num2)  # Converts to integers and adds together
    result_div = int(num1) / int(num2)  # Converts to integers and adds together

    print("\n" + num1 + " + " + num2 + " = " + str(result_add))
    print(num1 + " - " + num2 + " = " + str(result_sub))
    print(num1 + " * " + num2 + " = " + str(result_mult))
    print( num1 + " / " + num2 + " = " + str(result_div))

    input("\nPress <Enter> build a Calculator that allows decimals:  ")

    print("\n\n\n\n\n\n\n\n\n\n\n\n                           -------------------      Building a Calculator now we can use decimals using FLOAT decimal      -----------------------")
    print(" \n              ****  Example of using FLOAT (allows for decimals), Variables, and formulas  **** ")
    print("   As you can see, we are using  FLOAT allows for decimal.  Here is the code were going to use:\n")

    print("                num1 = input(\"Enter First Number: \")                                ---          Input Number with variable \"num1\"")
    print("                num2 = input(\"Enter Second Number: \")                           ---          Input Number with variable \"num2\"")
    print("                result_add = float(num1) + float(num2)                             ---          Converts to Integer and adds together")
    print("                result_sub = float(num1) - float(num2)                              ---          Converts to integers and adds together")
    print("                result_mult = float(num1) * float(num2)                             ---          Converts to integers and adds together")
    print("                result_div = float(num1) / float(num2)                                 ---          Converts to integers and adds together\n")

    print("                print(num1 + \" + \" + num2 + \" = \" + str(result_add))         ---         prints: first variable\")")
    print("                print(num1 + \" - \" + num2 + \" = \" + str(result_sub))          ---         plus operator (+,- ,* , / \")")
    print("                print(num1 + \" * \" + num2 + \" = \" + str(result_mult))         ---         second variable \")")
    print("                print(num1 + \" / \" + num2 + \" = \" + str(result_div))           ---         the equals sign\")")
    print("                                                                                                           ---        Converts {result_add} to string and prints it out.")



    input("\nPress <Enter> to run the code:  ")


    num1 = input("Enter First Number       - Now you can use decimals: ")  # Input Number with variable "num1"
    num2 = input("Enter Second Number  - Now you can use decimals: ")  # Input Number with variable "num2"
    result_add = float(num1) + float(num2)  # Converts to integers and adds together
    result_sub = float(num1) - float(num2)  # Converts to integers and adds together
    result_mult = float(num1) * float(num2)  # Converts to integers and adds together
    result_div = float(num1) / float(num2)  # Converts to integers and adds together

    print(num1 + " + " + num2 + " = " + str(result_add))
    print(num1 + " - " + num2 + " = " + str(result_sub))
    print(num1 + " * " + num2 + " = " + str(result_mult))
    print(num1 + " / " + num2 + " = " + str(result_div))

    a = input("\n\nThis is the end of this lesson - Do you want to redo The lesson? (y) or push <ENTER>: ")
    if str(a) == "y":
        lesson_8()
    else:
        main_menu_1()

def lesson_9():
    print(" \n\n\n\n\n\n\n\n              ****  Example of Mad Lib using various Variables  ****")
    print("   \n  Now were going to have a little fun by building a simple mad lib. ")
    print("   I don't believe there is anything have not covered in previous lessons.")
    print("   Here is the code we are using:\n")
    print("                      name = input(\"\\n What is your Name: \")     ")
    print("                      color = input(\"\\n What is your favorite  color: \")    ")
    print("                      animal = input(\"\\n What is your favorite  Animal: \")    ")
    print("                      number = input(\"\\n What is your favorite  Number: \")    ")
    print("                      girl = input(\"\\n What is your favorite  Girl's Name: \")    ")
    print("                      boy = input(\"\\n What is your favorite  Boy's Name: \")    ")
    print(" \n      print( name + \" was riding a \" + animal + \" when all of a sudden he saw scary a gang leader named \" + girl +\" with a group of thugs named \")     ")
    print("      print(boy + \", \" + color + \", \" + number + \" and \" + name + \" was scared.\")    ")

    input("\nPress <Enter> to run the code:  ")

    print("\n\n\n\n\n\n\n\n\n\n\n\n   Provide the following inputs to see the example: ")

    name = input("\n\n\n\n What is your Name: ")
    color = input("\n What is your favorite  color: ")
    animal = input("\n What is your favorite  Animal: ")
    number = input("\n What is your favorite  Number: ")
    girl = input("\n What is your favorite  Girl's Name: ")
    boy = input("\n What is your favorite  Boy's Name: ")

    print("\n\n\n\n Here is the Output:")
    print("\n       " + name + " was riding a " + animal + " when all of a sudden he saw scary gang leader named " + girl + " with a group of thugs named ")
    print(boy + ", " + color + ", " + number + " and " + name + " was scared.")




    a = input("\n\nThis is the end of this lesson - Do you want to redo The lesson? (y) or push <ENTER>: ")
    if str(a) == "y":
        lesson_9()
    else:
        main_menu_1()

def lesson_10():
    print("\n\n\n\n\n\n\n\n\n\n\n\n                  -------------------------------- 10>  WORKING WITH LISTS--------------------------------    \n")
    print("Were going to build a list called {Cars}.  Here is the format to enter a list: \n")
    print("              Cars = [\"Mustang\", \"Camaro\", \"Challenger\", \"Pinto\", \"Pizza Car\", \"Shoe Car\", \"Ram\", \"F150\", \"F250\"]\n")

    Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
    print("Here is the command to print list named Cars:")
    print("print(Cars)\n\n\n\n")
    input("Press <Enter> to print the list named Cars:  ")

    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n                  -------------------------------- 2>  PRINTING NDIVIDUAL ITEMS IN A LIST--------------------------------    \n")

    print("\n Let's  print our list using using the command:  ")
    print("                              print(Cars)\n")
    print(Cars)

    input("\n\n\n\n\nPress <Enter> to print the INDIVIDUAL items in a list:  ")

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  -------------------------------- 2>  PRINTING NDIVIDUAL ITEMS IN A LIST--------------------------------    \n")

    print("\nNow what if we want to print an individual item in the list, we can use the following command")


    print("              print(Cars[0])       ----          Print 1st item in List   ")
    print("              print(Cars[1])       ----          Print 2nd item in List  ")
    print("              print(Cars[2])       ----          Print 3rd item in List  ")
    print("              print(Cars[3])       ----          Print 4th item in List  ")
    print("              print(Cars[4])       ----          Print 5th item in List  ")
    print("              print(Cars[5])       ----          Print 6th item in List  ")
    print("              print(Cars[6])       ----          Print 7th item in List  ")
    print("              print(Cars[7])       ----          Print 8th item in List  ")
    print("              print(Cars[8])       ----          Print 9th item in List  ")

    input("\nPress <Enter> to run the commands:  ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n                  -------------------------------- 2>  PRINTING NDIVIDUAL ITEMS IN A LIST--------------------------------    \n")
    print("Here is the output:")
    print("           " + Cars[0] + "             ---- Print 1st item in List  ")
    print("           " + Cars[1] + "              ---- Print 2nd item in List  ")
    print("           " + Cars[2] + "         ----  Print 3rd item in List  ")
    print("           " + Cars[3] + "                  ----  Print 4th item in List  ")
    print("           " + Cars[4] + "          ----  Print 5th item in List  ")
    print("           " + Cars[5] + "           ----  Print 6th item in List  ")
    print("           " + Cars[6] + "                  ----  Print 7th item in List  ")
    print("           " + Cars[7] + "                 ----   Print 8th item in List  ")
    print("           " + Cars[8] + "                 ----   Print 9th item in List  ")

    a = input(" \n\nPress <Enter> for List in cars in Reverse order:  ")


    print("\n\n\n\n\n\n\n\n\n\n\n\n                  -------------------------------- 3>  PRINTING NDIVIDUAL ITEMS IN REVERSE ORDER--------------------------------    \n")
    print("If we put a minus in front of the number position, it will find the items in the list from last to first.\n")

    print("             print(Cars[-1])  --- Print last item in List    ")
    print("             print(Cars[-2])  --- Print 2nd to last item in List  ")
    print("             print(Cars[-3])  --- Print 3rd to last item in List  ")
    print("             print(Cars[-4])  --- Print 4th to last item in List  ")
    print("             print(Cars[-5])  --- Print 5th to last item in List  ")
    print("             print(Cars[-6])  --- Print 6th to last item in List  ")
    print("             print(Cars[-7])  --- Print 7th to last item in List  ")
    print("             print(Cars[-8])  --- Print 9th to last item in List  ")
    print("             print(Cars[-9])  --- Print 9th to last item in List  ")

    a = input(" \nPress <Enter> to run  the code:  ")

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  -------------------------------- 3>  PRINTING NDIVIDUAL ITEMS IN REVERSE ORDER--------------------------------    \n")
    print(" Here is the output:\n")
    print("           " + Cars[-1] + "                             ---- Print last item in List  ")
    print("           " + Cars[-2] + "                             ---- Print 2nd to last item in List ")
    print("           " + Cars[-3] + "                             ----  Print 3rd to last item in List  ")
    print("           " + Cars[-4] + "                     ----  Print 4th to last item in List  ")
    print("           " + Cars[-5] + "                    ----  Print 5th to last item in List  ")
    print("           " + Cars[-6] + "                            ----  Print 6th to last item in List  ")
    print("           " + Cars[-7] + "                  ----  Print 7th to last item in List  ")
    print("           " + Cars[-8] + "                      ----   Print 8th to last item in List  ")
    print("           " + Cars[-9] + "                      ---- Print 9th to last item in List  ")

    input("\nPress <Enter> to set a RANGE in a List :  ")

    print("\n\n\n\n\n\n\n\n\n\n\n                 ----------------------------------- 4>  PRINTING RANGES IN A LIST ------------------------------------------------  ")



    print("\n   Here is the command to print the LAST 2 items on the list :")
    print("                 print(Cars[7:])     -  prints LAST 2 items on the list.\n")
    print("       Our List -    " + str(Cars))
    print("                    Output -  "  + str( Cars[7:]))

    a = input("\n\n\nPress <Enter> First 2 cars:  ")

    print(
        "\n\n\n\n\n\n\n\n\n\n\n                 ----------------------------------- 4>  PRINTING RANGES IN A LIST ------------------------------------------------  ")
    print("  Prints FIRST 2 items on the list    \n")
    print("\n   Here is the command:")
    print("                 print(Cars[:2])     -  prints FIRST 2 items on the list.\n")
    print("       Our List -    " + str(Cars))
    print("                    Output -  "  + str( Cars[:2]))

    a = input(" \n\n\nPress <Enter> Range from the 3rd car to the 5th: ")

    print("\n\n\n\n\n\n\n\n\n\n\n                 ----------------------------------- 4>  PRINTING RANGES IN A LIST ------------------------------------------------  ")
    print(" Print Range from the 3rd position to the 5th.  Here is the command   ")
    print("\n   Here is the command:")
    print("                 print(Cars[2:5])     -  prints Range from the 3rd car to the 5th\n")
    print("       Our List -    " + str(Cars))
    print("                    Output -  " + str(Cars[2:5]))

    a = input(" \n\n\n\nPress <Enter> to see Changing items by index value: ")


    print("\n\n\n\n\n\n\n\n\n\n\n\n                  -------------------------------- 5> CHANGING ITEMS BY INDEX VALUES  --------------------------------    \n")
    print("We are going to change value in position 6 to \"Mouse\".  The command we are using:\n")
    print("         Cars[5] = \"Mouse\"")
    print("\n**** Before the Change ****")
    print(Cars)

    print("\n **** After the Change****")
    Cars[5] = "Mouse"
    print(Cars)

    a = input(" \nPress <Enter> to combine lists:  ")



    print("\n\n\n\n\n\n\n\n\n\n\n\n                  -------------------------------- 6> COMBINING LISTS TOGETHER USING EXTEND FUNCTION  --------------------------------    \n")
    print("   We are going to combine 2 lists together using the EXTEND Function. Lets look at the lists format we entered: \n  ")

    print("       Cars = [\"Mustang\", \"Camaro\", \"Challenger\", \"Pinto\", \"Pizza Car\", \"Shoe Car\", \"Ram\", \"F150\", \"F250\"]")
    print("       Numbers = [5, 21, 32, 52, 12, 22, 87]\n")
    input("\n\n\n\n\npress <Enter> to continue:  ")

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  -------------------------------- 6> COMBINING LISTS TOGETHER USING EXTEND FUNCTION --------------------------------    \n")
    print(" Now lets print the lists using the following commands:\n")
    print("             print(Cars)")
    print("             print(Numbers)\n")


    Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
    Numbers = [5, 21, 32, 52, 12, 22, 87]
    print("   List called \"Cars\" -               "+ str(Cars))
    print("   List called \"Numbers\" -        " + str(Numbers))


    a = input(" \n\n\n\nPress <Enter> for EXTEND Functions:   ")

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  -------------------------------- 6> COMBINING LISTS TOGETHER USING EXTEND FUNCTION --------------------------------    \n")
    print(" Adding 2 Lists together using the EXTEND Function      \n")
    print("We are using the EXTEND function to combine the two list using the following command:\n")
    print("             Cars.extend(Numbers)")
    print("\n**** Before the EXTEND Function   ****")
    print(Cars)
    print("\n**** After the EXTEND Function   ****")
    Cars.extend(Numbers)
    print(Cars)

    a = input(" \nPress <Enter> for APPEND Functions:  ")

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  -------------------------------- 7> APPENDING TO A LIST USING APPEND FUNCTION  --------------------------------    \n")

    print("We are going to add the value \"BMW\" to our \"Cars\" list by  Appending to a list using the APPEND function \n")
    print("The command we are using is:  ")
    print("             Cars.append(\"BMW\")")
    print("\n**** Before the APPEND Function   ****")
    print(Cars)
    print("\n**** After the APPEND Function   ****")
    Cars.append("BMW")
    print(Cars)

    a = input(" \nPress <Enter> for INSERT Functions:   ")


    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  8> USING THE INSERT FUNCTION  --------------------------------    \n")



    print("   Inserting Ferrari to a list in position 5 using the INSERT function \n")
    print("Here is the command we are using:")
    print("Cars.insert(5, \"Ferrari\")")
    print("\n**** Before the INSERT Function   ****")
    print(Cars)
    print("\n**** After the INSERT Function   ****")
    Cars.insert(5, "Ferrari")
    print(Cars)
    a = input(" \nPress <Enter> for REMOVE Functions:  ")


    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  9> USING THE REMOVE FUNCTION  --------------------------------    \n")

    print(" Removing  Shoe Car from list using the REMOVE function.  Here is the command we are using:\n")
    print("       Cars.remove(\"Shoe Car\")")
    print("\n **** Before the REMOVE function ****")
    print(Cars)
    print("\n **** After the REMOVE function ****")
    Cars.remove("Shoe Car")
    print(Cars)

    a = input(" \nPress <Enter> for CLEAR Functions:  ")


    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  10> USING THE CLEAR FUNCTION   --------------------------------    \n")

    print("\n Removing ALL item from list using the CLEAR function  Here is the command we are using:")
    print("                             Cars.clear() ")
    print("\n **** Before the Change****")
    print(Cars)
    print("\n **** After the Change****")
    Cars.clear()
    print(Cars)

    a = input(" \nPress <Enter> for POP Functions:  ")


    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  11> USING THE POP FUNCTION   --------------------------------    \n")

    Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]

    print("Because we used the CLEAR command in the previous section we first need to rebuild the list:")
    print("Cars = [\"Mustang\", \"Camaro\", \"Challenger\", \"Pinto\", \"Pizza Car\", \"Shoe Car\", \"Ram\", \"F150\", \"F250\"]")
    print("\nNow lets print the list using the command ----    print(Cars)")
    print(Cars)

    input(" \n\n\n\nPress <Enter> for pop Functions:  ")


    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  11> USING THE POP FUNCTION   --------------------------------    \n")
    print(" Next we'll Removing LAST item from list using the POP function:")
    print("\n **** Before the Change****")
    print(Cars)
    print("\n **** After the Change****")
    Cars.pop()
    print(Cars)
    input(" \nPress <Enter> for Finding Index value in list using INDEX:   ")


    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  12> USING THE INDEX FUNCTION   --------------------------------    \n")
    print("Lets see the list again using the command  -     print(Cars)")
    print(Cars)
    print("\n Lets see the index value of Pinto using the command: \n")
    print("                     print(Cars.index(\"Pinto\"))")
    print("                          Output - " + str(Cars.index("Pinto")))

    a = input("\n\nThis is the end of this lesson - Do you want to redo The lesson? (y) or push <ENTER>: ")
    if str(a) == "y":
        lesson_10()
    else:
        main_menu_1()

def lesson_11():

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  11> USING TUPLES   --------------------------------    \n")
    print("       - a TUPLE is a type of data structure which means its a (container) where we can store different values simular to a list. ")
    print("       - a TUPLE Cannot be changed or modified.\n ")
    print("       - The difference between TUPLE  and LIST:\n")
    print("                ---- In a list you can add, delete, append, clear or any of  functions that were in the list section.")
    print("                ---- In Tuple once its made it cannot be changed.")
    print("                ---- A Tuple is used for data that will  never be changed (SSN, coordinates and etc.")
    input("\n\n\nPress <ENTER> to continue the lesson:  ")

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  2> CREATING A TUPLES   --------------------------------    \n")
    print(" Let set up a TUPLE using the variable called {cord}.  Here is the line of code we are using:")
    print("                cord = (4, 5)")
    print(" \nNow we will print the TUPLE")
    cord = (4, 5)
    print("               Output = " + str(cord))

    a = input("\n\n\n\n\n\nPress <Enter> for example of INDEXing a Tuple:")

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  3> INDEXING THE TUPLE   --------------------------------    ")

    print("\n        Lets index the first value in the TUPLE at position 0")
    print("         The code we are using is:")
    print("                     print(cord[0])")
    print("               Output = " + str(cord[0]))

    print("\n        Lets index the second value in the TUPLE at position 1")
    print("         The code we are using is:")
    print("                     print(cord[1])")
    print("               Output = " + str(cord[1]))
    print("\n     As a reminder, here is our TUPLE" + str(cord))

    input("\nPress <ENTER> to continue the lesson:  ")

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  4> USING A TUPLE WITH MULTIPLE ENTRIES   --------------------------------    \n")

    print(" Here is the TUPLE that I created using multiple entries. I used the variable cord, and  here is the command we used")
    print("cord2 = [(4, 5), (2, 12), (15, 18), (17, 13), (14, 15), (19, 52)]\n")
    print("Now let's print the TUPLE.   ")
    cord2 = [(4, 5), (2, 12), (15, 18), (17, 13), (14, 15), (19, 52)]
    print(cord2)
    input("\n\n\n\n\n\n\nPress <ENTER> to continue the lesson:  ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  5> INDEXING A TUPLE WITH MULTIPLE ENTRIES   --------------------------------    \n")
    print(" Here a example if you want to look at the 5th position of the Tuple. Again using the 4 as the reference.  Here is the command I used")
    print("print(cord2[4])")
    print(cord2[4])

    print("\n Here a example if you want to look at the 3rd position of the Tuple. Again using the 2 as the reference.  Here is the command I used")

    print("print(cord2[2])")
    print(cord2[2])

    print("\n Here a example if you want to look at the 1st position of the Tuple. Again using the 0 as the reference,  Here is the command I used")
    print("print(cord2[0])")
    print(cord2[0])

    a = input("\nThis is the end of this lesson - Do you want to redo The lesson? (y) or push <ENTER>: ")
    if str(a) == "y":
        lesson_11()
    else:
        main_menu_1()

def lesson_12():
    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  12> FUNCTIONS  --------------------------------    \n")
    print("*  a FUNCTION is a  set of code to perform a specific task. ")
    print("*  So if your going to do things over and over again you can just CALL that function.\n ")

    a = input(" \n\n\n\n\n\n\nPress <Enter> for example of a function to say \"HI\":   ")

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  2> SIMPLE  FUNCTION TO SAY HI  --------------------------------    ")
    print(" * Here is an example of a simple function to say \"HI\".")
    print(" * When you name a function you want to use all lower case and in mult words us a   \"_\" where you would normally use a space. ")
    print("\nHere is the code we are going to use:")
    print("                    def say_hi(): ")
    print("                         print(\"Hello User\")")
    def say_hi():
        print("Hello User")

    print("\n * So at any time we can call the function that we named (say_hi) by just typing \"say_hi()\".")
    print(" Example:  here is the code were using:")
    print("                         say_hi()")
    say_hi()


    a = input(" \nPress <Enter> for example of a function to say HI with a name:  ")

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  3> SIMPLE  FUNCTION TO SAY HI WITH A NAME  --------------------------------    ")
    print(" * Now when you call the function and add a name in the call comman it will print out hello with a name that is hard coded")
    print(" * We are going to use the same FUNCTION name.  Now the variable data is in the call command.  I'll show you an example, so hopefully it will make more since")
    print("\ndef say_hi(name):")
    print("     print(\"Hello User \" + name)")
    print("say_hi(\"Dan \")")
    print("say_hi(\"George\")")
    def say_hi(name):
        print("Hello User " + name)
    print("\n         Here is the output:")
    say_hi("Dan ")
    say_hi("George ")

    a = input(" \nPress <Enter> for example of a function to say HI with a name and age (Mult Parameters):  ")

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  4> SIMPLE  FUNCTION TO SAY HI WITH NAME AND AGE (Mult Parameters)  --------------------------------  ")

    print(" *Now we add more than 1 parameter.  We'll include the age\n")
    print("The code to be used is:")
    print("             def say_hi(name, age):")
    print("                  print(\"Hello User \" + name + \"is your age really \" + age + \"?\")")
    print("             say_hi(\"Dan \", \"17\")")
    print("             say_hi(\"George \", \"12\")\n")
    print(" Now lets run the code:")
    def say_hi(name, age):
        print("Hello User " + name + "is your age really " + age + "?")

    say_hi("Dan ", "17")
    say_hi("George ", "12")

    a = input(" \nPress <Enter> for example of a function to say HI with a name:   ")

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  5> SIMPLE  FUNCTION TO SAY HI WITH NAME AND AGE (age as numeric) --------------------------------  \n ")
    print(" *This time were going to use the age variable but as an integer instead of a string.")
    print(" * Looks exactly the same but set the parameter is a numeric.  So in order to print it in a sentence we have to converte to a string.")
    print(" * Hopefully it will make more since when you see the code.\n")
    print("             def say_hi(name, age):")
    print("                     print(\"Hello User \" + name + \"is your age really \" + str(age) + \"?\")        -  Note [str(age)] is changing the variable \"age\" to a string")
    print("             say_hi(\"Dan \", 21)\"                                                                                            - Note - 21 is entered as an number")
    print("             say_hi(\"George \", 19)                                                                                         - Note - 19 is entered as an number")
    input(" \nPress <Enter> to run the code:    ")

    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  5> SIMPLE  FUNCTION TO SAY HI WITH NAME AND AGE (age as numeric) --------------------------------   ")
    def say_hi(name, age):
        print("Hello User " + name + "is your age really " + str(age) + "?")
    print(" ")
    say_hi("Dan ", 21)
    say_hi("George ", 19)

    print(" \n*You can pass any kind of data to include strings, numbers, bullion's, arrays, or whatever you want. \n")



    a = input("\n\n\nThis is the end of this lesson - Do you want to redo The lesson? (y) or push <ENTER>: ")
    if str(a) == "y":
        lesson_11()
    else:
        main_menu_1()


def lesson_13():
    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  13> RETURN STATEMENT --------------------------------   ")

    print("*  This portion will go over RETURN STATEMENTs while using a funciton. ")
    print("*  This is good for when you want to call a function and get information back. ")
    print("*  The  function ware are creating is going to cube a number and return it..\n ")
    print("*  Our first simple function is to multiply a number by itself 3 times. ")
    print("*  We will use the number 25.\n ")
    print("Here is the code were using")
    print("                 def cube(num):")
    print("                     return num * num * num")
    print("                 print(cube(25))")
    a = input(" \nPress <Enter> to run the code:  ")


    print("\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  2> RETURN STATEMENT --------------------------------   ")
    print("Here is the output:")
    def cube(num):
        return num * num * num

    print(cube(25))
    print("\nHere is a reminder of the code we are using:")
    print("                 def cube(num):")
    print("                     return num * num * num")
    print("                 print(cube(25))")


    input(" \n\n\n\nPress <Enter> for example of a FUNCTION with RETURN using a variable:     ")

    print( "\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  3> RETURN STATEMENT --------------------------------   ")
    print( "*  Basically were doing the exact same function except were going to Store the value in a varable we are calling [result]. ")
    print("*  We will use the number 5 this time. ")
    print(" * Note you cannot add code after a return statement for that function.\n ")
    print("                     def cube(num):")
    print("                         return num * num * num")
    print("                     result = (cube(5))")
    print("                     print(result)\n")
    print("    Here is the ouput:")

    def cube(num):
        return num * num * num
    result = (cube(5))
    print(result)

    input(" \n\nPress <Enter> for example of a FUNCTION with RETURN using an input variable:     ")

    print( "\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  4> RETURN STATEMENT with input --------------------------------   ")
    print("now were going to use an input statement.  This is beyond what we have go over but lets see if we can stretch our coding skills")
    print("At this point it is fully ok if you don't understand it all but I will walk you through the code.  Here is the code we are using:\n")
    print("    a = input(\"input number to multiply 3 times\"  - it will stop the program and store in what number the user uses in the varable \"a|\")")
    print("    def mult(num):                                                  - we set up a function called \"mult\" and the call is called \"num\"")
    print("        return num * num * num                               - this returns the value of num multiplied three times")
    print("    result = (mult(int(a)))                                        - this stores the takes the variable of \"a\", changes it to an integer, multiplies 3 times and stores in \"result\")")
    print("    print(result)                                                       - prints the value in the variable called result\n\n")
    a = input("input number to multiply 3 times:  ")

    def mult(num):
        return num * num * num
    result = (mult(int(a)))
    print(result)





    a = input("\nThis is the end of this lesson - Do you want to redo The lesson? (y)  or push <ENTER> for main menu: ")
    if str(a) == "y":
        lesson_12()
    if str(a) == "Y":
        lesson_12()
    if str(a) == "n":
        multiply2()
    else:
        main_menu_1()

def lesson_14():

    print( "\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  14> IF STATEMENT --------------------------------   ")
    print("We are going to make a simple IF STATEMENT using Boolean value of [True] in the variable [is male]")
    print("Condition 1 - boleen value of  [is male] = [True]\n")
    print("    Here is the code:")
    print("             is_male = True")
    print("             if is_male:")
    print("                 print(\"You are a male\")")
    print("             else:")
    print("                 print(\"you are not a male\")\n")
    print("\nHere is the output:")

    is_male = True
    if is_male:
        print("You are a male")
    else:
        print("you are not a male")
    input("Press <Enter> to continue the lesson")

    print( "\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------  2> IF STATEMENT --------------------------------   ")
    print("\nCondition 2 - Boolean value of and if [is_male] = [False]")
    print("    Here is the code:")
    print("             is_male = False")
    print("             if is_male:")
    print("                 print(\"You are a male\")")
    print("             else:")
    print("                 print(\"you are not a male\")\n")
    print("Here is the output:")
    is_male = False

    if is_male:
        print("You are a male")
    else:
        print("you are not a male")

    input("Press <Enter> to continue the lesson")

    print(
        "\n\n\n\n                                   -----------------------------------      IF STATEMENT with [if] [and] and [elif]      -----------------------------\n")

    print("We are going to make a more complex IF STATEMENT using boleen value of  [is male]  and [is_tall] =  ")
    print("\nCondition 1 - Boolean value of [is_male] = [True] and [is_tall] = [True]\n")

    print("Here is the code")
    print("    is_male = True")
    print("    is_tall = True")
    print("    if is_male and is_tall:")
    print("        print(\"You are a male and tall\")")
    print("    elif is_male and not (is_tall):")
    print("        print(\"Your a Short Male\")")
    print("    elif not (is_male) and (is_tall):")
    print("        print(\"Your a Tall Female \")")
    print("    else:")
    print("        print(\"Your a Short Female\")")

    is_male = True
    is_tall = True

    if is_male and is_tall:
        print("You are a male and tall")
    elif is_male and not (is_tall):
        print("Your a Short Male")
    elif not (is_male) and (is_tall):
        print("Your a Tall Female ")
    else:
        print("Your a Short Female")

    #     --------------------------------------------------------------------------------------------------------------------------------------------
    print("\nCondition 2 - Boolean value of [is_male] = [True] and [is_tall] = [False]")

    is_male = True
    is_tall = False

    if is_male and is_tall:
        print("You are a male and tall")
    elif is_male and not (is_tall):
        print("Your a Short Male")
    elif not (is_male) and (is_tall):
        print("Your a Tall Female ")
    else:
        print("Your a Short Female")

    #     --------------------------------------------------------------------------------------------------------------------------------------------
    print("\nCondition 3 - boleen value of [is_male] = [False] and [is_tall] = [True]")

    is_male = False
    is_tall = True

    if is_male and is_tall:
        print("You are a male and tall")
    elif is_male and not (is_tall):
        print("Your a Short Male")
    elif not (is_male) and (is_tall):
        print("Your a Tall Female ")
    else:
        print("Your a Short Female")

    #     --------------------------------------------------------------------------------------------------------------------------------------------
    print("\nCondition 4 - boleen value of [is_male] = [False] and [is_tall] = [False]")

    is_male = False
    is_tall = False

    if is_male and is_tall:
        print("You are a male and tall")
    elif is_male and not (is_tall):
        print("Your a Short Male")
    elif not (is_male) and (is_tall):
        print("Your a Tall Female ")
    else:
        print("Your a Short Female")

    a = input(" \nPress <Enter> to OR statement:")

    print("\n\n\n\n\n\n\n\nOne item we did not mention is if/or we only used and]\n\n\n\n\n\n")

    print("\n This is the END of this Lesson called IF STATEMENT\n")


    a = input("\nThis is the end of this lesson - Do you want to redo The lesson? (y)  or push <ENTER> for main menu: ")
    if str(a) == "y":
        lesson_14()
    if str(a) == "Y":
        lesson_14()
    else:
        main_menu_1()

def lesson_15():
    print(
        "\n\n\n\n\n                                   -----------------------------------    15>    IF STATEMENT and Comparisions    -----------------------------\n")
    print(" We can do comparisions in a function, you can use a varity of operator signs:")
    print("          * == means equals")
    print("          * != means not equals")
    print("          * > means greater than")
    print("          * <  means Less than")
    print("          * >= means greater than or equals")
    print("          * <=  means Less than or equals")

    input("\n\n\nPress <Enter> to continue lesson: ")

    print(
        "\n\n\n                                   -----------------------------------    2>  IF STATEMENT and Comparisions Find Highest Number    -----------------------------\n")
    print("Here is an example of a simple comparison statement:")

    print("         def max_num\(num1, num2, num3\):")
    print("             if num1 >= num2 and num1 >= num3:")
    print("                 return num1")
    print("             if num2 >= num1 and num2 >= num3:")
    print("                 return num2")
    print("             else:")
    print("                 return num3")

    print("\n             print(max_num(30, 40, 5))\n")



    def max_num(num1, num2, num3):
        if num1 >= num2 and num1 >= num3:
            return num1
        if num2 >= num1 and num2 >= num3:
            return num2
        else:
            return num3

    print("So as you an see we are using 30, 40, and 5.  When we run the code the output is - " + str(max_num(30, 40, 5)) + " - Which is the highest number.")
    input("\n\n\nPress <Enter> to continue lesson: ")



    print(
        "\n\n\n                                   -----------------------------------    3>  IF STATEMENT and Comparisions Find Lowest Number    -----------------------------")
    print("Here is an example of a simple comparison statement:\n")

    print("def max_num\(num1, num2, num3\):")
    print("    if num1 <= num2 and num1 <= num3:")
    print("        return num1")
    print("    if num2 <= num1 and num2 <= num3:")
    print("        return num2")
    print("    else:")
    print("       return num3")
    print(" (max_num(30, 40, 5))\n")

    def min_num(num1, num2, num3):
        if num1 <= num2 and num1 <= num3:
            return num1
        if num2 <= num1 and num2 <= num3:
            return num2
        else:
            return num3

    print("So as you can see we are using 30, 40, and 5.  When we run the code the output is - " + str(min_num(30, 40, 5)) + " - which is the lowest number.")
    input("\n\n\nPress <Enter> to continue lesson: ")




    print("\n\n\n                                   -----------------------------------    4>  IF STATEMENT and Comparisions with input    -----------------------------\n")

    def max_num1(num1, num2, num3):
        if num1 >= num2 and num1 >= num3:
            return num1
        if num2 >= num1 and num2 >= num3:
            return num2
        else:
            return num3

    def min_num1(num1, num2, num3):
        if num1 <= num2 and num1 <= num3:
            return num1
        if num2 <= num1 and num2 <= num3:
            return num2
        else:
            return num3

    print("Now its time to have some fun.")
    print("Lets do the same operation but you provide the data used\n")
    first_num = int(input("Enter FIRST number:  "))
    second_num = int(input("Enter SECOND number:  "))
    third_num =int( input("Enter THIRD  number:  "))

    print("\n\nThe LOWEST number you entered is - " + str(min_num1(first_num, second_num, third_num)))
    print("\nThe HIGHEST number you entered is - " + str(max_num1(first_num, second_num, third_num)))


    input("\n\n\nPress <Enter> to continue lesson: ")



    print(
        "\n\n\n\n                                   -----------------------------------      OPERATOR SIGNS   -----------------------------\n")

    print("* Again here are some of the operator signs")
    print("          * == means equals")
    print("          * != means not equals")
    print("          * > means greater than")
    print("          * <  means Less than")
    print("          * >= means greater than or equals")
    print("          * <=  means Less than or equals")



    a = input("\nThis is the end of this lesson - Do you want to redo The lesson? (y)  or push <ENTER> for main menu: ")
    if str(a) == "y":
        lesson_15()
    if str(a) == "Y":
        lesson_15()
    else:
        main_menu_1()

'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
def lesson_16():

    def title():
        new_page()
        print("\n                                   -----------------------------------    Lesson - 16  Building a better Calculator   -----------------------------\n")

    def definition():
        title()
        print("                                                                                  *****   Description of lesson  *****")
        print("We are building a calculator...  This is a little more smart than the one we built in previous exercises")
        print("                  *  We are using elif which means else/ if.  ")
        print("                         It is used for a filtering mechanism so it can detect if the oporator is valid or invalid  ")
        print("                  *  We are using FLOATs so we can use Decimals")
        print("                  *  We are converting the inputs to a float so it can accept decimals \n")
        end()

    def code():
        title()
        print("                                                                                *****   Running the code the Code  *****")
        print("Enter 2 numbers following by the operator [+, -, *, /]\n")
        num1 = float(input("Enter 1st Number: "))
        num2 = float(input("Enter 2nd Number: "))
        op = input("Enter operator :")
        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "x":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
        else:
            print("invalid operator")

        end()

    def print_code():
        title()
        print("                                                                                            *****   Here is the Code used  *****")
        print("         num1 = float(input(\"Enter 1st Number: \"))")
        print("         num2 = float(input(\"Enter 2nd Number: \"))   ")
        print("         op = input(\"Enter operator :\")    ")
        print("         if op == \"+\":    ")
        print("             print(num1 + num2)   ")
        print("         elif op == \"-\":   ")
        print("             print(num1 - num2)   ")
        print("         elif op == \"*\":   ")
        print("             print(num1 * num2)   ")
        print("         elif op == \"x\":    ")
        print("             print(num1 * num2)   ")
        print("         elif op == \"/\":    ")
        print("             print(num1 / num2)   ")
        print("         else:     ")
        print("             print(\"invalid operator\")    ")
        continue_lesson()
        end()


    def end():
        a = input("\n Please Select: "
            " \n           (R) to Run the program "
            "  \n           (P) to See the code used to build the program."
            "\n           (D) Description of the lesson\n "
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
            lesson_16()
        if str(a) == "D":
            lesson_16()
        else:
            main_menu_1()

    definition()

'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''


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
            main_menu_1()

    definition()

'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
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
        a = input("Do you want to do it again? Enter  \"X\" to exit; Press <Enter> to run the WHILE loop again.")
        if a == "x":
            lesson_18()
        elif a == "X":
            lesson_18()
        else:
            code()

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
            main_menu_1()

    definition()



'''
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''

def lesson_19():

    def title():
        new_page()
        print( "\n                                   -----------------------------------    Lesson 19 - THE GUESSING GAME   -----------------------------\n")

    def definition():
        title()
        print("In this Lesson, we are building a couple of simple guessing games.")
        print("We are going to use the tools we have learned in previouse lessons.  The pimary tools (or commands) is:")
        print("                                          - Inputs   ")
        print("                                          - Variables")
        print("                                          - IF Statements   ")
        print("                                          - While  Loops\n")
        print("So lets have fun!!!")
        end()


    def run_all_games():
        game_1()
        game_2()
        game_3()
        game_4()
        continue_lesson()
        end()

    def game_1():
        title()

        print("Guessing Game - 1: In this first game, there are no clues and no limits of number of tries.  The guess word is - \"glass\"\n")

        secret_word = "glass"
        guess = ""
        i = 0
        while secret_word != guess:
            i = i + 1
            guess = input("Guess number ---- " + str(i) + " Guess the Secret Word: ")

        print("\nYou Guessed it.  Yeah I know this game is lame, but It'll get better.\n")
        continue_lesson()

    def print_game_1():
        title()
        print("                         secret_word = \"glass\"   ")
        print("                         guess = \"\"  ")
        print("                          i = 0\") ")
        print("                          while secret_word != guess:  ")
        print("                              i = i + 1   ")
        print("                              guess = input(\"Guess number ---- \" + str(i) + \" Guess the Secret Word: \")  ")
        print("                          print(\"\\nYou Guessed it.  Yeah I know this game is lame, but It'll get better.\")  \n\n")
        continue_lesson()



    def game_2():
        title()
        print("Guessing Game - 2: Now we are going to make this game a little smarter.  We're going to set a limit of 3 tries.  The guess word is - \"glass\"\n")
        secret_word = "glass"
        guess = ""
        guess_count = 0
        guess_limit = 3
        out_of_guesses = False

        while guess != secret_word and not out_of_guesses:
            if guess_count < guess_limit:
                guess_count += 1
                guess = input("Guess #" + str(guess_count) + " Enter guess:   ")

            else:
                out_of_guesses = True

        if out_of_guesses:
            print("\nYou loose.  You had to make it in " + str(guess_limit) + " Tries.")
        else:
            print("\nYou win. You did it in " + str(guess_count) + " Tries.")
        continue_lesson()

    def print_game_2():
        title()
        print("     print(\"Guessing Game - 2: Now we are going to make this game a little smarter.  We're going to set a limit of 3 tries.  The guess word is - \"glass\"\\n\")   ")
        print("     secret_word = \"glass\" ")
        print("     guess = \"\" ")
        print("     guess_count = 0 ")
        print("     guess_limit = 3 ")
        print("     out_of_guesses = False ")

        print("     while guess != secret_word and not out_of_guesses:")
        print("         if guess_count < guess_limit:  ")
        print("             guess_count += 1  ")
        print("                     guess = input(\"Guess #\" + str(guess_count) + \" Enter guess:   \")   ")
        print("                 else:  ")
        print("                     out_of_guesses = True   ")

        print("             if out_of_guesses:  ")
        print("                 print(\"\\nYou loose.  You had to make it in \" + str(guess_limit) + \" Tries.\")   ")
        print("                 else:  ")
        print("                     print(\"\\nYou win. You did it in \" + str(guess_count) + \" Tries.\")\n")
        continue_lesson()


    def game_3():
        title()
        print("Guessing Game - 3: Now in this game, we are going to make it even more smarter.  It will have clues and you have 5 turns to figure out the word..\n")
        print("                  ****   please use all lower case   ****")
        print("Good luck!!!!\n")
        clues = {
            1: "It is pretty easy to learn and use. ",
            2: "It is a computer language (not BASIC, COBALT, FORTRAN, VISUAL BASIC, or the dreaded Assembly Language.",
            3: "It was named after snake. ",
            4: "I use PyCharm or VS code to code in it. ",
            5: "This program is built in it. ",
        }

        word = "python"
        guess = ""
        count = 0
        max_count = 5
        win = False

        while guess != word and not win:
            if count < max_count:
                count += 1
                print("Clue number - " + str(count) + " - " + clues[count])
                guess = input(" Guess number " + str(count) + ".  Enter guess : ")
            else:
                win = True

        if win:
            print(" \nYou Loose.  You only had " + str(count) + " tries.")
        else:
            print(" \nYou Win!!!!!!!!!  You did it in " + str(count) + " tries.")
        continue_lesson()

    def print_game_3():
        title()
        print("Guessing Game - 3: Now in this game, we are going to make it even more smarter.  It will have clues and you have 5 turns to figure out the word..\n")
        print("                  ****   please use all lower case   ****")
        print("Good luck!!!!\n")
        clues = {
            1: "It is pretty easy to learn and use. ",
            2: "It is a computer language (not BASIC, COBALT, FORTRAN, VISUAL BASIC, or the dreaded Assembly Language.",
            3: "It was named after snake. ",
            4: "I use PyCharm or VS code to code in it. ",
            5: "This program is built in it. ",
        }

        word = "python"
        guess = ""
        count = 0
        max_count = 5
        win = False

        while guess != word and not win:
            if count < max_count:
                count += 1
                print("Clue number - " + str(count) + " - " + clues[count])
                guess = input(" Guess number " + str(count) + ".  Enter guess : ")
            else:
                win = True

        if win:
            print(" \nYou Loose.  You only had " + str(count) + " tries.")
        else:
            print(" \nYou Win!!!!!!!!!  You did it in " + str(count) + " tries.")
        continue_lesson()

    def game_4():
        title()
        print("Guessing Game - 4: Now its your turn.  Your going to enter the guess word and the 5 clues.\n")
        print("         *****  NOTE - It is case sensitive  ****** ")
        print("Here we go!!!!\n")
        word = input("What is the guess word?  ")
        max_count = 5
        clue_1 = input("What is the first clue?  ")
        clue_2 = input("What is the second clue?  ")
        clue_3 = input("What is the third clue?  ")
        clue_4 = input("What is the forth clue? ")
        clue_5 = input("What is the fifth clue?  ")

        clues = {
            1: clue_1,
            2: clue_2,
            3: clue_3,
            4: clue_4,
            5: clue_5,
             }
        guess = ""
        count = 0
        win = False
        continue_lesson()
        title()
        print("You have 5 tries to guess the secrete word.  Good Luck!!!!")
        while guess != word and not win:
            if count < int(max_count):
               count += 1
               print("Clue number - " + str(count) + " - " + clues[count])
               guess = input(" Guess number " + str(count) + ".  Enter guess :")
            else:
               win = True

        if win:
          print(" You Loose.  You only had " + str(count) + " tries.")
        else:
          print(" You Win!!!!!!!!!  You did it in " + str(count) + " tries.")


    def print_game_4():
        title()
        print("             print(\"Guessing Game - 4: Now its your turn.  Your going to enter the guess word and the 5 clues.\\n\")  ")
        print("             print(\"         *****  NOTE - It is case sensitive  ****** \") ")
        print("             print(\"Here we go!!!!\\n\") ")
        print("             word = input(\"What is the guess word?  \") ")
        print("             max_count = 5   ")
        print("             clue_1 = input(\"What is the first clue?  \")   ")
        print("             clue_2 = input(\"What is the second clue?  \")   ")
        print("             clue_3 = input(\"What is the third clue?  \")   ")
        print("             clue_4 = input(\"What is the forth clue?  \")   ")
        print("             clue_5 = input(\"What is the fifth clue?  \")   ")

        print("             clues = {   ")
        print("                  1: clue_1,   ")
        print("                 2: clue_2,   ")
        print("                 3: clue_3,   ")
        print("                 4: clue_4,   ")
        print("                 5: clue_5,   ")
        print("             }  ")
        print("             guess = ""    ")
        print("             count = 0  ")
        print("             win = False  ")
        print("             continue_lesson()  ")
        print("             title()  ")
        print("             print(\"You have 5 tries to guess the secrete word.  Good Luck!!!!\")  ")
        print("             while guess != word and not win:  ")
        print("                 if count < int(max_count):  ")
        print("                     count += 1  ")
        print("                     print(\"Clue number - \" + str(count) + \" - \" + clues[count])  ")
        print("                     guess = input(\" Guess number \" + str(count) + \".  Enter guess : ")
        print("                 else:  ")
        print("                    win = True  ")

        print("             if win:  ")
        print("                 print(\" \nYou Loose.  You only had \" + str(count) + \" tries.\")  ")
        print("              else:")
        print("                 print(\" \nYou Win!!!!!!!!!  You did it in \" + str(count) + \" tries.\")  ")





    def end():
        a = input("\n Please Select: "
            "\n           (R) Run all the Example games "
            "\n           (1) Guessing Game - No Limits - No Clues                                                             (A) Show code for Game 1"
            "\n           (2) Guessing Game - 3 limit try - no Clues                                                               (B) Show code for Game 2"
            "\n           (3) Guessing Game - 5 limit try - Includes Clues                                                     (C) Show code for Game 3"
            "\n           (4) Guessing game - You enter the secrete word and clues                                    (D) Show code for Game 4\n"
            "\n           (D) Description "
            "\n           <Enter>  for main menu: ")
        if str(a) == "r":
            run_all_games()
            lesson_19()
        if str(a) == "R":
            run_all_games()
            lesson_19()
        if str(a) == "1":
            game_1()
            lesson_19()

        if str(a) == "A":
            print_game_1()
            lesson_19()
        if str(a) == "a":
            print_game_1()
            lesson_19()

        if str(a) == "B":
            print_game_2()
            lesson_19()
        if str(a) == "b":
            print_game_2()
            lesson_19()

        if str(a) == "D":
            print_game_4()
            continue_lesson()
            lesson_19()
        if str(a) == "d":
            print_game_4()
            continue_lesson()
            lesson_19()

        if str(a) == "2":
            game_2()
            lesson_19()
        if str(a) == "3":
            game_3()
            lesson_19()
        if str(a) == "4":
            game_4()
            lesson_19()


        if str(a) == "d":
            lesson_19()
        if str(a) == "D":
            lesson_19()
        else:
            main_menu_1()

    definition()

'''
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''



def lesson_20():

    def title():
        new_page()
        print( "\n                                   -----------------------------------    Lesson 20 - Using FOR LOOPS  -----------------------------\n")

    def definition():
        title()
        print(" *A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).")
        print("* This is less like the for keyword in other programming languages, and works more like an iterator method   ")
        print("             as found in other object-orientated programming languages.")
        print(" *With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.")
        print("\n  * Writing a for loop: ")
        print("           - Step 1 - It starts with the for keyword, followed by a value name that we assign to the item of the sequence.")
        print("           - Step 2 - Then, the in keyword is followed by the name of the sequence that we want to iterate.")
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
            b=b+1
            print(str(b) +" - "+ i)
        print("\nNOTE - I added the count number.\n")


    def example_2_code():
        title()
        print("\n                                                Code used for -- Example 2 - Using LOOP in ARRAY      \n")
        print("           1     print(\"\\nHere is the ARRAY we are working with:\")")
        print("           2     cars = [\"Mustang\", \"Camaro\", \"Challenger\", \"Pinto\", \"Pinto\", \"Pinto\", \"Pizza Car\", \"Shoe Car\", \"Ram\", \"F150\", \"F250\"]  ")
        print("           3     print(cars)  ")

        print("           4     a = input(\"\\nPress <Enter> to us FOR LOOP to display the ARRAY item by item:  \")")
        print("           5     print(\"\\nAs you can see, we used the FOR LOOP to display the ARRAY item by item:\\n\") ")
        print("           6     b = 0  ")
        print("           7     for i in (cars):   ")
        print("           8         b=b+1 ")
        print("           9     print(str(b) +\" - \"+ i)   ")
        print("         10     print(\"\\nNOTE - I added the count number.\n\")  ")


    def example_3():
      title()
      print("                                     Example 3 - Using LOOP with input value to set the end of the RANGE     \n")

      print("We are going to use a range.  Input a number and we will count using the range function. \n")
      a = int(input("ENTER how big you want to range to be?:  ")) + 1
      for i in range(int(a)):
            print(i)

      print("\n As you can the range counted between 1 and " + str(a-1) + "\n")



    def example_3_code():
      title()
      print("                                     Code used for -- Example 3 - Using LOOP with input value to set the end of the RANGE     \n")

      print("           1      print(\"We are going to use a range.  Input a number and we will count using the range function. \\n\")")
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
        for i in range(a , b):
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
        print( "                                     Example 5 - Using LOOP with  RANGE and LEN commands     ")
        cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pinto", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150",
                "F250"]

        print("\nWe are using a LOOP to print the ARRAY we are using the (len) command to determine the length of the array. \n")
        continue_lesson()
        for i in range(len(cars)):
            print(cars[i])
        print("\n Even though the it looks the same as example 2, in this example we set the ending variable of the if statement using the length (len) command.")
        print("\n you will not this when you/if you review the code..\n")

    def example_5_code():
        title()
        print(
            "                                              Example 5 - Using LOOP with  RANGE and LEN commands     ")
        print("           1     cars = [\"Mustang\", \"Camaro\", \"Challenger\", \"Pinto\", \"Pinto\", \"Pinto\", \"Pizza Car\", \"Shoe Car\", \"Ram\", \"F150\", \"F250\"]  ")

        print("           2     print(\"\\nWe are using a LOOP to print the ARRAY we are using the (len) command to determine the length of the array. \\n\")   ")
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
            print(str(i) + " - " +  cars[i])
        print("\n")

    def example_6_code():
        title()
        print(
            "\                                         Example 6 - Using Loop in to print out part of the array using INPUTED beginning and ending RANGE     \n")
        print("           1     cars = [\"Mustang\", \"Camaro\", \"Challenger\", \"Pinto\", \"Pinto\", \"Pinto\", \"Pizza Car\", \"Shoe Car\", \"Ram\", \"F150\", \"F250\"]  ")
        print("           2     print(\"Now lets try with an inputed RANGE\\n\\n\\n\\n\")        ")
        print("           3     number = len(cars) ")

        print("           4     a = int(input(\"\\nEnter the BEGINNING number of the range . Has to be less than \" + str(number) + \":  \"))  ")
        print("           5     b = int(input(\"\\nEnter the ENDING number of the range. Has to be less than \" + str(number) + \":  \")) + 1   ")

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
            main_menu_1()

    definition()


'''
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''


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
            main_menu_1()

    definition()


'''
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''


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
            main_menu_1()

    definition()

'''
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''


def lesson_23():
    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 23 - BUILDING A TRANSLATOR  -----------------------------\n")

    def definition():
        title()
        print(" In this lesson were going to have a little fun.  What we are going to concentrate on:")
        print("                                                          *  for / in")
        print("                                                          *  if / else / return\n")
        print(" We will recap what these terms mean:")
        print("                                 -for       = loops are used when you have a block of code which you want to repeat a fixed number of times.")
        print("                                - if          = It decides whether certain statements need to be executed or not.")
        print("                                - return   = used in a loop to return a value.")



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
        print("                          ----  Example 1 - Replacing Vowels with input Value ")
        def a(e):
            d = ""
            for c in e:  # like for c = 1 to len(e)
                if c in "AEIOUaeiou":
                    d = d + f
                else:
                    d = d + c
            return d

        print("In this example, we are going to ask for a phrase and replacement value.  What it will do is replace "
              "\nany vowels with the replacement value.  Give it a try and you'll see what I mean.\n")
        e = input("Enter a Phrase: ")
        f = input("Replacement: ")
        print("\n                             Output - " + a(e) )

        g = input("\nDo you want to try again? (Y/N):")
        if(g) == "y":
             example_1()
        elif(g) == "Y":
             example_1()
        else:
            lesson_23()

    def example_1_code():
        title()
        print("                          ----  Example 1 Code - Replacing Vowels with input Value \n")
        print("                     1       def a(e):  ")
        print("                     2           d = \"\" ")
        print("                     3           for c in e:  # like for c = 1 to len(e) ")
        print("                     4               if c in \"AEIOUaeiou\": ")
        print("                     5                   d = d + f ")
        print("                     6               else: ")
        print("                     7                   d = d + c ")
        print("                     8           return d ")
        print("                     8        e = input(\"Enter a Phrase: \")   ")
        print("                     9        f = input(\"Replacement: \")   ")
        print("                     8        print(a(e))   \n ")


    def example_2():
        title()
        title()
        print("                                                                     Example 2 - Replacing Vowels with input Value (Setting the variable to LOWER case). \n ")
        def a(e):
            d = ""
            for c in e:  # like for c = 1 to len(e)
                if c.lower() in "aeiou":
                    d = d + f
                else:
                    d = d + c
            return d

        print("In this example, we are going to ask for a phrase and replacement value.  What it will do is replace "
              "\nany vowels and replace it with the replacement value. This difference with this exercise vs previous one"
              "\nis in the previous exercise, the coder had to enter  both lower and upper case in the comparison.  In "
              "\nthis exercise what we did is to make the variable all LOWER case then do the comparison.   "
              "\nNOTE this when you review the code.\n")
        e = input("Enter a Phrase: ")
        f = input("Replacement: ")
        print("\n                             Output - " + a(e) )

        g = input("\nDo you want to try again? (Y/N):")
        if(g) == "y":
             example_2()
        elif(g) == "Y":
             example_2()
        else:
            lesson_23()

    def example_2_code():

        title()
        print("                                 Example 2 - Replacing Vowels with input Value (Setting the variable to LOWER case). \n ")


        print("                     1       def a(e):             ")
        print("                     2           d = \"\"                ")
        print("                     3           for c in e:   ")
        print("                     4               if c.lower() in \"aeiou\":     ----   NOTE  the \".lower \"")
        print("                     5                   d = d + f ")
        print("                     6               else: ")
        print("                     7                   d = d + c ")
        print("                     8           return d ")
        print("                     8        e = input(\"Enter a Phrase: \")   ")
        print("                     9        f = input(\"Replacement: \")   ")
        print("                     8        print(a(e))   \n ")

    def example_3():
        title()
        title()
        print("                              Example 3 - Replacing Vowels with input Value (Setting the variable to UPPER case). \n ")
        def a(e):
            d = ""
            for c in e:  # like for c = 1 to len(e)
                if c.upper() in "AEIOU":
                    d = d + f
                else:
                    d = d + c
            return d

        print("In this example, we are going to ask for a phrase and replacement value.  What it will do is replace "
              "\nany vowels and replace it with the replacement value. This difference with this exercise vs previous one"
              "\nis in the previous exercise, the coder had to enter  both lower and upper case in the comparison.  In "
              "\nthis exercise what we did is to make the variable all UPPER case then do the comparison.   "
              "\nNOTE this when you review the code.\n")
        e = input("Enter a Phrase: ")
        f = input("Replacement: ")
        print("\n                             Output - " + a(e) )

        g = input("\nDo you want to try again? (Y/N):")
        if(g) == "y":
             example_2()
        elif(g) == "Y":
             example_2()
        else:
            lesson_23()

    def example_3_code():

        title()
        print("                          ----  Example 3 - Replacing Vowels with input Value (Setting the variable to UPPER case). \n")


        print("                     1       def a(e):             ")
        print("                     2           d = \"\"                ")
        print("                     3           for c in e:   ")
        print("                     4               if c.upper() in \"AEIOU\":     ----   NOTE  the \".upper \"")
        print("                     5                   d = d + f ")
        print("                     6               else: ")
        print("                     7                   d = d + c ")
        print("                     8           return d ")
        print("                     8        e = input(\"Enter a Phrase: \")   ")
        print("                     9        f = input(\"Replacement: \")   ")
        print("                     8        print(a(e))   \n ")

    def end():
        a = input("\n Please Select: To see the code behind the example put \"C\" before the number\n"
                  "\n (D)   Description of Lesson "
                  "\n (C1) / (1) Example 1 - Replacing Vowels with input Value           "
                  "\n (C2) / (2) Example 2 - Replacing Vowels with input Value (Setting the variable to LOWER case).      "
                  "\n (C3) / (3) Example 3 - Replacing Vowels with input Value (Setting the variable to UPPER case).      "


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

        if str(a) == "r":
            run_all()
        if str(a) == "R":
            run_all()

        if str(a) == "d":
            definition()
        if str(a) == "D":
            definition()
        else:
            main_menu_1()

    definition()

'''
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''


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

    def EX3():
        print("ex3")
        continue_lesson()
        end()


    def EX3_code():
        print("ex3 - Code")
        continue_lesson()
        end()

    def EX4():
        print("ex4")
        continue_lesson()
        end()


    def EX4_code():
        print("ex4 - Code")
        continue_lesson()
        end()


    def end():
        a = input("\n Please Select: To see the code behind the example put \"C\" before the number\n"
                  "\n (D)   Description of Lesson "
                  "\n (R)   Run all the Examples "
                  "\n (C1) / (1) Example 1 -        "
                  "\n (C2) / (2) Example 2 -                      "
                  "\n (C3) / (3) Example 3 -    "
                  "\n (C4) / (4) Example 4 -            "


                  "\n (D) Description\n "
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

        if str(a) == "3":
            EX3()
            continue_lesson()
            definition()

        if str(a) == "c3":
            EX3_code()
            continue_lesson()
            definition()

        if str(a) == "4":
            EX4()
            continue_lesson()
            definition()

        if str(a) == "c4":
            EX4_code()
            continue_lesson()
            definition()

        else:
            main_menu_1()

    definition()

def lesson_25():

    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 25  - Working with Files    -----------------------------\n")

    def definition():
            title()
            print("Files are very powerful.  It is like a dictionary but outside of python.  The information is held in a Text file like a Table in a database."
                  "\nIn this lesson we are going to be be working with files.  We are going to:\n"
                  
                  
                  "\n                              Objectives of Lesson                                                     List Modes "
                  "\n             - Create a Text (txt) file using python code                               \"r\"   =  Read   "
                  "\n             - Append to the text file                                                             \"a\"  =  Append    "
                  "\n             - Input Variables and add to the list                                          \"w\" =  Write    "
                  "\n             - Check to see if the file is readable                                          \"c\"  =  create    "
                  "\n             - Read the file one at a time"
                  "\n             - Read the first three lines of the file"
                  "\n             - Read the file as an list   "  
                    "\n           - Create for loop to read all the items in a file   \n"  )

            input("press <Enter> for Menu")
            end()

    def read_file():
        Test_file1 = open("Test_File_1.txt", "r")
        print(Test_file1 .read())
        Test_file1 .close()

    def EX1():
        title()
        print("                                          Exercise 1 - Creating a Text (TXT) file.\n")
        print("CAUTION  - This will re-write the text file leaving it empty\n")
        print("We are going to WRITE  a Text (TXT) file using the write mode,  then CLOSE the file:")
        print("                 Here is the code:"
              "\n                                1           Test_file1 = open(\"Test_File_1.txt\", \"w\")"
                 "\n                                2           Test_file1.close()")
        Test_file1 = open("Test_File_1.txt", "w")
        Test_file1.close()
        print("\n If you look at the files list, you will see a new file called \"Test_File_1.txt\" ")
        print("\nNow were going to OPEN the file,  READ the file, then CLOSE the file.. ")

        print("                 Here is the code:"
              "\n                                 1           Test_file1 = open(\"Test_File_1.txt\", \"r\")   ")
        print("                                 2           print(Test_file1 .read()) ")
        print("                                 3           Test_file1 .close() ")

        read_file()

        print("As you can see it is empty\n")


        continue_lesson()
        end()



    def EX2():
        title()
        print("                                          Exercise 2 - Creating a Text (TXT) file with given data.\n")
        print("CAUTION  - This will re-write the text file leaving it with only the information  from this exercise.\n")
        print("Now were going to WRITE to our Text file, READ the file, then CLOSE the file."
              "\n  You can enter 4 lines and it will write it to the Text file ( Test_File_1.txt). "
              "\n                               Here is the code:  ")

        print("                                 1               a1 = input(\"Please enter the first line to enter into our text file:  \")    ")
        print("                                 2               a2 = input(\"Please enter the second line to enter into our text file:  \")   ")
        print("                                 3               a3 = input(\"Please enter the Third line to enter into our text file:  \")   ")
        print("                                 4               a4 = input(\"Please enter the forth line to enter into our text file:  \")   ")

        print("                                 5               Test_file1 = open(\"Test_File_1.txt\", \"w\")   ")
        print("                                 6               Test_file1.write(a1 + \"\\n\")   ")
        print("                                 7               Test_file1.write(a2 + \"\\n\")   ")
        print("                                 8               Test_file1.write(a3 + \"\\n\")   ")
        print("                                 9               Test_file1.write(a4 + \"\\n\")   ")
        print("                                 10             Test_file1.close() \n ")

        a1 = input("Please enter the first line to enter into our text file:  ")
        a2 = input("Please enter the second line to enter into our text file:  ")
        a3 = input("Please enter the Third line to enter into our text file:  ")
        a4 = input("Please enter the forth line to enter into our text file:  ")

        Test_file1 = open("Test_File_1.txt", "w")
        Test_file1.write(a1 + "\n")
        Test_file1.write(a2 + "\n")
        Test_file1.write(a3 + "\n")
        Test_file1.write(a4 + "\n")
        Test_file1.close()


        print("\nNow were going to OPEN the file,  READ the file, then CLOSE the file.. ")

        print("                             Here is the code:"
              "\n                                 1           Test_file1 = open(\"Test_File_1.txt\", \"r\")   ")
        print("                                 2           print(Test_file1 .read()) ")
        print("                                 3           Test_file1 .close() ")

        read_file()

        continue_lesson()
        end()




    def EX3():
        title()
        print(
            "                                                                          Exercise 3 - Appending to the file  \n")
        print("In this exercise we are going to add (APPEND) to the file. In the previous file we did a WRITE which means "
              "\nwe wiped out the table and added new data.  APPEND is when we add data to the existing data."
              " \n\n Were going to OPEN the file, APPEND the file, READ the file, then CLOSE the file. \n")

        print("                 Here is the code:")

        print("                         1           First_Input_Addition = input(\"Add another line to our text file.  :  \")   ")
        print("                         2           Second_Input_Addition = input(\"Add second line to our text file   :  \")  ")
        print("                         3           Third_Input_Addition = input(\"Add third line to our text file :    \")  ")

        print("                         4           print(\"\\n                    ----  File Output - --\")   ")

        print("                         5           Test_file1 = open(\"Test_File_1.txt\", \"a\")  ")
        print("                         6           Test_file1.write(First_Input_Addition + \"\\n\")  ")
        print("                         7           Test_file1.write(Second_Input_Addition + \"\\n\")  ")
        print("                         8           Test_file1.write(Third_Input_Addition + \"\\n\")  ")
        print("                         9           Test_file1.close() \n ")



        First_Input_Addition = input("Add another line to our text file.  :  ")
        Second_Input_Addition = input("Add second line to our text file   :  ")
        Third_Input_Addition = input("Add third line to our text file :    ")

        print("\n                    ----  File Output ---  ")

        Test_file1 = open("Test_File_1.txt", "a")
        Test_file1.write(First_Input_Addition + "\n")
        Test_file1.write(Second_Input_Addition + "\n")
        Test_file1.write(Third_Input_Addition + "\n")
        Test_file1.close()

        print("\nNow were going to OPEN the file,  READ the file, then CLOSE the file.. ")
        print("                             Here is the code:"
              "\n                                 1           Test_file1 = open(\"Test_File_1.txt\", \"r\")   ")
        print("                                 2           print(Test_file1 .read()) ")
        print("                                 3           Test_file1 .close() ")

        read_file()
        continue_lesson()
        end()


    def EX3_code():
        print("ex3 - Code")
        continue_lesson()
        end()

    def EX4():
        title()
        print("                                                      Exercise 4 - Checking to see if the file is readable in APPEND mode \n ")
        print("Were going to check to see if the file is readable.  ")

        print("\n We will OPEN the text filein APPEND mode, check to see if it is READABLE, then close the file..")
        print("\n                               Here is the code:"
              "\n                                      1           Test_file1 = open(\"Test_File_1.txt\",\"a\")")
        print("                                      2           print(Test_file1.readable())")
        print("                                      3           Test_file1.close()\n")

        Test_file1 = open("Test_File_1.txt", "a")
        print(Test_file1.readable())
        Test_file1.close()
        print("\nAs you can see since it will produce a \"False\" since it is not readable.")
        continue_lesson()
        end()

    def EX5():
        title()
        print("                                                      Exercise 5 - Checking to see if the file is readable in READABLE mode \n ")
        print("Were going to check to see if the file is readable.  ")

        print("\n We will OPEN the text filein APPEND mode, check to see if it is READABLE, then close the file..")
        print("\n                               Here is the code:"
              "\n                                      1           Test_file1 = open(\"Test_File_1.txt\",\"r\")")
        print("                                      2           print(Test_file1.readable())")
        print("                                      3           Test_file1.close()\n")

        Test_file1 = open("Test_File_1.txt", "r")
        print(Test_file1.readable())
        Test_file1.close()
        print("\nAs you can see since it will produce a \"True\" since it is not readable.")
        continue_lesson()
        end()

    def EX6():
            title()
            print(
                "                                                     Exercise 6 - READING one at a time in the file \n ")
            print("Now were going to read the first line using:  - print(dan_file1.readline())\")")
            print("                              The code is: ")
            print("                                     1       Test_file1 = open(\"Test_File_1.txt\"\,\"r\"))")
            print("                                     2       print(Test_file1.readline())")
            print("                                     3       Test_file1.close()\n")

            Test_file1 = open("Test_File_1.txt", "r")
            print(Test_file1.readline())
            Test_file1.close()
            continue_lesson()
            end()


    def EX7():
            title()
            print(
                "                                                     Exercise 6 - READING First 3 lines \n ")
            print("Now were going to read the first 3.")
            print("                              The code is: ")
            print("                                     1       Test_file1 = open(\"Test_File_1.txt\"\,\"r\"))")
            print("                                     2       print(Test_file1.readline())")
            print("                                     3       print(Test_file1.readline())")
            print("                                     4       print(Test_file1.readline())")
            print("                                     5       Test_file1.close()\n")
            print("                               Output")

            Test_file1 = open("Test_File_1.txt", "r")
            print(Test_file1.readline())
            print(Test_file1.readline())
            print(Test_file1.readline())
            Test_file1.close()
            continue_lesson()
            end()

    def EX8():
        title()
        print(
            "                                                     Exercise 8 - READING all lines in an list \n ")
        print("Now were going to create a list of all the entries on the list.")
        print("                              The code is: ")
        print("                                     1       Test_file1 = open(\"Test_File_1.txt\"\,\"r\"))")
        print("                                     2       print(Test_file1.readlines()) - notice the \"S\" after readline")
        print("                                     3       Test_file1.close()\n")

        Test_file1 = open("Test_File_1.txt", "r")
        print(Test_file1.readlines())
        Test_file1.close()
        continue_lesson()
        end()


    def EX9():
        title()
        print(
            "                                                     Exercise 9 - READING by selected index\n ")
        print("Now were going to index the 4th position of the TEXT file.")
        print("                              The code is: ")
        print("                                     1       Test_file1 = open(\"Test_File_1.txt\"\,\"r\"))")
        print("                                     2       print(Test_file1.readlines())    ---   To run the ful list")
        print("                                     3       Test_file1.close()")
        print("                                     4       Test_file1 = open(\"Test_File_1.txt\"\,\"r\"))")
        print("                                     5       print(Test_file1.readlines()[3])    ---   To run the 4th position\n")

        Test_file1 = open("Test_File_1.txt", "r")
        print("                                  Full File      - " + str(Test_file1.readlines()))
        Test_file1.close()
        Test_file1 = open("Test_File_1.txt", "r")
        print("           4th positon of the File       - " + str(Test_file1.readlines()[3]))
        print(" NOTE - Every time you generate a list by reading the file you have to open it."
              "\n             Since I ran it 2 time (once for the full list and another for 4th position, I had to open twice).\n")
        Test_file1.close()
        continue_lesson()
        end()

    def EX10():
        title()
        print(
            "                                                     Exercise 10 - READING by  indexing in a for loop\n ")
        print("Now were going to go use a for loop to index the file.\n")
        print("                              The code is: ")
        print("                                     1       Test_file1 = open(\"Test_File_1.txt\", \"r\")")
        print("                                     2       for item in Test_file1.readlines():")
        print("                                     3                   print(item)\n")
        Test_file1 = open("Test_File_1.txt", "r")
        print("                                  Full File      - " + str(Test_file1.readlines()))
        Test_file1.close()

        Test_file1 = open("Test_File_1.txt", "r")
        for item in Test_file1.readlines():
            print(item)

        Test_file1.close()
        continue_lesson()
        end()



    def end():
        title()
        print("                                                                                                  Menu of Exercises")
        print(" --------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        a = input("\n Please Select: To see the code behind the example put \"C\" before the number\n"
                  "\n (D)   Description of Lesson "
                  "\n (R)   Read the Text file "
                  "\n 1 -  Exercise 1 - Creating a Text (TXT) file  - Caution will wipe the text file clean   "
                  "\n 2 -  Exercise 2 - Creating a Text (TXT) file then adding  given data - Caution will wipe the text file clean and add the data inputed   "
                  "\n 3 -  Exercise 3 - Appending to the Text (TXT) file      "
                  "\n 4 -  Exercise 4 - Checking to see if the file is readable in APPEND mode       "
                  "\n 5 -  Exercise 5 - Checking to see if the file is readable in READ mode   "
                  "\n 6 -  Exercise 6 - READ one at a time in the file "
                  "\n 7 -  Exercise 7 - READ First 3 lines in the file "
                  "\n 8 -  Exercise 8 - READING all lines in an list "
                  "\n 9 -  Exercise 9 - READING by selected index " 
                  "\n 10 - Exercise 10 - READING by  indexing in a for loop"

                  "\n\n           <Enter>  for main menu: ")

        if str(a) == "r":
            title()
            print("Here is the current state or our text file:")
            read_file()
            continue_lesson()
            end()

        if str(a) == "r":
            EX1()
        if str(a) == "1":
            EX1()
        if str(a) == "2":
            EX2()
        if str(a) == "3":
            EX3()
        if str(a) == "4":
            EX4()
        if str(a) == "5":
            EX5()
        if str(a) == "6":
            EX6()
        if str(a) == "7":
            EX7()
        if str(a) == "8":
            EX8()
        if str(a) == "9":
            EX9()
        if str(a) == "10":
            EX10()
        else:
            main_menu_1()

    definition()

def lesson_26():

    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 26  - Modules and PIP  -----------------------------\n")

    def definition():
            title()
            print("\n -   Modules are simply files with the “. py” extension containing Python code that can be imported inside another Python Program.")
            print("\n -   We can consider a module to be the same as a code library or a file that contains a set of functions that you want to include in your application.")

            print("\n -   PIP is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes."
                  "\n      NOTE - PIP usually comes installed with Python Version 3 and above.\n")

            continue_lesson()
            end()


    def run_all():
        print("Run All")
        continue_lesson()
        end()

    def EX1():
        title()
        print("                                                                  Exercise 1 - Make sure you have PIP")
        print("\nMake sure you have pip by opening command prompt (CMD)"
              "\n           *   At the command line type \"pip --verson\" - I have verson 2.3.1"
              "\n           *   If you don't have pip you can look up in google to install\n")


    def EX2():
        title()
        print("                                                                                  Exercise 2 - Installing a module")
        print("\n How to install a Module:"
              "\n           *   We are using the example of \"Python Docs\" to install."
              "\n           *   Look in Google for the instructions.  It will say \"pip install python-docx\"."
              "\n           *    So at the command line type \"pip install python-docx\" and it will install pyton docs\"." 
              "\n           *    It stores it in Lib\site-packages.  If you downloaded it and look at Lib\site-packages, you will see it." 
              "\n           *    You will notice that it no only created a folder called \"pip install python-docx\", it also created \"docx\". "         
              "\n\n If you want to use in our program.  You just need to refer to the name of the module." 
              "\n           *  in this case it would be \"from docx import *\".\n"
                )

    def EX3():
        title()
        print("                                                                             Exercise 3 - Using modules")
        print("\n Created Modules - I created new modules (files) called:"
              "\n                       *       0-1-1_Useful-Tools.py                                      -       Where I put Various Tools I use.  "
              "\n                       *       B_1_26_Lesson_26_Modules_and_PiP.py      -       Where this lesson is stored"
              "\n                       That I will import and use the functions stored within the module "
               "\n                      There are built in modules and external modules            "
              "\n   Internal   - If you go to D\External Libraries\Lib you will see the external modules."
              "\n                       * You can access the functions in the modules by importing the given module"
              "\n                       *  \"import docx\" "
              "\n\n External Modules:"
              "\n                       * If you look in Google \"Python Module Index\" you will find Thounds of additional modules  in Google. "
             "\n                       * You can look/up install 3rd party modules  "
              "\n                                NOTE   -  You have to know what version of python to find the correct modules."
              )

    def run_all_lessons():
        EX1()
        continue_lesson()
        EX2()
        continue_lesson()
        EX3()
        continue_lesson()
        end()


    def end():
        title()
        print("                                                                                  Lesson Menu")
        a = input("\n Please Select: To see the code behind the example put \"C\" before the number\n"
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run all Lessons "
                  "\n  (1) Exercise 1 - Make sure you have PIP      "
                  "\n  (2) Exercise 2 - Installing a module                "
                  "\n  (3) Exercise 3 - Using modules    "


                  "\n           <Enter>  for main menu: ")

        if str(a) == "d":
            definition()

        if str(a) == "D":
            definition()

        if str(a) == "r":
            run_all_lessons()

        if str(a) == "R":
            run_all_lessons()

        if str(a) == "1":
            EX1()
            continue_lesson()
            end()

        if str(a) == "2":
            EX2()
            continue_lesson()
            end()

        if str(a) == "3":
            EX3()
            continue_lesson()
            end()

        else:
            main_menu_1()

    definition()




def lesson_27():
    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 27  - Classes and Objects  -----------------------------\n")

    def definition():
        title()
        print("\nWhat is an object:"
              "\n  *    Python is an object oriented programming language. "
              "\n  *    Almost everything in Python is an object, with its properties and methods."
              "\n  *    Objects have member variables and have behaviour associated with them. In python a class is created by the keyword class . An object is created using the constructor of the class."

              "\n\nWhat is a Class"
              "\n   *  A Class is like an object constructor, or a \"blueprint\" for creating objects."
              "\n   *  A class is a code template for creating objects. "
              " \n   *   In python a class is created by the keyword class."
              "\n   *   Class is another datatype we can use in python.\n\n"
              )

        enter_lesson_menu()
        end()

    def run_all():
        print("Run All")
        continue_lesson()
        end()

    def EX1():
        title()
        print("                                                                  Exercise 1 - Creating a Class")
        print("\nStep 1 - Create a new file Python file (.py).  I called it \"PC_1_1_1_Class_file.py\""
              "\n\nStep 2 - Create a class within that new python file  "
              "\n     *   It begins with \"class\" ."
              "\n     *   Followed by the name of the class then a colon \":\"."
              "\n     *   I called mine  \"class Car:\""
              "\n\nStep 3 -  Create an initialized function."
              "\n     *     Use \"def\" space, two underscores \"__\" the word \"init\" two more underscores \"__\" then \"(self) followed by colon\":\""
              "\n     *     Here is the full command:    def __init__(self):\n"

              )
        continue_lesson()
        title()
        print("                                                                  Exercise 1 - Creating a Class")
        print(
            "\n\nStep 4 - Assign the attributes of the class you can you use Strings, Numbers and Booleans.  How you do this is:"
            "\n         * Add in Attributes after \"Self,\")  These can be anything you want.  I used Make, Model, Year, Would I buy"
            "\n         * Here is what it looks like  \"def __init__(self, Make, Model, Year, Would_you_buy):\" \n " \
            "")

        print(
            "\nStep 5 - Now we have to assign some Values.  In order to do this we have to assign the attribute with a variable."
            "\n         *   The format is: \"self.\" the name of the attribute, followed by the name of the variable (you can use any name for the variable"
            "\n         *   Here is an example of the one i created:"
            "\n                      -      self.Make  = Make"
            "\n                      -      self.Model = Model"
            "\n                      -      self.Year    = Year"
            "\n                      -      Would_you_buy = Would_you_buy \n"
            )
        continue_lesson()
        title()
        print("                                                                  Exercise 1 - Creating a Class")
        print("\nHere is the full file:"
              "\n                           1   class Car:"
              "\n                           2      def __init__(self, Make, Model, Year, Would_you_buy):"
              "\n                           3       self.Make = Make"
              "\n                           4       self.Model = Model"
              "\n                           5       self.Year = Year"
              "\n                           6       self.Would_you_buy = Would_you_buy\n"
              "\n\n And that is how you create a class."
              )

    def EX2():
        title()
        print(
            "                                                                       Exercise 2 - Assigning the Attributes in the class")
        print("\n In the Python file you are working in (not the class file) you assign must:"
              "\n Step 1 - import the file.  Your code \"from\" name of the Class Python File \"import\" then the name of the class"
              "\n                                                                1   from C_1_1_1_Class_file import Car "
              "\n \nStep 2 - Assign the attributes."
              "\n * New Variable, \"=\" Class name \"(\"attrubute 1\",\" attrubute 2\" followed by all the (attributes assigned)  \")\". "
              "\n * Here is what I used                             2   Car1 = Car(\"Ford\", \"Mustang\" \"2008\", True)"
              "\n\n Step 3 - Now we can print any attrubute we want:"
              "\n       If we want to print the Make -          3   print(Car1.Make)  "
              "\n       If we want to print the Make -          4   print(Car1.Model)  "
              "\n       If we want to print the Year -           5   print(Car1.Year)  "
              "\n       If we want to print the Make -          6   print(Car1.Would_you_buy)  "
              )

    def EX3():
        title()
        print(
            "                                                                             Exercise 3 - Printing the Attrubutes in the Class")
        print("\n At this point, I'll show you the code followed by the output"
              "\n           Code used:"
              "\n                              1         from C_1_1_1_Class_file import Car "
              "\n                              2        Car1 = Car(\"Ford\", \"Mustang\" \"2008\", True)"
              "\n                              3        print(Car1.Make)  "
              "\n                              4        print(Car1.Model)  "
              "\n                              5        print(Car1.Year)  "
              "\n                              6        print(Car1.Would_you_buy)  "
              "\n\n           Output:"
              "")
        Car1 = Car("Ford", "Mustang", "2008", True)
        print(Car1.Make)
        print(Car1.Model)
        print(Car1.Year)
        print(Car1.Would_you_buy)
        print("")
        continue_lesson()
        title()
        print(
            "                                                                             Exercise 3 - Printing the Attrubutes in the Class")
        print("\n Lets enter another input.  Note we are using Car2 this time"
              "\n           Code used:"
              "\n                              1         from C_1_1_1_Class_file import Car "
              "\n                              2        Car1 = Car(\"GMC\", \"Hummer\" \"2008\", True)"
              "\n                              3        print(Car1.Make)  "
              "\n                              4        print(Car1.Model)  "
              "\n                              5        print(Car1.Year)  "
              "\n                              6        print(Car1.Would_you_buy)  "
              "\n\n           Output:"
              "")
        Car1 = Car("GMC", "Hummer H3", "2008", True)
        print(Car1.Make)
        print(Car1.Model)
        print(Car1.Year)
        print(Car1.Would_you_buy)
        print("")

    def run_all_lessons():
        EX1()
        continue_lesson()
        EX2()
        continue_lesson()
        EX3()
        continue_lesson()
        end()

    def end():
        title()
        print("                                                                                  Lesson Menu")
        a = input("\n Please Select: To see the code behind the example put \"C\" before the number\n"
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run all Lessons "
                  "\n  (1) Exercise 1 - Make sure you have PIP      "
                  "\n  (2) Exercise 2 - Installing a module                "
                  "\n  (3) Exercise 3 - Using modules    "


                  "\n           <Enter>  for main menu: ")

        if str(a) == "d":
            definition()

        if str(a) == "D":
            definition()

        if str(a) == "r":
            run_all_lessons()

        if str(a) == "R":
            run_all_lessons()

        if str(a) == "1":
            EX1()
            continue_lesson()
            end()

        if str(a) == "2":
            EX2()
            continue_lesson()
            end()

        if str(a) == "3":
            EX3()
            continue_lesson()
            end()

        else:
            main_menu_1()
    definition()


def lesson_28():
    ''''***********************************************************************************************************************
    *                                                               Car Trivia  - Game 1                                                                    *
    *************************************************************************************************************************'''

    def f1_car_trivia():
        title()
        print(
            "                                                            ------------            Car Trivia  - Game 1              --------------- \n")


        question_prompts = [
            "1. What is the best selling electric car model of all time?"
            "\n (a) Tesla Model S"
            "\n (b) Tesla Model 3"
            "\n (c) Tesla Model X"
            "\n (d) Tesla Model Y\n\n",

            "2. What German car brand has a logo that features four interlocking rings??"
            "\n (a)  BMW"
            "\n (b)  Audi"
            "\n (c)  Mercedes"
            "\n (d)  all the above\n\n",

            "3. What car company has produced the Corolla model since 1966?"
            "\n (a)  Datsun"
            "\n (b)  Toyota"
            "\n (c)  Nissian"
            "\n (d)  Honda\n",

            "4. What car brand produces the popular F-150 truck?"
            "\n (a)  Chevy"
            "\n (b)  Dodge"
            "\n (c)  Ford"
            "\n (d)  Pizza \n",

        ]

        questions = [
            Question(question_prompts[0], "b"),
            Question(question_prompts[1], "b"),
            Question(question_prompts[2], "b"),
            Question(question_prompts[3], "c"),

        ]

        def run_test(questions):
            score = 0
            for question in questions:
                answer = input(question.prompt + "Please select multiple choice:  ")
                if answer == question.answer:
                    print("Your are Correct\n")
                    score += 1
                else:
                    print("Incorrect\n")
            print("                     ****        Your got " + str(score) + "/" + str(
                len(questions)) + " Correct!!!              ****")

        run_test(questions)

        a = input("\nEnter \"y\" to play again or <Enter> to  Quiz Menu>):  ")
        if str(a) == "y":
            t1_python_trivia_1()
        elif str(a) == "y":
            t1_python_trivia_1()
        else:
            menu()


    '''  ==================================================================================
                                                                Tech Quiz Section
        ==================================================================================='''

    ''''***********************************************************************************************************************
    *                                                               Python Trivia  - Game 1                                                                    *
    *************************************************************************************************************************'''

    def t1_python_trivia_1():
        title()
        print(
            "                                                      ------------            Python Trivia  - Game 1              --------------- \n")
        question_prompts = [
            "1. Who developed Python Programming Language?"
            "\n (a) Wick van Rossum"
            "\n (b)  Rasmus Lerdorf"
            "\n (c)  Guido van Rossum"
            "\n (d)  Niene Stom\n\n",

            "2. Which type of Programming does Python support?"
            "\n (a)  object-oriented programming"
            "\n (b)  structured programming"
            "\n (c)  functional programming"
            "\n (d)  all the above\n\n",

            "3. Is Python case sensitive when dealing with identifiers?"
            "\n (a)  no"
            "\n (b)  yes"
            "\n (c)  machine dependent"
            "\n (d)  Non of the above\n",

            "4. Which of the following is the correct extension of the Python file?"
            "\n (a)  python"
            "\n (b)  .pl"
            "\n (c)  .py"
            "\n (d)  .p \n",

            "5. Is Python code compiled or interpreted?"
            "\n (a)  Python code is both compiled and interpreted"
            "\n (b)  Python code is neither compiled nor interpreted"
            "\n (c)  Python code is only compiled"
            "\n (d)  Python code is only interpreted \n",

            "6. All keywords in Python are in _________"
            "\n (a)  Capitalized"
            "\n (b)  lower case"
            "\n (c)  UPPER CASE"
            "\n (d)  None of the Above \n",

            "7. What will be the value of the following Python expression?\n 4 + 3 % 5"
            "\n (a)  7"
            "\n (b)  2"
            "\n (c)  4"
            "\n (d)  1 \n",

            "8. Which of the following is used to define a block of code in Python language?"
            "\n (a)  Indentation"
            "\n (b)  Key"
            "\n (c)  Brackets"
            "\n (d)  All the above \n",

            "9. Which keyword is used for function in Python language?"
            "\n (a)  Function"
            "\n (b)  def"
            "\n (c)  Fun"
            "\n (d)  Define \n",

            "10.  Which of the following character is used to give single-line comments in Python?"
            "\n (a)  //"
            "\n (b)  #"
            "\n (c)  !"
            "\n (d)  /* \n",

        ]

        questions = [
            Question(question_prompts[0], "c"),
            Question(question_prompts[1], "d"),
            Question(question_prompts[2], "b"),
            Question(question_prompts[3], "c"),
            Question(question_prompts[4], "a"),
            Question(question_prompts[5], "d"),
            Question(question_prompts[6], "a"),
            Question(question_prompts[7], "a"),
            Question(question_prompts[8], "b"),
            Question(question_prompts[9], "b"),
        ]

        def run_test(questions):
            score = 0
            for question in questions:
                answer = input(question.prompt + "Please select multiple choice:  ")
                if answer == question.answer:
                    print("Your are Correct\n")
                    score += 1
                else:
                    print("Incorrect\n")
            print("                     ****        Your got " + str(score) + "/" + str(
                len(questions)) + " Correct!!!              ****")

        run_test(questions)

        a = input("\nEnter \"y\" to play again or <Enter> to  Quiz Menu>):  ")
        if str(a) == "y":
            t1_python_trivia_1()
        elif str(a) == "y":
            t1_python_trivia_1()
        else:
            menu()

    ''''***********************************************************************************************************************
    *                                                               Python Trivia  - Game 2                                                                    *
    *************************************************************************************************************************'''

    def t2_python_trivia_2():
        title()
        print(
            "                                                        ------------            Python Trivia  - Game 2              --------------- \n")
        question_prompts = [
            "11. What will be the output of the following Python code?\n"
            "\ni = 1"
            "\nwhile True:"
            "\n    if i%3 == 0:"
            "\n    print(i)\n"
            "\n   i + = 1\n"

            "\n (a) 1 2 3"
            "\n (b)  error - shouldn’t be a space between + and = in +="
            "\n (c)  1 2"
            "\n (d)  None of the above\n\n",

            "12. Which of the following functions can help us to find the version of python that we are currently working on?"
            "\n (a)  sys.version(1)"
            "\n (b)  sys.version(0)"
            "\n (c)  sys.version()"
            "\n (d)  sys.version\n\n",

            "13. Python supports the creation of anonymous functions at runtime, using a construct called __________"
            "\n (a)  pi"
            "\n (b)  anonymous"
            "\n (c)  lambda"
            "\n (d)  Non of the above\n",

            "14. What is the order of precedence in python?"
            "\n (a)  Exponential, Parentheses, Multiplication, Division, Addition, Subtraction"
            "\n (b)  Exponential, Parentheses, Division, Multiplication, Addition, Subtraction"
            "\n (c)  Parentheses, Exponential, Multiplication, Division, Subtraction, Addition"
            "\n (d)  Parentheses, Exponential, Multiplication, Division, Addition, Subtraction \n",

            "15. What will be the output of the following Python code snippet if x=1?\n"
            "x<<2"
            "\n (a)  4"
            "\n (b)  2"
            "\n (c)  Python code is only compiled"
            "\n (d)  Python code is only interpreted \n",

            "16. What does pip stand for python"
            "\n (a)  Pip Installs Python"
            "\n (b)  Pip Installs Packages"
            "\n (c)  Preferred Installer Program"
            "\n (d)  all of the Above \n",

            "17. Which of the following is true for variable names in Python?"
            "\n (a)  underscore and ampersand are the only two special characters allowed"
            "\n (b)  unlimited length"
            "\n (c)  all private members must have leading and trailing underscores"
            "\n (d)  none of the Above \n",

            "18. What are the values of the following Python expressions?"
            "\n2**(3**2)"
            "\n(2**3)**2"
            "\n2**3**2\n"
            "\n (a)  512, 64, 512"
            "\n (b)  512, 512, 512"
            "\n (c)   64, 512, 64"
            "\n (d)   64, 64, 64 \n",

            "19. Which of the following is the truncation division operator in Python?"
            "\n (a)  |"
            "\n (b)  //"
            "\n (c)  /"
            "\n (d)  % \n",

            "20. What will be the output of the following Python code?"
            "\n l=[1, 0, 2, 0, 'hello', \'', []]"
            "\nlist(filter(bool, l))\n"
            "\n (a)   [1, 0, 2, ‘hello’, ”, []]"
            "\n (b)  Error"
            "\n (c)   [1, 2, ‘hello’]"
            "\n (d)   [1, 0, 2, 0, ‘hello’, ”, []] \n",

        ]

        questions = [
            Question(question_prompts[0], "b"),
            Question(question_prompts[1], "d"),
            Question(question_prompts[2], "c"),
            Question(question_prompts[3], "d"),
            Question(question_prompts[4], "a"),
            Question(question_prompts[5], "c"),
            Question(question_prompts[6], "b"),
            Question(question_prompts[7], "a"),
            Question(question_prompts[8], "b"),
            Question(question_prompts[9], "c"),
        ]

        def run_test(questions):
            score = 0
            for question in questions:
                answer = input(question.prompt + "Please select multiple choice:  ")
                if answer == question.answer:
                    print("Your are Correct\n")
                    score += 1
                else:
                    print("Incorrect\n")
            print("                     ****        Your got " + str(score) + "/" + str(
                len(questions)) + " Correct!!!              ****")

        run_test(questions)

        a = input("\nEnter \"y\" to play again or <Enter> to  Quiz Menu>):  ")
        if str(a) == "y":
            t2_python_trivia_2()
        elif str(a) == "y":
            t2_python_trivia_2()
        else:
            menu()

    ''''***********************************************************************************************************************
    *                                                               Python Trivia  - Game 3                                                                    *
    *************************************************************************************************************************'''

    def t3_python_trivia_3():
        title()
        print(
            "                                                        ------------            Python Trivia  - Game 3              --------------- \n")

        question_prompts = [
            " 0b- 21. Which of the following functions is a built-in function in python?"

            "\n (a) factorial()"
            "\n (b) print()"
            "\n (c) seed()"
            "\n (d) sqrt()\n\n",

            "1b- 22. Which of the following is the use of id() function in python?\n"
            "\n (a)  Every object does not have a unique id"
            "\n (b)  Id returns the identity of the object"
            "\n (c)  All of the mentioned"
            "\n (d)  None of the mentioned\n\n",

            "2a- 23. The following python program can work with ____ parameters.\n"
            "\n     def f(x):"
            "\n          def f1(*args, **kwargs):"
            "\n                     print(\"Sanfoundry\")"
            "\n                     return x(*args, **kwargs)"
            "\n     return f1\n"
            "\n (a)  any number of"
            "\n (b)  0"
            "\n (c)  1"
            "\n (d)  2\n",

            "3d 24. What will be the output of the following Python function?"
            "\nmin(max(False,-3,-4), 2,7)\n"

            "\n (a)  4"
            "\n (b)  -3"
            "\n (c)  2"
            "\n (d)  False \n",

            "4c- 25. Which of the following is not a core data type in Python programming?\n"

            "\n (a)  Tuples"
            "\n (b)  Lists"
            "\n (c)  Class"
            "\n (d)  Dictionary\n",

            "5d- 26. How you  doing?"

            "\n (a)  Been Better"
            "\n (b)  okay"
            "\n (c)  good"
            "\n (d)  Great\n",

            "6b- 27. Which of these is the definition for packages in Python?"
            "\n (a)  A set of main modules"
            "\n (b)  A folder of python modules"
            "\n (c)  A number of files containing Python definitions and statements"
            "\n (d) A set of programs making use of Python modules \n",

            "7c- 28. What will be the output of the following Python function?"
            "\nlen([\"hello\",2, 4, 6])"

            "\n (a)  Error"
            "\n (b)  6"
            "\n (c)  4"
            "\n (d)  3 \n",

            "8d  29. What will be the output of the following Python code?"
            "\n     x = 'abcd'"
            "\n     for i in x:"
            "\n         print(i.upper())"

            "\n (a) a\n B\n C\n D"
            "\n (b) a b c d"
            "\n (c)  error"
            "\n (d) A\n B\n C\n D"

            "8c  30. What is the order of namespaces in which Python looks for an identifier?"


            "\n (a) Python first searches the built-in namespace, then the global namespace and finally the local namespace"
            "\n (b) Python first searches the built-in namespace, then the local namespace and finally the global namespace"
            "\n (c) Python first searches the local namespace, then the global namespace and finally the built-in namespace"
            "\n (d) Python first searches the global namespace, then the local namespace and finally the built-in namespace"
        ]

        questions = [
            Question(question_prompts[0], "b"),
            Question(question_prompts[1], "b"),
            Question(question_prompts[2], "a"),
            Question(question_prompts[3], "d"),
            Question(question_prompts[4], "c"),
            Question(question_prompts[5], "d"),
            Question(question_prompts[6], "b"),
            Question(question_prompts[7], "c"),

        ]

        def run_test(questions):
            score = 0
            for question in questions:
                answer = input(question.prompt + "\nPlease select multiple choice:  ")

                if answer == question.answer:
                    print("Your are Correct\n")
                    score += 1
                else:
                    print("Incorrect\n")
            print("                     ****        Your got " + str(score) + "/" + str(
                len(questions)) + " Correct!!!              ****")

        run_test(questions)

        a = input("\nEnter \"y\" to play again or <Enter> to  Quiz Menu>):  ")
        if str(a) == "y":
            t3_python_trivia_3()
        elif str(a) == "y":
            t3_python_trivia_3()
        else:
            menu()

    ''''***********************************************************************************************************************
    *                                                               Coding                                                                  *
    *************************************************************************************************************************'''

    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson - 28  Quiz Time   -----------------------------\n")

    def menu():
        title()
        print("Now were going to have some fun.  I created a series of multiple choice quiz.   "
              "\nIt's for both to have fun and help learn programming and to help me learn classes better"
              "\n                See below for quizes  \n"
              "\n                                      Fun                                               Health                                        Technology"
              "\n--------------------------------------------------------------------------------------------------------------------------------------"
              "\n                               F1 - Cars  (WIP)                           H1 - Weight Lifting  (TBD)        T1 - Python Programming - Easy "
              "\n                               F2 - Motorcycles (TBD)                H2 - Cardio             (TBD)         T2 - Python Programming - Medium"
              "\n                               F3 - SXS (TBD)                            H3 - Outdoor Activity  (TBD       T3 - Python Programming - Hard)"
              "\n                               F4 - Electric Bikes (TBD)             H4 - Everyday Activity  (TBD     T4 - HTML \ CSS Programming (TBD"
              "\n                               F5 - Electric Motorcycles (TBD)                                                      T5 - Selenium (TBD)"
              "\n                                                                                                                                         T6 - JavaStrip (TBD)"
              "\n                                                                                                                                         T7 - Python GUI (TBD)"
              )
        end()

    def end():
        a = input("\nPlease select Quiz:  ")

        if str(a) == "f1":
            f1_car_trivia()
        elif str(a) == "F1":
            f1_car_trivia()
        elif str(a) == "t1":
            t1_python_trivia_1()
        elif str(a) == "T1":
            t1_python_trivia_1()
        elif str(a) == "t2":
            t2_python_trivia_2()
        elif str(a) == "T2":
            t2_python_trivia_2()
        elif str(a) == "t3":
            t3_python_trivia_3()
        elif str(a) == "T3":
            t3_python_trivia_3()
        else:
            main_menu_1()

    menu()


def lesson_29():
    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 29 - Object Function  -----------------------------\n")

    def definition():
        title()
        print("\nWhat is an object:"
              "\n       -   The object() function returns an empty object. You cannot add new properties or methods to this object. "
              "\n       -   This object is the base for all classes, it holds the built-in properties and methods which are default for all classes."
              "\n\n      -     Class Function is a function that we can use inside of a class and it can either modify tthe object of that class"
              "\n                   or give specific information about those objects.\n"
              )
        continue_lesson()
        ex1()

    def ex1():
        title()

        print(
            "\nStep 1 - I created a new class in our class file we created earlier.  The class file is calledC_1_1_1_Class_file.py"
            "\n   and the name of the new class I built is called class student_object:"
            "\n\nHere is the look at the class:\n"
            "\n                 class student_object:"
            "\n                           def __init__(self, name, major, gpa):"
            "\n                           self.name = name"
            "\n                           self.major = major"
            "\n                           self.gpa = gpa          \n  "
            )
        continue_lesson()
        title()
        print("  Step 2 - Now lets create the inputs for the class we are going to use:"
              "\n\n                   student1 = student_object(\"Micky Mouse\", \"Fun\", 4.0)"
              "\n                   student2 = student_object(\"Donald Duck\", \"Complaining\", 3.5)"
              "\n                   student3 = student_object(\"Goofy\", \"Goofing Around\", 1.7)\n"
              )
        continue_lesson()
        title()
        print("  Step 3 - Next steup is to crea a function that will tells us whether or not they are on Honor Roll: "
              "\n                     First thing we have to do is to add function in our class."
              "\n                               Here is the code I used "
              "\n\n                                     def on_honor_roll(self):"
              "\n                                             if (self.gpa) >= 3.5:      "
              "\n                                                return True"
              "\n                                            else:"
              "\n                                                return False\n\n   "
              )

        continue_lesson()
        title()
        print("     Step 4 - Now lets print the results.\n"
              "\n                         print(student1.on_honor_roll())"
              "\n                         print(student1.on_honor_roll())"
              "\n                         print(student1.on_honor_roll())\n"
              )

        student1 = student_object("Micky Mouse", "Fun", 4.0)
        student2 = student_object("Donald Duck", "Complaining", 3.5)
        student3 = student_object("Goofy", "Goofing around", 1.7
                                  )
        print((student1.name) + "is on honor role?  - " + str(student1.on_honor_roll()))
        print((student2.name) + "is on honor role?  - " + str(student2.on_honor_roll()))
        print((student2.name) + "is on honor role?  - " + str(student3.on_honor_roll()))

        a = input("\nWould you like to redu the lesson?   ")
        if a == "y":
            lesson_29()
        if a == "y":
            lesson_29()
        else:
            main_menu_1()

    definition()


def lesson_30():
    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 30  - Inheritance -----------------------------\n")

    def definition():
        title()
        print(
            "\n       *   Inheritance allows us to define a class that inherits all the methods and properties from another class. "
            "\n           Parent class is the class being inherited from, also called base class. "
            "\n           Child class is the class that inherits from another class, also called derived class.\n"
            "\n       *   Inheritance is basically where we can define a bunch of attributes, functions and things inside"
            " \n                 of a class.  Then we can create another class and inherit all of those attributes.\n"
            "\n       *   So you can have one class that has all the functionality of another class without having to physically write out"
            "any of the same methods or attributes."

            "\n\n        *  There are 5 type of inheritance:"
            "\n               -    Single Inheritance. "
            "\n               -    Multiple Inheritance."
            "\n               -    Multilevel Inheritance."
            "\n               -    Hierarchical Inheritance."
            "\n               -    Hybrid Inheritance.\n"
            )
        continue_lesson()
        end()

    def run_all_lessons():
        EX1()
        EX2()
        EX3()
        continue_lesson()
        end()

    def EX1():
        title()
        print("                                                         Exercise 1 - Building a common class")
        print(
            "\n     Created a new class in our class file we created earlier.  The class file is calledC_1_1_1_Class_file.py"
            "\n   and the name of the new class I built is called \"chef_class1\":"
            "\n\nHere is the look at the class:\n"
            "\n                 class chef_class1:"
            "\n                           def make_chicken(self):"
            "\n                               print(\"The chef makes a chicken\""
            "\n                           def make_salad(self):"
            "\n                               print(\"The chef makes a salad\""
            "\n                           def make_special_dish(self):"
            "\n                               print(\"The chef makes BBQ ribs\"\n"
        )
        continue_lesson()
        title()

        print("  Step 2 - Now we have to import the class we just made:"
              "\n                   from C_1_1_1_Class_file import chef_class\n"
              "\n\n   Step 3 - Now here is the code we used to use the class:"
              "\n                   mychef = chef_class()"
              "\n                   mychef.make_chicken()"
              "\n                   mychef.make_chicken()"
              "\n                   mychef.make_special_dish()\n"
              "\n\n   Step 4 - Now lets run the code:"
              )

        mychef = chef_class1()
        mychef.make_chicken()
        mychef.make_salad()
        mychef.make_special_dish()
        print()
        continue_lesson()

    def EX2():
        title()
        print(
            "                                                         Exercise 2 - Using the Common Class and adding Inheritance   ")
        print(
            "\n       In the previous exercise, we built a common class using a chef1. Now we have another chef (chef2)"
            "\n   and chef2 has the exact same attributes as chef1.  Now we could copy and paste, but that would be "
            "\n   inefficent and if you had any updates you'd have to remember to update both chefs.  So the answer to "
            "\nthis is inherit the class.  Hopefully this will make more since when we view the code.\n  "

            "\n       I created a new class in our class file we created earlier.  The class file is calledC_1_1_1_Class_file.py"
            "\n   that will inherit the attributes of chef1.  The new class name is \"chef_class2\".  This will be an inherit class."
            "\n   We also added another attribute unique to chef 2, which is \"is_pizza\". "

            "\n\nHere is the look at the class:\n"
            "\n                 class chef_class2(chef_class1):"
            "\n                           def make_pizza(self):"
            "\n                               print(\"The chef makes pizza\")\n"

            )
        continue_lesson()
        title()

        print("  Step 2 - Now we have to import the class we just made:"
              "\n                   from C_1_1_1_Class_file import chef_class\n"
              "\n\n   Step 3 - Now here is the code we used to use the class:"
              "\n                   mychef = chef_class2()"
              "\n                   mychef.make_chicken()"
              "\n                   mychef.make_salad()"
              "\n                   mychef.make_special_dish()\n"
              "\n                   mychef.make_pizza()"
              "\n\n   Step 4 - Now lets run the code:"
              )
        mychef = chef_class2()
        mychef.make_chicken()
        mychef.make_salad()
        mychef.make_special_dish()
        mychef.make_pizza()
        print()
        continue_lesson()

    def EX3():
        title()
        print(
            "                              Exercise 3 - Overriding Attribute in Inheritance Class")
        print(
            "\n      Another powerful item we can do is override an attribute.  in this exercise we are going to override "
            "\n     chef1's special (\"The chef makes a BBQ ribs\") , with a new dish for chef2.  We'll say hamburger."
            "\n\n       So lets first recap the class for chef1:"
            "\n                 class chef_class1:"
            "\n                           def make_chicken(self):"
            "\n                               print(\"The chef makes a chicken\")"
            "\n                           def make_salad(self):"
            "\n                               print(\"The chef makes a salad\")"
            "\n                           def make_special_dish(self):"
            "\n                               print(\"The chef makes BBQ ribs\"\n)")
        continue_lesson()
        title()
        print("        So lets look at the existing class for chef2 (before the change)"
              "\n                  class chef_class2(chef_class1):"
              "\n                           def make_pizza(self):"
              "\n                               print(\"The chef makes pizza\")"

              "\n\n        Now lets look at the override code:"
              "\n                  class chef_class2(chef_class1):"
              "\n                           def make_pizza(self):"
              "\n                               print(\"The chef makes pizza\")"
              "\n                           def make_special_dish(self):"
              "\n                               print(\"The chef makes hamburger\")\n"
              )
        continue_lesson()
        title()

        print("  Step 3 - Now here is the code we used to use the class:"
              "\n                   mychef = chef_class2()"
              "\n                   mychef.make_chicken()"
              "\n                   mychef.make_salad()"
              "\n                   mychef.make_special_dish()"
              "\n                   mychef.make_pizza()\n"
              "\n   NOTE - it overrode make_special_dish() from bbq to hamburger"

              "\n\n   Step 4 - Now lets run the code:"
              )
        mychef = chef_class2()
        mychef.make_chicken()
        mychef.make_salad()
        mychef.make_special_dish()
        mychef.make_pizza()

        print()

    def end():
        print("                                                                                  Lesson Menu")
        a = input("\n Please Select:  "
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run all Lessons "
                  "\n  (1) Exercise 1 - Building a common class   "
                  "\n  (2) Exercise 2 - Using the Common Class and adding Inheritance        "
                  "\n  (3) Exercise 3 - Overriding Attribute in Inheritance Class    "


                  "\n           <Enter>  for main menu: ")

        if str(a) == "d":
            definition()

        if str(a) == "D":
            definition()

        if str(a) == "r":
            run_all_lessons()

        if str(a) == "R":
            run_all_lessons()

        if str(a) == "1":
            EX1()
            continue_lesson()
            end()

        if str(a) == "2":
            EX2()
            continue_lesson()
            end()

        if str(a) == "3":
            EX3()
            continue_lesson()
            end()
        else:
            main_menu_1()

    definition()



def version_control():
    ''''***********************************************************************************************************************
    *                                                               Version Control                                                                  *
    *************************************************************************************************************************'''


    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Programming Notes   -----------------------------\n")

    def version_menu():
        title()

        print("\n                                                                                    Version Control"
               "\n   Date                        Name of File                                     Updates                                                  Notes"
              "\n--------------------------------------------------------------------------------------------------------------------------------------"
              "\n  4/2/2023            1-1-0_Lession_Program-1.py               Completed up to Lesson 7                       Not happy  format/layout - have to work on "
              "\n                                                                                   "
              "\n\n  4/4/2023            1-1-0_Lession_Program-2.py               Completed up to lesson 12                      Still do not feel like have layout nailed down    "
              "\n                                                                                           ising functions for lessons/Exercises        Navigation much better - "
              "\n\n  4/10/2023         1-1-0_Lession_Program-3.py               Completed up to lesson 23                       Okay with layout.  "
             "\n                                                                                            using Array of functions for main menu   The array of funcitnos much cleaner"      
             "\n\n  4/13/2023         1-1-0_Lession_Program-4.py               Completed up to lesson 28                        Going to use this base program for next program leaning"
              "\n\n  4/14/2023         1-1-0_Lession_Program-9.py               Added Terminology Section                      add to Quiz section (lesson 28)"
              "\n\n  4/14/2023         1-1-0_Lession_Program-10.py              Added lesson 29 and 30                          "
        )
        a = input("\n\nPlease select (F) Future Updates <Enter> to return to the main menu:  ")
        if a == "f":
            future_updates()
        elif a== "F":
            future_updates()
        if a == "V":
            version_control()
        elif a== "v":
            version_control()
        else:
            main_menu_1()




    def future_updates():
        title()
        print(
            "\n                                                                                    Future Updates"
              "\n--------------------------------------------------------------------------------------------------------------------------------------"
              "\n               *    Add in the last 2 python lessons  "
              "\n          - inheritance "
              "\n          - pyton interpreter "         
              "\n               *    Add CSS/HTML/Java.Script    "                                              
              "\n               *    Spend a week building python programs and add to the lesson program     "
              "\n               *    Learn and add lessons for Selenium       "
              "\n               *    Learn more advanced python  (OOP)"
              "\n               *    Learn more advanced Java.Script"
              "\n               *    Fun Stuff - UI for Python"
        )
        a = input("\n\nPlease select (V) Version Control  (F) Future Updates   or <Enter> to return to the main menu:  ")
        if a == "f":
            future_updates()
        elif a== "F":
            future_updates()

            terms()
        if a == "V":
            version_control()
        elif a== "v":
            version_control()
        else:
            main_menu_1()

    version_menu()

def terms():
    ''''***********************************************************************************************************************
    *                                                               Terms                                                                *
    *************************************************************************************************************************'''

    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Terms   -----------------------------\n")

    def terms_page_1():
        title()
        print("               *    Polymorphism  "
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
        terms_Menu()

    def terms_page_2():
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
        terms_Menu()

    def terms_page_3():
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
        continue_lesson()
        terms_Menu()

    def terms_page_4():
        title()
        print("                 *   Dictionaries: "
              "\n                    -  \"Dictionaries are Python's implementation of a data structure that is more generally known as an associative array."
              "\n                          A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.\""
              "\n\n               *     While Loop:"
              "\n                     -   \"With the while loop we can execute a set of statements as long as a condition is true.\""
              "\n\n               *     For Loop:  "
              "\n                     -   \"A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).\""
              "\n\n               *     Difference between While and For Loop  "
              "\n                     -   \"With Python, you can use while loops to run the same task multiple times and for loops to loop once over list data..\""
              "\n\n               *     2d List:  "
              "\n                     -   \"A 2D array in Python is a nested data structure, meaning it is a set of arrays inside another array. "
              "\n                           The 2D array is mostly used to represent data in a tabular or two-dimensional formatA 2D array in "
              "\n                           Python is a nested data structure, meaning it is a set of arrays inside another array. "
              "\n                           The 2D array is mostly used to represent data in a tabular or two-dimensional format..\"\n"
              )
        continue_lesson()
        terms_Menu()

    def terms_page_5():
        title()
        print("                 *   Object-Oriented Programming: "
              "\n                     -   \"Python is a fantastic programming language that allows you to use both functional and object-oriented programming paradigms. "
              "\n                             Python programmers should be able to use fundamental object-oriented programming concepts, whether they are software developers, "
              "\n                             machine learning engineers, or something else\""
              "\n\n               *   Inheritance:"
              "\n\                     -   \"Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being "
              "\n                           inherited from, also called base class. Child class is the class that inherits from another class, also called derived class."
              "\n\n               *   Agile:"  
              "\n                     -   \"Agile is an iterative approach to project management and software development that helps teams deliver value to their "
              "\n                           customers faster and with fewer headaches. Instead of betting everything on a \"big bang\" launch, an agile team delivers "
              "\n                           work in small, but consumable, increments\".\n "
              "\n\n               *   Agile Team:"
              "\n                     -   \"An Agile Team is a cross-functional group of typically ten or fewer individuals with all the skills necessary to define, build, test,"
              "\n                            and deliver value to their customer (Project Manager, Teach Lead, Developers, QA\".\n "
              )
        continue_lesson()
        terms_Menu()


    def terms_page_6():
        title()
        print("                 *   Scrum: "
              "\n                     -   \"Scrum is a framework for project management commonly used in software "
              "\n                           development, although it has been used in other fields including research, "
              "\n                           sales, marketing and advanced technologie\""
              "\n\n              *  Jira:     "
              "\n                           \"Jira is a proprietary issue tracking product developed by Atlassian that allows"
              "\n                            bug tracking and agile project management\""
              "\n\n              *  Software Development Life Cycle:      "
              "\n                           \"Definition. The Software Development Life Cycle (SDLC) is a structured process"
              "\n                              that enables the production of high-quality, low-cost software, in the shortest possible"
              "\n                              production time. The goal of the SDLC is to produce superior software that meets and "
              "\n                               exceeds all customer expectations and demands\"\n"
              "\n                                       - Screen Shots          - Steps to reproduce    - Expected outcome"
              "\n                                       - Actual Outcome      - Logs                           -  Identifier of person who reported bug   \n "
              "\n              *  Fibonacci number:  "
              "\n                           \"Applications of Fibonacci numbers include computer algorithms such as the Fibonacci "
              "\n                            search technique and the Fibonacci heap data structure, and graphs called Fibonacci cubes"
              "\n                            used for interconnecting parallel and distributed systems.\"\n"
              )
        continue_lesson()
        terms_Menu()

    def terms_page_7():
        title()
        print("                 *   QA Skills: "
              "\n                     -    Decision-making skills."
              "\n                     -    Teamwork and collaboration"
              "\n                     -    Time management"
              "\n                     -     Knowledge of quality standards"
              "\n                     -     Apply automation testing.  "
    
              "\n\n              *  Software Development Life Cycle:      "
              "\n                           Defining quality assurance standards. Quality assurance standards are the policies and procedures "
              "\n                           an organization uses to ensure that its products and services meet the quality standards of its customers. "
              "\n\n                           These standards are set by management to evaluate the performance of their goods or service.\n"

              )
        continue_lesson()
        terms_Menu()

    def terms_Menu():
        title()
        print("(1)  Page 1 - Polymorphism,  Lists, Tuples ")
        print("(2)  Page 2 - Functions (Built in,  Recursion Functions , Lambda Functions, User-defined Functions )            ")
        print("(3)  Page 3 - Expression,  Return Statement,  If Statement:,  IF STATEMENT and Comparison ")
        print("(4)  Page 4 - Dictionaries , While Loop, For Loop, Difference between While and For Loop, 2d List       ")
        print("(5)  Page 5 - Object-Oriented Programming, Inheritance, Agile, Agile Team       ")
        print("(6)  Page 6 - Jira, Agile, Agile Team,  Software Development Life Cycle, Fibonacci number           ")
        print("(7)  Page 7 - QA Skills, Software Development Life Cycle:         ")
        a = input("\n\nPlease select Page ")
        if a == "1":
            terms_page_1()
        if a == "2":
            terms_page_2()
        if a == "3":
            terms_page_3()
        if a == "4":
            terms_page_4()
        if a == "5":
            terms_page_5()
        if a == "6":
            terms_page_6()
        if a == "7":
            terms_page_7()
        else:
            main_menu_1

    terms_Menu()

main_menu_1()