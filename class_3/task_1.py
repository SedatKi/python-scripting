lst = ["zero", "one", "two", "three", "four", "five", "six"]

print("The original list is: " + str(lst))

reverse_string = [i[::-1] for i in lst]

reverse_string.append("seven")

print ("The reversed string list is : " + str(reverse_string))