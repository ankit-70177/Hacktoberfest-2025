# multiplication_table.py
# A simple program to print multiplication table of any number.

print("🧮 Multiplication Table Generator")

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
