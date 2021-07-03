import os 
import sys
sys.path.append(".")
#class.py import to utilize or access other function on the python program.
from FinalLabExam.Class import PMethod as PM

class Main:
    #Main method for the program
    def MMethod():
        #UserInput for name
        user_input = input("Enter your name:")
        #Setting the name
        PM.PlayerName(user_input)

        print("Welcome {}! Please choose a category.".format(PM.PlayerName(user_input)))

        #Choosing the category for the program. 
        Category = input("[a] Mathemathics \n[b] History \nEnter your choice:")
        if Category =='a' or Category == 'A':
            PM.Math(user_input)
        elif Category == 'b' or Category == 'B':
            PM.Histroy(user_input)
        else:
            print("Invalid Choice!")

Main.MMethod()
