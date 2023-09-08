from PC_1_1_Tools import *
def lesson_10():

    def title():
        new_page()
        print("\n                                -----------------------------    Lesson 10> Working with Lists   -----------------------------\n")

    def definition():
        title()
        print( "A Python list is an ordered and changeable collection of data objects. Unlike an array, which can contain objects"
               "\n of a single type, a list can contain a mixture of objects. \n\n\n\n\n")


        end()

    def EX1():
        title()
        print("                                    ****  Exercise 1 -  Creating a List    **** \n ")
        print("Were going to build a list called {Cars}.  Here is the format to enter a list: \n")
        print( "              Cars = [\"Mustang\", \"Camaro\", \"Challenger\", \"Pinto\", \"Pizza Car\", \"Shoe Car\", \"Ram\", \"F150\", \"F250\"]\n\n\n\n\n")



    def EX2():
        title()
        cord = (4, 5)
        print("                                    ****  Exercise 2 -  Printing a List   ****  ")
        Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
        print("\n Let's  print our list using using the command:  ")
        print("                              print(Cars)\n")
        print(str(Cars) + "\n\n\n\n\n")

    def EX3():
        title()
        Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
        print("                                    **** Exercise 3 - Printing individual items in a List ****")
        print("Here is the list we are working with  ----  " + str(Cars))
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


        print("\nHere is the output:")
        print("           " + Cars[0] + "             ---- Print 1st item in List  ")
        print("           " + Cars[1] + "              ---- Print 2nd item in List  ")
        print("           " + Cars[2] + "         ----  Print 3rd item in List  ")
        print("           " + Cars[3] + "                  ----  Print 4th item in List  ")
        print("           " + Cars[4] + "          ----  Print 5th item in List  ")
        print("           " + Cars[5] + "           ----  Print 6th item in List  ")
        print("           " + Cars[6] + "                  ----  Print 7th item in List  ")
        print("           " + Cars[7] + "                 ----   Print 8th item in List  ")
        print("           " + Cars[8] + "                 ----   Print 9th item in List  ")



    def EX4():
        title()
        Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
        print("                                    **** Exercise 4 - Printing individual items in a list  - Revers Order ****")
        print("Here is the list we are working with  ----  " + str(Cars))
        print("\nIf we put a minus in front of the number position, it will find the items in the list from last to first.")

        print("             print(Cars[-1])  --- Print last item in List    ")
        print("             print(Cars[-2])  --- Print 2nd to last item in List  ")
        print("             print(Cars[-3])  --- Print 3rd to last item in List  ")
        print("             print(Cars[-4])  --- Print 4th to last item in List  ")
        print("             print(Cars[-5])  --- Print 5th to last item in List  ")
        print("             print(Cars[-6])  --- Print 6th to last item in List  ")
        print("             print(Cars[-7])  --- Print 7th to last item in List  ")
        print("             print(Cars[-8])  --- Print 9th to last item in List  ")
        print("             print(Cars[-9])  --- Print 9th to last item in List  ")


        print(" \nHere is the output:")
        print("           " + Cars[-1] + "                             ---- Print last item in List  ")
        print("           " + Cars[-2] + "                             ---- Print 2nd to last item in List ")
        print("           " + Cars[-3] + "                             ----  Print 3rd to last item in List  ")
        print("           " + Cars[-4] + "                     ----  Print 4th to last item in List  ")
        print("           " + Cars[-5] + "                    ----  Print 5th to last item in List  ")
        print("           " + Cars[-6] + "                            ----  Print 6th to last item in List  ")
        print("           " + Cars[-7] + "                  ----  Print 7th to last item in List  ")
        print("           " + Cars[-8] + "                       ----  Print 8th to last item in List  ")
        print("           " + Cars[-9] + "                      ----  Print 9th to last item in List  ")


    def EX5():
        title()
        print("                                                     **** Exercise 5 - Printing Ranges in a List (First 2 items)****")
        Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
        print("\nHere is the list we are working with  ----  " + str(Cars))

        print("\n  Prints FIRST 2 items on the list    ")
        print("\n   Here is the code we are using::")
        print("                 print(Cars[:2])     -  prints FIRST 2 items on the list.\n")
        print("                                    " + str(Cars[:2]) + "\n\n\n\n")

    def EX6():
        title()
        print("                                    **** Exercise 6 - Printing Ranges in a List (3rd position to the 5th)****")
        Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
        print("\nHere is the list we are working with  ----  " + str(Cars))
        print("\n Print Range from the 3rd position to the 5th.     ")
        print("\n   Here is the code we are using:")
        print("                 print(Cars[2:5])     -  prints Range from the 3rd car to the 5th\n")

        print("                    Output -  " + str(Cars[2:5]) + "\n\n\n\n")



    def EX7():
        title()
        Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
        print("                                    **** Exercise 7 - Changing Items by Index Value  ****")
        print("\nHere is the list we are working with  ----  " + str(Cars))
        print("\nWe are going to change value in position 6 to \"Mouse\".  The command we are using:\n")
        print("         Cars[5] = \"Mouse\"")
        print("\n**** Before the Change ****")
        print(Cars)

        print("\n **** After the Change****")
        Cars[5] = "Mouse"
        print(Cars)
        print("\n\n\n\n\n")


    def EX8():
        title()
        Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
        print("                                    **** Exercise 8 - Combining 2 Lists using EXTEND Function****")
        print(
            "   We are going to combine 2 lists together using the EXTEND Function. Lets look at the lists format we entered: \n  ")

        print(
            "       Cars = [\"Mustang\", \"Camaro\", \"Challenger\", \"Pinto\", \"Pizza Car\", \"Shoe Car\", \"Ram\", \"F150\", \"F250\"]")
        print("       Numbers = [5, 21, 32, 52, 12, 22, 87]\n")
        print(" Now lets print the lists using the following commands:\n")
        print("             print(Cars)")
        print("             print(Numbers)\n")
        Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
        Numbers = [5, 21, 32, 52, 12, 22, 87]
        print("   List called \"Cars\" -               " + str(Cars))
        print("   List called \"Numbers\" -        " + str(Numbers))
        print(" Adding 2 Lists together using the EXTEND Function      \n")
        print("We are using the EXTEND function to combine the two list using the following command:\n")
        print("             Cars.extend(Numbers)")
        print("\n**** Before the EXTEND Function   ****")
        print(Cars)
        print("\n**** After the EXTEND Function   ****")
        Cars.extend(Numbers)
        print(Cars)

    def EX9():
        title()
        print("                                    **** Exercise 9 - Appending to a List  using Append Function****")
        Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
        print("We are going to add the value \"BMW\" to our \"Cars\" list by  Appending to a list using the APPEND function \n")
        print("The command we are using is:  ")
        print("             Cars.append(\"BMW\")")
        print("\n**** Before the APPEND Function   ****")
        print(Cars)



    def EX10():
        title()
        print("                                    **** Exercise 10 - Using the Insert Function  ****")
        Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
        print("   Inserting Ferrari to a list in position 5 using the INSERT function \n")
        print("Here is the command we are using:")
        print("Cars.insert(5, \"Ferrari\")")
        print("\n**** Before the INSERT Function   ****")
        print(Cars)
        print("\n**** After the INSERT Function   ****")
        Cars.insert(5, "Ferrari")
        print(Cars)


    def EX11():
        title()
        print("                                    **** Exercise 11 - Using the Remove Function  ****")
        Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]

        print(" Removing  Shoe Car from list using the REMOVE function.  Here is the command we are using:\n")
        print("       Cars.remove(\"Shoe Car\")")
        print("\n **** Before the REMOVE function ****")
        print(Cars)
        print("\n **** After the REMOVE function ****")
        Cars.remove("Shoe Car")
        print(Cars)
        a = input(" \nPress <Enter> for CLEAR Functions:  ")

    def EX12():
        title()
        print("                                    **** Exercise 12 - Using the Clear Function  ****")
        Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
        print("\n Removing ALL item from list using the CLEAR function  Here is the command we are using:")
        print("                             Cars.clear() ")
        print("\n **** Before the Change****")
        print(Cars)
        print("\n **** After the Change****")
        Cars.clear()
        print(Cars)

    def EX13():
        title()
        print("                                    **** Exercise 13 - Using the POP Function  ****")
        Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
        print("Because we used the CLEAR command in the previous section we first need to rebuild the list:")
        print(
            "Cars = [\"Mustang\", \"Camaro\", \"Challenger\", \"Pinto\", \"Pizza Car\", \"Shoe Car\", \"Ram\", \"F150\", \"F250\"]")
        print("\nNow lets print the list using the command ----    print(Cars)")
        print(Cars)
        print(" Next we'll Removing LAST item from list using the POP function:")
        print("\n **** Before the Change****")
        print(Cars)
        print("\n **** After the Change****")
        Cars.pop()
        print(Cars)
        input(" \nPress <Enter> for Finding Index value in list using INDEX:   ")

    def EX14():
        title()
        print("                                    **** Exercise 14 - Using the Index Function  ****")
        Cars = ["Mustang", "Camaro", "Challenger", "Pinto", "Pizza Car", "Shoe Car", "Ram", "F150", "F250"]
        print("Lets see the list again using the command  -     print(Cars)")
        print(Cars)
        print("\n Lets see the index value of Pinto using the command: \n")
        print("                     print(Cars.index(\"Pinto\"))")
        print("                          Output - " + str(Cars.index("Pinto")))



    def end():
        input("Press <Enter> to go to  Lesson Menu:  ")
        new_page()
        print("\n                                -----------------------------    Lesson Main Menu  -----------------------------\n")
        a = input("\n Please Select:  "
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run all Lessons "
                  "\n  (1)  Exercise 1 -  Creating a List  "
                  "\n  (2)  Exercise 2 -  Printing a List      "
                  "\n  (3)  Exercise 3 - Printing individual items in a list"
                  "\n  (4)  Exercise 4 -  Printing individual items in a list  - Revers Order"
                  "\n  (5)  Exercise 5 - Printing Ranges in a List (First 2 items) "
                  "\n  (6)  Exercise 6 - Printing Ranges in a List (3rd position to the 5th)"
                  "\n  (7)  Exercise 7 - Changing Items by Index Value"

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
            continue_lesson()
            EX4()
            end()

        if str(a) == "R":
            EX1()
            continue_lesson()
            EX2()
            continue_lesson()
            EX3()
            continue_lesson()
            EX4()
            end()


        if str(a) == "1":
            EX1()
            end()
        if str(a) == "2":
            EX2()
            end()
        if str(a) == "3":
            EX3()
            end()
        if str(a) == "4":
            EX4()
            end()
        if str(a) == "5":
            EX5()
            end()
        if str(a) == "6":
            EX6()
            end()
        if str(a) == "7":
            EX7()
            end()
        if str(a) == "8":
            EX8()
            end()
        if str(a) == "9":
            EX9()
            end()
        if str(a) == "10":
            EX10()
            end()
        if str(a) == "11":
            EX11()
            end()
        if str(a) == "12":
            EX12()
            end()
        if str(a) == "13":
            EX13()
            end()
        if str(a) == "14":
            EX14()
            end()

        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()

