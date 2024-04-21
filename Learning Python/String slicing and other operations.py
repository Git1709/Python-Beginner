s="hello it is a string here"
print(s)
print("Printing the elements from 0 to n-1, here n=5: ",s[0:5])# include 0 not 5
print("Printing the elements from 5 to 9:",s[5:10])# include 5 not 10
print("from 1st element to the element which is 3 steps away from end:",s[0:-3])
print("",s[3:-1])#removes last element from the string
print("",s[-3:-1])#it wont print

a="Hello World"
print(a)
b="!!!!!!!!!!!!!!!!!!Hello World war 2!!!!!!!!!!!!!!"
print(len(a))
print(a.lower())
print(a.upper())
print(b.rstrip("!"))
print(b.lstrip("!"))
print(b.rstrip("!").lstrip("!"))
print(b.strip("!"))

c="introduction to js. hello world"
print(c.capitalize())
print(c.center(50))
print(c.capitalize().center(50)+"hello world")
print(len(c))
x=c.center(50)
print(len(x))
print(s.replace("hello","world").center(50))
