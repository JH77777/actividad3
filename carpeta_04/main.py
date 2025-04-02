# Estudiante: corrige este código y haz un pull request con la versión corregida.
with open('datos.txt', 'w') as archivo:
    archivo.write('Hola')
with open('datos.txt', 'r') as archivo:
    print(archivo.read())