import GrossSalary as GS

def SalaryDeduction(Hour,Loan,Insurance):
    LAmmount = Loan
    IAmmount = Insurance
    Taxed = GS.Tax(Hour)
    TotalDeduction = LAmmount + IAmmount + Taxed
    print("Total Deduction:Php {}".format(TotalDeduction))

def deduction(Hour,Loan,Insurance):
    LAmmount = Loan
    IAmmount = Insurance
    Taxed = GS.Tax(Hour)
    return LAmmount + IAmmount + Taxed


