# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\DELL\Documents\IPC2_Proyecto2_201445840\ventanas\estado_punto.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setMinimumSize(QtCore.QSize(800, 600))
        self.frame.setMaximumSize(QtCore.QSize(800, 600))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel{\n"
"color: rgb(18, 82, 200);\n"
"\n"
"font: 75 12pt \"Arial Black\";\n"
"    \n"
"}\n"
"\n"
"QLabel:hover{\n"
"color: white;\n"
"\n"
"\n"
"font: 75 12pt \"Arial Black\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 75 12pt \"Arial\";\n"
"    \n"
"}\n"
"\n"
"QTextEdit{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 75 12pt \"Arial\";\n"
"    \n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt_regresar = QtWidgets.QPushButton(self.frame)
        self.bt_regresar.setGeometry(QtCore.QRect(650, 550, 141, 40))
        self.bt_regresar.setMinimumSize(QtCore.QSize(100, 40))
        self.bt_regresar.setStyleSheet("QPushButton{\n"
"background-color: rgb(18, 82, 200);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Documents\\IPC2_Proyecto2_201445840\\ventanas\\../imagenes/pngfind.com-back-png-1934895.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_regresar.setIcon(icon)
        self.bt_regresar.setIconSize(QtCore.QSize(32, 32))
        self.bt_regresar.setObjectName("bt_regresar")
        self.btnempresa = QtWidgets.QPushButton(self.frame)
        self.btnempresa.setGeometry(QtCore.QRect(510, 220, 201, 40))
        self.btnempresa.setMinimumSize(QtCore.QSize(100, 40))
        self.btnempresa.setStyleSheet("QPushButton{\n"
"background-color: rgb(18, 82, 200);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Documents\\IPC2_Proyecto2_201445840\\ventanas\\../imagenes/escritura.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnempresa.setIcon(icon1)
        self.btnempresa.setIconSize(QtCore.QSize(32, 32))
        self.btnempresa.setObjectName("btnempresa")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 0, 400, 35))
        self.label_8.setMinimumSize(QtCore.QSize(400, 35))
        self.label_8.setMaximumSize(QtCore.QSize(200, 30))
        self.label_8.setObjectName("label_8")
        self.lineidempresa = QtWidgets.QLineEdit(self.frame)
        self.lineidempresa.setGeometry(QtCore.QRect(240, 50, 231, 20))
        self.lineidempresa.setObjectName("lineidempresa")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 50, 200, 35))
        self.label_9.setMinimumSize(QtCore.QSize(200, 35))
        self.label_9.setMaximumSize(QtCore.QSize(200, 30))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(30, 80, 200, 35))
        self.label_10.setMinimumSize(QtCore.QSize(200, 35))
        self.label_10.setMaximumSize(QtCore.QSize(200, 30))
        self.label_10.setObjectName("label_10")
        self.lineNombreempresa = QtWidgets.QLineEdit(self.frame)
        self.lineNombreempresa.setGeometry(QtCore.QRect(240, 90, 231, 20))
        self.lineNombreempresa.setObjectName("lineNombreempresa")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(30, 110, 200, 35))
        self.label_11.setMinimumSize(QtCore.QSize(200, 35))
        self.label_11.setMaximumSize(QtCore.QSize(200, 30))
        self.label_11.setObjectName("label_11")
        self.lineabreviatura = QtWidgets.QLineEdit(self.frame)
        self.lineabreviatura.setGeometry(QtCore.QRect(240, 120, 231, 20))
        self.lineabreviatura.setObjectName("lineabreviatura")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(30, 150, 400, 35))
        self.label_12.setMinimumSize(QtCore.QSize(400, 35))
        self.label_12.setMaximumSize(QtCore.QSize(200, 30))
        self.label_12.setObjectName("label_12")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(30, 220, 200, 35))
        self.label_18.setMinimumSize(QtCore.QSize(200, 35))
        self.label_18.setMaximumSize(QtCore.QSize(200, 30))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(30, 190, 200, 35))
        self.label_19.setMinimumSize(QtCore.QSize(200, 35))
        self.label_19.setMaximumSize(QtCore.QSize(200, 30))
        self.label_19.setObjectName("label_19")
        self.lineidpunto = QtWidgets.QLineEdit(self.frame)
        self.lineidpunto.setGeometry(QtCore.QRect(240, 190, 231, 20))
        self.lineidpunto.setObjectName("lineidpunto")
        self.linenombrepunto = QtWidgets.QLineEdit(self.frame)
        self.linenombrepunto.setGeometry(QtCore.QRect(240, 230, 231, 20))
        self.linenombrepunto.setObjectName("linenombrepunto")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(260, 360, 200, 35))
        self.label_21.setMinimumSize(QtCore.QSize(200, 35))
        self.label_21.setMaximumSize(QtCore.QSize(200, 30))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(30, 330, 200, 35))
        self.label_22.setMinimumSize(QtCore.QSize(200, 35))
        self.label_22.setMaximumSize(QtCore.QSize(200, 30))
        self.label_22.setObjectName("label_22")
        self.lineidescritorio = QtWidgets.QLineEdit(self.frame)
        self.lineidescritorio.setGeometry(QtCore.QRect(240, 330, 231, 20))
        self.lineidescritorio.setObjectName("lineidescritorio")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(30, 290, 400, 35))
        self.label_24.setMinimumSize(QtCore.QSize(400, 35))
        self.label_24.setMaximumSize(QtCore.QSize(200, 30))
        self.label_24.setObjectName("label_24")
        self.btnporescritorio = QtWidgets.QPushButton(self.frame)
        self.btnporescritorio.setGeometry(QtCore.QRect(650, 420, 141, 40))
        self.btnporescritorio.setMinimumSize(QtCore.QSize(100, 40))
        self.btnporescritorio.setStyleSheet("QPushButton{\n"
"background-color: rgb(18, 82, 200);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"}")
        self.btnporescritorio.setIcon(icon1)
        self.btnporescritorio.setIconSize(QtCore.QSize(32, 32))
        self.btnporescritorio.setObjectName("btnporescritorio")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(30, 250, 400, 35))
        self.label_13.setMinimumSize(QtCore.QSize(400, 35))
        self.label_13.setMaximumSize(QtCore.QSize(200, 30))
        self.label_13.setObjectName("label_13")
        self.textEditinfo = QtWidgets.QTextEdit(self.frame)
        self.textEditinfo.setGeometry(QtCore.QRect(30, 400, 611, 191))
        self.textEditinfo.setObjectName("textEditinfo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Editar_curso"))
        self.bt_regresar.setText(_translate("MainWindow", "Regresar"))
        self.btnempresa.setText(_translate("MainWindow", "Punto de atencion"))
        self.label_8.setText(_translate("MainWindow", "Punto atencion"))
        self.label_9.setText(_translate("MainWindow", "Escritorios activos"))
        self.label_10.setText(_translate("MainWindow", "Escritorios Inactivos"))
        self.label_11.setText(_translate("MainWindow", "Clientes en espera"))
        self.label_12.setText(_translate("MainWindow", "Tiempo promedio de espera"))
        self.label_18.setText(_translate("MainWindow", "Tiempo min espera"))
        self.label_19.setText(_translate("MainWindow", "Tiempo max de espera "))
        self.label_21.setText(_translate("MainWindow", "POR ESCRITORIO"))
        self.label_22.setText(_translate("MainWindow", "Tiempo min atencion"))
        self.label_24.setText(_translate("MainWindow", "Tiempo max atencion"))
        self.btnporescritorio.setText(_translate("MainWindow", "Escritorios"))
        self.label_13.setText(_translate("MainWindow", "Tiempo promedio de atencion"))
        self.textEditinfo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
