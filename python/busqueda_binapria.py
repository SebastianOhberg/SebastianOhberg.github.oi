objetivo = int(input('Escoge un numero: '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo) #max utiliza el valor mas alto entre dos valores
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon: #respuesta ^2 - objetivo es mayor o igual epsilon
    print(f'{bajo}, {alto}, {respuesta}') #muestra en pantalla el proceso de busqueda
    if respuesta**2 < objetivo: #algoritmo que de decide que numero es el resultado
        bajo = respuesta
    else:
        alto = respuesta
    
    respuesta = (alto + bajo) / 2 #divide entre 2 el espacio de busqueda y redefine los valores de alto y bajo

print(f'La raiz cuadrada de {objetivo} es {respuesta}' ) 