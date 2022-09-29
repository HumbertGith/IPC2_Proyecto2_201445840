from xml.dom import minidom
import xml.etree.ElementTree as ET
from archivos_py.clases import *

from archivos_py.lista import Lista_simple, Nodo

class Metodos:
    def __init__(self) -> None:
        pass
    def leer_archivo_empresas(lista:Lista_simple, archivo ):
       
        
        with open(archivo, encoding='utf-8') as file:
            if file.readable():
                xml_data= ET.fromstring(file.read())
                lst_empresas= xml_data.findall('empresa')
                
                for empre in lst_empresas:
                    empresa=Empresa("","","")
                    codigoempresa=""
                    codigo=empre.attrib.values()
                    for x in codigo:
                        codigoempresa=x
                        empresa.iden=codigoempresa
                    nombreempre=empre.find('nombre').text
                    #print(nombreempre)
                    empresa.nombre=nombreempre
                    nombreabre=empre.find('abreviatura').text
                    empresa.abrebiatura=nombreabre
                    lista.agregar_al_final(empresa)
                    listapuntos=empre.findall('listaPuntosAtencion')
                    for puntos in listapuntos:
                        idenpunto=""
                        atencionpuntos=puntos.findall('puntoAtencion')
                        for puntos in atencionpuntos:
                            codigopunto=puntos.attrib.values()
                            for x in codigopunto:
                                idenpunto=x
                        
                            nombrepuntos=puntos.find('nombre').text
                            direccionpunto=puntos.find('direccion').text
                            encontrado=lista.find(codigoempresa)
                            punto=Punto_atencion(idenpunto,nombrepuntos,direccionpunto)
                            encontrado.dato.lista_puntos_atencion.agregar_al_final(punto)
                            listaescritorio=puntos.findall('listaEscritorios')
                            for liescritorio in listaescritorio:
                                escritorios=liescritorio.findall('escritorio')
                                cod=""
                                for escritorio in escritorios:
                                    codigescri=escritorio.attrib.values()
                                    for x in codigescri:
                                        cod=x
                                    nombreiden=escritorio.find('identificacion').text
                                    nombreencagargado=escritorio.find('encargado').text
                                    escritorior=Escritorio(cod,nombreiden,nombreencagargado)
                                    nodo1=encontrado.dato.lista_puntos_atencion.find(idenpunto)
                                    nodo1.dato.lista_escritorios.agregar_al_final(escritorior)
                    listatransacciones=empre.findall('listaTransacciones')
                    for transaciones in listatransacciones:
                        transaciones1=transaciones.findall("transaccion")
                        codtrans=""
                        for transacion in transaciones1:
                            codigostran=transacion.attrib.values()
                            for x in codigostran:
                                    codtrans=x
                            nombretrasaccion=transacion.find('nombre').text
                            tiempoaten=transacion.find("tiempoAtencion").text
                            trancansion=Transaccion(codtrans,nombretrasaccion,tiempoaten)
                            encontrado.dato.lista_transacciones.agregar_al_final(trancansion)

            else:
                print(False)
    def leer_archivo_clientes(lista:Lista_simple, archivo ):
      
      
        
        with open(archivo, encoding='utf-8') as file:
            if file.readable():
                    xml_data= ET.fromstring(file.read())
              
                    lst_clientes= xml_data.findall('configInicial')
                    #encontrado2:Nodo
                    #encontrado1:Nodo
                    for client in lst_clientes:
                        cliente1=Cliente("","")
                        confi=Confi("","","")
                        
                        codigoempresa=""
                        codigo=client.attrib.values()
                        listas=[]
                        for x in codigo:
                            #print("la llvae es:" ,x)
                            
                            listas.append(x)
                        confi.iden=listas[0]
                        #print(confi.iden)
                        confi.idenempresa=listas[1]
                        
                        
                        confi.idenpunto=listas[2]
                       
                        lista.agregar_al_final(confi)
                        escritoriosactivos=client.findall('escritoriosActivos')
                        for escritorios in escritoriosactivos:
                            escri= escritorios.findall('escritorio')
                            for activos in escri:
                                for x in activos.attrib.values():
                                  #print("la llave es :" ,x)
                                  encontrado=lista.find(confi.iden)  
                                  if encontrado!=None:
                                    encontrado.dato.escritoriosactivos.agregar_al_final(x)
                        clienteslista=client.findall('listadoClientes')
                        for clientes in clienteslista:
                            clientesli=clientes.findall('cliente')
                            for cliente in clientesli:
                                for x in cliente.attrib.values():
                                    cliente1.iden=x
                                cliente1.nombre=cliente.find('nombre').text
                                encontrado.dato.clientes_lista.agregar_al_final(cliente1)
                                listadoop=cliente.findall('listadoTransacciones')
                                for listop in listadoop:
                                    lisasop=listop.findall('transaccion')
                                    for op in lisasop:
                                        
                                        x1=""
                                        for x in op.attrib.values():
                                            x1=x+","+x1
                                        x2=x1.split(',')
                                        
                                        f=x2[1]
                                        c=x2[0]
                                        opcliente=Transacciones_cliente(f,c)
                                        encontrado1=encontrado.dato.clientes_lista.find(cliente1.iden)
                                        if encontrado!=None:

                                            encontrado1.dato.lista_trasaciones_cliente.agregar_al_final(opcliente)
                   

            else:
                print(False)
    def agregarconfiguracion(listaempresa:Lista_simple, listaconfi:Lista_simple):
        tamanio=listaconfi.tamanio
        #print(tamanio)
        confi:Confi
        i=0
        for i in range(tamanio+1):
            print(i)
            confi=listaconfi.get(i)
            #print(confi.idenempresa)
            encontrado=listaempresa.find(confi.idenempresa)
            if encontrado!=None:
               
                encontrado1=encontrado.dato.lista_puntos_atencion.find(confi.idenpunto)
                if encontrado1!=None:
                    #print("algo")
                    #print(confi.clientes_lista.tamanio)
                    for i in range(confi.clientes_lista.tamanio):
                        encontrado1.lista_clientes.agregar_al_final(confi.clientes_lista.get(i))
            