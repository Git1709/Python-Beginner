marks = [10, 20, 30, 40, 50]
print(marks)
marks.append(20)
print(marks)
print (type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print("-------------------")
for mark in marks:
    print(mark)
marks.append([10, 20, 30, 40, 50])
print("-------------------")
for mark in marks:
    print(mark)
print("-------------------")
for mark in marks:
    if isinstance(mark,list):
        for list1 in mark:
            print(list1)
    else:
        print(mark)
print("-------------------")
print(marks[-3])
print(marks[len(marks)-3])
print("-------------------")
if 7 in marks:
     print("Yes")
else:
     print("no")
print("-------------------")
marks.append("Harry")
print("Harry" in marks)
print(marks)
if ("Harry") in marks:
    print("YES")


print("-------------------")
lst=[i for i in range (4)]
print(lst)
lst1=[i*i for i in range (4)]
print(lst1)
lst3=[i*i for i in range (4) if i%2==0]
print(lst3)