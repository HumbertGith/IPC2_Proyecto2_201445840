import string
import time

from archivos_py.lista import Lista_simple

class Empresa:
    iden:string 
    nombre:string
    abrebiatura:string
    lista_puntos_atencion:Lista_simple
    lista_transacciones:Lista_simple
    def __init__(self,id, nombre,abrebiatura):
        self.iden = id
        self.nombre = nombre
        self.abrebiatura = abrebiatura
        self.lista_puntos_atencion = Lista_simple()
        self.lista_transacciones = Lista_simple()
class Punto_atencion:
    iden:string
    nombre:string
    direccion:string
    lista_escritorios:Lista_simple
    lista_clientes: Lista_simple
    lista_activos=Lista_simple
    idenempresa:string
    def __init__(self,id, nombre,direccion):
        self.iden = id
        self.nombre = nombre
        self.direccion=direccion
        self.lista_escritorios = Lista_simple()
        self.lista_clientes = Lista_simple()
        self.lista_activos=Lista_simple()
        self.idenempresa=""
    
class Cliente:
    iden:string
    nombre:string
    lista_trasaciones_cliente:Lista_simple
    def __init__(self,dpi, nombre):
        self.iden = dpi
        self.nombre = nombre
        self.lista_trasaciones_cliente=Lista_simple()
class Escritorio:
    iden:string
    id_escritorio:string
    nombre_encargado:string
    cliente:Cliente
    activo:bool
    ocupado:bool
    listaatendidos:Lista_simple
    def __init__(self,id, id_escritorio,nombre_encargado):
        self.iden = id
        self.id_escritorio = id_escritorio
        self.nombre_encargado = nombre_encargado
        self.activo = False
        self.ocupado=False
        self.cliente=Cliente("","")
        self.listaatendidos=Lista_simple()
class Transaccion:
    iden:string
    nombre:string
    minutos:float
    def __init__(self,id, nombre, minutos):
        self.iden = id
        self.nombre = nombre
        self.minutos=minutos
class Transacciones_cliente:
    iden:string
    cantidad:int
    def __init__(self,iden, cantidad):
        self.iden = iden
        self.cantidad = cantidad
       

class Confi:
    iden:string
    idenempresa:string
    idenpunto:string
    escritoriosactivos:Lista_simple
    clientes_lista:Lista_simple
    def __init__(self,iden, idenempresa, idenpunto):
            self.iden = iden
            self.idenempresa = idenempresa
            self.idenpunto=idenpunto
            self.escritoriosactivos=Lista_simple()
            self.clientes_lista=Lista_simple()
class Atendido:
    iden:string
    nombre:string
    tiempo:float
    def __init__(self,iden, nombre, tiempo):
            self.iden = iden
            self.nombre = nombre
            self.tiempo=tiempo
         