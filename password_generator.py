import random
import string

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Generate pass
password_chars = (
    [random.choice(string.ascii_letters) for _ in range(nr_letters)] +
    [random.choice(string.punctuation) for _ in range(nr_symbols)] +
    [random.choice(string.digits) for _ in range(nr_numbers)]
)

# Shuffle
random.shuffle(password_chars)
password = "".join(password_chars)

print(f"Your password is {password}")