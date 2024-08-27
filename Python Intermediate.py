def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

while True:
    user_input = input("Enter a number to check if it's prime (or 'all' to find all primes up to a number): ").strip()

    if user_input.isdigit():
        number = int(user_input)
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    elif user_input.lower() == 'all':
        limit = int(input("Enter the upper limit to find all prime numbers up to: ").strip())
        primes = find_primes_up_to(limit)
        print(f"Prime numbers up to {limit}: {primes}")
    else:
        print("Invalid input. Please enter a valid number or 'all'.")

    check_again = input("Do you want to check another number? (yes/no): ").lower()
    if check_again != "yes":
        break

print("Thanks for using the prime number checker! Goodbye!")