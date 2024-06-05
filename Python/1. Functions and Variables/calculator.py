"""
x = 1
x = input("What's x? ")
x = int(input("What's x? "))
x = float(input("What's x? "))
y = 2
y = input("What's y? ")
y = int(input("What's y? "))
y = float(input("What's y? "))

z = x + y
z = int(x) + int(y)
z = round(x + y)
z = x / y
z = round(x / y, 2)

print(z)
print(x + y)
print(f"{z:,}")
print(f"{z:.2f}")

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(f"{z:.2f}")
"""

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    # return n * n
    # return n ** 2
    return pow(n, 2)

main()