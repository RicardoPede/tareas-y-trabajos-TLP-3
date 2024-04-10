def sum(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))
print(sum(num1, num2))