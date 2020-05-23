from turtle import *
from random import randint
speed(5)
penup()
goto(-140,140)
for step in range(15):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  for dotted in range(8):
    forward(10)
    penup()
    forward(10)
    pendown()  
  penup()
  backward(170)
  left(90)
  forward(20)
  

  
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160,100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160,70)
bob.pendown()

mike = Turtle()
mike.color('yellow')
mike.shape('turtle')

mike.penup()
mike.goto(-160,40)
mike.pendown()

elen = Turtle()
elen.color('green')
elen.shape('turtle')

elen.penup()
elen.goto(-160,10)

for twirl in range(8):
  ada.right(45)


for twirl in range(8):
  bob.left(45)

for twirl in range(8):
  mike.left(45)

for twirl in range(8):
  elen.right(45)
  

elen.pendown()

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  mike.forward(randint(1,5))
  elen.forward(randint(1,5))
