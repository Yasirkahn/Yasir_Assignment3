import math
# Input
x = [] 
y = []
n = int(input("no of vertices:")) 
# where, n is the number of sides/vertices and should not be less than 3.

for n in range(n):
    xplus = float(input(f"x-coordinate: "))
    yplus = float(input(f"y-coordinate: "))
    x.append(xplus)
    y.append(yplus)
print(f"\nlocation {'x':>8} {'y':>12}")
print("." * 35)
for n in range(n):
    print(f"{n+1} {x[n]:15.2f} {y[n]:15.2f}")

# For determination of various quantities
Ax= 0
print("\nDetermined quantities")
print("." * 30)
x.append(x[0])
y.append(y[0])

for i in range(n):
    xpl = (x[i+1]*y[i])
    ymi = (y[i+1]*x[i])
    Ax = ((xpl)-(ymi)) + Ax

Ax = Ax/2
print(f"Ax = {Ax:15.2f}")

Sx=0
Sy=0

for i in range(n):
    Sx = ((x[i+1] - x[i]) * (y[i+1]**2 + y[i]*y[i+1] + y[i]**2)) + Sx
    Sy = ((y[i+1] - y[i]) * (x[i+1]**2 + x[i]*x[i+1] + x[i]**2)) + Sy
Sx = Sx/-6
Sy = Sy/6
print(f"Sx=  {Sx:15.2f}")
print(f"Sy=  {Sy:15.2f}")

Ix=0
Iy=0
Ixy=0
for i in range(n):
    Ix = ((x[i+1] - x[i]) * (y[i+1]**3 + (y[i+1]**2)*y[i] + y[i+1]*(y[i]**2) + y[i]**3)) + Ix
    Iy = ((y[i+1] - y[i]) * (x[i+1]**3 + (x[i+1]**2)*x[i] + x[i+1]*(x[i]**2) + x[i]**3)) + Iy
    Ixy = ((y[i+1] - y[i]) * (y[i+1] * (3*x[i+1]**2 + 2*x[i+1]*x[i] + x[i]**2) + y[i] *(3*x[i]**2 + 2*x[i+1]*x[i] + x[i+1]**2))) + Ixy
Ix = Ix/-12
Iy = Iy/12
Ixy = Ixy/-24
print(f"Ix=  {Ix:15.2f}")
print(f"Iy=  {Iy:15.2f}")
print(f"Ixy=  {Ixy:15.2f}")
print(f"Ixt=  {Ix-(Sx/Ax)**2*Ax:15.2f}")
print(f"Iyt=  {Iy-(Sy/Ax)**2*Ax:15.2f}")
print(f"Ixyt=  {Ixy+(Sy/Ax)*(Sx/Ax)*Ax:15.2f}")