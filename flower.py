import turtle

turtle.pensize(10)
turtle.speed(10)                         #Just setting the scene

turtle.left(75)

turtle.up()
turtle.goto(100,-400)
turtle.down()

#Finished setting up

#Making the stem

turtle.color("green")

turtle.circle(1000,30)

#Stem done!

#Making the petals

turtle.color("red")

turtle.begin_fill()
for i in range(12):
    turtle.circle(100, 100)
    turtle.left(75)

    turtle.circle(100, 100)
    turtle.right(125)
turtle.end_fill()

#Petals done!

#Making the inner part 

turtle.color("yellow")

turtle.dot(200)

#done!

turtle.done()

#Flower done!!!
