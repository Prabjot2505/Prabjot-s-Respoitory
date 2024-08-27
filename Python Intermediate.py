def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(2, int(n**0.5) + 1):
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
    choice = input("Would you like to check if a number is prime or find all primes up to a certain number? (check/find): ").lower()

    if choice == "check":
        number = int(input("Enter a number to check if it's prime: "))
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    
    elif choice == "find":
        limit = int(input("Enter the upper limit to find all prime numbers up to: "))
        primes = find_primes_up_to(limit)
        print(f"Prime numbers up to {limit}: {primes}")
    
    else:
        print("Invalid choice. Please enter 'check' or 'find'.")
        continue

    play_again = input("Do you want to perform another operation? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for using the Prime Number Checker! Goodbye!")
