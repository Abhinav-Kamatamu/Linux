a=int(input('enter value for a : '))
b=int(input('enter value for b : '))
c=int(input('enter value for c : '))
if (a+b>c and c+b>a and a+c>b):
    
    print ("possible")
else:
    print("not possible")