num = int(input("enter num value: "))
factorial = 1
if num<0:
    print("factorial doesnt exit for negative numbers")
elif num == 0:
    print("factorial of zero is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("factorial of",num,"is",factorial)