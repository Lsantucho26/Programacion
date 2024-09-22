#Constantes
A: str();
E: str();
I: str();
O: str();
U: str();
VOCALES: str();

#Declaramos las variables
letra_user: str();

#Inicializamos variables
A= "a" or "A";
E= "e" and "E";
I= "i" and "I";
O= "o" and "O";
U= "u" and "U";
VOCALES= A,E,I,O,U;
letra_user= "";

#Importamos librerias
import os;
import time;

#Proceso
os.system("cls");
print("Bienvenido nuevamente! Escuchamos que tambien estas aprendiendo a diferenciar entre Letras y Vocales!");
time.sleep(6);
os.system("cls");

print("Eso es algo muy bueno y util para la vida cotidiana!");
time.sleep(6);
os.system("cls");

letra_user= str(input("Para ayudarte primero debemos conocer tu letra-----> "))

#Creamos nuestras condiciones e imprimimos por pantalla
if letra_user == A  or letra_user == E or letra_user == I or letra_user == O or letra_user == U:
      print("La letra que ingresaste, ", letra_user.upper(), ", es una VOCAL.")
else:
     print("La letra que ingresaste, ", letra_user.upper(), ", efectivamente es una LETRA.")

