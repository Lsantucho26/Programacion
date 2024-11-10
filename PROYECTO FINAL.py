#Importamosa librerias
import random;
import os;
import time; 
import sys;

#Declaramos funcion Inicio Calculadora
def fcalculadora_inicio():
      print("****************************************");
      print("*                                      *");
      print("*     Elige que necesitas convertir    *");
      print("*          en el dia de hoy:           *");
      print("*                                      *");
      print("*                                      *");
      print("*  1)Temperatura🌡️(fahrenheit_celsius)  *");
      print("*  2)Monedas/Divisas 💰                *");
      print("*  3)Unidades de Medidas📏             *");
      print("*                                      *");
      print("****************************************");
      eleccion = int(input("\nCual deseas elegir?: "));

      while eleccion <1 or eleccion >3:
        print("Por favor, ingresa una opcion valida.");
        eleccion = int(input("\nCual deseas elegir?: "));
        time.sleep(1);

      if eleccion == 1:
          fcalculadora_temp();
      elif eleccion == 2:
          fcalculadora_moneda();
      elif eleccion == 3:
           fcalculadora_medidas();

#Declaramos si seguir usando el programa
def fcontinuar_usando():      
      print("¿Quieres seguir usando el programa?:\n1) SI \n2) NO");
      eleccion = int(input());
      while eleccion <1 or eleccion >2:
        print("Por favor, ingresa una opcion valida.");
        eleccion = int(input("\nCual deseas elegir?: "));

      if eleccion == 1:
          print("\nQue agradable que decidas quedarte, sigamos...");
          time.sleep(2);
          os.system("cls");
          fcalculadora_inicio();
          
      
      elif eleccion == 2:
          print("Nos veremos pronto. ¡Buena suerte y mas que suerte!");
          time.sleep(5);
          os.system("cls");          
          quit();


#Declaramos Opciones Calculadora           
def fcalculadora_temp():
      os.system("cls");
      print("****************************************");
      print("*                                      *");
      print("*       Podras elegir convertir        *");
      print("*        entre esta opciones:          *");
      print("*                                      *");
      print("*                                      *");
      print("*       1️⃣ Fahrenheit a Celsius        *");
      print("*       2️⃣ Celsius a Fahrenheit        *");
      print("*                                      *");
      print("****************************************");
      eleccion = int(input("\nCual deseas elegir?: "));
      while eleccion <1 or eleccion >2:
        print("Por favor, ingresa una opcion valida.");
        eleccion = int(input("\nCual deseas elegir?: "));
      if eleccion == 1:
            ffahrenheit_celsius();
      elif eleccion == 2:
            fcelsius_fahrenheit();
      


def fcalculadora_moneda():
      os.system("cls");      
      print("****************************************");
      print("*                                      *");
      print("*       Podras elegir convertir        *");
      print("*        entre esta opciones:          *");
      print("*                                      *");
      print("*                                      *");
      print("*       1️⃣ Pesos a Dolar                *");
      print("*       2️⃣ Pesos a Real                 *");
      print("*       3️⃣ Pesos a Yen                  *");
      print("*       4️⃣ Pesos a Btc                  *");
      print("*                                      *");
      print("****************************************");
      eleccion = int(input("\nCual deseas elegir?: "));
      while eleccion <1 or eleccion >4:
        print("Por favor, ingresa una opcion valida.");
        eleccion = int(input("\nCual deseas elegir?: "));
      if eleccion == 1:
            fcalculadora_peso_dolar();
      elif eleccion == 2:
            fcalculadora_peso_real();
      elif eleccion == 3:
            fcalculadora_peso_yen();
      elif eleccion == 4:
            fcalculadora_peso_btc();

def fcalculadora_peso_dolar():
      os.system("cls");      
      print("****************************************");
      print("*                                      *");
      print("*       Podras elegir convertir        *");
      print("*        entre esta opciones:          *");
      print("*                                      *");
      print("*                                      *");
      print("*       1️⃣ Peso a Dolar                *");
      print("*       2️⃣ Dolar a Peso                *");
      print("*                                      *");
      print("****************************************");
      eleccion = int(input("\nCual deseas elegir?: "));
      while eleccion <1 or eleccion >2:
        print("Por favor, ingresa una opcion valida.");
        eleccion = int(input("\nCual deseas elegir?: "));
      if eleccion == 1:
            fpesos_dolar();
      elif eleccion == 2:
            fdolar_peso();

def fcalculadora_peso_real():
      os.system("cls");      
      print("****************************************");
      print("*                                      *");
      print("*       Podras elegir convertir        *");
      print("*        entre esta opciones:          *");
      print("*                                      *");
      print("*                                      *");
      print("*       1️⃣ Peso a Real                 *");
      print("*       2️⃣ Real a Peso                 *");
      print("*                                      *");
      print("****************************************");
      eleccion = int(input("\nCual deseas elegir?: "));
      while eleccion <1 or eleccion >2:
        print("Por favor, ingresa una opcion valida.");
        eleccion = int(input("\nCual deseas elegir?: "));
      if eleccion == 1:
            fpesos_real();
      elif eleccion == 2:
            freal_peso();


def fcalculadora_peso_yen():
      os.system("cls");      
      print("****************************************");
      print("*                                      *");
      print("*       Podras elegir convertir        *");
      print("*        entre esta opciones:          *");
      print("*                                      *");
      print("*                                      *");
      print("*       1️⃣ Peso a Yen                  *");
      print("*       2️⃣ Yen a Peso                  *");
      print("*                                      *");
      print("****************************************");
      eleccion = int(input("\nCual deseas elegir?: "));
      while eleccion <1 or eleccion >2:
        print("Por favor, ingresa una opcion valida.");
        eleccion = int(input("\nCual deseas elegir?: "));
      if eleccion == 1:
            fpesos_yen();
      elif eleccion == 2:
            fyen_peso();


def fcalculadora_peso_btc():
      os.system("cls");      
      print("****************************************");
      print("*                                      *");
      print("*       Podras elegir convertir        *");
      print("*        entre esta opciones:          *");
      print("*                                      *");
      print("*                                      *");
      print("*       1️⃣ Peso a Btc                  *");
      print("*       2️⃣ Btc a Peso                  *");
      print("*                                      *");
      print("****************************************");
      eleccion = int(input("\nCual deseas elegir?: "));
      while eleccion <1 or eleccion >2:
        print("Por favor, ingresa una opcion valida.");
        eleccion = int(input("\nCual deseas elegir?: "));
      if eleccion == 1:
            fpesos_btc();
      elif eleccion == 2:
            fbtc_peso();


def fcalculadora_medidas():
      os.system("cls");      
      print("****************************************");
      print("*                                      *");
      print("*       Podras elegir convertir        *");
      print("*        la opcion que quieras:        *");
      print("*                                      *");
      print("*                                      *");
      print("*       1️⃣ Metro a Kilometro            *");
      print("*       2️⃣ Gramo a Kilo                 *");
      print("*       3️⃣ Megabyte a Gigabyte          *");
      print("*                                      *");
      print("****************************************");
      eleccion = int(input("\nCual deseas elegir?: "));
      while eleccion <1 or eleccion >3:
        print("Por favor, ingresa una opcion valida.");
        eleccion = int(input("\nCual deseas elegir?: "));
      if eleccion == 1:
            fcalculadora_metro_kilo();
      elif eleccion == 2:
            fcalculadora_gramo_kilo();
      elif eleccion == 3:
            fcalculadora_mega_giga();




def fcalculadora_metro_kilo():
      os.system("cls");      
      print("****************************************");
      print("*                                      *");
      print("*       Podras elegir convertir        *");
      print("*        entre esta opciones:          *");
      print("*                                      *");
      print("*                                      *");
      print("*       1️⃣ Metro a Kilometro           *");
      print("*       2️⃣ Kilometro a Metro           *");
      print("*                                      *");
      print("****************************************");
      eleccion = int(input("\nCual deseas elegir?: "));
      while eleccion <1 or eleccion >2:
        print("Por favor, ingresa una opcion valida.");
        eleccion = int(input("\nCual deseas elegir?: "));
      if eleccion == 1:
            fmetro_km();
      elif eleccion == 2:
            fkm_m();


def fcalculadora_gramo_kilo():
      os.system("cls");      
      print("****************************************");
      print("*                                      *");
      print("*       Podras elegir convertir        *");
      print("*        entre esta opciones:          *");
      print("*                                      *");
      print("*                                      *");
      print("*       1️⃣ Gramo a Kilo                *");
      print("*       2️⃣ Kilo a Gramo                *");
      print("*                                      *");
      print("****************************************");
      eleccion = int(input("\nCual deseas elegir?: "));
      while eleccion <1 or eleccion >2:
        print("Por favor, ingresa una opcion valida.");
        eleccion = int(input("\nCual deseas elegir?: "));
      if eleccion == 1:
            fg_k();
      elif eleccion == 2:
            fk_g();


def fcalculadora_mega_giga():
      os.system("cls");      
      print("****************************************");
      print("*                                      *");
      print("*       Podras elegir convertir        *");
      print("*        entre esta opciones:          *");
      print("*                                      *");
      print("*                                      *");
      print("*       1️⃣ Megabyte a Gigabyte         *");
      print("*       2️⃣ Gigabyte a Megabyte         *");
      print("*                                      *");
      print("****************************************");
      eleccion = int(input("\nCual deseas elegir?: "));
      while eleccion <1 or eleccion >2:
        print("Por favor, ingresa una opcion valida.");
        eleccion = int(input("\nCual deseas elegir?: "));
      if eleccion == 1:
            fmb_gb();
      elif eleccion == 2:
            fgb_mg();



#Declaramos funciones TEMPERATURA
def ffahrenheit_celsius ():
    fahrenheit = int(input("Por favor, ingresa la temperatura en grados Fahrenheit: "));
    celsius = (fahrenheit -32 ) * 5.0/9.0;
    print('{} grados Fahrenheit son {} grados Celsius'.format(fahrenheit, celsius));
    fcontinuar_usando();


def fcelsius_fahrenheit():
    celsius = int(input('Ingrese la temperatura en grados Celsius: '));
    fahrenheit = 9.0/5.0 * celsius +32;
    print('{} grados Celsius son {} grados Fahrenheit'.format(celsius, fahrenheit));
    fcontinuar_usando();

#Declaramos funciones MONEDAS
def fpesos_dolar ():
      pesos = float(input("Ingresa tu total en pesos a calcular: $ "));
      dolar = pesos / DOLAR;
      print('Si tenes ${}, en total son {} dolares.'.format(pesos, dolar));
      print("-cotizacion Dolar Blue al dia 08-11-2024-");
      fcontinuar_usando();


def fpesos_real ():
      pesos = float(input("Ingresa tu total en pesos a calcular: $ "));
      real = pesos / REAL;
      print('Si tenes ${}, en total son {} reales.'.format(pesos, real));
      print("-cotizacion Real Blue al dia 08-11-2024-");
      fcontinuar_usando();


def fpesos_yen ():
     pesos = float(input("Ingresa tu total en pesos a calcular: $ "));
     yen = pesos / YEN;
     print('Si tenes ${}, en total son {} yenes.'.format(pesos, yen));
     print("-cotizacion Yen Japones al dia 08-11-2024-");
     fcontinuar_usando();


def fpesos_btc ():
     pesos = float(input("Ingresa tu total en pesos a calcular: $ "));
     btc = pesos / BTC;
     print('Si tenes ${}, en total son {} BTCs.'.format(pesos, btc));
     print("-cotizacion BTC al dia 08-11-2024-"); 
     fcontinuar_usando();


def fdolar_peso ():
      dolar = float(input("Ingresa tu total de dolares a calcular -descuida, no le diremos nada a la AFIP-: "));
      pesos = dolar * DOLAR;
      print('Si tenes {} dolares, en total son ${} pesos.'.format(dolar, pesos));
      print("-cotizacion Dolar Blue al dia 08-11-2024-");   
      fcontinuar_usando();

def freal_peso ():
      real = float(input("Ingresa tu total de reales a calcular: "));
      pesos = real * REAL;
      print('Si tenes {} reales, en total son ${} pesos.'.format(real, pesos));
      print("-cotizacion Real Blue al dia 08-11-2024-"); 
      fcontinuar_usando();

   
def fyen_peso ():
      yen = float(input("Ingresa tu total de yenes a calcular: "));
      pesos = yen * YEN;
      print('Si tenes {} yenes, en total son ${} pesos.'.format(yen, pesos));
      print("-cotizacion Real Blue al dia 08-11-2024-");
      fcontinuar_usando();


def fbtc_peso ():
      btc = float(input("Ingresa tu total de BTCs a calcular: "));
      pesos = btc * BTC;
      print('Si tenes {} BTCs, en total son ${} pesos.'.format(btc, pesos));
      print("-cotizacion Real Blue al dia 08-11-2024-");
      fcontinuar_usando();


#Declaramos funciones U.M.
def fmetro_km ():
      metro = float(input("Ingresa tu total en Metros: "));
      km = metro / 1000;
      print(f"Habiendo calculado ",metro,"metros, su conversion total a Km's es de: ",km,"Kilometros.");
      fcontinuar_usando();


def fkm_m ():
      km = float(input("Ingresa tu total en Km: "));
      m = km * 1000;
      print(f"Habiendo calculado ",km,"Km, su conversion total a Metros es de: ",m,"Kilometros.");
      fcontinuar_usando();


def fg_k ():
      g = float(input("Ingresa tu total en Gramos: "));
      k = g / 1000;
      print(f"Habiendo calculado ",g,"Gramos, su conversion total a Kilos es de: ",k,"Kilos.");
      fcontinuar_usando();


def fk_g ():
      k = float(input("Ingresa tu total en Kilos: "));
      g = k * 1000;
      print(f"Habiendo calculado ",k,"Kilos, su conversion total a Gramos es de: ",g,"Gramos.");
      fcontinuar_usando();
   
def fmb_gb ():
      mb = float(input("Ingresa tu Megabytes totales a convertir: "));
      gb = mb / 1024;
      print(f"Listo! El calculo final es:",mb,"da un total de",gb,"Giganytes.");
      fcontinuar_usando();



def fgb_mg ():
      gb = float(input("Ingresa tu Gigabytes totales a convertir: "));
      mb = gb * 1024;
      print(f"Listo! El calculo final es:",gb,"da un total de",mb,"Megabytes.");
      fcontinuar_usando();




#Declaramos CONSTANTES
DOLAR: int(); 
REAL: int();
YEN: float();
BTC: float();


#Declaramos Variables
user: str();
contra: int()
contra_2: int();
eleccion: int();

#Inicializamos Constantes
DOLAR = 1135; 
REAL= 172;
YEN = 6.54;
BTC = 82152000;


#Inicializamos Variables
user = "";
contra = 0;
contra_2 = 0;
eleccion = 0;

#Arranca nuestro Programa
os.system('cls');
print("""
                 |----------------------------------------------------------|
                 |  █▀█ █▀█ █▀█ █▄█ █▀▀ █▀▀ ▀█▀ █▀█   █▀▀ █ █▄░█ ▄▀█ █░░ ▀  |
                 |  █▀▀ █▀▄ █▄█ ░█░ ██▄ █▄▄ ░█░ █▄█   █▀░ █ █░▀█ █▀█ █▄▄ ▄  |
                 |----------------------------------------------------------|
█▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ █▀▄ █▀█ █▀█ ▄▀█   █▀▄ █▀▀   █▀▀ █▀█ █▄░█ █░█ █▀▀ █▀█ █▀ █ █▀█ █▄░█
█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ █▄▀ █▄█ █▀▄ █▀█   █▄▀ ██▄   █▄▄ █▄█ █░▀█ ▀▄▀ ██▄ █▀▄ ▄█ █ █▄█ █░▀█

                                 █▀▄▀█ ▄▀█ █▀▀ █ █▀▀ ▄▀█
                                 █░▀░█ █▀█ █▄█ █ █▄▄ █▀█""");
time.sleep(6);
os.system('cls');

user = input("Antes de comenzar, logueate ingresando tu Nombre: ");
print(f"Muy bien ",user,"a continuacion te brindaremos 5 digitos para que accedas por primer vez.\nIngresalos en el campo 'Contraseña'.\nRecuerda que tienes 3 intentos para ello.");
time.sleep(6);

contra = random.randint(0,99999);
print(contra);

contra_2 = int(input("Contraseña: "));

#Comienza autenticación
cont = 3;
while contra_2 != contra and cont > 1 :
        cont -= 1;
        print(f"Te quedan ",cont,"intentos");
        contra_2 = int(input("Contraseña: "));

if cont <= 1 and contra_2 != contra :
        print("Lo lamentamos, se ha bloqueado tu acceso.\nIntentalo nuevamente más tarde.")
        sys.exit();
        time.sleep(6);
        os.system('cls');
else:
       print(f"Felicitaciones",user.upper(), "ingresaste al sistema.")
       time.sleep(6);
       os.system('cls');

#Si esta Ok! Muestra menú
fcalculadora_inicio()
while eleccion <1 or eleccion >3:
        print("Por favor, ingresa una opcion valida.");
        eleccion = int(input("\nCual deseas elegir?: "));
        
        if eleccion == 1:
            fcalculadora_temp();
        elif eleccion == 2:
            fcalculadora_moneda();
        elif eleccion == 3:
            fcalculadora_medidas();
      
    









