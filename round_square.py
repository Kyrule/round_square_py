import turtle

def draw_squareShape(brad):
	for i in range(0,4):
		brad.forward(100);
		brad.right(90);

def draw_square():
	window = turtle.Screen();
	window.bgcolor("red");

	brad = turtle.Turtle();
	brad.shape("turtle");
	brad.color("yellow");
	brad.speed(2);

	i=0

	while i<37:
		draw_squareShape(brad)
		brad.right(10);
		i=i+1;

	window.exitonclick();

draw_square()
