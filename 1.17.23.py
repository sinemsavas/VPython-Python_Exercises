from visual import *
import numpy as np

scene = display(width=550, height=580, range=8)

UpperBox = box(pos =(0,4,0), size=(7,1,7),color =color.cyan)
LeftBox =box(pos =(-4,0,0), size=(1,7,7),color =color.cyan)
RightBox =box(pos =(4,0,0), size=(1,7,7),color =color.cyan)
DownBox = box(pos =(0,-4,0), size=(7,1,7),color =color.cyan)
BackBox = box(pos=(0,0,-4), size=(7,7,1),color=color.cyan)

X = random.random()
Y = random.random()

ball = sphere(pos=(2,2), radius=0.4, color=color.white, mass=1)
ball.vel = vector(X,Y)

Xa = random.random()
Ya = random.random()

bigBall = sphere(pos=(0,0), radius=0.9, color=color.red,make_trail=True,retain=3000, mass=0.15)
bigBall.vel = vector(Xa,Ya)

t = 0
dt = 0.005
Fc = vector(0,0,0)

while True:

    rate(1000)
    ball.pos += ball.vel*dt
    bigBall.pos += bigBall.vel*dt

    distance = mag(ball.pos-bigBall.pos)
    check = (distance<(ball.radius+bigBall.radius))
    
    if(check == True):
        
        oldBall = ball.vel
        oldBigBall = bigBall.vel
        
        ball.vel = ((ball.mass-bigBall.mass)/(ball.mass+bigBall.mass))* oldBall + ((2*bigBall.mass) / (ball.mass+bigBall.mass))*oldBigBall
        bigBall.vel = ((2*ball.mass) / (ball.mass + bigBall.mass)) * oldBall - ((ball.mass - bigBall.mass) / (ball.mass + bigBall.mass)) * oldBigBall
        
    if abs(bigBall.pos.x) >= RightBox.pos.x-1.5:
        bigBall.vel.x=-bigBall.vel.x
        
    if abs(ball.pos.x) >= RightBox.pos.x-1:
        ball.vel.x = -ball.vel.x
        
    if abs(ball.pos.y) >= UpperBox.pos.y-1:
        ball.vel.y = -ball.vel.y
        
    if abs(bigBall.pos.y) >= UpperBox.pos.y-1.5:
        bigBall.vel.y = -bigBall.vel.y


    t += dt
