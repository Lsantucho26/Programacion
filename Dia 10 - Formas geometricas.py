#Importamos librerias
import math;
import os;
import time;

#Declaramos funciones
def fcirculo (radio):
        radio = float(input("Ingresa el radio de tu circulo: "))
        area = math.pi * (radio**2);
        perimetro = 2 * math.pi * radio;
        print ("El Area de tu circulo es: " + str(area));
        print("El perime de tu circulo es: " + str(perimetro));


def fcuadrado (lado):
        lado = float(input("Ingresa el lado de tu cuadrado: "))
        area = lado**2;
        perimetro = 4 * lado;
        print ("El Area de tu cuadrado es: " + str(area));
        print("El Perimetro de tu cudrado es: " + str(perimetro));


def ftriangulo (base, altura, l1, l2, l3):
        base = float(input("Ingresa la base de tu triangulo: "));
        altura = float(input("Ingresa la altura de tu triangulo: "));
        l1 = float(input("Ingresa el 1er lado de tu triangulo: "));
        l2 = float(input("Ingresa el 2do lado de tu triangulo: "));
        l3 = float(input("Ingresa el 3er lado de tu triangulo: "))
        area = (base*altura) / 2;
        perimetro = l1+l2+l3;
        print ("El Area de tu triangulo es: " + str(area));
        print("El Perimetro de tu triangulo es: " + str(perimetro));


def frectangulo (base, altura):
        base = float(input("Ingresa la base de tu rectangulo: "));
        altura = float(input("Ingresa la altura de tu rectangulo: "));
        area = base * altura;
        perimetro = 2 * (base + altura);
        print ("El Area de tu rectangulo es: " + str(area));
        print("El Perimetro de tu rectangulo es: " + str(perimetro));



#Declaramos Varibles
eleccion: int();


#Inicializamos
eleccion= 0;

#Comienza programa
os.system("cls");
print("""
¡Bienvenido! En el dia de hoy te ayudaremos a calcular el área y el perímetro de algunas formas geometricas.\n A continuacion podras elegir tu figura""")
time.sleep(10);
os.system("cls");

print("""
Figuras disponibles:
      
1. Círculo ◍
2. Cuadrado ◼
3. Triángulo 🔺
4. Rectángulo 🔲""")
time.sleep(4);

#User elige su opcion
eleccion = int(input("Escoge tu opcion: "));
time.sleep(2);
os.system("cls");

#Segun eleccion, con condicionales, llamamos funcion para calcular
if eleccion == 1:
       fcirculo(0);
elif eleccion ==2:
        fcuadrado(0);
elif eleccion == 3:
        ftriangulo(0,0,0,0,0);
elif eleccion == 4:
        frectangulo(0,0);
else:
        print("Error");
