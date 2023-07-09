def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    """Find prime numbers within a given range."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

prime_numbers = find_primes(start_num, end_num)
print("Prime numbers between", start_num, "and", end_num, "are:")
print(prime_numbers)
