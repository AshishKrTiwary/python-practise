# Generate code for lambda Anonymous function in Python that processes 
#lambda arguments and returns a value.

x=lambda a: a*a
x(3)
# This lambda function takes one argument 'a' and returns its square.

def A(x):
    return(lambda y: x + y)
t=A(4)
print(t(5))
# This code defines a function A that takes an argument x and returns a lambda function.
# The returned lambda function takes another argument y and returns the sum of x and y.

# When we call A(4), it returns a lambda function that adds 4 to its argument.
# Then, we call this lambda function with the argument 5, resulting in 4 + 5 = 9, which is printed.

# Output:
# 9 

myList = [1, 2, 3, 4, 5]
newlist=list(filter(lambda a:(a/3)==2,myList))
print(newlist)

squaredList = list(map(lambda x: x**2, myList))
print(squaredList)# This code uses the filter function with a lambda to filter elements in myList
# that satisfy the condition (a/3)==2, resulting in [6].

# It also uses the map function with a lambda to create a new list squaredList
# containing the squares of each element in myList, resulting in [1, 4, 9, 16, 25].

#map(func,iterables)
mylist=[1,2,3,4,5]
p=list(map(lambda a:(a/3)!=2,mylist))
print(p)
# This code uses the map function with a lambda to create a new list p
# where each element is twice the corresponding element in mylist, resulting in [2, 4, 6, 8, 10].   

#reduce(func,sequence)
from functools import reduce
mylist=[1,2,3,4,5]
s=reduce(lambda a,b:a+b,mylist)
print(s)

# This code uses the reduce function from the functools module with a lambda
# to compute the sum of all elements in mylist, resulting in 15.

