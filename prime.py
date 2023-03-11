

def is_prime(n):
    if n < 2:
        return False
    else:
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        return prime


num = int(input("Enter an integer: "))
print(is_prime(num))
