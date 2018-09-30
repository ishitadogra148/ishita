#Q.1- Reverse the whole lst using list methods.

lst=['ishita','dogra',12,34,'shoolini']
lst.reverse()
print(lst)

#Q.2- Print all the uppercase letters from a string.

s=("Pythen Classes")
for i in s:
    if i==i.upper():
        print(i,end=',')

#Q.3- Split the user input on comma's and store the values in a list as integers.

x=list(input("enter the no. of elements:").split(","))
print(x)

#Q.4- Check whether a string is palindromic or not.

s=input("enter the string")
if s[::-1]==s:
    print("it is palindrome:")
else:
    print("it is not palindrome")


#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.

import copy

old_list = [[0, 0, 0], [2, 2, 2], [4, 4, 4]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)  
