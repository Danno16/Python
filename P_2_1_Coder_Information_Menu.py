from PC_1_1_Tools import *
from math import *



def Coder_main_menu_1():            #                Main Menu Screen
    new_page()
    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n                  --------------------------------           Programming Notes            --------------------------------    \n")
    print( "  (1) - Version Control  "
           "\n  (2) - Future Updates                  "
           "\n  (3) - Coding Terms")

    a = input("\nSelect Item or <Enter> for Main Menu:  ")

    if str(a) == "1":
            import P_2_2_Version_Control
            P_2_2_Version_Control.version_menu()

    if str(a) == "2":
            import P_2_3_Future_Updates
            P_2_3_Future_Updates.future_updates()

    if str(a) == "3":
            import P_2_4_Coding_Terms
            P_2_4_Coding_Terms.terms_page()()

    else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1



