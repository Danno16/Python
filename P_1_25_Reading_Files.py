
from PC_1_1_Tools import *

def lesson_25():
    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 25  - Working with Files    -----------------------------\n")

    def definition():
        title()
        print(
            "Files are very powerful.  It is like a dictionary but outside of python.  The information is held in a Text file like a Table in a database."
            "\nIn this lesson we are going to be be working with files.  We are going to:\n"


            "\n                              Objectives of Lesson                                                     List Modes "
            "\n             - Create a Text (txt) file using python code                               \"r\"   =  Read   "
            "\n             - Append to the text file                                                             \"a\"  =  Append    "
            "\n             - Input Variables and add to the list                                          \"w\" =  Write    "
            "\n             - Check to see if the file is readable                                          \"c\"  =  create    "
            "\n             - Read the file one at a time"
            "\n             - Read the first three lines of the file"
            "\n             - Read the file as an list   "
            "\n           - Create for loop to read all the items in a file   \n")

        input("press <Enter> for Menu")
        end()

    def read_file():
        Test_file1 = open("Test_File_1.txt", "r")
        print(Test_file1.read())
        Test_file1.close()

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

        print(
            "                                 1               a1 = input(\"Please enter the first line to enter into our text file:  \")    ")
        print(
            "                                 2               a2 = input(\"Please enter the second line to enter into our text file:  \")   ")
        print(
            "                                 3               a3 = input(\"Please enter the Third line to enter into our text file:  \")   ")
        print(
            "                                 4               a4 = input(\"Please enter the forth line to enter into our text file:  \")   ")

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
        print(
            "In this exercise we are going to add (APPEND) to the file. In the previous file we did a WRITE which means "
            "\nwe wiped out the table and added new data.  APPEND is when we add data to the existing data."
            " \n\n Were going to OPEN the file, APPEND the file, READ the file, then CLOSE the file. \n")

        print("                 Here is the code:")

        print(
            "                         1           First_Input_Addition = input(\"Add another line to our text file.  :  \")   ")
        print(
            "                         2           Second_Input_Addition = input(\"Add second line to our text file   :  \")  ")
        print(
            "                         3           Third_Input_Addition = input(\"Add third line to our text file :    \")  ")

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
        print(
            "                                                      Exercise 4 - Checking to see if the file is readable in APPEND mode \n ")
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
        print(
            "                                                      Exercise 5 - Checking to see if the file is readable in READABLE mode \n ")
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
        print(
            "                                     2       print(Test_file1.readlines()) - notice the \"S\" after readline")
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
        print(
            "                                     5       print(Test_file1.readlines()[3])    ---   To run the 4th position\n")

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
        print(
            "                                                                                                  Menu of Exercises")
        print(
            " --------------------------------------------------------------------------------------------------------------------------------------------------------------------")
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
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()
