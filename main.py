def pedir_confirmacion(prompt, reintentos=4, queja='Si o no, por favor!"):
    while True:
        ok = input(prompt)
        1f ok in ('s', 'S','si', 'S1','SI'):
           return True
        if ok in ('n','no','No','NO'):
           return False
        reintentos a reintentos - 1
        if reintentos ‹ 0:
           raise OSError('usuario duro')
        print (queja)
#Esta función puede ser llamada de distintas maneras:
#• pasando sólo el argumento obligatorio: 
pedir_confirmacion ('¿Realmente queres salir?')
#• pasando uno de los argumentos opcionales:
 pedir_confirmacion(/'¿Sobreescribir archivo?' , 2)