from visual import *
import random

scene = display(width=550,height=580)

myX = random.random()
myY = random.random()
myZ = random.random()

ball = sphere(pos=(0,0,0), radius=0.5, color=color.white)
ball.vel = vector(myX,myY,myZ)

wallR = box(pos=(4,0,0), size=(1,7,7),color=color.green)
wallL = box(pos=(-4,0,0), size=(1,7,7),color=color.red)
wallU = box(pos=(0,4,0), size=(7,1,7),color=color.blue)
wallD = box(pos=(0,-4,0), size=(7,1,7),color=color.orange)
wallB = box(pos=(0,0,-4), size=(7,7,1),color=color.cyan)

t = 0
dt = 0.005

while t<50:
    rate(1000)
    ball.pos += ball.vel*dt
    if abs(ball.pos.x) >= wallR.pos.x-1:
        ball.vel.x = -ball.vel.x
        if -(ball.vel.x) < 0:
            ball.color = wallL.color
        else:
            ball.color = wallR.color
    if abs(ball.pos.y) >= wallU.pos.y-1:
        ball.vel.y = -ball.vel.y
        if ball.vel.y < 0:
            ball.color = wallU.color
        else:
            ball.color = wallD.color
    if abs(ball.pos.z) >= -(wallB.pos.z+1):
        ball.vel.z = -ball.vel.z
        if ball.vel.z < 0:
            ball.color = color.white
        else:
            ball.color = wallB.color
    t += dt
