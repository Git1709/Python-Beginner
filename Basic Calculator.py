print("Basic calculator\n")
print("Format : a (operator) b")
print("Operations Available are Addition(+),Subtraction(-),Multiplication(*),Division(/),Floor Division(//)")
a=int(input("Enter First Integer:"))
c=input("Enter Operator:")
b=int(input("Enter Second Integer:"))


if c=='+':
    result=a+b
elif c=='-':
    result=a-b
elif c=='*':
    result=a*b
elif c=='/':
    result=a/b
elif c=='//':
    result=a//b
else:print("Enter a Valid operator")


print("\n\nThe Answer is:",result)

