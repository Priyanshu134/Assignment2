a=int(input("1st side"))
b=int(input("2nd side"))
c=int(input("3rd side"))
if a<b+c and b<a+c and c<a+b:
    print("Yes")
else:
    print("no")