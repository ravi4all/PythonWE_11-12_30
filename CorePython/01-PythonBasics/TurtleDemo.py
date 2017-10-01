Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello")
Hello
>>> import turtle
>>> turtle.pen()
{'shown': True, 'pendown': True, 'pencolor': 'black', 'fillcolor': 'black', 'pensize': 1, 'speed': 3, 'resizemode': 'noresize', 'stretchfactor': (1.0, 1.0), 'shearfactor': 0.0, 'outline': 1, 'tilt': 0.0}
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.reset()
>>> turtle.shape("tortoise")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    turtle.shape("tortoise")
  File "<string>", line 8, in shape
  File "C:\Python36\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named tortoise
>>> turtle.shape("turtle")
>>> for i in range(4):
	turtle.forward(200)
	turtle.left(90)

	
>>> turtle.reset()
>>> for i in range(20):
	turtle.forward(200)
	turtle.left(45*i)

	
>>> turtle.reset()
>>> for i in range(20):
	turtle.forward(20*i)
	turtle.left(45)

	
>>> turtle.reset()
>>> for i in range(20):
	turtle.forward(5*i)
	turtle.left(45)

	
>>> turtle.reset()
>>> for i in range(20):
	turtle.circle(5*i)

	
>>> turtle.reset()
>>> for i in range(20):
	turtle.circle(5*i)
	turtle.left(45)

	
>>> turtle.reset()
>>> turtle.speed(0)
>>> for i in range(50):
	turtle.circle(5*i)
	turtle.left(45)

	
>>> 
