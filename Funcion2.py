def letras(palabra):
    
    letras_unicas = list(set(palabra))
    
    letras_unicas.sort()
    
    return letras_unicas

# Prueba 
print(letras("banana"))  
print(letras("abecedario"))