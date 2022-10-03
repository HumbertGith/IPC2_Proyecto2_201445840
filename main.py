
import time
from tkinter import filedialog, messagebox
from archivos_py.clases import Punto_atencion
from archivos_py.lista import Lista_simple
from archivos_py.metodos import Metodos
from PyQt5 import QtCore
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

#cargar ventanas
menu = uic.loadUi("ventanas/menu.ui")
config = uic.loadUi("ventanas/seleccion.ui")
manual = uic.loadUi("ventanas/carga_manual.ui")
seleccion=uic.loadUi("ventanas/selecionar_empresa.ui")

lista_empresas=Lista_simple()
listaconfi=Lista_simple()
punto=Punto_atencion("","","")
metodo= Metodos

#metodos de navegacion entre ventanas
def cerrar_v():
       menu.close()
def ir_config():
       menu.hide()
       config.show()
def ir_seleccion():
       menu.hide()
       seleccion.show()
def ir_de_conf_a_menu():
       config.hide()
       menu.show()
def ir_manual():
       config.hide()
       manual.show()
def ir_selecion_a_menu():
       seleccion.hide()
       menu.show()
def ir_de_manual_a_conf():
       manual.hide()
       config.show()

def limpiar():
  try:  
    global lista_empresas
    global listaconfi
    lista_empresas=Lista_simple()
    listaconfi=Lista_simple()
    messagebox.showinfo("info","Se limpio las estructuras")
  except:
    messagebox.showerror("error","error de ejecicion")  
def cargarEmpresa():
       try:
              file = filedialog.askopenfilename(title="abrir", filetypes=(("xml files","*.xml"),("all files", "*.*")))
              metodo.leer_archivo_empresas(lista_empresas,file)
              messagebox.showinfo("info","Empresa agregada con exito")
              
       except:
              messagebox.showerror("error","El contenido del archivo no es valido o  no has selecionado un archivo")  
def cargarcliente():
       try:
               file1 = filedialog.askopenfilename(title="abrir", filetypes=(("xml files","*.xml"),("all files", "*.*")))
               metodo.leer_archivo_clientes(listaconfi,file1)
               listaconfi.imprimir_lista("idenpunto")
               metodo.agregarconfiguracion(lista_empresas,listaconfi)
               messagebox.showinfo("info","Archivo de configuracion agregado con exito")
       except:
               messagebox.showerror("error","El contenido del archivo no es valido o  no has selecionado un archivo")  
def carga_manualempresa():
       try:
              iden= manual.lineidempresa.text()
              nombre=manual.lineNombreempresa.text()
              abreviatura=manual.lineabreviatura.text()
              metodo.manualempresa(lista_empresas, iden,nombre,abreviatura)
              messagebox.showinfo("info","empresa agregada con exito")
       except:
              messagebox.showerror("error","Los datos ingresados no son validos")
def carga_manualempunto():
       try:
              idenempresa= manual.lineidempresa.text()
              idpunto=manual.lineidpunto.text()
              nombre=manual.linenombrepunto.text()
              direccion=manual.linedireccion.text()
              metodo.manualpunto(lista_empresas,idenempresa,idpunto,nombre,direccion)
              messagebox.showinfo("info","Punto de Antencion agregado con exito")
       except:
              messagebox.showerror("error","Los datos ingresados no son validos")
def carga_manualescritorio():
       try:
              idenempresa= manual.lineidempresa.text()
              idpunto=manual.lineidpunto.text()
              idescritorio=manual.lineidescritorio.text()
              id2=manual.lineid2escritorio.text()
              encargado=manual.linenombreencargado.text()
              metodo.manualescritorio(lista_empresas,idenempresa,idpunto,idescritorio,id2,encargado)
              messagebox.showinfo("info","Escritorio agregado con exito a : ")
       except:
              messagebox.showerror("error","Los datos ingresados no son validos")
def carga_manualop():
       try:
              idenempresa= manual.lineidempresa.text()
              idop=manual.lineidtransaccion.text()
              nombre=manual.linenombretransaccion.text()
              tiempo=manual.linetiempo.text()
              metodo.manualtransaccion(lista_empresas,idenempresa,idop,nombre,tiempo)
              messagebox.showinfo("info","Transaccion agregada con exito a :  ")
       except:
              messagebox.showerror("error","Los datos ingresados no son validos")
def mostrardatosempresa():
       try:
              seleccion.textEditinfo.setPlainText(str(metodo.mostrarEmpresas(lista_empresas)))
       except:
              messagebox.showerror("error","No se pueden mostrar datos vacios") 
def obtenerpuntoAtencion():
       try:
              global punto
              idenempresa= seleccion.lineEditempresa.text()
              idpunto=seleccion.lineEditpunto.text()
              punto=metodo.seleccion_punto(lista_empresas,idenempresa,idpunto)
              punto.lista_escritorios.imprimir_lista("activo")
              punto.lista_clientes.imprimir_lista("nombre")
              metodo.desencolarcliente(punto)
              punto.lista_escritorios.imprimir_lista("ocupado")
              
              punto.lista_clientes.imprimir_lista("nombre")
              inicio =time.time()
              tiempo=metodo.atender_cliente(punto,lista_empresas)
              time.sleep(tiempo)
              final=time.time()
              print("cliente atendido")
              print(final-inicio)
              for i in range(punto.lista_escritorios.tamanio+1):
                     escri=punto.lista_escritorios.get(i)
                     escri.listaatendidos.imprimir_lista("iden")
       except:
              messagebox.showerror("error","No se pueden mostrar datos vacios")
       
menu.bt_cerrar.clicked.connect(cerrar_v)            
menu.bt_conf.clicked.connect(ir_config)
menu.bt_seleccionar.clicked.connect(ir_seleccion)

config.bt_regresar.clicked.connect(ir_de_conf_a_menu)
config.bt_limpiar.clicked.connect(limpiar)
config.bt_cargarSistema_2.clicked.connect(cargarEmpresa)
config.btn_cargarArchivo.clicked.connect(cargarcliente)
config.bt_crearempresa.clicked.connect(ir_manual)

manual.bt_regresar.clicked.connect(ir_de_manual_a_conf)
manual.btnempresa.clicked.connect(carga_manualempresa)
manual.btnpunto.clicked.connect(carga_manualempunto)
manual.btnescritorio.clicked.connect(carga_manualescritorio)
manual.btntransacion.clicked.connect(carga_manualop)

seleccion.bt_regresar.clicked.connect(ir_selecion_a_menu)
seleccion.btnmostrar.clicked.connect(mostrardatosempresa)
seleccion.btnseleccion.clicked.connect(obtenerpuntoAtencion)

menu.show()
app.exec()