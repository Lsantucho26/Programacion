from getpass import *;

#Declaramos constantes
PASS: str();

#Declaramos variables
user: str();
contra: str();

#Inicializamos
PASS= "estudiante2024";
user= "";
contra= "";

#Proceso
user= input("Ingresa tu usuario D.N.I.: ");
contra= getpass("Ingresa tu contraseña: ");

if contra == PASS:
        print("""
               ***************************
               *                         *
               *    INGRESO CORRECTO     *
               *  Bienvenido al Campus!  *
               *                         *
               ***************************""");
else:
        print(f"Contraseña incorrecta. Ingresaste: {contra}");
        print("Intentalo nuevamente");