def List():
    words = []
    counter = False
    word_checker = 0
    while counter == False:
        user_input = input("Enter a Word:")
        words.append(user_input)
        word_checker += 1
        choice = input("Try again? Y/y or N/n:")
        user_choice = choice.casefold()
        if user_choice == 'y':
            counter = False
        elif user_choice == 'n':
            counter= True
            print("Inputted Words ",words)
            print("Total number of words:{}".format(word_checker))
        else:
            print("Invalid choice!")



List()