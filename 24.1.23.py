from visual import *
import numpy as np
import math
scene = display(width=550, height=580)

mass = 1
t = 0
L1=1
L2= 1.0000000001
g=9.8

g2=9.80000000001

#pivot=sphere(pos=(0,0,0),radius=0.1,color=color.red)#starting
ball1=sphere(pos=vector(0,0,0), radius=0.1, color = color.cyan, opacity=0.6)
pendulum1=cylinder(pos=vector(0,0,0), axis=ball1.pos-vector(0,0,0), radius=0.015, color=color.yellow)

ball2=sphere(pos=ball1.pos-vector(0,L1,0), radius=0.1, color = color.cyan, opacity=0.6)
pendulum2=cylinder(pos=ball1.pos, axis=ball2.pos-ball1.pos, radius=0.015, color=color.yellow)

#ball3=sphere(pos=(0,0,0), radius=0.1, color = color.red, opacity=0.6)
#pendulum3=cylinder(pos=(0,0,0), axis=ball3.pos-pivot.pos, radius=0.015, color=color.red)
#ball4=sphere(pos=ball3.pos-vector(0,L2,0), radius=0.1, color = color.red, opacity=0.6)
#pendulum4=cylinder(pos=ball3.pos, axis=ball4.pos-ball3.pos, radius=0.015, color=color.red)


theta1 = 3.14
theta2 =0
omega1 = 3.14-0.1#3.04
omega2 = 0

ball1.pos=vector(0,0,0)+vector(L1*sin(theta1),-L1*cos(theta1),0)
ball2.pos=ball1.pos+vector(L1*sin(theta2),-L1*cos(theta2),0)

#ball3.pos=pivot.pos+vector(L2*sin(theta1),-L2*cos(theta1),0)
#ball4.pos=ball3.pos+vector(L2*sin(theta2),-L2*cos(theta2),0)

pendulum1.axis =ball1.pos-vector(0,0,0)
pendulum2.axis =ball2.pos-ball1.pos

#pendulum3.axis =ball3.pos-pivot.pos
#pendulum4.axis =ball4.pos-ball3.pos


dt= 0.0001
while True:
    rate(5000)
    
    thetadot =(-g/L1)*(2*sin(theta1)-sin(omega1)*cos(theta1-omega1))-1/2*(theta2**2)*sin(2*theta1-2*omega1)-(omega2**2)*sin(theta1-omega1)/(1+(sin(theta1*omega1))**2)
    omegadot =(-g/L1)*(2*sin(theta1)-2*sin(omega1)*cos(theta1-omega1))-1/2*(omega2**2)*sin(2*theta1-2*omega1)+(2*(theta2**2))*sin(theta1-omega1)/(1+(sin(theta1*omega1))**2)
   
    
    theta1=theta1+theta2*dt
    theta2=theta2+thetadot*dt
    
    omega1=omega1+omega2*dt
    omega2=omega2+omegadot*dt

    ball1.pos=vector(0,0,0)+vector(L1*sin(theta1),-L1*cos(theta1),0)
    ball2.pos=ball1.pos+vector(L1*sin(theta2),-L1*cos(theta2),0)

    

    pendulum1.axis=ball1.pos-vector(0,0,0)
    pendulum2.pos=ball1.pos
    pendulum2.axis=ball2.pos-ball1.pos
    t=t+dt



    
