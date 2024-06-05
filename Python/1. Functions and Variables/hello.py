"""
print("hello, world")
print("hello, world" # SyntaxError: '(' was never closed

# Ask user for their name
print("What's your name? ")
name = input("What's your name? ")
name = input("What's your name? ").strip().title()

# Remove whitespace from str
name = name.strip()

# Capitalize user's name
name = name.capitalize()
name = name.title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print("hello,")
print(name)
print("hello, " + name)
print("hello,", name)
print("hello, ", end="???")
print(name)
print("hello,", name, sep="???")
print("hello, "friend"") # SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('hello, "friend"')
print("hello, \"friend\"")
print(f"hello, {name}")
print(f"hello, {first}")

# Ask user for their name
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

print(f"hello, {first}")

def hello(to="world"):
    print("hello,", to)

hello()
name = input("What's your name? ")
hello(name)
"""

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()