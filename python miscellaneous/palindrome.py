"""5. Implement a function that checks if a given string is a palindrome."""

def palindrome(name):
    new_name=""
    for char in name:
        new_name=char + new_name
    if new_name==name:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")

a_name=input("enter a string:")
palindrome(a_name)