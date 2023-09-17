def swap_numbers(a, b):
    a,b=b,a
    return a, b

# Example
a = 10
b = 50

print("Before Swap ")
print("a =", a)
print("b= ", b)

print("-------------------------")

# Swapping using a third variable
a, b = swap_numbers(a, b)


# Print the result
print("After Swap ")
print("a =", a)
print("b =", b)
