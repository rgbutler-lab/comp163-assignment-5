#Challenge 1: Number sequence generator:
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter a positive integer: "))
step_count = 0

print(f"Sequence: {current_number}", end=" ")
# It will only stop once equal to 1
while current_number != 1:
    if current_number >= 0:
        #Even number
        if current_number % 2 == 0:
            current_number //= 2
        #Odd number
        else:
            current_number = 3 * current_number + 1
        print(f"{current_number}", end=" ")
        step_count += 1

print(f"\nSteps: {step_count}")
print("")

#Challenge 2: Prime number tester:
print("=== Challenge 2: Prime Number Tester ===")
n = int(input("Enter a number greater than 1: "))
print(f"Testing divisors from 2 to {n - 1}...")

# Check divisibility from 2 to n-1
for divisor in range(2, n):
    # Check if is not prime
    if n % divisor == 0:
        print(f"{n} is not prime (divisible by {divisor})")
        break
# Check if is prime
else:
    print(f"{n} is prime!")

