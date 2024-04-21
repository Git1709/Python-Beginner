L = input().split(',')

real_dict = dict()

for word in L:
    start = word[0]
    if start not in real_dict:
        real_dict[start] = [ ]
    real_dict[start].append(word)
for key, value in real_dict.items():
    print(f'{key}:{",".join(value)}')





def sorting(z):
    l=len(z)
    for i in range(l):
        for j in range(i+1,l):
            if z[i] > z[j]:
                z[i], z[j] = z[j], z[i]
    print(z)
L=list(input())
sorting(L)
x=int(input())
L.append(x)
sorting(L)
