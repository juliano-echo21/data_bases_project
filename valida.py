from  PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import mysql.connector
from ventana_admin import ventana_admin
from ventana_vendedor import ventana_vendedor
from ventana_super import ventana_super
#from ventana_supervisor import ventana_supervisor


class valida(QMainWindow):

    def __init__(self,role):
        super(valida,self).__init__()
        self.resize(421,379)
        self.setWindowTitle('VALIDACION ')
        self.role = role
        with open("style.css") as f:
            self.setStyleSheet(f.read())
        self.setupUi()

    def setupUi(self):

        self.usuario = QtWidgets.QLineEdit(self)
        # Establece posicion y tamaño
        self.usuario.setGeometry(QtCore.QRect(40, 50, 261, 31))
        # Establece el texto que contiene (vacio para que el usuario lo llene)
        self.usuario.setText("")
        # Establece el nombre del objeto
        self.usuario.setObjectName("admin_input")
        # Establece el texto que indicará a que corresponde el campo
        self.usuario.setPlaceholderText("Nombre de usuario")
        # Definimos la longitud maxima de caracteres
        self.usuario.setMaxLength(20)
        # Establece la visibilidad del objeto
        self.usuario.setVisible(True)
        # Pone el foco en este campo
        self.usuario.setFocus()
        # Llama funcion para manejar el foco a travez de key_Enter
        #self.lnCodigoServicio.returnPressed.connect(self.registroChkServicio)

        #para contraseña
        self.password = QtWidgets.QLineEdit(self)
        self.password.setGeometry(QtCore.QRect(40, 100, 261, 31))
        self.password.setText("")
        self.password.setObjectName("admin_input_ps")
        self.password.setPlaceholderText("Contraseña")
        self.password.setMaxLength(20)
        self.password.setVisible(True)
        #self.password.setFocus()
        #self.lnCodigoServicio.returnPressed.connect(self.registroChkServicio)

        self.commit = QtWidgets.QPushButton(self)
        self.commit.setGeometry(QtCore.QRect(40, 180, 120, 30))
        self.commit.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.commit.setText("Acceder")
        self.commit.setObjectName("commit")
        self.commit.clicked.connect(self.validar_datos)

    #se valida que los datos coincidan con los d elos usuarios de la base de datos
    def validar_datos(self):
        if self.role == 'mpcalderon':
            if self.password.text() == '12345678' and self.usuario.text() == 'mpcalderon':
                self.ventana_admin = ventana_admin('mpcalderon')
                
                self.ventana_admin.show()
            
        elif self.role == 'jmanosalva':
            if self.password.text() == '7654321' and self.usuario.text() == 'jmanosalva':
                self.ventana_vendedor = ventana_vendedor('jmanosalva')
                
                self.ventana_vendedor.show()

        elif self.role == 'jrincon':
            if self.password.text() == '3333333' and self.usuario.text() == 'jrincon':
                self.ventana_super = ventana_super('jrincon')
                
                self.ventana_super.show()


