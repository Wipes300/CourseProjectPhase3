#
#
#
from datetime import datetime ########################

def GetEmpName():
    empname = input("Enter employee name:  ")
    return empname
def GetDatesWorked():
    fromdate = input("Enter Start Date  (mm/dd/yyyy: ")
    todate = input("Enter End Date (mm/dd/yyyy:  ")
    return fromdate, todate
def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate  "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input("Enter tax rate:"))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax * grosspay * incometax
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo():
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
#################################################

    while True:
        rundate = input ("Enter start date for report (MM/DD/YYYY) or ALL for all data in file: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format.  Try again")
            print("\n")
            continue # skip next if statement and re-start loop
        while True:
           EmpDetail = EmpFile.readline()
           if not EmpDetail:
               break



