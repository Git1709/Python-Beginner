def hello_world(name):
    print("Hello",name)
    print()
#To pass the code for currently and may return to complete it later
def passing():
    pass

def mean(a,b):
    print((a*b)/(a+b))
def greater(a,b):
    if(a>b):
        print("Greatest is",a)
    elif(a==b):
        print(a,"=",b)

    else:
        print("Greatest is",b)

hello_world("Rachit")
mean(5,1)
greater(2,2)
greater(2,-2)