tuple1 = ("apple", "banana", "hello", True, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
print(tuple1)

tuple2 = ("apple", "banana", "")
list1 = list(tuple1)
print(list1)
print(tuple2.count("banana"))
print(tuple2.index("banana"))
print(tuple1.index(True, 3, 7))
print(len(tuple1))