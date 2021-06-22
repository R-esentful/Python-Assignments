def List():
    words = []
    word_checker = 0
    choice = 'y'
    while choice == 'y' or choice == 'Y':
        word_input = []
        word = input("Enter a word:")
        word_input.append(word)
        word_checker +=1
        for x in word_input:
            words.append(x)
        choice = input("Try again? [Y/y] or [N/n]:")
    print("Inputted words:{}".format(words))
    print("Total number of words:{}".format(word_checker))


List()
