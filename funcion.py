def devolver_distintos(a, b, c):
    
    suma = a + b + c
    
    numeros_ordenados = sorted([a, b, c])
    
    if suma > 15:
        return numeros_ordenados[2]  
    elif suma < 10:
        return numeros_ordenados[0]  
    else:
        return numeros_ordenados[1] 

# Prueba 
print(devolver_distintos(6, 4, 5))  
print(devolver_distintos(6, 2, 1)) 
print(devolver_distintos(10, 5, 6)) 
