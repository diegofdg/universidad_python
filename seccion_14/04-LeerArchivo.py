print('*** Leer Archivo con Python ***')

nombre_archivo = 'mi_archivo.txt'

# Leer un archivo usando el metodo readlineas
with open(nombre_archivo, 'r') as archivo:
    # Leer todas las lineas del archivo
    #print(archivo.readlines())
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())

# Leer el contenido del archivo usando read
print('Leyendo el contenido con el metodo read')
with open(nombre_archivo, 'r') as archivo:
    print(archivo.read().strip())