#CST-305
#Jacob Silveira
#ODEs using Green’s function

#ODEs:
#1.  y"+2y'+2=2x;t>=0;y(0)=y'(0)=0
#2.  y"+y=4;t>=0;y(0)=y'(0)=0

#Implementation:
#1. Solve ODEs with Greens function for implementing functions into the program
#2. dU_dx functions determined to put into code
#3. create an array for the data (x,y) so it can be plotted
#4. print out graphs

#required math libs
import numpy as np #for mathematical functions             
import matplotlib.pyplot as plt # for graph    
from scipy.integrate import odeint #to use ODEINT 

#Y as a vector to store terms
#with inputs Y and x and returning array for function #1
def dU0_dx(Y, x):                           
    return [Y[1],-2*Y[1]+2*x-2]    
#for function #2 returning array of y' and 4-y
def dU1_dx(Y, x):                           
    return [Y[1],4-Y[0]]                 

#Greens functions from solving manually 
def funct1(x):
    return (0.5*pow(x, 2))-(1.5 * x)-(0.75*np.exp(-2*x))+0.75
def funct2(x):
    return 4-(4*np.cos(x))
    
#setting up ODEint for graphing
#vector values
Y0 = [0, 0] 
#x (0-10) space defined with # of steps set to 100
xs0 = np.linspace(0, 10, 100)
#y space
ys0 = odeint(dU0_dx, Y0, xs0)   
ys0 = ys0[:,0]                  
#vector values
Y1 = [0, 0]
#x (0-10) space defined with # of steps set to 100
xs1 = np.linspace(0, 10, 100)   
#y space
ys1 = odeint(dU1_dx, Y1, xs1)   
ys1 = ys1[:,0]                  

#conditions from IVP 
x = 0   
y0 = 0  
y1 = 0  

#arrays for holding all data
xs2 = []    
ys2 = []    
xs3 = []    
ys3 = []    

#run the loop 200 times, add x and y vals to x and y space, update values and increment my 0.05
for i in range(0, 200): 
   xs2.append(x)       
   ys2.append(y0)      
   xs3.append(x)       
   ys3.append(y1)      
   y0 = funct1(x)      
   y1 = funct2(x)      
   x += 0.05           


#plotting graphs

#for ODE #1
plt.title("ODE with IVP #1")
#plting x and y
plt.xlabel("x")                                                         
plt.ylabel("y")                                                         
plt.plot(xs0, ys0, 'g-', label = "ODEint 1", linewidth = 1)             
plt.plot(xs2, ys2, 'r-', label = "Green's Function 1", linewidth = 1)   
plt.legend()                                                            
plt.show()                                                              

#for ODE 2
plt.title("ODE with IVP #2") 
#plting x and y
plt.xlabel("x")                                                         
plt.ylabel("y")                                                         
plt.plot(xs1, ys1, 'g-', label = "ODEint 2", linewidth = 1)             
plt.plot(xs3, ys3, 'r-', label = "Green's Function 2", linewidth = 1)   
plt.legend()                                                            
plt.show()                                                              

#second graph will appear after exiting the first