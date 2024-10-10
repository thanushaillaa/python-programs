a=int(input("enter a value: "))
b=int(input("enter b value: "))
c=int(input("enter c value: "))
 
if(a>=b) and (a>=c):
    largest=a
elif(b>=c) and (b>=a):
    largest=b
else:
    largest=c
print("the largest number is", largest)