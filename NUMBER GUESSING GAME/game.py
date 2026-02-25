print()
print("--- WELCOME TO NUMBER GUESSING GAME---")
print()
print("---ARE YOU READY---")
print()
print("Think of a number between 0 and 100.")
print()
print("I will try to guess it!")
print()
print("Answer only with: yes / no")
print()
low = 0
high = 100

while low <= high:
    mid = (low + high) // 2

    print(f"\nIs your number {mid}?")
    answer = input().lower()

    if answer == "yes":
        print("Yay! I guessed your number!")
        break
    else:
        print(f"Is your number greater than {mid}?")
        hint = input().lower()

        if hint == "yes":
            low = mid + 1
        else:
            high = mid - 1