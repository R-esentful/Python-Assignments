frate = 500
tax = .12

def Gross(Hour):
     return Hour * frate

def Tax(Hour):
    return (Hour * frate) *.12

def printVal(Hour):
    print("Gross Salary:{}".format(Gross(Hour)))
    print("Tax:Php {}".format(Tax(Hour)))


