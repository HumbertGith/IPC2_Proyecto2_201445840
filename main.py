
from pydoc import cli
import threading
import time
from tkinter import filedialog, messagebox
from archivos_py.clases import Escritorio, Punto_atencion
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
manejo=uic.loadUi("ventanas/manejo_puntos.ui")
estadopunto=uic.loadUi("ventanas/estado_punto.ui")
cliente=uic.loadUi("ventanas/solicitud_cliente.ui")
simular=uic.loadUi("ventanas/simular_punto.ui")

lista_empresas=Lista_simple()
listaconfi=Lista_simple()
punto=Punto_atencion("","","")
metodo= Metodos
inicio=time.time()

menu.setWindowFlag(QtCore.Qt.FramelessWindowHint)
config.setWindowFlag(QtCore.Qt.FramelessWindowHint)
seleccion.setWindowFlag(QtCore.Qt.FramelessWindowHint)
manejo.setWindowFlag(QtCore.Qt.FramelessWindowHint)
estadopunto.setWindowFlag(QtCore.Qt.FramelessWindowHint)
cliente.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#simular.setWindowFlag(QtCore.Qt.FramelessWindowHint)
manual.setWindowFlag(QtCore.Qt.FramelessWindowHint)

#metodos de navegacion entre ventanas
def cerrar_v():
       menu.close()
def ir_config():
       menu.hide()
       config.show()
def ir_manejo():
       menu.hide()
       manejo.show()
def ir_manejo_estadopunto():
       manejo.hide()
       estadopunto.show()
def ir_manejo_solicitudcliente():
       manejo.hide()
       cliente.show()
def ir_cliente_manejo():
       
       cliente.hide()
       manejo.show()
def ir_estadopunto_manejo():
       estadopunto.hide()
       manejo.show()
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
def ir_manejo_a_menu():
       manejo.hide()
       menu.show()
def ir_manejo_a_simular():
       manejo.hide()
       simular.show()
def ir_simular_a_manejo():
       simular.hide()
       manejo.show()
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
             
              punto.lista_escritorios.imprimir_lista("ocupado")
              
              punto.lista_clientes.imprimir_lista("nombre")
              metodo.moverescritorioinactivo(punto)
              #inicio =time.time()
              #tiempo=metodo.atender_cliente(punto,lista_empresas)
              
              #final=time.time()
             
              #print(final-inicio)
              
       except:
              messagebox.showerror("error","No se pueden mostrar datos vacios")
def activar_escri():
       try:
              metodo.activar_escritorios(punto)
              messagebox.showinfo("info","escritorio activado correctamente")
       except:
              messagebox.showerror("error","Error de activacion de escritorio") 
def desactivar_escri():
       try:
              metodo.desactivar_escritorios(punto)
              messagebox.showinfo("info","escritorio desactivado correctamente")
              print("****************************")
              punto.lista_activos.imprimir_lista("activo")
              punto.lista_inactivos.imprimir_lista("iden")
       except:
              messagebox.showerror("error","Error de desactivacion de escritorio") 
def atendercliente():
       inicio=time.time()
       tiempo=metodo.atender_cliente(punto,lista_empresas)
       time.sleep(tiempo)
       final=time.time()
       messagebox.showinfo("info","Cliente atendido correctamente su tiempo fue:    "+str(final-inicio))
      
def atenderclientebtn():
       try: 
              fin= time.time()
              espera=fin-inicio  
              escri:Escritorio
              #punto.lista_clientes.graficar("cliente")
              metodo.desencolarcliente(punto,espera)
              #punto.lista_clientes.graficar("cliente")
              #punto.lista_activos.graficarescritorios("Escritorio")
              for i in range(punto.lista_activos.size()):
                     escri=punto.lista_activos.get(i)
                     print("*************************************")
                     escri.cliente.lista_trasaciones_cliente.imprimir_lista("iden")
                     punto.lista_activos.imprimir_lista("ocupado")
                     #escri.listaatendidos.graficar("ClienteEscritorio")
                     
              for i in range(punto.lista_activos.size()):
                     escri=punto.lista_activos.get(i)
                     if escri.activo==True and escri.ocupado==True:
                           
                            timer = threading.Timer(1.0, atendercliente)
                            timer.start()
                     
              
                      
       except:
              messagebox.showerror("error","Error en la atencion del cliente") 
def calculo_porescritorio():
       try:
              cadena=metodo.calculo_atencion(punto)
              cadena2=metodo.calculo_atenciondesactivado(punto)
              estadopunto.textEditinfo.setPlainText(str(cadena+cadena2))
       except:
              messagebox.showerror("error","De calculo de atencion") 
def calculo_porpunto():
       try:
              estadopunto.labelpunto.setText("Punto atencion  "+str(punto.iden))
              estadopunto.labelescriactivo.setText("Escritorios activos            "+str(metodo.devolveractivos(punto)))
              estadopunto.labelescridesactivo.setText("Escritorios Inactivos            "+str(metodo.devolverdesactivos(punto)))
              estadopunto.labelclienteespera.setText("Clientes en espera            "+str(punto.lista_clientes.size()))
              promedio, maxi, mini=metodo.sumaresperapopunto(punto)
              estadopunto.labeltiempopromedioespera.setText("Tiempo promedio de espera            "+str(promedio))
              estadopunto.labeltiempomaxespera.setText("Tiempo max de espera             "+str(maxi))
              estadopunto.labeltiempominespera.setText("Tiempo min espera             "+str(mini))
              promedioatencion,maxiatencion,ministencion=metodo.sumaratencionporpunto(punto)
              estadopunto.labeltiempopromedioatencion.setText("Tiempo promedio de atencion            "+str(promedioatencion))
              estadopunto.labeltiempomaxatencion.setText("Tiempo max atencion             "+str(maxiatencion))
              estadopunto.labeltiempominatencion.setText("Tiempo min atencion             "+str(ministencion))
              messagebox.showinfo("info","Calculo correcto")
       except:
              messagebox.showerror("error","De calculo de atencion") 
def mostraropempresa():
       try:
              #cadena=metodo.calculo_atencion(punto)
              cadena=metodo.mostraropempresa(punto,lista_empresas)
              cliente.textEditinfo.setPlainText(str(cadena))
       except:
              messagebox.showerror("error","No hay Transacciones por mostrar") 
def agregarclientemanual():
       try:
              iden= cliente.lineEditDPI.text()
              nombre=cliente.lineEditnombre.text()
       
              metodo.agregarclientemanual(punto,iden,nombre)
              messagebox.showinfo("info","cliente agregado de forma  correcta"+"   Debes esperar "+str(punto.tiempopromedio))
       except:
              messagebox.showerror("error","Error al agregar cliente")  
def agregaropclientemanual():
       try:
              dpi= cliente.lineEditDPI.text()
              iden= cliente.lineEditidtransaccion.text()
              numero=cliente.lineEditnumero.text()
       
              metodo.agregaropclientemanual(punto,dpi,iden,int(numero))
              messagebox.showinfo("info","Opracion agregada correctamente ")
       except:
              messagebox.showerror("error","la opracion no corresponde al cliente o no exixte") 

def calculo_porescritoriosimular():
       try:
              cadena=metodo.calculo_atencionsimular(punto)
              cadena2=metodo.calculo_atenciondesactivadosimular(punto)
              simular.textEditinfo.setPlainText(str(cadena+cadena2))
              for i in range(punto.lista_activos.size()):
                            escri=punto.lista_activos.get(i)
                            escri.listaatendidos.graficarclientesescritoio("clientesescri")
       except:
              messagebox.showerror("error","De calculo de atencion")   
def calculo_porpuntosimular():
       try:
              simular.labelpunto.setText("Punto atencion  "+str(punto.iden))
              simular.labelescriactivo.setText("Escritorios activos            "+str(metodo.devolveractivos(punto)))
              simular.labelescridesactivo.setText("Escritorios Inactivos            "+str(metodo.devolverdesactivos(punto)))
              simular.labelclienteespera.setText("Clientes en espera            "+str(punto.lista_clientes.size()))
              promedio, maxi, mini=metodo.sumaresperapopunto(punto)
              simular.labeltiempopromedioespera.setText("Tiempo promedio de espera            "+str(promedio))
              simular.labeltiempomaxespera.setText("Tiempo max de espera             "+str(maxi))
              simular.labeltiempominespera.setText("Tiempo min espera             "+str(mini))
              promedioatencion,maxiatencion,ministencion=metodo.sumaratencionporpunto(punto)
              simular.labeltiempopromedioatencion.setText("Tiempo promedio de atencion            "+str(promedioatencion))
              simular.labeltiempomaxatencion.setText("Tiempo max atencion             "+str(maxiatencion))
              simular.labeltiempominatencion.setText("Tiempo min atencion             "+str(ministencion))
              messagebox.showinfo("info","Calculo correcto")
       except:
              messagebox.showerror("error","De calculo de atencion")

def atenderclientebtnsimular():
       try: 
              
                     #punto.lista_clientes.graficar("cliente")
              
                     fin= time.time()
                     espera=fin-inicio  
                     escri:Escritorio
                     punto.lista_clientes.graficar("cliente")
                     metodo.desencolarcliente(punto,espera)
                     punto.lista_clientes.graficar("cliente")
                     punto.lista_activos.graficarescritorios("Escritorio")
                            
                            
                     for i in range(punto.lista_activos.size()):
                            escri=punto.lista_activos.get(i)
                            if escri.activo==True and escri.ocupado==True:
                            
                                   timer = threading.Timer(1.0, atendercliente)
                                   timer.start()
                                   
                     
       except:
              messagebox.showerror("error","Error en la atencion del cliente")  
menu.bt_cerrar.clicked.connect(cerrar_v)            
menu.bt_conf.clicked.connect(ir_config)
menu.bt_seleccionar.clicked.connect(ir_seleccion)
menu.btn_manejo.clicked.connect(ir_manejo)

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

manejo.bt_regresar.clicked.connect(ir_manejo_a_menu)
manejo.bt_activar.clicked.connect(activar_escri)
manejo.bt_desactivar.clicked.connect(desactivar_escri)
manejo.btn_atender.clicked.connect(atenderclientebtn)
manejo.bt_verestado.clicked.connect(ir_manejo_estadopunto)
manejo.btn_solicitud.clicked.connect(ir_manejo_solicitudcliente)
manejo.btn_simular.clicked.connect(ir_manejo_a_simular)

estadopunto.bt_regresar.clicked.connect(ir_estadopunto_manejo)
estadopunto.btnporescritorio.clicked.connect(calculo_porescritorio)
estadopunto.btnempresa.clicked.connect(calculo_porpunto)

cliente.bt_regresar.clicked.connect(ir_cliente_manejo)
cliente.btn_mostrar.clicked.connect(mostraropempresa)
cliente.btncliente.clicked.connect(agregarclientemanual)
cliente.btntransaccion.clicked.connect(agregaropclientemanual)

simular.bt_regresar.clicked.connect(ir_simular_a_manejo)
simular.btnempresa.clicked.connect(calculo_porpuntosimular)
simular.btnporescritorio.clicked.connect(calculo_porescritoriosimular)
simular.btnsimular.clicked.connect(atenderclientebtnsimular)
menu.show()
app.exec()
for i in range(punto.lista_activos.size()):
              escri=punto.lista_activos.get(i)
              print("*************************************")
              escri.listaatendidos.imprimir_lista2("iden","nombre","tiempoespera")
              #escri.listaatendidos.graficar("ClienteEscritorio")
              print("***")
