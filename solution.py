def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


n = int(input("Enter number : "))
var1 = [str(fibonacci(i)) for i in range(0, n+1)]
print(",".join(var1))
