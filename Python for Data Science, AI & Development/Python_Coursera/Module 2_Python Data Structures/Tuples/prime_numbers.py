def find_primes(count):
    primes_list = []  # List to store prime numbers
    num = 2           # Start checking from the first prime number

    while len(primes_list) < count:
        # Check if num is a prime
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            primes_list.append(num)
        
        num += 1

    # Convert the list to a tuple
    primes_tuple = tuple(primes_list)
    return primes_list, primes_tuple

# Find the first 10 prime numbers
primes_list, primes_tuple = find_primes(10)

print("Prime numbers as a list:", primes_list)
print("Prime numbers as a tuple:", primes_tuple)
