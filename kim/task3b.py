
bmi = float(input("What is your bmi"))

#Control structures -Making decision
#if, if else,elif

if bmi >0 and bmi <=18.5:
    print("Thin")

elif bmi >=18.6 and bmi <=24.9:
    print("Healthy")

elif bmi >=25 and bmi <=29.9:
    print("Overweight")

elif bmi >=30:
    print("Obese")

else :
    print("no end")