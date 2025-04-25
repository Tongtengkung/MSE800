number = input("input value(PLEASE PUT INTENGER NUMBER):")

n = float(number)
n = round(n)
def factorial(n):
    if n < 0:
        return "Unidentify number lower than zero"

    elif 0 < n <= 1:
        return 1


    else:
        n = factorial(n-1)*n
        return n
    

print(factorial(n))