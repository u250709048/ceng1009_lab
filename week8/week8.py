# import turtle
#
# alex=turtle.Turtle()
# wn=turtle.Screen()
# height_list=(48,117,200,240,160,260,220)
#
# def barChart(t,height,color):
#     t.begin_fill(color)
#     t.left(90)
#     t.forward(height)
#     t.write(str(height))
#     t.right(90)
#     t.forward(50)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(height_list):
#     max_height=max(height_list)
#     num_bars=len(height_list)
#
#
#     border=10
#     gap=(max_height+border)/25
#     wn.bgcolor("lightgreen")
#
#     right=40+num_bars+border
#
#     top=max_height+4*border
#     wn.setworldcoordinates(-border,-bottom,-right,-top)
#
#     for height in height_list:
#         drawBar(t,height,gap)
#
#     wn.exitonclick()




# import turtle
#
# def drawBar(t,height):
#     t.begin_fill()
#     t.left(90)
#
#     if height <0:
#         t.right(90)
#         t.right(90)
#         t.forward(height)
#         t.left(90)
#
#     else:
#         t.forward(height)
#         t.right(90)
#         t.right(90)
#         t.forward(height)
#         t.left(90)
#
#     t.end_fill()
#     t.forward(10)
#
# wn = turtle.Screen()
# tess=turtle.Turtle()
# height=[48,117,-200,160,-50,260]
# drawBar(tess,height)
# wn.exitonclick()










# def findHypot(a,b):
#     return (a**2+b**2)**0.5
#
# print(findHypot(3,4))



# import math
# def findHypot(a,b):
#     return math.sqrt((a**2+b**2))
# print(findHypot(3,4))



