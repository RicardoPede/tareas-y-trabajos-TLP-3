def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            temp = result
            for j in range(1, i):
                temp += result
            result = temp
        return result

num = int(input("Ingresa un número: "))
print(factorial(num))
