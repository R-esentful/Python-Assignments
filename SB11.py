def GradeCalcu(Name,Math,Science,English):
    Gtotal = (int(Math) + int(English)+ int(Science))/3
    print("{}'s grade ( Math = {},Science = {},English = {} ) and the average is {:.2f}".format(Name, Math, Science, English, Gtotal))

GradeCalcu("Cooky",100,90,33)
GradeCalcu("Chimmy",98,80,95)
GradeCalcu("Tata",100,100,100)