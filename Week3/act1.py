class Factorial:
    def __init__(self, n):
        self.n = n

    def calculate(self):
        if self.n < 0:
            return "Unidentify number lower than zero"

        elif 0 < self.n == 1:
            return 1

        else:
            result = 1
            for i in range(1, self.n + 1):
                result *= i
            return result

number = input("input value(PLEASE PUT INTENGER NUMBER):")
n = int(number)

factorial = Factorial(n)
print(f"Factorial of {n} is {factorial.calculate()}")

class Prime:
    def __init__(self, n):
        self.n = n

    def is_prime(self):
        if self.n < 2:
            return False
        for i in range(2, int(self.n ** 0.5) + 1):
            if self.n % i == 0:
                return False
        return True

prime = Prime(n)
print(f"{n} is prime: {prime.is_prime()}")