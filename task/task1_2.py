def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

number = int(input("Enter a number: "))

if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")