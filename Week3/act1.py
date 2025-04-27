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