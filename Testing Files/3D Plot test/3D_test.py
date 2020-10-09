import matplotlib.pyplot as plt #-> 
from matplotlib import cm #-> This is important
import numpy as np #-> This is important
import math #-> mmm, this is not important
#           |-> I was not able to use functions
#from this library to take the sine and cosine
#of x2 and y2, perhaps because these are now
#arrays which were created by numpy. However,
#usning np.sin(x2) or np.cos(y2) works perfectly
#with the arrays x2, y2 that's cool! Didn't know :|

fig = plt.figure()
ax = fig.gca(projection='3d')

x,x2 = 0,0
y,y2 = 0,0
z,z2 = 0,0
x_val, y_val, z_val = [], [], []
x_val2, y_val2, z_val2 = [], [], []

for i in range (0, 1001):

    x = math.sin((i*math.pi)/180)
    y = math.cos((i*math.pi)/180)
    z = math.cos((i*math.pi)/180)

    x_val.append(x)
    y_val.append(y)
    z_val.append(z)

#ax.plot(x_val,y_val,z_val)

x2 = np.arange(-5,5, 0.1)
y2 = np.arange(-5,5, 0.1)
print("This is x2:\n")
print(x2)
print("This is y2:\n")
print(y2)
x2,y2 = np.meshgrid (x2,y2)
#Write Expression here
z2 = x2**3+y2**2+1

#Apparenty, making this grid is super important for the graph
#without this grid we cannot plot anything. Also, this function
#'meshgrid' accepts an aarray of values but it seems not to get
#along with regular lists I make in python like x_val = [] :(.
#Also we definitely need 'cm' which is imported from matplotlib
surf = ax.plot_surface(x2, y2, z2, cmap=cm.coolwarm)
plt.show()

# How does x2 and y2 look like?
print("This is x2:\n")
print(x2)
print("This is y2:\n")
print(y2)
#x2 and y2 both look different after these are used to create a
#meshgrid when printed. As expected, this 'meshgrid' thing is a
#totally different thing, it contains more than one list within.
#I will take a look at the function meshgrid to see what is it
#about.
    
    
