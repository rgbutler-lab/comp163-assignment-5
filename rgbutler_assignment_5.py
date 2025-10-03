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

