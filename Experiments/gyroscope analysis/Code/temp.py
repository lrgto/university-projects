import matplotlib.pylab as plt, os
dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

Sx = (0.15,0.12,0.13)
Sy = (0.43,0.41,0.40)

Cx = (6.3545,4.3193,2.4444,0.0000,3.104,4.9128,6.0528)
Cy = (-0.03,-0.02,-0.01,0.00,0.01,0.02,0.03)

Nx = (0.00,6.84,9.97,12.93)
Ny = (0.00,10.47,15.25,20.53)

plt.figure()
plt.plot(Sy, Sx)
plt.ylabel('Angular Frequency (Hz)')
plt.xlabel('Angular Frequency of Precession (Hz)')
plt.title('Frequency of Precession vs Angular Frequency')
plt.savefig(dir+'/results/StillAngularFrequencyvsFrequencyofPrecession.png')

plt.figure()
plt.plot(Cy, Cx)
plt.ylabel('Angular Frequency (Hz)')
plt.xlabel('Distance (m)')
plt.title('Distance vs Angular Frequency')
plt.savefig(dir+'/results/ChangeAngularFrequencyvsFrequencyofPrecession.png')

plt.figure()
plt.plot(Nx, Ny)
plt.ylabel('Angular Frequency of Nutation (Hz)')
plt.xlabel('Angular Frequency (Hz)')
plt.title('Angular Frequency vs Angular Frequency of Nutation')
plt.savefig(dir+'/results/AngularFrequencyvsFrequencyofNutation.png')

plt.show()