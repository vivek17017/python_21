"""
#Q1
n=int(input("Enter N"))
for e in range(1,n+1):
    print(2*e)

    
#Q2
n=int(input("Enter N"))
for e in range(1,n+1):
    print(2*e-1)
    
#Q3
n=int(input("Enter N"))
for e in range(1,n+1):
    print(e**2)


#Q4
n=int(input("Enter N"))
for e in range(1,n+1):
    print(e**3)


"""

#Q5
print("Enter range ")
a,b=int(input()),int(input())
print()
for e in range(a,b):
    y=0
    for i in range(1,e+1):
        if e%i==0:
            y+=1
    if(y==2):
        print(e,end=' ')



