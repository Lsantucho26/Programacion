#Declaramos las variables
num_user: int();
resto: int();

#Inicializamos variables
num_user= 0;
resto= num_user % 2;

#Importamos librerias
import os;
import time;

#Proceso
print("Hola! Nos enteramos que querias comprobar si tu numero, es un numero PAR o IMPAR");
time.sleep(6);
os.system("cls");

print("Nos alegra saber que quieras aprender. Nosotros podemos ayudarte!");
time.sleep(6);
os.system("cls");

num_user= int(input("Primero debemos saber tu numero, ingresalo a continuacion -----> "))

#Creamos nuestras condiciones e imprimimos por pantalla
if resto == 0:
    print("El numero que ingresaste, ", num_user,  ", es un numero PAR.")

else:
    print("El numero que ingresaste, ",num_user, ", es un numero IMPAR.")

