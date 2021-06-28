import GrossSalary as GS
import SalaryDeduction as SD

def NetSalary(Hour,Loan,Insurance):
    Gross = GS.Gross(Hour)
    Deduction = SD.deduction(Hour,Loan,Insurance)
    total = Gross - Deduction
    print("Net Salary: Php {}".format(total))
