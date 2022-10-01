
from tkinter import filedialog, messagebox
from archivos_py.lista import Lista_simple
from archivos_py.metodos import Metodos
from PyQt5 import QtCore
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

#cargar ventanas
menu = uic.loadUi("ventanas/menu.ui")
config = uic.loadUi("ventanas/seleccion.ui")
manual = uic.loadUi("ventanas/carga_manual.ui")


lista_empresas=Lista_simple()
listaconfi=Lista_simple()
metodo= Metodos

#metodos de navegacion entre ventanas
def cerrar_v():
       menu.close()
def ir_config():
       menu.hide()
       config.show()

def ir_de_conf_a_menu():
       config.hide()
       menu.show()
def ir_manual():
       config.hide()
       manual.show()
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


menu.bt_conf.clicked.connect(ir_config)

config.bt_regresar.clicked.connect(ir_de_conf_a_menu)
config.bt_limpiar.clicked.connect(limpiar)
config.bt_cargarSistema_2.clicked.connect(cargarEmpresa)
config.btn_cargarArchivo.clicked.connect(cargarcliente)
config.bt_crearempresa.clicked.connect(ir_manual)
manual.bt_regresar.clicked.connect(ir_de_manual_a_conf)
menu.show()
app.exec()