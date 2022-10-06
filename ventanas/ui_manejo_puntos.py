# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\DELL\Documents\IPC2_Proyecto2_201445840\ventanas\manejo_puntos.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 400)
        MainWindow.setMinimumSize(QtCore.QSize(710, 400))
        MainWindow.setMaximumSize(QtCore.QSize(700, 400))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(710, 400))
        self.centralwidget.setObjectName("centralwidget")
        self.frame_lateral = QtWidgets.QFrame(self.centralwidget)
        self.frame_lateral.setGeometry(QtCore.QRect(0, 0, 710, 400))
        self.frame_lateral.setMinimumSize(QtCore.QSize(710, 400))
        self.frame_lateral.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_lateral.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_lateral.setAutoFillBackground(False)
        self.frame_lateral.setStyleSheet("\n"
"QFrame{\n"
"background-color: rgb(18, 82, 200);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
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
        self.frame_lateral.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_lateral.setObjectName("frame_lateral")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_lateral)
        self.verticalLayout.setContentsMargins(150, -1, 150, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_lateral)
        self.label.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color:rgb(0,0,0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.bt_verestado = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_verestado.setMinimumSize(QtCore.QSize(400, 40))
        self.bt_verestado.setMaximumSize(QtCore.QSize(200, 16777215))
        self.bt_verestado.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.bt_verestado.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Documents\\IPC2_Proyecto2_201445840\\ventanas\\../imagenes/base-de-datos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_verestado.setIcon(icon)
        self.bt_verestado.setIconSize(QtCore.QSize(32, 32))
        self.bt_verestado.setObjectName("bt_verestado")
        self.verticalLayout.addWidget(self.bt_verestado)
        self.bt_activar = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_activar.setMinimumSize(QtCore.QSize(400, 40))
        self.bt_activar.setToolTipDuration(0)
        self.bt_activar.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Documents\\IPC2_Proyecto2_201445840\\ventanas\\../imagenes/archivo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_activar.setIcon(icon1)
        self.bt_activar.setIconSize(QtCore.QSize(32, 32))
        self.bt_activar.setObjectName("bt_activar")
        self.verticalLayout.addWidget(self.bt_activar)
        self.bt_desactivar = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_desactivar.setMinimumSize(QtCore.QSize(400, 40))
        self.bt_desactivar.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Documents\\IPC2_Proyecto2_201445840\\ventanas\\../imagenes/encriptado.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_desactivar.setIcon(icon2)
        self.bt_desactivar.setIconSize(QtCore.QSize(32, 32))
        self.bt_desactivar.setObjectName("bt_desactivar")
        self.verticalLayout.addWidget(self.bt_desactivar)
        self.btn_atender = QtWidgets.QPushButton(self.frame_lateral)
        self.btn_atender.setMinimumSize(QtCore.QSize(400, 40))
        self.btn_atender.setStyleSheet("")
        self.btn_atender.setIcon(icon2)
        self.btn_atender.setIconSize(QtCore.QSize(32, 32))
        self.btn_atender.setObjectName("btn_atender")
        self.verticalLayout.addWidget(self.btn_atender)
        self.btn_solicitud = QtWidgets.QPushButton(self.frame_lateral)
        self.btn_solicitud.setMinimumSize(QtCore.QSize(400, 40))
        self.btn_solicitud.setStyleSheet("")
        self.btn_solicitud.setIcon(icon2)
        self.btn_solicitud.setIconSize(QtCore.QSize(32, 32))
        self.btn_solicitud.setObjectName("btn_solicitud")
        self.verticalLayout.addWidget(self.btn_solicitud)
        self.btn_simular = QtWidgets.QPushButton(self.frame_lateral)
        self.btn_simular.setMinimumSize(QtCore.QSize(400, 40))
        self.btn_simular.setStyleSheet("")
        self.btn_simular.setIcon(icon2)
        self.btn_simular.setIconSize(QtCore.QSize(32, 32))
        self.btn_simular.setObjectName("btn_simular")
        self.verticalLayout.addWidget(self.btn_simular)
        self.bt_regresar = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_regresar.setMinimumSize(QtCore.QSize(400, 40))
        self.bt_regresar.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Documents\\IPC2_Proyecto2_201445840\\ventanas\\../imagenes/pngfind.com-back-png-1934895.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_regresar.setIcon(icon3)
        self.bt_regresar.setIconSize(QtCore.QSize(32, 32))
        self.bt_regresar.setObjectName("bt_regresar")
        self.verticalLayout.addWidget(self.bt_regresar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu manejo punto"))
        self.label.setText(_translate("MainWindow", "Elija una opcion para seleccionar"))
        self.bt_verestado.setText(_translate("MainWindow", "Ver estado del punto"))
        self.bt_activar.setText(_translate("MainWindow", "Activar escritorio"))
        self.bt_desactivar.setText(_translate("MainWindow", "Desactivar escritorio"))
        self.btn_atender.setText(_translate("MainWindow", "Atender cliente"))
        self.btn_solicitud.setText(_translate("MainWindow", "Solicitud de atencion"))
        self.btn_simular.setText(_translate("MainWindow", "Simular actividad"))
        self.bt_regresar.setText(_translate("MainWindow", "Regresar"))