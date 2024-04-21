text = input().lower()
length = len(text)
def output_string(x):
    print("Mine")
    x=x.lower()
    x_list=list(x)

    print(x_list)
    print(type(x_list))

    y_list= x_list.sort()
    y_list = ''.join(x_list)
    print((y_list).strip())


def swayam(x):
    print("Swayam")
    x = x.lower()
    x_list = list(x)
    new_string = ''
    print(x_list)
    print(type(x_list))
    for bit in 'abcdefghijklmnopqrstuvwxyz':
        for i in range(len(x_list)):
            if bit == x[i]:
                new_string += bit
    print(new_string)

text = "Example Text"
swayam(text)

output_string(text)
