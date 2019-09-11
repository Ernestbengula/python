# python data types
#1. Number
#2.String
#3.Lists
#Tuples
#Dictionary
#Boolean
#Sets


##=========Numbers======
num1 =78 # int
num2 =45.7 # float
print(num1)
print(num2)


#=====String=======
name ="kim"
School ='Modcom'
print(name)
print(School)

#message ="my weight is" # string
weight = 56 # number
print("my weight is",weight)
print("The first number was", num2)


#=====Lists======
#lists are  like arrays
marks =[78,67,56,56,23,78.5,90,76.9,'']
prizes =['Book','Pen','Cash','Trip','Fees']
counties =['kisumi','Nakuru','Mombasa','Nairobi']
print(marks)
print(prizes)
print(counties)

#print by indexes from zero === e.g ==start from[0,1,2,3]
print(prizes[1])
print("i live in ", counties[3])


#=========tuple======
supamarkets =('Tuskeys','Naivas','Uchumi','Nakumatt')
cars =('Toyota','nissan','jeep',)
age =(21,13,40,11,22)
print("i do like ",supamarkets[2])
print("i do drive ",cars[1])
print("my sister is",age[4])

#=====Lists vs tuples====
counties.append("Embu")
counties.remove("nakuru")
print(counties)

#list are flexible/mutable/updated
#tuples are updable
cars .append("mazda") # cant work in tuples