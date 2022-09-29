
from tkinter import filedialog
from archivos_py.lista import Lista_simple
from archivos_py.metodos import Metodos

lista_empresas=Lista_simple()
listaconfi=Lista_simple()
metodo= Metodos
file = filedialog.askopenfilename(title="abrir", filetypes=(("xml files","*.xml"),("all files", "*.*")))
metodo.leer_archivo_empresas(lista_empresas,file)
encontrado=lista_empresas.find("2567j")
lista_empresas.imprimir_lista("iden")
#print(encontrado.dato.nombre)
encontrado.dato.lista_puntos_atencion.imprimir_lista("nombre")
encontrado1=encontrado.dato.lista_puntos_atencion.find('mac45')
encontrado1.dato.lista_escritorios.imprimir_lista("id_escritorio")
encontrado.dato.lista_transacciones.imprimir_lista('iden')
file1 = filedialog.askopenfilename(title="abrir", filetypes=(("xml files","*.xml"),("all files", "*.*")))
metodo.leer_archivo_clientes(listaconfi,file1)
encontrado1.dato.lista_escritorios.imprimir_lista("activo")
#listaconfi.imprimir_lista("iden")
encontrado2=listaconfi.find("confi123")
encontrado2.dato.escritoriosactivos.imprimir_lista1()
encontrado3=encontrado2.dato.clientes_lista.find("6689758")
encontrado2.dato.clientes_lista.imprimir_lista("nombre")
encontrado3.dato.lista_trasaciones_cliente.imprimir_lista("iden")
metodo.agregarconfiguracion(lista_empresas,listaconfi)
encontrado1.dato.lista_clientes.imprimir_lista("nombre")
'''conf=listaconfi.get(0)
conf.clientes_lista.imprimir_lista("nombre")
print(conf.idenempresa)
conf1=listaconfi.get(1)
conf1.clientes_lista.imprimir_lista("nombre")
print(conf1.idenempresa)'''



