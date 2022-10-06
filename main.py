# need to make this a python file with the code

import turtle
graph = turtle.Turtle()
window = turtle.Screen()

graph.color("grey")
graph.width(1)
x = -140
graph.right(90)
for i in range(15):
  graph.penup()
  graph.goto(x, 140)
  x = x + 20
  graph.pendown()
  graph.forward(280)
y = -140
graph.left(90)
for i in range(15):
  graph.penup()
  graph.goto(-140, y)

  graph.forward(280)

graph.penup()
graph.right(90)
graph.goto(0, 140)
graph.pendown()
graph.color("red")
graph.width(5)
graph.forward(280)
graph.penup()
graph.goto(-140, 0)
graph.left(90)
graph.pendown()
graph.forward(280)
mx = float(input("What is your first term?: "))
b = float(input("What is your second term?: "))
line = turtle.Turtle()
line.penup()
line.width(3)
y2 = 20 * b
line.goto(0, y2)
line.color("blue")
line.left(45 * (0.5 * (mx - 1) + 1))
line.pendown()
line.forward(200)
line.backward(400)
