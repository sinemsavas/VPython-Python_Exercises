from visual import *

scene = display(width=550, height=580, range=2)

#ball = sphere(pos=(0,1,0), radius=0.4)

#txt = label(pos=ball.pos,space=50, xoffset=50, yoffset=50, text="white ball",
#           height=20, color=color.white,linecolor =color.red)

#pyr = pyramid(pos=(0,0,0), size =(7,4,2), axis =(1,0,0), color=color.green)

#co = cone(pos=(0,0,0), axis =(0,6,-2), length=6, radius =3, color = color.yellow)

#eli = ellipsoid(pos=(0,0,0), axis=(1,0,0), size=(5,5,5),material=materials.plastic
                #, color= color.red)

#ar = arrow(pos=(0,0,0), axis=(1,0,0),length=5, color=color.cyan)
#ar.headwith=2


#ba = sphere(pos=(0,0,0), radius=1.5, color=color.cyan, opacity=0.6)
#ba.v = vector(5,0,0)
#ar = arrow(pos=ba.pos, axis=ba.v, color=color.green)

#ri = ring(pos=(0,0,0), axis=(1,0,0), radius=1.5, thickness=0.3, color=color.cyan)


#tt = text(pos=(0,0,0),text="Sinem \nSAVAS", height=2,align="center",depth=+10,color=color.red,
         # font="Times",material = materials.wood)
#tt1= text(pos=(-5,0,0), text="Sinem \nSavas", height=2, align="center", depth=-1,
          #color=color.red, axis=(-1,0,0))
#tt2 = text(pos=(5,0,0),text="Sinem \nSavas", height=2, align="center", color=color.blue,axis=(1,0,0))

#tt3 = text(pos=(0,8,0),text ="Sinem \nSavas", height=1, align="center",depth=-1,color=color.yellow,axis=(0,1,0))


ball = sphere()
light1 =local_light(pos=(5,0,0), color=color.red)
light2=local_light(pos=(-5,0,0), color=color.green)




sleep(2)
t=0
dt = 0.001

while 1:
    rate(500)
    # ball.pos.x = (sint(t),0,0)
    # ball.pos = (sin(t),cos(t), 0)
    #txt.pos = ball.pos
    
    #pyr.axis = 7*vector(cos(t),0,-sin(t))
    
    #eli.size = (5+t, 5,5)
    
     #ba.v = vector(5*cos(t),0,0)
     #ba.pos += ba.v*dt
     #ar.pos = ba.pos
     #ar.axis= ba.v
     #t=t+dt
    
    #ri.axis =(cos(t), -1+exp(0.06*t), sin(t))
    #t=t+dt

    
    #t +=0.01
