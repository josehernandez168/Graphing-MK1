# This demo program aims to investigate a problem I've been encountering with
# odd roots. For example if I get a value lets say 8 and I set it equal to a
# variable 'd' and then I rise this variablle to an odd root like 1/3, the
# program returns an imaginary number instead of 8**(1/3) = 2.0. This problem
# also shows up in the main program in the section for graphing the x^(1/3)
# function, or cubic root function. This problem only results if the root is
# odd, if the root is even there is no problem at all. Then how can I solve
# this? First I am going to try to tackle the issue from different directions
# to see if the problem is the power operator, the variable, the format of the
# base or the exponent.

print("..............Test Set #1................")

# Simple- '8' as an integer
print(8**(1/3))
print(8**1/3)
print(8**(1/3.0))
print(8**(1.0/3.0))
print(8**1/3.0)
print(8**1.0/3.0)
# Simple- '8' as a float
print(8.0**(1/3))
print(8.0**1/3)
print(8.0**(1/3.0))
print(8.0**(1.0/3.0))
print(8.0**1/3.0)
print(8.0**1.0/3.0)
# With base as a variable- 'b' as an integer
b = 8
print(b**(1/3))
print(b**1/3)
print(b**(1/3.0))
print(b**(1.0/3.0))
print(b**1/3.0)
print(b**1.0/3.0)
# With base as variable- 'b' as a float
b = 8.0
print(b**(1/3))
print(b**1/3)
print(b**(1/3.0))
print(b**(1.0/3.0))
print(b**1/3.0)
print(b**1.0/3.0)

# The result of this first set of tests show that for the program to computer
# the root correctly, the exponent, in this case 1/3 need to be inside a
# parenthesis. If I write 8**(1/3) I will get the correct value '2.0',
# however, if I write 8**1/3 I will get 2.666...- which is wrong. However,
# these results doesn't explain why I get an imaginary number in my program
# for the Asymptote Problem and in the Python Calculator program. Now, I will
# perform another set of tests in which for the base I will use a value from
# one of the indexes of a list and see what happens.

print("..............Test Set #2................")

# With base as a number from a list- base as an integer
base_list = [0, 8, 27, 125, -8, -27, -125]
print(base_list[1]**(1/3))
print((base_list[1])**(1/3))
print(base_list[2]**(1/3))
print((base_list[2])**(1/3))
print(base_list[4]**(1/3))
print((base_list[4])**(1/3))
print(base_list[6]**(1/3))
print((base_list[6])**(1/3))

# This second test confirms that the main problem while trying to compute
# an odd root is having a negative base. For example, the cubic roots for
# -8 and -125 were given as imaginary numbers. Let's try and see if a simple
# base like in the Test Set # 1 but negative results also in an imaginary
# number.

print("..............Test Set #3................")

# With negative simple base- '-8' as an integer
print(-8**(1/3))
print((-8)**(1/3))

# This test resulted in an imagniary number for (-8) however, -8 without the
# parenthesis resulted in -2.0 which is correct. So, let's try to avoid those
# parenthesis around the base number. Now this does not explain why I got ima_
# ginary numbers for base_list[4]**(1/3) and base_list[6]**(1/3). Perhaps the
# fact that we are retriving the value from a list has the same effect as if
# we put parenthesis around the base, to confirm if this is true I will set
# the retrieved value from the list equal to a variable and see what effect it
# has when an odd root is applied.

print("..............Test Set #4................")

# Negative base as a number from a list equal to a variable- '-8' as an integer
base_list = [0, 8, 27, 125, -8, -27, -125]
n = base_list[4]
m = base_list[6]
print(n**(1/3))
print(m**(1/3))

# Nope, this test also resulted in imaginary values. I believe the problem lies
# in the way that the basic arithmetic operators interpret the negative sign
# that comes attached to the value. If the base comes as one piece negative
# number like (-8), like a negative package, then the exponential operator also
# incorporates the negative sign while taking the cubic root and when it cal_
# culates the square root or finds two same numbers which multiplied give you
# -4 it runs into imaginary numbers, and then follows up to finish the cubic
# root, but with an imaginary value already. So, since the problem is the
# negative (-) we could simply take it out, perform the odd root and then mul_
# tiply the -1 again to the result. Perhaps I should make this into a function
# to save space for future use in other programs.

# *** SOLUTION # 1: Root Function Algorithm ***

# Purpose: The purpose of this function is to take in as one of the arguments
# a specific value from certain index of a list as the base and another value
# which will be the root of such base. Then this function will return the
# correct value especifically of odd roots of negative numbers like -8 for
# example. To accomplish this, I will always take the root of positive values
# and if the value was originally negative- as recognized by a conditional
# statement- then the negative will be re incorporated after the odd root is
# taken. Notice, this procedure of the exclusion of the negative sign will
# only be applied when the root is odd, if the root is even then ofcourse
# we will have an imaginary result which cannot be avoided. So, let's do it.

def my_root (base, n):
    if n % 2 == 0:
        result = base**(1/n)

    else:
        if base >= 0:
            result = base**(1/n)
        else:
            base = -base
            result = -(base**(1/n))

    return result
            
print("..........Test of SOLUTION # 1..........")  

# Here we test SOLUTION # 1 using base_list as our test sample list (Odd root)  
print(my_root(base_list[0], 3))
print(my_root(base_list[1], 3))
print(my_root(base_list[2], 3))
print(my_root(base_list[3], 3))
print(my_root(base_list[4], 3))
print(my_root(base_list[5], 3))
print(my_root(base_list[6], 3))

# Success! The fucntion my_root(base, n) works perfect at least for calculating
# odd roots. Now let's test it using even roots (let's start by 2)

base_list_even = [0, 4, 9, 400, -4, -9, -400]

# Here we test SOLUTION # 1 using base_list as our test sample list (Even root)
print(my_root(base_list_even[0], 2))
print(my_root(base_list_even[1], 2))
print(my_root(base_list_even[2], 2))
print(my_root(base_list_even[3], 2))
print(my_root(base_list_even[4], 2))
print(my_root(base_list_even[5], 2))
print(my_root(base_list_even[6], 2))

# Success! The function my_root(base, n) works perfect also with even roots.
# Problem is solved! Now I can use this function to make calculations involving
# even and odd roots without having the issue of complex numbers as the result
# of odd roots for negative numbers. NOTICE: optimization is needed for example
# to approximate the result of 125**(1/3) to be 5, not 4.99999999999, which I
# don't need for now but well just in case ;)


