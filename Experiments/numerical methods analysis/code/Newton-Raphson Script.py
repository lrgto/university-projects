import numpy as np
import time as time
import os

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

it = 0
f = open(dir+'/source/Newton Raphson Script.csv', 'w')
# Where f is the output file for the values made by the 
# following code.

n = 100
diff = 100

num = float(input("Enter Value to be Square Rooted: "))
# num is a use typed input and is the value to be square rooted.

start = time.clock()

mid = num
    
for i in range(n):
    x = mid - ((mid**2 - num)/(2*mid))
    if diff != 0:
        it = i
        diff = (((np.sqrt(num)-x)/np.sqrt(num))*100)
        mid = x
        f.write("{0}, {1}, {2}\n".format(str(it), str(mid), str(diff)))
        
    else:
        break
    
f.close()
end = time.clock()
time = end - start
# This line of code measures the time taken to calculate the 
# values.

print("The inputted number was", num, ".")
print("The root of", num, "is", x, ".")
print("This process took the program", time, "seconds.")
print("this took", it, "iterations to find")
print("Per iteration, this took", time/it, "s.")
# Telling the script to show the user specfied data.