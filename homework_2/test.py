special_characters = "#$%^&*()-+?_=,<>/!@*\."
s = input()
# Example: $tackoverflow

if any(char in special_characters for char in s):
    print("yes")
else:
    print("no")