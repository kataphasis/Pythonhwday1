def add(g, h):
    return g + h
def subtract(g, h):
    return g - h
def multiply(g, h):
    return g * h
def divide(g, h):
    return g / h
print("Select")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
choice = input("Enter choice: ")
num_1= float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == 'd':
    if num_2 == 0.0:
        print("Division error")
    else:
        print(num_1, "/", num_2, divide(num_1, num_2))