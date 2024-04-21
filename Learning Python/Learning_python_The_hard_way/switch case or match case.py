x=4
match x:
    case 0:
        print("x is zero")
    case 12:
        print("x is 12")

    case 4:
        print("x is 4")
    case _:
        print("This is for default case")
y=90
match y:
    case 0:
        print("y is zero")
    case 4 :
        print("y is 4")
    case 2:
        print("y is 2")
    case _ if (y == 50):
        print("y is  50")
    case _ if(y!=90):
              print("y is not 90")
    case _:
        print("WTH did u entered")

