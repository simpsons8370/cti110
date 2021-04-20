import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Square and Triangle')

franklin = turtle.Turtle()
franklin.shape('turtle')
franklin.color('blue')
franklin.pensize(6)

for i in [0,1,2,3]:
    franklin.forward(150)
    franklin.left(90)

franklin.penup()
franklin.backward(200)
franklin.pendown()

for f in [0,1,2]:
    franklin.forward(150)
    franklin.left(120)
    
    
    
    



