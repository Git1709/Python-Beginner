x= int(input(""))

for i in range (1,x+1):
    if i%3==0 and i%5==0:
        print(i,"=FizzBuzz")

    elif i%3==0:
        print(i,"=Fizz")

    elif i%5==0:
        print(i,"=buzz")
    else:
        print(i)
print("\n\n\n\n\n\n\n\n\n")
def fizzbuzz(range_val):
    for i in range(1, range_val+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i,"=FizzBuzz")
        elif i % 3 == 0:
            print(i,"=Fizz")
        elif i % 5 == 0:
            print(i,"=Buzz")
        else:
            print(i)

# Call the function with the desired range
fizzbuzz(50)