# to declare a tuple of 1 input only then ',' is necessary
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ("a",)
tuple3 = tuple1 + tuple2
print(tuple3, type(tuple3))
# in list lis[0]=90 whould have changed the 1st element to 90 but tuple will throw error if tuple1[0]=90 is passed
print(tuple3[0])
print(tuple3[1])
print(tuple3[2])
print(tuple3[3])
print(tuple3[-1])  # will print (length-1)th element
print("------------------------")
print(len(tuple3))
print(tuple3[5])
print(tuple3[6 - 1])
print(tuple3[-1])
print("------------------------")
if 2 in tuple3:
    print("Yes it is present in tuple")
print("------------------------")
# tuple slicing creates new tuple and won't modify old one
print(tuple3[1:4])
print(tuple3[1:-1])
print(tuple3[1:-2])
tuple2 = tuple3
print(tuple2)
