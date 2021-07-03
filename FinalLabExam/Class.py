
from random import choice
class PMethod:
    # Takes user inputted name and returns the val.
    def PlayerName(name):
        return name 

    # If user selected [a] Math will directly proceed to this function
    def Math(UName):
        total = 0
        print("You have chosen: Math!")
        Questions = ["5 x 5 is equal to?",
        "You are lying 120 ft away from a tree that is 50 feet tall. You look up at the top of the tree. Approximately how far is your hear from the top of the tree in a straight line?",
        "Sarah is twice as old as her youngest brother. If the difference between their ages is 15 years. How old is her youngest brother?",
        "What will it cost to tile a kitchen floor that is 12 feet wide by 20 feet long if the tile cost $8.91 per square yard?",
        "If y(x-1)=z then x="]

        #Utilize Dictioanry in accessing the choices with the use of Key-Value sys.
        Choices = {"1": ["a. 30","b. 350","c. 25"],"2":["a. 135 ft","b. 130 ft","c.190 ft"],"3":["a. 15","b. 20","c. 25"],"4":["a. $237.6","b. $230.5","c. 240"],"5":["a. z/y + 1","b. z = y + 1","c. y = 1 + z"]}
        Qanswer = ["c","b","a","a","a"]
        QNum = 1

        # Loop enumerating the the questions and the choices also Includes the user input option for the answer.
        # Checking also the correct answers and displaying the name and score
        for x in Questions:

            print("Question {}: {}".format(QNum,Questions[QNum-1]))
            print("\n".join(Choices[str(QNum)]))
            answer = input("Enter your Answer:")
            if x == Questions[0]:
                if answer == Qanswer[0]:
                    total = total + 20
                    print("Correct! Score: {}".format(total))
                else:
                    print("Sorry {}, Wrong Answer. Score {}".format(UName,total))
            elif x == Questions[1]:
                if answer == Qanswer[1]:
                    total = total + 20
                    print("Correct! Score: {}".format(total))
                else:
                        print("Sorry {}, Wrong Answer. Score {}".format(UName,total))
            elif x == Questions[2]:
                if answer == Qanswer[2]:
                    total = total + 20
                    print("Correct! Score: {}".format(total))
                else:
                    print("Sorry {}, Wrong Answer. Score {}".format(UName,total))
            elif x == Questions[3]:
                if answer == Qanswer[3]:
                    total = total + 20
                    print("Correct! Score: {}".format(total))
                else:
                    print("Sorry {}, Wrong Answer. Score {}".format(UName,total))
            elif x == Questions[4]:
                if answer == Qanswer[4]:
                    total = total + 20
                    print("Correct! Score: {}".format(total))
                else:
                    print("Sorry {}, Wrong Answer. Score {}".format(UName,total))
            else:
                print()
            if total == 100:
                print("Congratulations! You've got the perfect score!")
            QNum += 1
            
            
    # If user selected [b] History will directly proceed to this function
    def Histroy(UName):
        total = 0
        print("You have chosen: History!")
        Questions = ["What was the shortest war in human history?",
        "How long did the war between England and Zanzibar last?",
        "How many years did the 100 years war last?",
        "What was the name of the research ship Charles Darwin traveled with?",
        "In which year did Hitler commit suicide?"]

        Answers = ["The war between England and Zanzibar",
        "Between 38 & 45 minutes",
        "116 years",
        "The Beagle",
        "1945"]

        QNum = 1
        #Utilize Dictioanry in accessing the choices with the use of Key-Value sys.
        Choices = {"1": ["a. Pacquiao vs Mosley","b. The war between England and Zanzibar","c. Vietnam War"],"2":["a. Between 1 to 3 hours","b. Between 38 & 45 minutes","c. 10 minutes"],"3":["a. 15 years","b. 20 years","c. 116 years"],"4":["a. The Beagle","b. The Eagle","c. The Beetles"],"5":["a. 1945","b. 2000","c. 1888"]}
        Qanswer = ["b","b","c","a","a"]

        # Loop enumerating the the questions and the choices also Includes the user input option for the answer.
        # Checking also the correct answers and displaying the name and score
        for x in Questions:

            print("Question {}: {}".format(QNum,Questions[QNum-1]))
            print("\n".join(Choices[str(QNum)]))
            answer = input("Enter your Answer:")
            if x == Questions[0]:
                if answer == Qanswer[0]:
                    total = total + 20
                    print("Correct! Score: {}".format(total))
                else:
                    print("Sorry {}, Wrong Answer. Score {}".format(UName,total))
            elif x == Questions[1]:
                if answer == Qanswer[1]:
                    total = total + 20
                    print("Correct! Score: {}".format(total))
                else:
                        print("Sorry {}, Wrong Answer. Score {}".format(UName,total))
            elif x == Questions[2]:
                if answer == Qanswer[2]:
                    total = total + 20
                    print("Correct! Score: {}".format(total))
                else:
                    print("Sorry {}, Wrong Answer. Score {}".format(UName,total))
            elif x == Questions[3]:
                if answer == Qanswer[3]:
                    total = total + 20
                    print("Correct! Score: {}".format(total))
                else:
                    print("Sorry {}, Wrong Answer. Score {}".format(UName,total))
            elif x == Questions[4]:
                if answer == Qanswer[4]:
                    total = total + 20
                    print("Correct! Score: {}".format(total))
                else:
                    print("Sorry {}, Wrong Answer. Score {}".format(UName,total))
            else:
                print()
            if total == 100:
                print("Congratulations! You've got the perfect score!")
            QNum += 1
