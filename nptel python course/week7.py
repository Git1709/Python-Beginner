print("Enter 4 integers, 1 in each line")
numbers = []
for i in range(4):
    numbers.append(int(input()))

matrix=[[],[]]
matrix[0] = numbers[:2]
matrix[1]= numbers[2:]

for row in matrix :
    for element in row:
        print(element, end=" ")
    print()
