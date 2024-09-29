import math

u,I,N,R,x,L = 0.0000001,16,30,0.042,0,0.10

n = (N/2*L)
na, pa = ((x+(L/2))),((x-(L/2)))
na2, pa2 = (x+(L/2)**2),(x-(L/2)**2)

if na < 0:
    na = 0
elif pa < 0:
    pa=0
elif na2 < 0:
    na2 = 0

B = u * I * n * ((pa/math.sqrt((pa2+0.0025000000000000005)+R**2))-(na/math.sqrt(na2+R**2)))
print('B =', B)