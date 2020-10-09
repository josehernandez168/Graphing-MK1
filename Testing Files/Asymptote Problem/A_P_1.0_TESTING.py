#A_P_1.0_TESTING

# In this program I will be testing Case 1 and Case 2 fucntions for recognizing asymptotes

def my_root (base, n): #-> Wee need this function to find roots
    if n % 2 == 0:
        result = base**(1/n)
    else:
        if base >= 0:
            result = base**(1/n)
        else:
            base = -base
            result = -(base**(1/n))
    return result

# Functions compeeting in this test are...

def case_1_rational_function(polynomial_list, degree):
    asymptote = my_root (-polynomial_list[0]/polynomial_list[1], degree)
    if degree %2 == 0:
        asymptote_2 = -asymptote #CHECK!
        print("Trigered")
        return asymptote, asymptote_2 #-> Returning a tuple
    else:
        return asymptote

# and...

def case_2_rational_function(polynomial_list):
    discriminant = (polynomial[1])**2-4*polynomial[2]*polynomial[0]
    if discriminant < 0:
        print("ERROR. Ups.. this rational function has imaginary asymptotes") 
    elif discriminant == 0:
        asymptote = (-polynomial[1])/2*polynomial[2]
    elif discriminant > 0:
        asymptote = (-polynomial[1]-(discriminant)**1/2)/2*polynomial[2]
        asymptote_2 = (-polynomial[1]+(discriminant)**1/2)/2*polynomial[2]
    return asymptote

# CASE 1 Testing
    # Sample denominator polynimoal 1 (3x^5 + 9)
poly_coef_case1 = [9, 3]
asymptote = case_1_rational_function(poly_coef_case1,5)
    # Expected solution: -(3)^1/5 =~ -1.24573094
print("Case_1_ploy_1: ", asymptote)

    # Sample denominator polynimoal 2 (x^2 - 9)
poly_coef_case1 = [-9, 1]
asymptotes = case_1_rational_function(poly_coef_case1,2)#-> This returns the tuple (3,-3) 
    # Expected solution: 3 and -3
    
print("Case_1_ploy_1: ", asymptotes[0], " and ", asymptotes[1])

# TEST RESULTS:
# In this test it was confirmed that to export several values
# using a single function I could just simply type return a,b,c...
# and the function will return a tuple containing (a,b,c,...).
# So, by setting a variable 'var' equal to this function, I could
# collect all those returned and call any value inside the tuple
# by typing the corresponding index of the value like in a list,
# or var[0], var[1], var[2], etc. That's cool and more organized
# than using pointers, like in C programming language.

#----------------------------------------------------------------------------------

# CASE 2 Testing
    # Sample denominator polynomial (x^2 - 5x + 6)
poly_coef_case2 = [6, -5, 1]



# \\Testing Zone End ;)\\
