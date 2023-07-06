string = "The cat is black, and it likes to sleep on the mat. Its name is Max."
string_length = (len(string))
if string_length < 100:
    word1 = string[:3]
    if (len(word1)) < 5 and (len(word1)) > 2:
        print('Success!')
    else:
        print('Your word does not meet the requirement')