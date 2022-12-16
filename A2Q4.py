a=int(input("Enter 1st no."))
b=int(input("Enter 2nd no."))
c=int(input("Enter 3rd no."))
if a>c and a>b:
    print("Greatest no.=",a)
elif b>c and b>a:
    print("Greatest no.=",b)
else:
    print("Greatest no.=",c)