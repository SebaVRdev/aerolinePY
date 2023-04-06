"""     
    FICHERO con la logica para validar si el RUT que se ingresa este bien validado
"""
from itertools import cycle

def digito_verificador(rut): 
    split_rut = rut.split("-")
    rut_num   = split_rut[0]             #OBTENEMOS solo los numeros del RUT
    dv        = split_rut[1].upper()     #OBTENEMOS el digito verificador que ingreso el usuario lo convertimos en MAYUSCULA
    
    # CALCULAMOS el digito verificador que deberia tener el RUT
    reversed_digits = map(int, reversed(str(rut_num)))
    factors         = cycle(range(2, 8))
    s               = sum(d * f for d, f in zip(reversed_digits, factors))

    #ASIGNAMOS el digito verificador    
    dv_calculated = (-s) % 11

    #si el digito verificado es 10 entonces le asignamos 'K'
    if dv_calculated == 10:
       dv_calculated  = 'K'

    #RETORNAMOS un booleano, TRUE <- en caso de que el dv calculado sea igual al dv original que mando el usuario
    return dv == str(dv_calculated)

#print(digito_verificador('20790208-k'))
