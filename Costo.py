#Declaramos variables
consumo_kwh: float();
costo_fijo: int();
costo_variable: float();
costo_total: float();

#Inicializamos las variables
consumo_kwh= 0.0;
costo_fijo= 0;
costo_variable= 0.0;
costo_total= 0.0;

#Proceso
consumo_kwh= float (input ("¿Cuánto fue el consumo de luz en el mes?:"));

costo_fijo= 300;
costo_variable = consumo_kwh * 60;
costo_total = costo_fijo + costo_variable;

print(f"Habiendo consumido: {consumo_kwh} Kwh, ", f"el total de tu factura de este mes será: $ {costo_total} en total.");



