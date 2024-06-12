'''
Cree un menu para una empresa que permita guardar autos
un auto tiene una patente, un modelo y una marca
El menu debe tener las siguientes opciones :
1.- agregar auto
2.- imprimir todos los autos
3.- buscar auto por patente
4.- eliminar auto
5.- Modificar modelo por patente
6.- Guardar datos
0.- salir
'''
import csv
lista=[] #principal
#esta lista va agregabdoi en cada ciclo los nuevos autos que se agregan a la lista principal
while True:
    
    print ("        menu")
    print ("")
    print ("1-. Agregar auto")
    print ("2-. Imrimir todos los autos")
    print ("3-. Buscar auto por patente")
    print ("4-. Eliminar auto")
    print ("5-. Modificar auto")
    print ("0-. Salir")

    op=int(input("ingrese una opcion : "))

    if op==1:
        print("")
        print(".-.- A G R E G A N D O   V E H Í C U L O .-.-.-")
        print("")
        patente = input("Ingrese patente : ")
        modelo=input("ingrese modelo : ")
        marca=input("ingrese marca : ")
        #diccionario={"patente":patente,"modelo":modelo,"marca":marca}
        #lista.append(diccionario)
        nuevalista=[patente,marca,modelo]
        lista.append(nuevalista)
        print("")
        print("Vehículo agregado correctamente...")
        print("")

    elif op==2:
        print("")
        print(".-.- V E H Í C U L O S .-.-.-")
        print("")
        for autitos in lista:
            #print("Patente : ",autitos["patente"], " Marca : ",autitos["marca"], " Modelo : ",autitos["modelo"])
            
            print ("Patente : ",autitos[0], " Marca : ",autitos[1], " Modelo : ",autitos[2])
            print("-----")
    elif op==3:
        encontrado = False
        print("")
        patente=input("Ingrese patente a buscar: ")
        for autitos in lista:
            if patente==autitos[0]:
                print("DATOS VEHÍCULO BUSCADO : \n")
                print("Patente : ",autitos[0], " Marca : ",autitos[1], " Modelo : ",autitos[2]) 

                print("-----")
                encontrado = True
                break
            
        if encontrado==False:
            print("El vehículo no existe...")
        
    elif op==4:
        encontrado = False
        print("")
        patente=input("Ingrese patente a eliminar: ")
        for autitos in lista:
            if patente==autitos[0]:
                print("DATOS VEHÍCULO BUSCADO : \n")
                print("Patente : ",autitos[0], " Marca : ",autitos[1], " Modelo : ",autitos[2]) 
                lista.remove(autitos)
                print("Auto eliminado")
                print("-----")
                encontrado = True
                break
            
        if encontrado==False:
            print("El vehículo no existe...")
        


    elif op==5:
        encontrado = False
        print("")
        patente=input("Ingrese patente a actualizar: ")
        for autitos in lista:
            if patente==autitos[0]:
                print("DATOS VEHÍCULO BUSCADO : \n")
                print("Patente : ",autitos[0], " Marca : ",autitos[1], " Modelo : ",autitos[2]) 
                nuevo_modelo=input("Ingrese el nuevo modelo : ")
                autitos[2]=nuevo_modelo
                print("Auto ACTUALIZADO")
                print("-----")
                encontrado = True
                break
            
        if encontrado==False:
            print("El vehículo no existe...")

    elif op==6:
        print ("creando archivo csv")
        #with open('nombre''tipo (w/r),newline='')
        with open ('listaautos.csv','w',newline='') as listaautos:
            escritor_csv = csv.writer(listaautos)
            #se procede a escribir la primera fila del archivo que corresponde al nombre de los dato)
            escritroe_csv.writerow (['patente','marca','modelo'])

            #se procede a agregar todos los elemtos al archvivo csv
            #se agregaran los datos desde una lista

            escritor.csv.writerows(nuevalista)

    elif op==7:
        print ("abriendo archivo")

        with open ('listaautos.csv','w',newline='') as listaautos:
            lector_csv = csv.reader(listaautos)

            for fila in lector_csv:
                print (fila)

          
                            
     
        
        



    elif op==0:
        print("")
        print("chao")
        orint("Osorio weko")
        break

    else:
        print("")
        print("error, ingrese una opcion correcta")

        

            

        

            
           
