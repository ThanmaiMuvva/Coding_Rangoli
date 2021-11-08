import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
color = ("yellow","pink","light green","red","cyan","blue")
x = 190
for i in range(0,100):
    for j in range(12):
        t.pencolor(color[j % 6])
        t.circle(x - i/2 ,90)
        t.lt(90)
        t.circle(x-i/3,90)
        t.lt(60)
    x = x -10
    if x == 0:
        break
s.exitonclick()
