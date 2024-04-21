import random
names=['John','Smith','Srijan','mehul','paras','alok','aayush','ansh','raju']
with open("C:\\Users\\rachi\\PycharmProjects\\Learning Python\\NptelProjects\\New.txt","r+") as file1:
    print(file1.read())
    x = random.choice(names)
    z= x.rjust(50).rstrip(" ")
    chu="chimera"
    file1.write(f"\n{z}  {chu}")
    print(file1.read())
    n=random.randrange(1,10)
    m=random.randint(1,10000)
    print(m)
    file1.write(f"      {m}     {n}")


