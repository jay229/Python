# How to read multiple values from the keyboard in a single line:
a, b = [int(x) for x in input("Enter 2 numbers :").split(",")]
print(a*b)
