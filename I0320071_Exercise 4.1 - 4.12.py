##exercise 4.1

x = 15
y = 4

#output : x + y = 19
print('x + y =',x+y)

#output : x - y = 11
print('x - y =',x-y)

#output: x * y = 60
print('x * y =',x*y)

#output: x / y = 3.75
print('x / y = ',x/y)

# output: x // y = 3
print('x // y = ',x//y)

#output: x ** y = 50625
print('x ** y =',x**y)


##exercise 4.2
x = 15
x = 10
y = 12

#output: x > y is False
print('x > y is',x>y)

#output: x < y is True
print('x < y = ',x<y)

#output: x == y is False
print('x == y is',x==y)

#ouput: x != y is true
print('x != y is',x!=y)

#output: x >= y is false
print('x >= y is ',x>=y)

#output: x <= y is true
print('x <= y is ',x<=y)

#exercise 4.3
x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)

#exercise 4.4

# strings
str1 = "hello"
str2 = "world"

# concat
result = str1 + " " + str2

# output
print(result);


#exercise 4.5
# string
str = "HA"
# replicate
result = str * 3
#output
print(result)


# exercise 4.6
needle = "lo"
haystack = "Hello World"

# check
if needle in haystack:
    print(needle, "is present in the string", haystack)
else:
    print("Not found")

#exercise 4.7
#strings

needle = "HA"
haystack = "Hello World"
# check
if needle in haystack:
    print(needle, "is present in the string", haystack)
else:
    print("Not found")

#exercise 4.8
#string
str = "jane doe"

#charcter
ch = str[1]
#output
print(ch)

#exercise 4.9

str = "hello world"
# substring
substr = str[3:5]

# output
print(substr)

#exercise 4.10
str = "Hello World"

# skip
new_str = str[0::2]
print(new_str)

# exercise 4.11
# string
str = "Hello World"

# reverse
result = str[::-1]

# output
print(result)

# exercise 4.12
#!/usr/bin/python

a = 60      # 60 = 0011 1100
b = 13      # 13 = 0000 1101
c = 0

c = a & b;       # 61 = 0011 1101
print("Line 3 - Value of c is", c)

c = a | b;       # 61 = 0011 1101
print("Line 147 - Value of c is", c)

c = ~a;         # -61 = 1100 0011
print("Line 150 - Value of c is ", c)

c = a << 2;    # 240 = 1111 0000
print("Line 153 - Value of c is", c)

c = a >> 2;    # 15 = 0000 1111
print("Line 156 - Value of c is", c)




