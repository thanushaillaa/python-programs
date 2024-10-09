a = float(input("enter a value: "))
b = float(input("enter b value: "))
c = float(input("enter c value: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5

#print('area of triangle is %0.4f' %area)

area_rounded=round(area,4)
print(area_rounded)