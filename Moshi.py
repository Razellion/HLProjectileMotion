from visual import *
from math import sin, cos

initialheight = 50

#the surface
ground = box(pos = vector(0,0,0), size = vector(150,0.5,5), color = color.green)
tower = box(pos = vector(3,24,0), size = vector(15,48,0), color = color.blue)

#the ball
#in here the initial height are filled
#pos = ball first position
ball = sphere(pos = vector(0, initialheight,0), radius = 1, color = color.red, make_trail = true)

#gravity
g=vector(0,-9.8,0)

#initial velocity
v0 = 10

#angle 0 because it start from 0 angle (from max height)
theta=0
ball.m=5

#vector (x velocity, y velocity)
ball.v=vector(v0,0,0)

t=0
dt=0.01
F=ball.m*g

#Drag with assumption air density and area is 1
#Drag coefficient is 0.47 (sphere)
D = vector(0,(0.47*1*v0*v0*1)/2,0)
a = (F-D)/ball.m

t0=0
#launch
while ball.pos.x<10:
  rate(100)
  ball.pos = ball.pos + ball.v * dt
  t0 = t0 + dt
  launch = ball.pos.x

#projectile motion start
while ball.pos.y>0:
  rate(100)
  ball.v = ball.v + a * dt
  ball.pos = ball.pos + ball.v * dt
  t = t + dt
  

print("Time in the air = ",t," s")
print("Range = ",(ball.pos.x)-launch," m")
