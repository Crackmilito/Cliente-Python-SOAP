# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIEliminarEspecie.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EliminarEspecie(object):
    def setupUi(self, EliminarEspecie):
        EliminarEspecie.setObjectName("EliminarEspecie")
        EliminarEspecie.resize(492, 163)
        self.centralwidget = QtWidgets.QWidget(EliminarEspecie)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 55, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 100, 191, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 40, 191, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(300, 40, 93, 28))
        self.btnEliminar.setObjectName("btnEliminar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 55, 16))
        self.label_2.setObjectName("label_2")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(300, 100, 93, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        EliminarEspecie.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EliminarEspecie)
        self.statusbar.setObjectName("statusbar")
        EliminarEspecie.setStatusBar(self.statusbar)

           #Accion del boton
        self.btnEliminar.clicked.connect(self.deleteEspecie)

        self.retranslateUi(EliminarEspecie)
        QtCore.QMetaObject.connectSlotsByName(EliminarEspecie)

    def retranslateUi(self, EliminarEspecie):
        _translate = QtCore.QCoreApplication.translate
        EliminarEspecie.setWindowTitle(_translate("EliminarEspecie", "Eliminar Especie"))
        self.label.setText(_translate("EliminarEspecie", "ID"))
        self.btnEliminar.setText(_translate("EliminarEspecie", "Eliminar"))
        self.label_2.setText(_translate("EliminarEspecie", "Nombre"))
        self.btnBuscar.setText(_translate("EliminarEspecie", "Buscar"))

    def deleteEspecie(self):
        ID = self.txtID.text()
        nom  = self.txtNombre.text()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EliminarEspecie = QtWidgets.QMainWindow()
    ui = Ui_EliminarEspecie()
    ui.setupUi(EliminarEspecie)
    EliminarEspecie.show()
    sys.exit(app.exec_())
