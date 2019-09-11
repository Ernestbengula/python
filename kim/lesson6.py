
def area(r): #r is an unknown parameter
   # r =5
    pi =3.14
    answer =pi*r*r
    print("area of Circle is",answer)

# call
#area()

def si(p,r,t):
    answer =(p*r*t)/100
    print("Your answer is", answer)




def Net_Pay(N,H,F,S,D):
    answer =((H*N)*F)-(S*(H*N)(F-S)+(H+N))
    print("Your Net_Pay", answer)
    print(" Ernte Your Full Name")
Net_Pay(N=float(input("Your Number of Hours Worked in a week"))
        ,H=float(input("Your Hourly_pay_Rate i.e $6.75"))
        ,F=float(input(" Your Federal_Tax_withholding"))
        ,S=float(input("State_Tax_Withholding"))
        ,D=float(input("Your Deductions")))

