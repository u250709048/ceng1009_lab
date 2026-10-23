import turtle
#
def drawPoly(someturtle, somesides, somesize):
    angle = 360 / somesides
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(angle)

def drawSpiral(someturtle,angle):
    size=1
    for i in range(100):
        someturtle.forward(size)
        someturtle.right(angle)
        size=size+2


def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)



def drawStar(someturtle,size):
    for i in range(5):
        someturtle.forward(size)
        someturtle.right(144)


def drawSprite(someturtle, legs, length):
    angle = 360 / legs
    for i in range(legs):
        someturtle.forward(length)
        someturtle.backward(length)
        someturtle.left(angle)



wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("pink")
tess.pensize(3)

drawPoly(tess, 8, 50)







#exercise3
# tess.pencolor("blue")
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# drawSpiral(tess,90)
#
# tess.penup()
# tess.goto(150,0)
# tess.pendown()
# drawSpiral(tess,89)




#exercise4
# drawEquitriangle(tess,100)


#exercise5
# tess.color("hotpink")
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
#  for i in range(5):
#      drawStar(tess, 100)
#      tess.penup()
#      tess.forward(350)
#      tess.righ(144)
#      tess.pendown()




#exercise5

drawSprite(t, 15, 120)


wn.exitonclick()





