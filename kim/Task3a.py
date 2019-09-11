#Given 3 numbers ,check largest or equal.


x=float(input("Your Number"))
y =float(input("Your Number"))
z=float(input("Your Number"))

#Control structures -Making decision
#Check largest or equal


if x > y and x > z:
    print("x is the Largest")

elif y > x and y > z:
    print("y is the Largest")

elif z > y and z > x:
    print("is the Largest")

elif y==x and y==z:
    print("equal")

else :
    print("invalid")