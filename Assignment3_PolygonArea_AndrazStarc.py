#imports
import math

#variable declaration
xcor = [] #x coordinates
ycor= [] #y coordinates
coordinates = [] #coordinates - temporary
A = 0 #area
Sx = 0 #section modulus X
Sy = 0 #section modulus Y
Ix = 0 #moment of inertia X
Ix = 0 #moment of inertia X
npoints = 0 #number of points for the polygon
nsides = 0 #number of sides for the polygon

#input of number of points of the polygon
nsides = int(input("Please enter the number of sides for the polygon: "))
npoints = nsides
print(f"The number of sides is {nsides}, the number of points is {npoints}.")

#input of point coordinates
print("Now input the coordinates in X and Y - consider clockwise input!")
for pointnumber in range(npoints):
    pointcoordinate = input(f"Point {pointnumber + 1} coordinates are (X, Y): ")
    coordinates = pointcoordinate.split(", ")
    xcor.append(float(coordinates[0]))
    ycor.append(float(coordinates[1]))
    print(f"Point number {pointnumber+1} is: {coordinates[0]}, {coordinates[1]}.")

#adding for the computational purposes
xcor.append(coordinates[0])
ycor.append(coordinates[1])

#calculation of area
for i in range(npoints-1):
    A += ((xcor[i+1] + xcor[i])*(ycor[i+1]-ycor[i]))/2

print(f"Area of the polygon is: {A}.")