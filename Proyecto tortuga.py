#IMPORTAMOS TODOS LOS ATRIBUTOS
# DE LA BIBLIOTECA
from turtle import *
import turtle
shape ('classic')
color ("#ff6e26")
width(4)

#LLEVAMOS EL "PUNTERO" A:
penup()
goto (90,90)
pendown();

#DIBUJA LINEA DE LLEGA
for _ in range(4):
    forward(80)
    left(90);

shape("square")
color("black")
forward(10)
left(90)
forward(10);

for _ in range(2):
    stamp()
    penup()
    forward(30)
    pendown()
    stamp();

penup()
right(90)
forward(20)
right(90)
forward(15);

for _ in range (1):
    pendown()
    stamp()
    penup()
    forward(30)
    pendown()
    stamp();

penup()
forward(15)
left(90)
forward(20)
left(90);
for _ in range(2):
    stamp()
    penup()
    forward(30)
    pendown()
    stamp();

penup()
right(90)
forward(20)
right(90)
forward(15);

for _ in range (1):
    pendown()
    stamp()
    penup()
    forward(30)
    pendown()
    stamp();

penup()
goto(90,90)
pendown()
shape("classic")
color ("#ff6e26")
left(90);

#DIBUJA 2DO CUADRADO
for _ in range(4):
    back(80)
    right(90);
left(180);



#DIBUJA 3ER CUADRADO
for _ in range(4):
    forward(80)
    left(90);
#AVANZA
left(90)
forward(80);

#DIBUJA 4TO CUADRADO
for _ in range(4):
    forward(80)
    right(90);
#AVANZA
right(90)
forward(80);


#DIBUJA 5TO CUADRADO
for _ in range(4):
    forward(80)
    left(90);

#CONFIGURAMOS A MANUELITA
shape("turtle")
penup()
goto(-40,-30)
pendown()
right(180)
color("green")
stamp()
width(4)
pencolor("#64ff33")
turtle.pen(speed=0.3);

#COMIENZA RECORRIDO
forward(95)
left(90)
forward(160)
right(90)
forward(70)
turtle.speed(8)
right(2160);


done();






