# Function for Count the Character in String
def count_char(input_string, target_character):
    count = 0
    for char in input_string:
        if char == target_character:
            count += 1
    return count


# Example 1
input_string1 = "geeksforgeeks"
target_character1 = 'e'
result1 = count_char(input_string1, target_character1)
print("Input : ", input_string1)
print("Charater : ",target_character1)
print("Output : ",result1)


print("-------------------------------------------")


# Example 2
input_string2 = "abccdefgaa."
target_character2 = '3'
result2 = count_char(input_string2, target_character2)
print("Input : ", input_string2)
print("Charater : ",target_character2)
print("Output : ",result2)
