n = int(input("Enter an integer: "))

if n < 2:
    print(n, "is not a prime number.")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")
