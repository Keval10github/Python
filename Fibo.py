a=1
b=0
c=0
n = int(input("Enter value of n = "))

i=1

while i<=n:
    print(c,end=" ")

    c=a+b
    a=b
    b=c

    i=i+1