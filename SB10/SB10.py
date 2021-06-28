import GrossSalary as GS
import NetSalary as NS
import SalaryDeduction as SD

def Main():
    name = input("Name:")
    hour = int(input("Hour:"))

    GS.Gross(hour)
    GS.Tax(hour)
    GS.printVal(hour)

    Loan = int(input("Loan: Php "))
    Insurance = int(input("Insurance: Php "))

    SD.SalaryDeduction(hour,Loan,Insurance)
    SD.deduction(hour,Loan,Insurance)

    NS.NetSalary(hour,Loan,Insurance)

Main()