# Programa: Ejemplo de concatenacion de cadenas

# 1. Usando el operador +
nombre = "Lucia"
apellido = "Garcia"
nombre_completo = nombre + " " + apellido
print("Usuando + : " + nombre_completo)

# 2. Usando el metodo print
edad = 28
print("Usando comas:", "Nombre", nombre_completo, ", Edad:", edad)

# 3. Usando f-strings
ciudad = "Barcelona"
pais = "España"
profesion = "Ingeniera"
presentacion = f"Hola, soy {nombre_completo}, tengo {edad + 1} años y soy {profesion} en {ciudad}, {pais}"
print(presentacion)