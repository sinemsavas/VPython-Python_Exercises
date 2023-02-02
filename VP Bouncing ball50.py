from vpython import *
import random

scene = canvas(width=550, height=580)


wallR= box(pos= vector(4,0,0), size= vector(1,7,7), color=color.cyan)
wallL= box(pos= vector(-4,0,0), size= vector(1,7,7), color=color.red)
wallT= box(pos= vector(0,4,0), size=vector(7,1,7), color=color.blue)
wallB= box(pos= vector(0,-4,0), size=vector(7,1,7), color=color.orange)
wallBck= box(pos= vector(0,0,-4), size=vector(7,7,1), color=color.magenta)

ball=[]
n=50



for i in range(n):
    ball.append(sphere(pos= vector(0,0,0), radius=0.8, color=color.red))
    rndX = random.random()
    rndY = random.random()
    rndZ = random.random()

    ball[i].vel = vector(rndX,rndY,rndZ)

    t = 0
    dt = 0.01

    while t<50:
        rate(1000)
        ball[i].pos = ball[i].pos + ball[i].vel*dt
        if abs(ball[i].pos.x) >= wallR.pos.x-1:
            ball[i].vel.x = -ball[i].vel.x
            if ball[i].vel.x <0:
                ball[i].color = wallR.color
            else :
                ball[i].color = wallL.color
        elif abs(ball[i].pos.y) >= wallT.pos.y-1:
            ball[i].vel.y = -ball[i].vel.y
            if ball[i].vel.y <0:
                ball[i].color = wallT.color
            else :
                ball[i].color = wallB.color
        elif abs(ball[i].pos.z) >= -(wallBck.pos.z+1):
            ball[i].vel.z = -ball[i].vel.z
            if ball[i].vel.z <0:
                ball[i].color = color.white
            else :
                ball[i].color = wallBck.color
        
        t = t + dt
