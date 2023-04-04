import os

#NOS DA la carpeta en la que estamos trabajando. automatico ruta
rutaProyecto = os.path.dirname(os.path.realpath(__file__))

# OBTENEMOS la ruta del fichero que posteriormente vamos a abrir
rutaAsientos = rutaProyecto + r'\aerolinea.txt'

listaAsientos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]

#DICCIONARIO DE USUARIOS VACIO
usuarios = {}

#METODO MOSTRAR ASIENTOS
def mostrarAsientos():
    print(f"|	{listaAsientos[0]}	{listaAsientos[1]}	{listaAsientos[2]}		{listaAsientos[3]}	{listaAsientos[4]}	{listaAsientos[5]}	|\n" +
        f"|								|\n" +
        f"|	{listaAsientos[6]}	{listaAsientos[7]}	{listaAsientos[8]}		{listaAsientos[9]}	{listaAsientos[10]}	{listaAsientos[11]}	|\n" +
        f"|								|\n" +
        f"|	{listaAsientos[12]}	{listaAsientos[13]}	{listaAsientos[14]}		{listaAsientos[15]}	{listaAsientos[16]}	{listaAsientos[17]}	|\n" +
        f"|								|\n" +
        f"|	{listaAsientos[18]}	{listaAsientos[19]}	{listaAsientos[20]}		{listaAsientos[21]}	{listaAsientos[22]}	{listaAsientos[23]}	|\n" +
        f"|								|\n" +
        f"|	{listaAsientos[24]}	{listaAsientos[25]}	{listaAsientos[26]}		{listaAsientos[27]}	{listaAsientos[28]}	{listaAsientos[29]}	|\n" +
            f"\t |__________________         __________________|\n" +
            f"\t |__________________         __________________|\n" +
        f"|	{listaAsientos[30]}	{listaAsientos[31]}	{listaAsientos[32]}		{listaAsientos[33]}	{listaAsientos[34]}	{listaAsientos[35]}	|\n" +
        f"|								|\n" +
        f"|								|\n" +
        f"|	{listaAsientos[36]}	{listaAsientos[37]}	{listaAsientos[38]}		{listaAsientos[39]}	{listaAsientos[40]}	{listaAsientos[41]}	|") 


#METODO DE LLENAR
def llenarListaOcupados(filename):
    fichero = open(filename ,'r', encoding = 'utf-8')#LEE EL TEXTO CON IDIOMA ESPANOL
    listaOcupados =[]
    
    for i in fichero:
        asientos = i[0:2]
        listaOcupados.append(asientos)
    fichero.close()  
    return listaOcupados  

ocupados = llenarListaOcupados(rutaAsientos)


#METODO DE COMPRA
def realizarCompra(rutUsuario,nombre,numAsiento,tel,precio,Banco):
    totalDescuento = 0
    indice = numAsiento - 1
    print("Numero Asiento: " + str(numAsiento) + " Precio: " + str(precio)+" Banco del Usuario: "+Banco)
    if Banco == "bancoUmayor":
        print("entro")
        totalDescuento = precio - (precio * 0.15)
    else:
        totalDescuento = precio

    listaAsientos[indice] = "X"
    usuarios[rutUsuario] = [numAsiento,nombre,tel,Banco,totalDescuento]
        

# INICIO de la aplicacion y su MENU

print('***BIENVENIDO A AEROLINEA VUELOS FREE***')
menu=(input("1.-Procesar Ventas por Internet.\n2.-Ver Asientos Disponibles.\n3.-Comprar Asiento.\n4.-Anular Vuelo.\n5.-Modificar Datos de pasajero.\n0.-Salir.\nIngrese opcion: "))

while menu != '0' :

    if menu == '1' :
        os.system('cls')
        print('***PROCESAR VENTAS POR INTERNET***')
        for ventasIn in ocupados:            
            #NUMEROS QUE EPIECEN CON 0X
            if ventasIn[0] == "0":
                indice = int(ventasIn[1]) - 1
                listaAsientos[indice] = "X"
            else:
                indice = int(ventasIn) - 1
                listaAsientos[indice] = "X"
        print("VENTAS DE ASIENTOS POR INTERNET PROCESADAS!!!")
              
    elif menu == '2' :
        os.system('cls')
        print('***ASIENTOS DISPONIBLES***')
        mostrarAsientos()
        
    elif menu == '3' :
        os.system('cls')
        print('***COMPRAR ASIENTO***')

        print('***ASIENTOS DISPONIBLES***')
        
        mostrarAsientos()
        
        #SOLICITAMOS LOS DATOS DEL PASAJERO
        nombrePasajero = input("Ingerse el nombre del pasajero : \n")
        rutPasajero=input("Ingerse el rut del pasajero : \n")
        telefonoPasajero = input("Ingrese le telefono del pasajero : \n")
        bancoPasajero = input("Ingrese el banco del pasajero : \n")
        
        asientoAComprar = int(input("Ingrese el numero del asiento que deseas comprar:\n"))
        
        while asientoAComprar not in listaAsientos:
            asientoAComprar = int(input("El asiento no se encuentra disponible, Ingrese el numero del asiento que deseas comprar:\n"))
        
        if asientoAComprar > 24 and asientoAComprar < 36:
            precioAsiento = 240000
            realizarCompra(rutPasajero,nombrePasajero,asientoAComprar,telefonoPasajero,precioAsiento,bancoPasajero)
        else:
            precioAsiento = 78900 
            realizarCompra(rutPasajero,nombrePasajero,asientoAComprar,telefonoPasajero,precioAsiento,bancoPasajero)
        print(usuarios)
                 
    elif menu == '4' :
        os.system('cls')
        print('***ANULAR VUELO***')
        sRUT = input('Ingrese su RUT para la información : ')
        if sRUT in usuarios :
            asientoUsu = usuarios[sRUT][0]
            if listaAsientos[asientoUsu - 1] == "X": 
                #SIGNIFICA QUE HAY UN ASIENTO COMPRADO
                listaAsientos[asientoUsu - 1] = asientoUsu
                del usuarios[sRUT]
                print('SE ANULO EL VUELO INGRESADO CON EXITO!')
        else:
            print("NO EXISTE ESTE RUT")

    elif menu == '5' :
        os.system('cls')
        print('MODIFICAR DATOS DE PASAJERO')

        #SOLICITA EL ASIENTO Y RUT(PARA VERIFICAR DATOS)
        sRUT = input('Ingrese su RUT para la información : ')
        #SI NO SE ENCUENTRA VOLVEMOS A SOLICITAR LA INFORMACION
        while sRUT not in usuarios and sRUT != '0':
            sRUT = input('El RUT no se encuentra, porfavor ingrese su RUT valido para verificar la información o 0 para salir. : ')

        if sRUT in usuarios :
            
            sAsiento = int(input('Ingrese el numero de asiento para verificar la información : '))
            #SI NO SE ENCUENTRA VOLVEMOS A SOLICITAR LA INFORMACION
            while sAsiento != usuarios[sRUT][0] and sAsiento != '0':
                sAsiento = int(input('El numero de asiento no se encuentra, porfavor ingrese su numero de asiento valido para verificar la información : '))

            if sAsiento == usuarios[sRUT][0]:
                #SIGNIFICA QUE EL ASIENTO ES DEL RUT ASIGNADO
                #SUBMENU CON LAS OPCIONES
                submenu = (input("1.-Modificar Nombre Pasajero.\n2.-Modificar Telefono Pasajero.\n3.-No Modificar Nada o Salir. -->"))

                while submenu != '3' :
                    if submenu == '1' :
                        print('MODIFICAR NOMBRE PASAJERO')
                        nuevoNombreP = input("Ingrese el nuevo nombre para actualizarlo : ")
                        #diccionario original
                        print(usuarios)
                        #diccionario actualizado
                        usuarios[sRUT][1] = nuevoNombreP
                        print(usuarios)

                    if submenu == '2' :
                        print('MODIFICAR TELEFONO PASAJERO')
                        nuevoTelefono = input("Ingrese el nuevo numero de telefono para actualizarlo : ")
                        #diccionario original
                        print(usuarios)
                        #diccionario actualizado
                        usuarios[sRUT][2] = nuevoTelefono
                        print(usuarios)

                    else:
                        print("Digite una opcion correcta!!")

                    submenu = (input("1.-Modificar Nombre Pasajero.\n2.-Modificar Telefono Pasajero.\n3.-No Modificar Nada o Salir. --."))

                if submenu == '3' :
                    print("NO SE HA MODIFICADO NADA!!!")
            else:
                print("EL ASIENTO INGRESADO NO COINCIDE CON EL USUARIO")
        else:
            print("EL RUT NGRESADO NO ESTA EN LOS REGISTROS")
               
    else:
        print("Digite una opcion correcta!!")

    menu=(input("1.-Procesar Ventas por Internet.\n2.-Ver Asientos Disponibles.\n3.-Comprar Asiento.\n4.-Anular Vuelo.\n5.-Modificar Datos de pasajero.\n0.-Salir.\nIngrese opcion: "))              

if menu == '0' :
    os.system('cls')
    print("Se a terminado la aplicacion!!!")