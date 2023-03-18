#nombre del archivo: validar.py
#AUTOR: Isabella Delgado Rendón
menu="""
        Bienvenidos al registro de usuarios, llene los campos que le soliciten y seleccione un numero del 1 al 3:
        [1] Digitar su nombre
        [2] Digitar su edad
        [3] Dijitar su correo electronico
        [4] Salir
        """
print(menu)
opcion=input('entre la opcion 1, 2, 3 o 4:  ')
if opcion == '1':
        while True:
            nombre= input('digite su nombre ')
            if nombre.isalpha():
                print("su nombre es: ",nombre)
            else:
                print('su nombre esta mal digitado')
                break  
elif opcion == '2':
        while True:
            edad=input('ingrese su edad: ')
            if edad.isnumeric():
                print('Su edad es: ',edad)
            else:
                print('Ingrese una edad válida')
                break
elif opcion =='3':
        while True:
            correo = input('Ingresa tu correo:  ')
            if correo.find('@')>=0 and correo.find('.')>=0:
                print('Tu correo es ',correo)
            else:
                print('No ingresaste tu dirección de correo válido')
                break
elif opcion == '4':
    exit