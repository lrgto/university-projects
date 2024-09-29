import numpy as np
import time as time
import os

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

f = open(dir+'/source/Bi-Section.csv', 'w')
# Where f is the output file for the values made by the 
# following code.

a = float(input("Enter Value to be Square Rooted: "))
# a is a use typed input and is the value to be square rooted.

n = 100
# n is maximum number of iterations to be conducted.

x_high = a 
x_low = x_high - x_high
x_mid = a/2
dx = x_high/4

start = time.clock()
# This line of code measures the time taken to calculate the 
# values.

for i in range(n):
    k = x_mid**2 - a
# k is a constant that needs to be as close to 0 as possible, 
# the equation is in reference to the workshop 10 guide.
    
    Per_err = (x_mid / np.sqrt(a)) * 100
# This equation defines the percentage of error of the 
# estimated value.

    print("Iteration No.",i)
    print("Estimate Value for", i, "=", x_mid)
    print("Percentage Error for", i, "=", Per_err, "%")
    print(k)
    print(" ")

# In the previous 5 lines, when displayed, the values for: 
# iteration, estimated value, percentage error and the 
# constant that needs to be as close to 0 as possible , then 
# follow by a gap to allow the calculated values to be 
# easily read.
    if k > 0:
        x_mid = x_mid - dx
        
    elif k < 0:
        x_mid = x_mid + dx
    
    dx = dx/2
        
    if -1e-16 < k and k < 1e-16:
        break
    
    f.write("{0}, {1}, {2}\n".format(str(i), str(x_mid), str(Per_err)))
# Saving all data to and external csv file for 
# further analysis

end = time.clock()
time = end - start

print("Enter Value to be Square Rooted =", a)
print("Final Square Rooted Value =", x_mid)
print("Total Number of Iterations =", i)
print("Percentage Error =", Per_err)
print("Total Time (In Seconds) =", time)
# Telling the script to show the user specfied data.