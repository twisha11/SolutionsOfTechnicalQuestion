def is_palindrome(input_string):
    w = ""
    for i in input_string:
        w = i + w

    if (input_string == w):
        result = "Yes"
    else:
        result = "No"

    return result

# Example 1
input_string1 = "anna"
result1 = is_palindrome(input_string1)
print("Input : ",input_string1)
print("output : ", result1)

print("-------------------------------")
# Example 2
input_string2 = "India"
result2 = is_palindrome(input_string2)
print("Input : ",input_string2)
print("output : ", result2)

