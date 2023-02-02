from visual import *
import numpy as np

scene = display(width = 800, height= 800, range = 3*10**11)

R=15e9
G = 6.67e-11
Ms = 2e30

sun = sphere(pos = vector(0,0,0), radius = R, color = color.yellow)
mercury = sphere(pos = vector(70e9,0,0), radius = 0.2*R, color = color.green, make_trail = True)
venus = sphere(pos = vector(110e9,0,0), radius = 0.2*R, color = color.cyan, make_trail = True)
earth = sphere(pos = vector(150e9,0,0), radius = 0.2*R, color = color.blue, make_trail = True)
mars = sphere(pos = vector(250e9,0,0), radius = 0.2*R, color = color.red, make_trail = True)

mercuryVec = vector(0,47e3,0)
venusVec = vector(0,35e3,0)
earthVec = vector(0,30e3,0)
marsVec = vector(0,24e3,0)

dt = 3600

while True:
   rate(100)

   mercuryoldvec = mercuryVec
   mercuryVec = mercuryoldvec + (-G*Ms)/(mag(mercury.pos)**3)*dt*(mercury.pos)
   mercuryoldpos = mercury.pos
   mercury.pos = mercuryVec*dt + mercuryoldpos

   venusVec2 = venusVec
   venusVec = venusVec2 + (-G*Ms)/(mag(venus.pos)**3)*dt*(venus.pos)
   venus2 = venus.pos
   venus.pos = venusVec*dt + venus2

   earthVec2 = earthVec
   earthVec = earthVec2 + (-G*Ms)/(mag(earth.pos)**3)*dt*(earth.pos)
   earth2 = earth.pos
   earth.pos = earthVec*dt + earth2

   marsVec2 = marsVec
   marsVec = marsVec2 + (-G*Ms)/(mag(mars.pos)**3)*dt*(mars.pos)
   mars2 = mars.pos
   mars.pos = marsVec*dt + mars2

   


   

   

   

   
   
   



    

    




