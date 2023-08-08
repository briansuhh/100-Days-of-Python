def prime_checker(number):
    is_prime = 1
    if number == 0 or number == 1:
        is_prime = 0

    for i in range(2, number):
        if number % i == 0:
            is_prime = 0
            break

    if is_prime == 1:
        print("It's a prime number.")
    elif is_prime == 0:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(n)