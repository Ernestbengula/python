# create a payroll
#Gross_Pay
salary =float(input("Enter  salary"))
wa =float(input("Enter wa"))
ha=float(input("Enter ha"))
ta =float(input("Enter ta"))
Gross_Pay =(salary+wa+ha+ta)
print("Gross Pay ", Gross_Pay)


#Deduction
NSSF =float(input("Enter NSSF"))
Tax =float(input("Enter Tax"))
Deductions=(NSSF+Tax)

print("Deductions: ", Deductions)

#formula Net_Pay =Gross_Pay-Deduction

Net_pay =Gross_Pay-Deductions
print("Your net_pay",Net_pay)
