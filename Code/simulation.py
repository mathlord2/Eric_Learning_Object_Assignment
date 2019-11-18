from tkinter import *
from math import *
from time import *

print("Welcome to Eric's object-sliding simulation!")
mass = int(input("Enter the mass of the block (in kg): "))
appliedForce = int(input("Enter the amount of force you will push onto the block (in N): "))
staticFrictionCo = float(input("Enter the static friction coefficient: "))
kineticFrictionCo = float(input("Enter the kinetic friction coefficient: "))
initTime = float(input("Enter the amount of time the force will act on the block (in s): "))

interface = Tk()
s = Canvas(interface, width=600, height=600)
s.pack()

#Floor
s.create_line(0, 500, 600, 500, width=10)

#Calculations
weight = mass * 9.81
staticFrictionForce = staticFrictionCo * weight
kineticFrictionForce = kineticFrictionCo * weight
initVelocity = ((appliedForce - staticFrictionForce) * initTime) / mass
initAcceleration = (appliedForce - staticFrictionForce) / mass
acceleration = -kineticFrictionCo * 9.81
initDisplacement = initVelocity * initTime / 2

s.create_text(10, 0, text=("Weight: " + str(round(weight, 2)) + " N [down]"), anchor="nw")
s.create_text(10, 20, text=("Static Friction Force: " + str(round(staticFrictionForce, 2)) + " N [left]"), anchor="nw")

if initVelocity > 0:
    s.create_text(10, 40, text=("Initial Acceleration: " + str(round(initAcceleration)) + " m/s^2 [right]"), anchor="nw")
    s.create_text(10, 60, text=("Initial Velocity: " + str(round(initVelocity, 2)) + " m/s [right]"), anchor="nw")
    s.create_text(10, 80, text=("Kinetic Acceleration: " + str(round(-acceleration, 2)) + " m/s^2 [left]"), anchor="nw")
    s.create_text(10, 100, text=("Kinetic Friction Force: " + str(round(kineticFrictionForce, 2)) + " N [left]"), anchor="nw")
else:
    s.create_text(10, 40, text=("Initial Velocity: 0 m/s"), anchor="nw")
    s.create_text(10, 60, text=("Displacement: 0 m"), anchor="nw")

#Animation
for time in range(10000):
    time = time/10
    if initVelocity > 0:
        x1 = (initVelocity*time) + (0.5*acceleration*(time**2))
        y1 = 455

        block = s.create_rectangle(x1, y1, x1+60, y1+40, fill="orange")
        
        finalVelocity = initVelocity + acceleration*time
        if finalVelocity < 0:
            s.create_text(590, 0, text=("Displacement: " + str(round(x1+initDisplacement, 2)) + " m [right]"), anchor="ne")
            s.create_text(590, 20, text=("Total Time: " + str(time) + " s"), anchor="ne")
            break

        s.update()
        sleep(0.01)
        s.delete(block)
    
    else:
        x1 = 0
        y1 = 455
        s.create_rectangle(x1, y1, x1+60, y1+40, fill="orange")
