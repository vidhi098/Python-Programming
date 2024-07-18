a = [1, 2, 3]
try:
    print("Second element =", a[1])

    # Attempting to access an element out of range
    print("Fourth element =", a[3])
except IndexError:
    print("An error occurred: Index out of range")

print()

b = [3, 2, 1]
try:
    if a == b:
        print("Both Equal")
    else:
        print("They are not equal")
except Exception as e:
    print(f"An error occurred: {e}")

print()

try:
    k = 5 / 0
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print('This is always executed')
