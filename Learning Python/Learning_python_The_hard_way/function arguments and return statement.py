#Defines a default case for the function if no parameters eneterd
def average(a=9,b=1):
    print("---------------")
    print((a+b)/2)
def name(fname,lname="Sharma",mname="Sanju"):
    print("---------------")
    print(fname,mname,lname)


# no boundation to number of inputs
def average1(*numbers):
    print("---------------------")
    sum=0
    for i in numbers:
        sum=sum+i
    print(sum/len(numbers))

average()
#Overrides the default parameters
average(1,3)
#To change the order
average(b=3,a=1)
#can only override a single parameter
average(b=10)


name("Rachit")

average1(1,2,3,4,5,6,7)

# '**' in parameter to define a dictionary type input
def name1(**name):
    print("---------------")
    print(type(name))
    print("Hello",name["fname"],name["lname"])
name1(fname="Rachit", lname="Tejpal " ,mname="Sanju" )

def returnaverage(*numbers):
    print("---------------------")
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

A=returnaverage(1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print(A)