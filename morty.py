# If you run this there is a bunch of intro stuff that will print

a = 10

print(a + a)

my_income = 100

tax_rate = 0.1

my_taxes = my_income * tax_rate

print(my_taxes)

print('hello \nworld')

print('hello \tworld')

print(len('hello'))

print(len('I am'))

mystring = "Hello World"

print(mystring[2])

print(mystring[-1])

mystring2 = "abcdefghijk"

print(mystring2[2:])
# stop index below is upto but not including 
print(mystring2[:3])

print(mystring2[3:6])

print(mystring2[1:3])

# for what ever reason you can do this to get everything
print(mystring2[::])
# same thing to reverse 
print(mystring2[::-1])

# there is this step size thing to jump every character 
print(mystring2[::2])

print(mystring2[::3])
# start : stop : step size

# Immutability

name = "Sam"
# name[0] = 'P' doesn't work

last_letters = name[1:]

print(last_letters)
# String Concatenation
print('P' + last_letters)

x = 'Hello '
print(x + 'my name is Sam')

letter = 'z'
print(letter * 10)

print(letter.upper)