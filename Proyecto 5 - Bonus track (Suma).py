#Declaramos variables
num1: int();
num2: int();
num3: int();
user: int();

#Inicializamos varibles
num1= 0;
num2= 0;
num3= 0;
user= 0;

#Importamos libreria
import random;
import os;
import time;

#Comenzamos!
print("Que alegria encontrarte por aca!");
time.sleep(4);
print("Hoy te propondremos resolver algunos desafios matematicos");
time.sleep(4);
print("Descuida, no son nada dificiles y confiamos en tu habilidad 👻");
time.sleep(4);
print(" C O M E N C E M O S ");
time.sleep(4);
os.system("cls");

#Primer numero
num1= random.randint(0,10);
print(" ",num1);

#Segundo mumero
num2= random.randint(0,10);
print("+", num2);
print("--------")

#Resultado suma
num3= int(num1 + num2);

#Respuesta del niño
user= int(input());

if num3 == user:
   print("🌟🌟🌟 Muy bien! Felicitaciones, sabiamos que podias lograrlo! 🌟🌟🌟")
else:
    print("😮😮😮 Estuviste muy cerca, no aflojes y volve a intentarlo! 😮😮😮")