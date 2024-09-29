import matplotlib.pylab as plt, numpy as np, os

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Import packages: Matplotlib to plot the desired graphs.
#                  Numpy to calculate a series of equations.
qe = 2.0 #(AU)
qAu = 79.0 #(AU)
me = 7294.3 #(AU)
ke = 1.0 #(AU)
c = 137.035999 #(AU)
tA = 1e-5 #(AU)
# Presetting the constant parameters which are goin to be used within 
# this script. 
# NOTE: All units displayed are in astronomical units. NOT SI UNITS!

print("Enter the x-axis value for the particle:")
X_Par = float(input())
print("Enter the y-axis value for the particle:")
Y_Par = float(input())
# Displays message to "enter the x & y coordinates" and allows the 
# user to input values.

for X_Par in np.arange(0.00000001,0.005,0.0005):
    ri = np.array([X_Par,Y_Par]) 
    vi = np.array([0.0,0.03*c])
    rlim = np.sqrt(ri[0]**2 + ri[1]**2)*1.1
    r_x = []
    r_y = []
# If the x terms in the cartersian co-ordinates fit in the range of
# the values ditacted in line 29 then the script will run the 
# following parameters, it will match both seperate x,y interger values
# into the format of [x,y] thus giving the script a starting location
# in whcih the alpha particle emits from. 
# rlim (line 32) is a boundary that is 1.1 times the distance away 
# from the nucleas to the starting position of the alpha particle.
 
    while (np.sqrt(ri[0]**2 + ri[1]**2) < rlim):
        ai = (ke/me) * ((qAu*qe) / (np.sqrt(ri[0]**2 + ri[1]**2)**3)) * ri
        vi = (vi) + (ai * tA)
        ri = ri + (vi * tA)
        r_x.append(ri[0])
        r_y.append(ri[1])
# The following lines of script are equations dictated in the assessment
# C4 brief. These lines of script are a loop in which the script will 
# repeatedly run till the final values is suitable enought, the previous
# values will also be plotted with the final value to show the effect on 
# the alpha particle will it moves closer to the gold nucleas.

    plt.plot(r_x,r_y)
ax = plt.gca()
ax.set_aspect('equal')
plt.scatter([0],[0])
plt.savefig(dir+'/results/RSA Graph')
# These lines of script format the data recieved into a plot.