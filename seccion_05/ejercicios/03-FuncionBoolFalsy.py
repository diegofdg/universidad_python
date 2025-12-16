# Programa: Funcion bool

print(f'Valor 0: {bool(0)}') # False, 0 se considera falso
print(f'Valor 1: {bool(11.0)}') # True, si es distinto de 0 se considera verdadero

print(f'Valor "": {bool("")}') # False, "" se considera falso
print(f'Valor "Hola": {bool("Hola")}') # True, cualquier cadena distinto de "" se considera verdadero

print(f'Valor None: {bool(None)}') # False, None se considera ausencia de valor