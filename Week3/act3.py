class Factorial:
    
    def factorial(num1):                                                    # Factorial method takes num1 as a parameter
        result = 1                                                          # Initialized before the loop to store the product.
        for i in range(1, num1 + 1):
            result *= i
        return result

    def check_prime(num1):                                                  # Prime check method takes num1 as a parameter
        if num1 < 2:                                                        # 0 and 1 are not prime numbers
            return False
        for i in range(2, int(num1 ** 0.5) + 1):                            # Check up to the square root of num1
            if num1 % i == 0:                                               # Check if num1 is divisible by i
                return False
        return True

    def display(num1):                                                      # Display method takes num1 as a parameter
        print("Factorial of", num1, "is", Factorial.factorial(num1))
        if Factorial.check_prime(num1):
            print(f"{num1} is a prime number.")
        else:
            print(f"{num1} is not a prime number.")

Factorial.display(10)                                                       # Call the display method   
#132               