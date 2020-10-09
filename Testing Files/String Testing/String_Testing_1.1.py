#String Testing

string = "Hello"
print(string[0])

# Since a string by deffinition is a list of characters, then I could use
# a string as a list to identify predifined mathematical expressions and
# instead of having the user enter choices for the type of expression, the
# user can enter the mathematical expression separated by mathematical
# operators (*, /, +, -, ^) and my program will recognize it using if statements

"""
    So, basically in this second section of string testing I will be trying to
    identify numbers and variables in a mathematical expression which will be
    typed by the user. After the program identifies a simple expression I will
    translate such expression which is a string into a mathematical operation
    that can be computed and solved by the computer. Finally I will print the
    result. Variables will be represented with the letters x,y or z.
"""
expression_list = []
number_holder = 0
decimal_place_location = 0

math_expression = input("\nPlease enter a very simple math expression (no spaces please): ")

##for i in range (0,len(math_expression)):
##        if math_expression[i] == '.':
##                print(math_expression[i+1])

for i in range (0,len(math_expression)):
        if math_expression[i] != '+' or math_expression[i] != '-' or math_expression[i] != '*' or math_expression[i] != '/':

                                # Decimal filter identification   
                if math_expression[i] == '.' or decimal_place_location > 0:

                        if decimal_place_location > 0:

                                if math_expression[i] == '1':
                                        number_holder = number_holder + 1/10**((i)-decimal_place_location)
                                elif math_expression[i] == '2':
                                        number_holder = number_holder + 2/10**((i)-decimal_place_location)                       
                                elif math_expression[i] == '3':
                                        number_holder = number_holder + 3/10**((i)-decimal_place_location)
                                elif math_expression[i] == '4':
                                        number_holder = number_holder + 4/10**((i)-decimal_place_location)
                                elif math_expression[i] == '5':
                                        number_holder = number_holder + 5/10**((i)-decimal_place_location)
                                elif math_expression[i] == '6':
                                        number_holder = number_holder + 6/10**((i)-decimal_place_location)
                                elif math_expression[i] == '7':
                                        number_holder = number_holder + 7/10**((i)-decimal_place_location)
                                elif math_expression[i] == '8':
                                        number_holder = number_holder + 8/10**((i)-decimal_place_location)
                                elif math_expression[i] == '9':
                                        number_holder = number_holder + 9/10**((i)-decimal_place_location)
                                elif math_expression[i] == '0':
                                        number_holder = number_holder + 0/10**((i)-decimal_place_location)
                        if decimal_place_location == 0:                
                                decimal_place_location = i
                                #Testing/ print("\tDECIMAL PLACE LOCATION: ", decimal_place_location)
                        #Testing/ print("\tNUMBER HOLDER: ", number_holder)

                #Integer filer identificaiton
                if (math_expression != 'x' or math_expression != 'y' or math_expression != 'z') and decimal_place_location == 0:
                    
                        
                        if math_expression[i] == '1':
                            number_holder = number_holder*10 + 1
                        elif math_expression[i] == '2':
                            number_holder = number_holder*10 + 2                        
                        elif math_expression[i] == '3':
                            number_holder = number_holder*10 + 3
                        elif math_expression[i] == '4':
                            number_holder = number_holder*10 + 4
                        elif math_expression[i] == '5':
                            number_holder = number_holder*10 + 5
                        elif math_expression[i] == '6':
                            number_holder = number_holder*10 + 6
                        elif math_expression[i] == '7':
                            number_holder = number_holder*10 + 7
                        elif math_expression[i] == '8':
                            number_holder = number_holder*10 + 8
                        elif math_expression[i] == '9':
                            number_holder = number_holder*10 + 9
                        elif math_expression[i] == '0':
                            number_holder = number_holder*10 + 0
                                
                if math_expression[i] == '+' or  math_expression[i] == '-' or  math_expression[i] == '*' or  math_expression[i] == '/':
                        print("Not quite there yet (+,-,*,/)")
                        

print("\n\tThis is your input squared: ", number_holder**2) #Success!
            

            

            

        

        
    

