import re
import graphviz

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
    def agregar_al_final1(self, dato):
        if not self.cabeza:
            self.cabeza = Nodo(dato=dato)
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(dato=dato)
        self.tamanio=self.tamanio+1
    def agregar_al_final(self, dato):
        if not self.cabeza:
            self.cabeza = Nodo(dato=dato)
            return
        elif self.encontrado(dato.iden) == False :
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(dato=dato)
            self.tamanio=self.tamanio+1
    def encontrado(self, e):
       try: 
         
        encontrar = False
        temp = self.cabeza
        while temp != None:
            if e==temp.dato.iden :
                encontrar = True
            temp = temp.siguiente      
        return encontrar


       except:
        print("algo")
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
    def imprimir_lista2(self,llave,llave1, llave2):
        nodo = self.cabeza
        while nodo != None:
            print( getattr(nodo.dato, llave)  ," => ", getattr(nodo.dato, llave1)," => ",getattr(nodo.dato, llave2)," => ")
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
    def pop(self):
        if self.cabeza is None:
            return None

        temp = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return temp.dato
    def size(self):
        contador = 0
        temp = self.cabeza 
        while temp is not None:
            contador += 1
            temp = temp.siguiente

        return contador
    def popultimo(self):
        temp:Nodo
        if self.cabeza is None:
            return None
        else:
            temp=self.cabeza
            while temp.siguiente.siguiente is not None:
                temp=temp.siguiente
            escri=temp.siguiente.dato
            temp.siguiente=None
            return escri
    def graficar(self, nombre):
        counter = 0    #grafica para mostrar con cola.graficar
        print(self.__class__.__name__)
        dot = graphviz.Digraph(comment=self.__class__.__name__+str(counter), format='png')
        dot.attr(rankdir='LR')
        dot.attr('node', shape='box')
        temp = self.cabeza
        
        while temp is not None:
            dot.node(str(counter), str("El cliente No:   "+str(counter)+"\n"+"Con id :  "+temp.dato.iden+"\n"+"Nombre: "+temp.dato.nombre))
            temp = temp.siguiente
            if temp is not None:
                dot.edge(str(counter), str(counter + 1))

            counter += 1

        dot.view('./graficas/clientes/'+nombre+str(counter))
    def graficarescritorios(self, nombre):
        counter = 0    #grafica para mostrar con cola.graficar
        print(self.__class__.__name__)
        dot = graphviz.Digraph(comment=self.__class__.__name__, format='png')
        dot.attr(rankdir='LR')
        dot.attr('node', shape='box')
        temp = self.cabeza
        
        while temp is not None:
            dot.node(str(counter), str("Escritorio No:   "+str(counter)+"\n"+"Con id :  "+temp.dato.iden+"\n"+"Nombre encargado: "+temp.dato.nombre_encargado))
            temp = temp.siguiente
            if temp is not None:
                dot.edge(str(counter), str(counter + 1))

            counter += 1

        dot.view('./graficas/escritorio/'+nombre+str(counter))           
    def graficarclientesescritoio(self, nombre):
        counter = 0    #grafica para mostrar con cola.graficar
        print(self.__class__.__name__)
        dot = graphviz.Digraph(comment=self.__class__.__name__+str(counter), format='png')
        dot.attr(rankdir='LR')
        dot.attr('node', shape='box')
        temp = self.cabeza
        
        while temp is not None:
            dot.node(str(counter), str("El cliente No:   "+str(counter)+"\n"+"Con id :  "+temp.dato.iden+"\n"+"Nombre: "+temp.dato.nombre+"\n"+"Tiempo de atencion:   "+ str(temp.dato.tiempo)+"\n"+"Tiempo de espera:    "+ str(temp.dato.tiempoespera)))
            temp = temp.siguiente
            if temp is not None:
                dot.edge(str(counter), str(counter + 1))

            counter += 1

        dot.view('./graficas/clientesescritorio/'+nombre+str(counter))