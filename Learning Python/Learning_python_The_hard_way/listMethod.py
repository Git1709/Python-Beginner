list1 = [1,2,3,4,5,6,7,8,9]

print(list1)
print(list1[0])
list1.sort(reverse=True)
print(list1)
list1.append([3,4,5,6,7,8,9,9])
print(list1)

for element in list1:
    if isinstance(element,list):
        for item in element:
            print(item)
    else:
            print(element)

list1.insert(1,[1,2,3,4,5,6,7,8,9])
print(list1)

for element in list1:
    if isinstance(element,list):
        for item in element:
            print(item)
    else:
            print(element)
list1.reverse()

print(list1)
l=[100,200,300,400,500]
c=list1+l
print(l)
print(c)