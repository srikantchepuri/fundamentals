print("Hello World!")

num1 = 2
num2 = 3
num3 = 10
# Arithmetic Operations
print(num1**num2)  # power
print(num3 % num2)  # modulus
print(num3//num2)  # division that gives lower whole number, floor division

print(3.4//2.2)


# Assignment Operators
num4 = num1+num2

num4 += num3  # as same as num4=num4+num2

print(num4)

x = 5
x /= 5  # as same as x=x/5
print(x)

x = 5
x %= 3  # as same as x=x%3
print(x)


x = 5
x //= 3  # as same as x=x//3
print(x)


x = 5
x **= 3  # as same as x=x**3
print(x)


# Comparison Operators
# >,<,==,!= #pretty straightforward

# Logical Operators , any number <=0 is considered False, else True
# and , in x and y, return x when x is False, else return y
print(True and False)
print(2 and 3)

# or , in x or y, return y when x is False, else return x
print(False or True)
print(2 or 3)

# not

print(not 2)  # returns False as 2 is considered True


# Bitwise Operators
print(7 | 8)  # results 15
print(7 & 8)  # results 0
print(7 ^ 8)  # results 15


# shift
print(3 >> 2)  # 0011 to 0000

print(3 << 2)  # 0011 to 1100


# identity operations
x = 5
print(x is 5)

print(x is not 5)

# Membership operators
y = [1, 2, 3, 4, 5]

print(3 in y)  # True

print(3 not in y)  # False

# Data Types, loosly typed, no need to define data type
#Immutable - Numbers, Strings, Tuples

# Number - integer, float, complex data type  -
a, b, c = 1, 1.2, 10+3j  # maximum range is set based on your system memory
print(a, b, c)

str1 = 'Python'
str2 = "Tutorial"

str3 = str1+str2

print(str3)

print(str1*2)  # results PythonPython
print(str2[2:5])  # returns tor , index starts from zero, upper bound is not included
print(str1[-1])  # Returns n, last character


# Type specific methods
str1.find('on')  # returns 4 , returns the index of first occurance
str2.replace('Tuto', 'Memo')  # Returns Memorial :)
str4 = 'P,y,t,h,o,n'
str3.split(',')  # rerurns ['P','y','t','h','o','n']

str2.count('to')  # returns 1, in Tutorial , does not have beg, end parameters

str1.upper()
str1.max()  # does not work
str1.min()  # does not work
str1.isalpha()

# Tuple - sequence of immutable pyton objects like floating number,string literals, they can not be changed

myTuple = ('Srikant', 1213, 'Toper of the Batch', 2.0)
myTuple+('He is an awesome', 'guy !')  # Concatanation

print(('a', 1)*2)  # prints ('a',1,'a',1) #repetition

tup = ('a', 1, 2.0, 'abc')
tup[1:3]  # results (1,2.0) , upper bound is not included

tup[2]  # 2.0


#Mutable - Lists, Dictionaries, Sets


# If Condition
number = 22
if (number == 23):
    print("You have guessed it right")
elif number > 23:
    print("You have guessed it more")
else:
    print("You have guessed it less")


for i in range(1, 5):
    print(i)
print("End of for loop")

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


print(str(1)+'my string')

a = 1
a = 2/float(3)
print(a)


shoplist = ['a', 'b'.'c']

mylist = shoplist  # copying the reference

mylist = shoplist[:]  # copy by value


a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 

print(a[1][2:4])

#Lists

#Touples

#Dictionaries

Import numpy as np 