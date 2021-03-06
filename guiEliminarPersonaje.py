# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIEliminarPersonaje.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EliminarPersonaje(object):
    def setupUi(self, EliminarPersonaje):
        EliminarPersonaje.setObjectName("EliminarPersonaje")
        EliminarPersonaje.resize(327, 495)
        self.centralwidget = QtWidgets.QWidget(EliminarPersonaje)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 55, 16))
        self.label.setObjectName("label")
        self.txtID = QtWidgets.QLineEdit(self.centralwidget)
        self.txtID.setGeometry(QtCore.QRect(70, 50, 181, 22))
        self.txtID.setObjectName("txtID")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 190, 55, 16))
        self.label_4.setObjectName("label_4")
        self.txtMana = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMana.setGeometry(QtCore.QRect(70, 210, 181, 22))
        self.txtMana.setObjectName("txtMana")
        self.txtFuerza = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFuerza.setGeometry(QtCore.QRect(70, 160, 181, 22))
        self.txtFuerza.setObjectName("txtFuerza")
        self.cbJugador = QtWidgets.QComboBox(self.centralwidget)
        self.cbJugador.setGeometry(QtCore.QRect(70, 360, 181, 22))
        self.cbJugador.setObjectName("cbJugador")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 240, 55, 16))
        self.label_5.setObjectName("label_5")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(50, 420, 93, 28))
        self.btnEliminar.setObjectName("btnEliminar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 55, 16))
        self.label_2.setObjectName("label_2")
        self.txtEnergia = QtWidgets.QLineEdit(self.centralwidget)
        self.txtEnergia.setGeometry(QtCore.QRect(70, 260, 181, 22))
        self.txtEnergia.setObjectName("txtEnergia")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 290, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 55, 16))
        self.label_3.setObjectName("label_3")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(70, 110, 181, 22))
        self.txtNombre.setObjectName("txtNombre")
        self.cbEspecie = QtWidgets.QComboBox(self.centralwidget)
        self.cbEspecie.setGeometry(QtCore.QRect(70, 310, 181, 22))
        self.cbEspecie.setObjectName("cbEspecie")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 340, 55, 16))
        self.label_7.setObjectName("label_7")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(180, 420, 93, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        EliminarPersonaje.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EliminarPersonaje)
        self.statusbar.setObjectName("statusbar")
        EliminarPersonaje.setStatusBar(self.statusbar)

            #Accion del boton
        self.btnEliminar.clicked.connect(self.deletePersonaje)

        self.retranslateUi(EliminarPersonaje)
        QtCore.QMetaObject.connectSlotsByName(EliminarPersonaje)

    def retranslateUi(self, EliminarPersonaje):
        _translate = QtCore.QCoreApplication.translate
        EliminarPersonaje.setWindowTitle(_translate("EliminarPersonaje", "Eliminar Personaje"))
        self.label.setText(_translate("EliminarPersonaje", "ID"))
        self.label_4.setText(_translate("EliminarPersonaje", "Mana"))
        self.label_5.setText(_translate("EliminarPersonaje", "Energia"))
        self.btnEliminar.setText(_translate("EliminarPersonaje", "Eliminar"))
        self.label_2.setText(_translate("EliminarPersonaje", "Nombre"))
        self.label_6.setText(_translate("EliminarPersonaje", "Especie"))
        self.label_3.setText(_translate("EliminarPersonaje", "Fuerza"))
        self.label_7.setText(_translate("EliminarPersonaje", "Jugador"))
        self.btnBuscar.setText(_translate("EliminarPersonaje", "Buscar"))

    def deletePersonaje(self):
        ID = self.txtID.text()
        nom  = self.txtNombre.text()
        fuer = self.txtFuerza.text()
        mana = self.txtMana.text()
        ener = self.txtEnergia.text()
        #espec = self.cbEspecie.text()
        #juga = self.cbJugador.text()
        estReg = 1
        FechaReg = 11111


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EliminarPersonaje = QtWidgets.QMainWindow()
    ui = Ui_EliminarPersonaje()
    ui.setupUi(EliminarPersonaje)
    EliminarPersonaje.show()
    sys.exit(app.exec_())
