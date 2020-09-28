#This program attempts to create a graphing calculator using the library matplotlib.

import matplotlib.pyplot as graph
import math

#setting up variables and lists to store data

#Variables
a,b,c,d,n,x,y,t = 0,0,0,0,0,0,0,0
t_2 = (2*math.pi)
graph_extension, sine, cosine, graph_counter = 0,0,0,0
precision = 1000 #Manual precision change (default: 100)

#List pairs / Check if this is needed Perhaps only the final_x and final_y should be here
x_val, y_val = [],[]
x_val2, y_val2 = [],[]
x_val3, y_val3 = [],[]
final_x, final_y = [],[]
poly_c, poly_d = [],[]
poly_c2, poly_d2 = [],[]

repeat = 1 # Control variable for while loop

# -----------------------------FUNCTIONS-------------------------------

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


while(repeat == 1):

    repeat, switch = 3,0
    asymptote,  asymptote2 = 0,0
    x,t,y,y1,y2 = 0,0,0,0,0
    x_val, y_val =  [],[]
    x_val2, y_val2 = [],[]
    x_val3, y_val3 = [],[]
    poly_c, poly_d = [],[]
    poly_c2, poly_d2 = [],[]
    
    # User interface/ Getting input

    print("\nWelcome to the graphing calculator!\n")
    print("From the list imput the number corresponding to the desired function type\n")
    print("1) Plynomial       2) Squared root       3) Cubic root\n"
          "4) Cardioid        5) Spiral             6) Lemniscate\n"
          "7) Roses           8) Logarithm          9) Exponential\n"
          "10) Rational      11) Sine              12) Cosine\n"
          "13) Tangent       14) Exit")
    user_choice = int(input("\nPlease input your choice: "))

    if user_choice == 1 or user_choice == 2 or user_choice == 3 or user_choice == 8 or user_choice == 9 or user_choice == 10:
        
        number_of_points = int (input("Please enter the number of points to plot (even quantity): "))

    elif user_choice != 14: #change to an 'elif'. If user inputs any number, the program displays the input unnecessarily
        max_angle = int (input("Please enter the maximum angle desired for the graph (in degrees): "))

    # Identifying the type of graph desired

    if user_choice == 2:

        graph_label = 'Squared root'
        print("Function in the form: y = a*x^1/2 + c")
        a = float(input("Input the 'a' coefficient: "))
        c = float(input("Input the y-shift: "))

        for i in range (0, (number_of_points * precision)+1):

            y = a*x**0.5 + c # Equation for the squared root

            x_val.append(x)
            y_val.append(y)

            x += (1/precision)
        
    elif user_choice == 3:

        graph_label = 'Cubic root'
        print("Function in the form: y = a*x^1/3 + c")
        a = float(input("Input the 'a' coefficient: "))
        c = float(input("Input the y-shift: "))
        x = -(number_of_points/2)
        
        for i in range (0, (number_of_points * precision)+1):
            
            y = a*my_root(x, 3)+c # Equation for the cubic root

            x_val.append(x)
            y_val.append(y)

            x += (1/precision)

    elif user_choice == 1:
        
        graph_label = 'Polynomial'
        print("Function in the form: y = an*x^n + a(n-1)*x^(n-1)+ ... + a2*x^2 + a1*x + a0")
        degree = int(input("Enter the maximum degree of the polynomial: "))
        x = -number_of_points/2
        
        for i in range (0, (degree+1)):
            poly_c.append(float(input("Enter the coefficients from right to left: ")))
            poly_d.append(i)

        for i in range (0, (number_of_points * precision)+1):
            for j in range (0, (degree+1)):
                y += poly_c[j]*x**poly_d[j]
                
            x_val.append(x)
            y_val.append(y)

            x += (1/precision)   
            y = 0
        
    elif user_choice == 4:

        graph_label = 'Cardioid'
        print("Function in the form: r = a + b*(sin(t)/cos(t))")
        a = float(input("Input the 'a' number of the polar equation: "))
        b = float(input("Input the 'b' coefficient of the polar equation: "))
        trig_function = input("Is it the 'sine' or the 'cosine'? (Input the name of the corresponding trigonometric function): ")
        
        if trig_function == 'sine':

            for i in range (0, (max_angle*precision)):

                r = a + b*math.sin(t) # Cardioid equation (sine)

                x = r*math.cos(t) # Conversion from Polar to Cartesian
                y = r*math.sin(t) #-^
                
                t += ((math.pi/180)/precision) # Update rate(~1 degree in radians)
                
                x_val.append(x)
                y_val.append(y)

        elif trig_function == 'cosine':

            for i in range (0, (max_angle*precision)):
                
                r = a + b*math.cos(t) # Cardioid equation (cosine)

                x = r*math.cos(t)
                y = r*math.sin(t)
                
                t += ((math.pi/180)/precision)

                x_val.append(x)
                y_val.append(y)
                
        else:
             print("Error, trigonometric function not recognized or available.")

    elif user_choice == 5:

        graph_label = 'Spiral'
        print("Function in the form: r = a*t^n")
        a = float(input("Input numerical coefficient 'a': "))
        degree = float(input("Input the degree of the angle: "))
        
        for i in range (0, max_angle*precision):

            r = a*t**degree # Spiral equation

            x = r*math.cos(t)
            y = r*math.sin(t)

            t += ((math.pi/180)/precision) # Update rate(~1 degree in radians)

            x_val.append(x)
            y_val.append(y)
            
    elif user_choice == 6:
        
        graph_label = 'Lemniscate'
        print("Function in the form: r = (a*(sin(t)/cos(t)))^1/2")
        a = float(input("Enter the 'a' coefficient: "))
        n = int(input("Enter the coefficient of the angle: "))
        trig_function = input("Is it 'sine' or the 'cosine'?"
                              "(Input the name of the corresponding trigonometric function): ")
       
        if trig_function == 'sine':
            
            for i in range (0, (max_angle*precision)):

                r = (a*math.sin(n*t))**0.5 # Lemniscate equation (sine)

                x = r*math.cos(t)
                y = r*math.sin(t)

                if a*math.sin(n*t) > 0:
                    x_val.append(x)
                    y_val.append(y)
                if i == 0:
                    x_val.append(0)
                    y_val.append(0) 
                                    
                t += ((math.pi/180)/precision) # Update rate(~1 degree in radians)

        elif trig_function == 'cosine': 
            
            for i in range (0, (max_angle*precision)):
                
                r = (a*math.cos(n*t))**0.5 # Lemniscate equation (cosine)
                
                x = r*math.cos(t)
                y = r*math.sin(t)

                if a*math.cos(n*t) > 0:
                    x_val.append(x)
                    y_val.append(y)
                
                t += ((math.pi/180)/precision) # Update rate(~1 degree in radians)

    elif user_choice == 7:

        graph_label = 'Roses'
        print("Function in the form: r = a*(sin(n*t)/cos(n*t))")
        a = float(input("Input the 'a' coefficient: "))
        n = int(input("Input the 'n' coefficient for the angle: "))
        trig_function = input("Is it 'sine' or the 'cosine'? (Input the name of the corresponding trigonometric function): ")
        
        if trig_function == 'sine':
            
            for i in range (0, (max_angle*precision)):

                r = a*math.sin(n*t) # Roses equation (sine)
                
                x = r*math.cos(t)
                y = r*math.sin(t)
                
                x_val.append(x)
                y_val.append(y)            

                t += ((math.pi/180)/precision) # Update rate (depends on 'precision')
                
        elif trig_function == 'cosine': 

            for i in range (0, (max_angle*precision)):
                
                r = a*math.cos(n*t) # Roses equation (cosine)
                
                x = r*math.cos(t)
                y = r*math.sin(t)
                
                x_val.append(x)
                y_val.append(y)            

                t += ((math.pi/180)/precision)# Update rate (depends on 'precision')
            
        else:
             print("Error, trigonometric function not recognized or available.")

    elif user_choice == 8:

        graph_label = 'Logarithm'
        print("Function in the form: a*log base(x)")
        a = float(input("Input the 'a' coefficient: "))
        base = float(input("Input the 'base' for the logarithm: "))
        x = 1/(precision)**3
        
        for i in range (0, (number_of_points * precision)+1):

            y = a*math.log(x,base)

            y_val.append(y)
            x_val.append(x)

            x += (1/precision)
            
    elif user_choice == 9:

        graph_label = 'Exponential'
        print("Function in the form: a*(base)^x")
        a = float(input("Input the 'a' coefficient: "))
        base = float(input("Input the 'base' for the logarithm: "))
        x = -number_of_points/2

        for i in range (0, (number_of_points * precision)+1):

            y = a*(base)**x

            y_val.append(y)
            x_val.append(x)

            x += (1/precision)
##--------------------------------CONSTRUCTION IN PLACE, CAUTION! ;) ---------------------------------
##    elif user_choice == 10:
##
##        graph_label = 'Rational' #FIX: Fix this print for function form
##        print("Function in the form:     an*x^n + a(n-1)*x^(n-1)+ ... + a2*x^2 + a1*x + a0\n"
##              "                     y =  _________________________________________________\n"
##              "                          an*x^n + a(n-1)*x^(n-1)+ ... + a2*x^2 + a1*x + a0\n")
##        
##        l_dom = float(input("Input the smaller number of the domain: "))
##        h_dom = float(input("Input the greatest number of the domain: "))
##        #Ask also for range to set boundaries for the graph because it's infinite
##        degree = int(input("Enter the greatest degree of the nominator: "))
##        degree2 = int(input("Enter the greatest degree of the denominator: "))
##
##        domain_size = int(math.fabs(l_dom) + math.fabs(h_dom))
##        x = l_dom
##        graph_jump = 0
##        
##        for i in range (0, (degree+1)):
##            poly_c.append(float(input("Enter the coefficients from right to left (nominator): ")))
##            poly_d.append(i)
##            
##        for i in range (0, (degree2+1)):
##            poly_c2.append(float(input("Enter the coefficients from right to left(denominator): ")))
##            poly_d2.append(i)
##
##        #print(*poly_c)
##        #print(*poly_c2)
##        #print(*poly_d)
##        #print(*poly_d2)
##        #FIX: Not graphing all values stored on the lists
##        #FIX: Apparently graph_jump is not working properly
##        #FIX: Find Assymptotes
##        for i in range (0, (domain_size*precision)+1):
##            
##            for j in range (0, (degree2+1)):   
##                y2 += poly_c2[j]*x**poly_d2[j]
##                
##            #print(y2)
##            # Recognizing the functions's asymptotes
##            if math.fabs(y2) < (1/precision**2) and switch == 0:
##                asymptote = x #remember that there might be more than one asymptote
##                switch = 1
##                print("***The asymptote is: ", asymptote)
##            elif math.fabs(y2) < (1/precision**2) and switch == 1:
##                asymptote2 = x
##                print("***The asymptote # 2 is: ", asymptote2)
##                
##            y2 = 0
##            x += (1/precision)
##            
##        x = l_dom
##         
##------------------------------------------------------------------------------------------     
##        for i in range (0, (domain_size*precision)+1):
##            
##            for j in range (0, (degree+1)):
##                y1 += poly_c[j]*x**poly_d[j]
##
##            for j in range (0, (degree2+1)):   
##                y2 += poly_c2[j]*x**poly_d2[j]
##                
##            #print(y,"      ",x)
##            y = y1/y2 #FIX: Zero division error, check y2
##
##            # Trigger to recognize when to separate different sections of the graph
##            if x >= asymptote or x>= asymptote2:
##                if x >= asymptote and x<= asymptote2:
##                    graph_jump = 1
##                    x += (1/precision)
##                elif x >= asymptote2:
##                    graph_jump = 2
##                    x += (1/precision)
##                
##            if graph_jump == 0:
##                y_val.append(y)
##                x_val.append(x)
##                
##            elif graph_jump == 1:
##                if y > 0: #FIX: Why is the y negative still in 1/x?
##                    y_val2.append(y)
##                    x_val2.append(x)
##
##            elif graph_jump == 2:
##                y_val3.append(y)
##                y_val3.append(x)
##
##            y1, y2 = 0,0
##            x += (1/precision)
##            #print("***Graph Jum", graph_jump)
##    #...
##---------------------------------END OF CONSTRUCTION ZONE--------------------------------------
            
    elif user_choice == 11:
        graph_label = 'Sine'

        print("Function of the form: a*sin(c*(t-b))+d")

        a = float(input("Input the 'a' coefficient: "))
        b = float(input("Input the 'b' coefficient: "))
        c = float(input("Input the 'c' coefficient: "))
        d = float(input("Input the 'd' coefficient: "))

        for i in range (0, (max_angle*precision)):

            y = a*math.sin(c*(t-b))+d

            x_val.append(t)
            y_val.append(y)

            t += ((math.pi/180)/precision)

    elif user_choice == 12:
        graph_label = 'Cosine'

        print("Function of the form: a*cos(c*(t-b))+d")

        a = float(input("Input the 'a' coefficient: "))
        b = float(input("Input the 'b' coefficient: "))
        c = float(input("Input the 'c' coefficient: "))
        d = float(input("Input the 'd' coefficient: "))

        for i in range (0, (max_angle*precision)):

            y = a*math.cos(c*(t-b))+d

            x_val.append(t)
            y_val.append(y)

            t += ((math.pi/180)/precision)
            
    elif user_choice == 13:
        print("\nSorry Option not yet available.\n"
              "It is needed an algorithm to set the Asymptotes first\n"
              "Without it I cannot make an accurate graph that follows\n"
              "Such a smooth path towards infinity. Iprovement needed!\n")
        
    elif user_choice == 14:
        graph_label = 'Close this plotting window to exit...Bye!'
        repeat = 0
        
        
    #----------------------------------PLOTTING (MATPLOTLIB)--------------------------------

    # Testing checks
    
    #print(*x_val)
    #print(*y_val)
    #print(*x_val2)
    #print(*y_val2)
    #print(graph_counter)

    final_x.append(x_val)
    final_y.append(y_val)
    
    if user_choice == 6: # Only for Cubic root function
        final_x.append(x_val3)
        final_y.append(y_val3)
        graph_counter += 1
        
    if user_choice == 10:
        
        if graph_jump == 1:
            final_x.append(x_val2)
            final_y.append(y_val2)
            graph_counter += 1
            
        elif graph_jump == 2:
            final_x.append(x_val2)
            final_y.append(y_val2)
            final_x.append(x_val3)
            final_y.append(y_val3)
            graph_counter += 2            
    
    # plotting values on the graph
            
    for k in range (0, (graph_counter+1)): 
        graph.plot(final_x[k], final_y[k])# Graph mother graph(s)
        
        # Testing checks
        
        #print(k)
        #print(*final_x[k])
        #print(*final_y[k])

    # labeling and formatting axis and axes
    graph.xlabel('x-axis')
    graph.ylabel('y-axis')
    if (graph_counter == 0):
        graph.title(graph_label)
    else:
        graph.title('Multiple graphs')
    
    graph.grid(color='k', linestyle='-', linewidth=0.20)

    # Determining and setting axis limits; this may be used for zooming in when
    # calculating areas for especific regions.
    
##    if graph_counter == 0:
##        x_min = min(x_val)
##        x_max = max(x_val)
##        y_min = min(y_val)
##        y_max = max(y_val)
##    else:
##        if min(x_val) < x_min:
##            x_min = min(x_val)
##        if max(x_val) > x_max:
##            x_max = max(x_val)
##        if min(y_val) < y_min:
##            y_min = min(y_val)
##        if max(y_val) > y_max:
##            y_max = max(y_val)    
##    graph.axis([x_min,x_max,y_min,y_max]) 

    # Showing the graph
    
    graph.show()
    
    while(repeat != 1 and repeat != 0):
        repeat = int(input("To sketch multiple graphs enter '1', to exit enter '0': "))
        
    graph_counter += 1
    
print("BYE!")

    #----------------------------------------- TO IMPROVE LIST AND NOTES ----------------------------------------

    # 1) (MK3)User interface (Add Tekinter) and also improve the input validation system and error prompts
    
    # 2) (MK1)Add precision choice. We could set precision as user choice in like advanced mode,
    #    but I believe it would be more appropiate to set a presicion standard between all
    #    function graphs. This would allow the presicion to be the same for all graphs,
    #    trully that's what we need, the same resolution. 
    
    # 3) (MK1)Add multiple graphig choice: This may be done by assigning one list per
    #    graph choice (12-13 lists in total). The program will have an inner while loop
    #    which will let the user fill the lists corresponding to each graph (up to 12)
    #    then it will get out of the loop with the lists filled up and these will be graphed.
    #    However, there is a problem with this technique of a assigning a fixed list to each
    #    function and is that if I wanted to make different graphs of the same function type
    #    the program may delete the coordinates stored from a previous graph in order to
    #    store new data. Wait, this is an assumption, it deserves testing. If the points do not
    #    get erased we could even use a single list to store all values from all functions, if
    #    these are erased then I will try something else. If these are not erased then I have
    #    about 536,870,912 numbers that can be contained in one list, I just need to make sure
    #    that these are in the right order for each function to be graphed correclty.
    
    #    -> SOLVED: Actually what I needed is to embed one list within anotherone. So, basically
    #               by adding the x_val and y_val lists to final_x and final_y respectively, it
    #               allowed me to store the values from one function inside the final_x and final_y,
    #               so I was able to clear the x_val and y_val lists to avoid the points from one
    #               function te get mixed up with those of another function. The program does not
    #               delete the data within the lists unless I set the list to be empty or unless
    #               the program is closed. The problem with assigning one list per function is
    #               that besides having an excesive amount of lists which is hard to manage, the
    #               values previously stored for the firts graph get mixed up with those of a new
    #               graph. Thus, when the plot() function graphs those values, a straight line is
    #               created from the last point belonging to the first graph to the firt point
    #               of the last graph. This was solved by saving the data for the points stored
    #               in x_val and y_val inside final_x and final_y respectively, in index order
    #               allowing to store values from one function in one index different from another
    #               function.
    
    # 4) (MK2)Add option to calculate area using integration techniques (rectangles for regular graphs
    #    and circles for polar curves). Adding this function will recquire much more precision
    #    to give out an accurate value wich of course will never be exact. My idea is to make the
    #    spaces between every point very small (adding 'precision') of course not as small as a
    #    derivative, but small enough to approximate the actual value. Then, I will calculate the
    #    area of the rectangle or section of the cricle between two points and add them up
    #    inside a desired domain (x-value or angle value). For this function I will also need to
    #    consider the size of the list, so that way I could play with the precision since very
    #    presice graphs will contain a lot of points which may get close to filling up the list.
    
    # 5) (MK1)Add 'Other Polinomial', 'Rational', 'Logarithmic', 'Exponential', 'Sine', 'Cosine', 'Tangent'.
    
    # 6) (MK1)For the 'Other polinomial' function I will need to add different variables which will hold
    #    the user input for every term depending on the degree of the polynomial. This means that
    #    the degree of the polynomial will determine how many variables I will have, for example,
    #    if the degree is '4' I will need a,b,c,e,f in which all of these will be the coefficients
    #    of the function from x^4 to x^0. Now, for the function, I believe I could make a single
    #    expression which will hold a polynomial of up to ten degrees. To do this I will make the
    #    user input the maximum degree of the polynomial, then based on this degree I could put it
    #    into the functino as an exponent equal to 'n', then it will start to decrease in the form
    #    (n-1), (n-2), (n-3), (n-4) for each of the other terms in the function. The excess of
    #    terms will have an exponent of zero and a coefficient of zero. However, for the user to enter
    #    all the corresponding coefficients I may need a for loop which maybe, by means of if/else
    #    statements will let me alternate variables to store different coefficients in different values.
    #    The program will change variables (1+maximum degree) times in order to store all coefficents.

    #    -> FEEDBACK: The previous idea didn't work. Besides it was too long the algorithm the program
    #                 got stuck when the degree was less than 10 (which was the maximum). A possible
    #                 solution would be to store all of the degrees and corresponding coefficients into
    #                 lists. The coefficient and corresponding degree should be store in different lists
    #                 but in the same index. This will allow to make all the computations by calling
    #                 the desired index from those lists in the computation of the values for the
    #                 polynomial function.
    
    #    -> SOLVED: The problem of a very complex and long function was solved by using two pairs of
    #               lists. One list was named poly_c and its function was to hold the values of the
    #               coefficients for the polynomial in order from the right to the left or (a1 - an).
    #               The other list, poly_d stores the values for the degrees in ascending order, from
    #               the smallest to the greatest degree of the polynomial. Both lists store the coeffi-
    #               cients and corresponding degree of the variable (x) that the same coefficient mul-
    #               tiplies in the same index. This allowes as previously mention in the feedback to
    #               make clean computations by calling the same index from both lists while making
    #               calculations. The logic for the calculations in this function uses two 'for' loops
    #               the inner loop makes all calculations for each individual term inside the polynomial
    #               and add all of those up to the variable y. This inner loop returns the full value of
    #               y to be appended to the y_val list. The outer 'for' loop like all other loops from
    #               different functions has the goal of repeating this process as many times as the user
    #               especified when asked for number of points, besides of course updating the y and x
    #               variables for the next set of calculations.

    
    # 7) (MK1)For the number of points to plot it could be changed especially for the polar fuctions from
    #    'number of points' to 'degrees'. An if statement that recognizes whether the function sele-
    #    ted is polar or not will work just fine. If the function is polar, the user will be asked
    #    until what degree he/she desires to graph the function.
    
    #    -> SOLVED: It was added an if statement that recognizes wether the user wants to graph polar
    #               functions. If the user wants a polar function he/she is asked for the angle instead
    #               of the number of points.

    # 8) (MK1)Also, I added to the display an especification of the form the function has so that the user
    #    is clear of what the function looks like.

    # 9) (MK1)I believe that instead of number of points, the user should be asked by the domain he/she
    #    wants the function to have. Asking for number of points may be confusing for the user since
    #    I am not especifying how far apart each point is from each other.

    # 10) (MK1)Also, I should add an option to change the domain of the function after this function have
    #     been plotted because probably the user wants to see how other section of the graph looks
    #     like without having to repeat the whole process of inputing values to allow for more program
    #     flexibility.

    # 11) (MK1)Plotting intersection points. The idea is to identify a set of coordinates that corresponds
    #     to one or more graphs for the same plot. The algorithm will be kind of similar to the com-
    #     parison algorithm for setting axis limits, using if/ else statements. Instead the purpose
    #     of this comparison is to find the same x and y values between two different pair of lists
    #     belonging to two different functions. When a pair of coordinates are found to be the same,
    #     a red dot will be plotted at such coordinate.

    # 12) (MK1)Precision needs to be fixed for the cubic and squared root functions. When graphing values near
    #     to zero the plot resolution or precision is too big and a noticeable line is plotter for the
    #     graph of such functions. To solve this, the value of the precision could be increased when the
    #     user wants to graph those two functions by using a simple 'if' statement.

    # 13) (MK1)The functions 'Quadratic', 'Cubic' and 'linear' should be deleted. Thanks to the good functionality
    #     of the 'Other polynomial' function it can already graph those three functions with no problem.
    #     However, some extra features should be added like x and y shifts especially for graphing the
    #     'Linear' function, perhaps using an 'if' statement if the maximum degree is 1 can help to ask for
    #     the shifts to the user.

    # 14) (MK1)FIX the cubic root function so that the graph shows with the same color. Investigate why the
    #     plotter is recognizing imaginary values for this function and store all values inside the same
    #     lists like all the other functions to plot with the same color.

    # 15) (MK1)For making the Rational function's graph I will need several different function that will aid
    #     in the process of computing and plotting the values. With the current algorithm in interation
    #     MK1.2 I am running into different problems that may be related to the assymptote. Also, since there
    #     is a break in the graph due to the existence of an assymptote the plot should be made in different
    #     sections to avoid the problem of two separate sections of the graph from connecting with each other
    #     for this I will need to deparate the values belonging to one section of the graph into separate lists
    #     the 'val','val2' and 'val2' lists. However, in order to identify the specific point where each
    #     section ends I will need to know approximately where the assymptotes are to manage how close the 'x'
    #     can get to such asymptote based on the precision used for the computations (usually 0.001). Also,
    #     considering a way to identify symmetry can help a lot to reduce innecessary computations.

    #     -> SOLUTION BREAKDOWN: First I need to create an algorithm that will calculate what is/ are the
    #        asymptote(s) for the rational function in the given domain. After this is done I could use
    #        such asymptote(s) value(s) especially for the 'x' in order to control how close the computation
    #        gets to the asymptote before ending that section of the graph and starting a newone in a
    #        different list. But how will I do such asymtote recognition algorithm? An idea is to make all
    #        the computationsfor the function in the given range before storing the values ready for plotting
    #        and let the program analyze the behavior of the 'y'. For example if the y gets big and suddenly
    #        it becomes very small this indicates that somewhere in between there is an asymptote. Also,
    #        another idea is to use the expression belonging to 'y2' and find which value of x makes it zero
    #        using the same computational process, that sounds easier and will not cause a zero division
    #        error. Imma try it.
