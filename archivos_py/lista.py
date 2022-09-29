class Nodo():
    
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

class Lista_simple(): 
    def __init__(self):
        self.cabeza = None
        self.tamanio=0
    
    # Método para agregar elementos en el frente de la linked list
    def agregar_al_inicio(self, dato):
        self.cabeza = Nodo(dato=dato, siguiente=self.cabeza)  

    # Método para verificar si la estructura de datos esta vacia
    def vacio(self):
        return self.cabeza == None

    # Método para agregar elementos al final de la linked list
    def agregar_al_final(self, dato):
        if not self.cabeza:
            self.cabeza = Nodo(dato=dato)
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(dato=dato)
        self.tamanio=self.tamanio+1
    
    # Método para eleminar nodos
    def borrar_nodo(self, key):
        actual = self.cabeza
        temporal = None
        while actual and actual.dato != key:
            temporal = actual
            actual = actual.siguiente
        if temporal is None:
            self.cabeza = actual.siguiente
        elif actual:
            temporal.siguiente = actual.siguiente
            actual.siguiente = None

    # Método para obtener el ultimo nodo
    def obtener_ultimo_nodo(self):
        temp = self.cabeza
        while(temp.siguiente is not None):
            temp = temp.siguiente
        return temp.dato

    # Método para imprimir la lista de nodos
    def imprimir_lista(self,llave):
        nodo = self.cabeza
        while nodo != None:
            print( getattr(nodo.dato, llave)  ," => ")
            nodo = nodo.siguiente
    def imprimir_lista1(self):
        nodo = self.cabeza
        while nodo != None:
            print( nodo.dato ," => ")
            nodo = nodo.siguiente
    def find(self,iden):
           #debido a que el nombre viene de tipo objeto, es necesario pasarlo a String
          aux=self.cabeza
          while aux!=None:
                #Se comparan los nombres para ver si existe
                if(aux.dato.iden==iden):
                    return aux;   #si es la persona que buscamos se retorna el nodo
                    print("encontrado")
                else:
                    aux=aux.siguiente; 
    def  get(self, i):
        temp = self.cabeza
        for  j in range(i) :
            temp=temp.siguiente
        
        return temp.dato