import random

def Main():

    user = set()
    winning = set()
    matched = set()
    count = 0


    #For checking of the winning combination
    #for x in range(6):
    #    b = random.randint(1,50)
    #    winning.add(b)
    #print(winning)   

    print("Enter your 6 numbers from 1-50 , one at a time!")

    for x in range(6):
        x = int(input())
        user.add(x)
    for x in range(6):
        b = random.randint(1,50)
        winning.add(b)
             

    for x in user:
        for y in winning:
            if x == y:
                matched.add(x)
                count +=1

    user = str(user)[1:-1]
    winning = str(winning)[1:-1]
    matched = str(matched)[1:-1]
    match_chcker = len(matched)

    print("Your Lotter Numbers: {}".format(user))
    print("Winning Numbers: {}".format(winning))

    if(match_chcker == 0):
        print("Matched: None")
    else:
        print("Matched: {}".format(matched))
    
    if count == 6:
        print("Congratulation, You Won!")
    else:
        print("Sorry, You lose!")
    

Main()
