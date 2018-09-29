#Q.1- Create a list with user defined inputs.
lst=list(input().split())
print(lst)
#Q.2 -Add the following list to above created list:
# ['google','apple','facebook','microsoft','tesla']
lst=lst+['smile','smile','apple','facebook','microsoft','tesla']
print(lst)
#Q.3- Count the number of time an object occurs in a list.
print(lst.count('smile'))
#Q.4 - Create a list with numbers and sort it in a ascending order.
lst2=[12,23,4,5,66,7,8,]
lst2.sort()
print(lst2)
#Q.5 - Given are two one-dimensional arrays A and B which are sorted in ascending order.Write a program merge them into a single
#sorted array C that contains every item from arrays A and B in ascending order. [List]
A=[1,3,5,7,9]
B=[2,4,6,8,10]
C=A+B
C= sorted(C)
print(C)
#Q.6 - Count even and odd numbers in that list.
lst3= [1,2,3,4,5]
no_even = 0
no_odd = 0
for i in lst3:
   if i%2==0:
      no_even+=1
   else:
         no_odd+=1
   print("Count of even numbers: "+str(no_even))
   print("Count of odd numbers: "+str(no_odd))
#Tuples
#Q.7 - Print a tuple in reverse order
tup= [1,2,3,4,5,6,7]
print(tup[::-1])
#Q.8 - Find Largest and Smallest elements in tuple.
tup = [1,2,3,4,5,6,7,8,9]
print("Largest:",max(tup),"Smallest:",min(tup))
#Strings
#Q.9 - Convert a string to uppercase
str1 = "pythen classes"
str1 = str1.upper()
print(str1)
#Q.10 - Print true if the string contain all numeric characters.
str2 = "12345"
print(str2.isnumeric())
#Q.11 - Replace the word "World" with your name in the string "Hello World"
str3 = "Hello World"
str3 = str3.replace("World","Ishita")
print(str3)

