
# This program is a demo belonging to the Python Calculator Project in which we test possible
# ways to solve the Asymptote Problem. The Asymptote Problem consists of making an algorithm
# that allows the computer to locate or approximate the asymptote of a graph, lets say 1/x.
# This problem arises when we try to create a graph for rational graphs in the Python
# Calculator Project. The goals of this demo program is to adress the following:
#   1) Finding exact (natural) valued vertical assymptotes/ Ex. 1/x; Assymptote at x=0.
#   2) Finding inexact (irrational) valued vertical assymptotes/ Ex. 1/x-pi; Assymptote at x=pi
#   3) Finding oblique asymptotes/ Ex. (x^2+1)/(x-1). We would need to make an algorithm to
#      perform division of polynomials
#   4) Implement algorithms that finds the limits of the rational function for appliable
#      cases in order to find the horizontal asymptote, for example in (x^2+2x+1)/(3x^2+6x+1)
#      the horizontal asymptote is y = 1/3
#   5) Skipping value or list of values which lead to undefined values while making the
#      computations

# The methods (theory) I plan to use to find such asymptotes include:
#   1) Making an algorithm that searches for the value that makes the denominator zero.
#      This method only applies to goals 1 and 2, in which the degree of the nominator
#      is less than the denominator. When we mention search for the asymptote we mean that
#      the algorithm will try every value in the domain set default or by the user with a
#      default update rate of 0.001 (precision = 1000) to see of some value results in
#      zero. This works very well with goal 1, exact valued asumptotes. Now, when it comes
#      to inexact valued asymptotes, we will need to use approximation methods to
#      approximate the asymptote without causing an error in the program. The approxiation
#      method will greatly depend on the precision of the function, and of course this is
#      limited. What we could do is to use the same procedure of trying every value in the
#      especified domain with update rate 0.001 and use the Intermediate Value Theorem
#      to determine aproximately where the asymtote is approximately. For example, for the
#      function 1/x-pi if the algorithm (with an accuracy of 0.001) finds that at x~3.141
#      x-pi= a negative number and at 3.142 x-pi is positive the that means that between
#      3.141 and 3.142 there is an assymptote. So if we take the mean of these two values
#      we could approximate the location of the assymptote.

#   2) Also, when it comes to simple functions like 1/x, 1/(x^2-2), 1/(x-pi), etc. which
#      only involve one instance of x and a number in the denominator, we could design a
#      smarter algorithm that recognizes for example that when x is alone in the
#      denominator, then the asymptote is x=0 or when there is another number like -pi
#      and the degree of the x is 1 then the asumptote is at -(-pi) or if the degree of x
#      is 2 or 3, then the asumptote is at (-(-pi))^1/2 or (-(-pi))^1/3 respectively. Now,
#      when it happens that there is more than one instance of x in the denominator and
#      a number, like x^2-x+3, then we use method 1, since the problem is more complex.

#   3) consider the degrees if these are equal then the asymptote is the division of the
#      coefficients of the x with greater degree in the nominator and denominator. This
#      is for horizontal asymptotes.

#   4) Very important! We should make an algorithm which is specialized in recognizing the
#      type of rational function we are dealing with, this is critical.




import matplotlib.pyplot as graph
import math

precision = 100
x,y = -50,0
x_val,y_val = [],[]
poly_coef_nom = []
poly_coef_den = []

# ------------------------- FUNCTIONS --------------------------

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

# Case #1 exact vertical assymptotes

    # In this symple case why to make calculations at all?
    # in fact as we know what is the asymptote from just
    # seeing the expression why not to teach our algorithm
    # the same thing! The only condition we need to be aware
    # is that x should only appear in the denominator once.
    # Ex. 1/x+1; 2/x^2+3; a/x^n+b ... However, expressions
    # like 1/x^2+2x+1 which involve factoring or the qua_
    # dratic formula do not apply for this trick. So, what
    # we need to do is help the computer to identify the
    # following:
    #   1) Degree of the single instance of x in the deno_
    #      minator
    #   2) Number adding or substracting that only instan_
    #      ce of x in the denominator.
    #   3) That's it! We could achieve this by using the
    #      polynomial approach in the main program and
    #      identify each item in the denominator indepen_
    #      dently. Let's reproduce a demo of the main
    #      program here.

# Getting maximum degrees of the rational expression

print("Enter the following information for the Rational Function (Case 1 Only)")

nominator_degree = float(input("Enter the maximum degree of the nominator: "))
if nominator_degree == 0:
    nominator_num = float(input("Enter the number in the nominator:"))
    
else:
    for i in range(0, 2):

        coefficients = float(input("Enter the coefficients of x^: "))#FIX
        poly_coef_num.append(coefficients)

denominator_degree = float(input("Enter the maximum degree of the denominator: "))

if denominator_degree % 2 == 0: #1*
    signs = ' +/- '             #1*
else:                           #1*
    signs = ' '                 #1*
    
if denominator_degree == 0:     #1*
    print("This is not a rational function")#1*
    
else:
    for i in range (0, 2):

        coefficients = float(input("Enter the coefficients of x^: "))#FIX
        poly_coef_den.append(coefficients)

        if poly_coef_den[0] < 0 and denominator_degree % 2 == 0:
            print("ERROR. The Asymptote is not a real number")

asymptote = my_root (-poly_coef_den[0]/poly_coef_den[1], denominator_degree)#1*-> This is our target for goal 1.

if signs == ' +/- ':
    asumptote_2 = -asymptote # Later on when we make #1* into a function lets make
                             # the function return asymptote if 'denominator_degree % 2 == 0'
                             # is True. Need to research on how to export a second value
                             # or at least an indicator which lets the rest of the function
                             # know that there are two asymptotes.
    
        
print("The vertical Asymptote(s) is/are", signs, asymptote)
print("The horizontal Asymptote is...Comming soon!")

# FIX: We need to consider that we may have (+/-) asymptotes if so, we need to store the negative
# one in a different variable Ex. asymptote_2 if the degree of the denominator is even.

# NOTICE: No validation will be needed to recognize
# if the user inputed a rational function of type 1
# because we will make an algorithm in the future
# which identifies which type is the rational fun_
# ction. In fact this algorithm to find asymptotes
# will not even need a for loop to fill the list
# with coefficients, we do so now because this is
# a demo so we need to recreate the conditions.

# After we put the values for the coefficients of the
# numerator and denominator in the lists. We think,
# and really if the function has only one instance
# of x then we care about the location of the coeffi_
# cient on the list since the index # in which this
# number is located is the actual degree of the x in
# the denominator. Finally, we care about the coeffi_
# ent stored in the index zero because it is the
# number for which the instance -(x^n) should no be
# equal to.

# NOTICE: the condition to execute case 1 algorithm
# to find the asymptote(s) is the fact that all the
# numbers stored in the poly_coef_den list in the
# indexes between 0 and n (for n is the degree
# of the denominator) are equal to zero only.

# CASE 1 Analysis Outcome
def case_1_rational_function(polynomial_list, degree, asymptote_2):
    asymptote = my_root (-polynomial[0]/polynomial[1], degree)
    if degree %2 == 0:
        asymptote_2 = -asymptote
    return asymptote

    
# Now that we are done with Case 1 lets start the
# analysis of case 2 which describes the recogni_
# tion of inexact and irrational valued vertical
# asymptotes. We may think, well what is the
# problem with an irrational number, isn't the
# same procedure as finding the asymptote in
# Case 1? And indeed it is the same thing, in
# fact we will be using case 1 function. I was
# sleepy when I wrote case 2 at the start of this
# demo program. However, I have a potential
# candidate to occupy the position for case 2 and
# it is the case when we have a polynomial with a
# second instance of x in the denominator. Now,
# if we have something like 7/x^2+9x-2 how do we
# do to find the zeros of this polynomial? The
# answer is simple: The Quadratic Equation!!!
# with this equation we could find the zeros and
# recognize weather there are real zeros using
# the discriminant or b^2-4ac.
# The Quadratic Equation is:
#   x = (-b +/- (b^2-4ac)^1/2)/2a
# This case will use the same setup as Case 1,
# just that we now will use three elements from
# the polynomial list polynomial[0],
# polynomial[1] and polynomial[2] which represent
# the coefficients c, b, a respectively of the
# second degree polynomial in the denominator.
# Then we simply substitute into the quadratic
# formula and find the zeros. Let's do it!!!

# CASE 2 Analysis Outcome
def case_2_rational_function(polynomial_list, asymptote_2):
    discriminant = (polynomial[1])**2-4*polynomial[2]*polynomial[0]
    if discriminant < 0:
        print("ERROR. Ups.. this rational function has imaginary asymptotes") 
    elif discriminant == 0:
        asymptote = (-polynomial[1])/2*polynomial[2]
    elif discriminant > 0:
        asymptote = (-polynomial[1]-(discriminant)**1/2)/2*polynomial[2]
        asymptote_2 = (-polynomial[1]+(discriminant)**1/2)/2*polynomial[2]
    return asymptote

#TESTING STILL NEEDS TO BE DONE, REFER TO A_P_1.0_TESTING




    

    

    
    






















    
