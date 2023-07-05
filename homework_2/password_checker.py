password = input('Enter a password: ')
password_len = len(password)
special_chars = "#$%^&*()-+?_=,<>/!@*\."
if password_len >= 8 \
    and any(char.islower() for char in password) == True \
    and any(char.isupper() for char in password) == True \
    and any(char.isdigit() for char in password) == True \
    and any(char in special_chars for char in password) == True:
    print("Password success!")
else:
    print("Password fail")