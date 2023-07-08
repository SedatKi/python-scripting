lst = [i for i in range(1,51)]    #initialization of list 1-50

#For sum of even numbers 
even_lst = []                      #output list initialization for even numbers
for num in lst:
    if num % 2 == 0:               #Check for each lst element remainder to equal 0
        even_lst.append(num)   #append all elements meeting conditions in original list into new list
print('Even list is: ', even_lst)

sum_total = 0
for num in range(0, len(even_lst)):
    sum_total = sum_total + even_lst[num]
print("Sum of all even numbers is: ", sum_total)

#For product of odd numbers
odd_lst = []
for num in lst:
    if num % 2 != 0:
        odd_lst.append(num)
print('Odd list is: ', odd_lst)

product_total = 1
for num in range(0, len(odd_lst)):
    product_total = product_total * odd_lst[num]
print("Product of all odd numbers is: ", product_total)

#Finding the largest number
print("Entire list is: ", lst)
lst.sort()
print("Largest element is: ", lst[-1])