from visual import*

scene = display(width=800,height=800)

k=1
m=1

ba1=sphere(pos=(-5,0,0),color = color.cyan)
ba2=sphere(pos=(0,10,0),color = color.cyan)
ba3=sphere(pos=(5,0,0),color = color.cyan)

V1=vector(0,0,0)
V2=vector(0,0,0)
V3=vector(0,0,0)

wa1=box(pos=(-10,0,0),size=(1,3,1),color = color.green)
wa2=box(pos=(10,0,0),size=(1,3,1),color = color.green)

sp1=helix(pos=wa1.pos, axis=ba1.pos - wa1.pos ,radius=0.05,coils=20,thickness=0.3, color = color.red)
sp2=helix(pos=ba1.pos, axis=ba2.pos - ba1.pos ,radius=0.05,coils=20,thickness=0.3, color = color.red)
sp3=helix(pos=ba2.pos, axis=ba3.pos - ba2.pos ,radius=0.05,coils=20,thickness=0.3, color = color.red)
sp4=helix(pos=ba3.pos, axis=wa2.pos - ba3.pos ,radius=0.05,coils=20,thickness=0.3, color = color.red)

dt = 0.001
sleep(3)
while True:
    rate(1000)
    P1=ba1.pos
    P2=ba2.pos
    P3=ba3.pos

    V1Old=V1
    V2Old=V2
    V3Old=V3
    
    F1=k*(vector(-10,0,0)+P2-2*P1)
    F2=k*(P1+P3-2*P2)
    F3=k*(P2 + vector(10,0,0) - 2*P3)
    
    Q1=F1
    Q2=F2
    Q3=F3

    V1=V1Old+F1*dt
    V2=V2Old+F2*dt
    V3=V3Old+F3*dt
    
    ba1.pos = P1 + V1*dt
    ba2.pos = P2 + V2*dt
    ba3.pos = P3 + V3*dt

    sp1.pos=wa1.pos
    sp1.axis=ba1.pos-wa1.pos
    sp2.pos=ba1.pos
    sp2.axis=ba2.pos-ba1.pos
    sp3.pos=ba2.pos
    sp3.axis=ba3.pos-ba2.pos
    sp4.pos=ba3.pos
    sp4.axis=wa2.pos-ba3.pos
