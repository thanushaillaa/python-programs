def my_function(n):
    if n==0:
        return 0
    return my_function(n-1)+n
n=int(input("enter n value: "))
answer = my_function(n)
print(answer)