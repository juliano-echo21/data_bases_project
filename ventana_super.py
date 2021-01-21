from  PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import mysql.connector
from ventana_ingresar import ventana_ingresar
from ventana_update import ventana_update
from ventana_borrar import ventana_borrar
from ventana_consulta import ventana_consulta




class ventana_super(QMainWindow):

    def __init__(self,role):
        super(ventana_super,self).__init__()
        self.role = role
        self.resize(900, 650)
        self.showMaximized()
        self.setWindowTitle('SUPERVISOR')
        with open("style.css") as f:
            self.setStyleSheet(f.read())
        self.setupUi()



    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        # Establece el nombre al objeto
        self.centralwidget.setObjectName("centralwidget")
        # Establece el widget central
        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        # Establece tamaño y posicion del objeto
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 31))
        # Establece el nombre del obejto
        self.menubar.setObjectName("menubar")
        # Establece el MenuBar en MainWindow
        self.setMenuBar(self.menubar)


        self.widgetLienzo = QtWidgets.QWidget(self.centralwidget)
        # Establece tamaño y posicion del objeto
        self.widgetLienzo.setGeometry(QtCore.QRect(70, 0, 1200, 300))
        # Establece si el fondo se llena automaticamente
        self.widgetLienzo.setAutoFillBackground(False)
        # Establece el nombre del obejto
        self.widgetLienzo.setObjectName("widgetLienzo")
        # Da visibilidad al bojeto
        self.widgetLienzo.setVisible(True)

        self.menuLateralMostrar()



    def menuLateralMostrar(self):
        try:
            self.widgetMenuLateral.setParent(None)
        except:
            pass

        # Damos valor a la variable auxiliar para evitar que se mueva el widgetLiezon cuando no corresponde
        self.aumenul = False

        # Crear el objeto Widget que contiene el menu lateral
        self.widgetMenuLateral = QtWidgets.QWidget(self.centralwidget)
        # Establece tamaño y posicion del objeto
        self.widgetMenuLateral.setGeometry(QtCore.QRect(0, 0, 300, 2000))
        # Establece el nombre del obejto
        self.widgetMenuLateral.setObjectName("widgetMenuLateral")
        # Establecer visibilidad del widget
        self.widgetMenuLateral.setVisible(True)
    
        self.animacionLateralWidgetLateral1 = QtCore.QPropertyAnimation(self.widgetMenuLateral, b'geometry')
        # Establece la duracion de la animacion
        self.animacionLateralWidgetLateral1.setDuration(400)
        # Establece la posición y tamaño donde empezará la animacion
        self.animacionLateralWidgetLateral1.setStartValue(QtCore.QRect(0, 0, 0, 2000))
        # Establece la posición y tamaño donde terminará la animacion
        self.animacionLateralWidgetLateral1.setEndValue(QtCore.QRect(0, 0, 250, 2000))
        self.animacionLateralWidgetLateral1.start()

        self.botonLateral_1 = QtWidgets.QPushButton(self.widgetMenuLateral)
        # Establece tamaño y posicion del QpushButton
        self.botonLateral_1.setGeometry(QtCore.QRect(10, 20, 41, 41))
        # Establece el texto al QPushButton
        self.botonLateral_1.setText("")
        # creamos una variable local para el objeto QIcon
        self.botonLateral_1.setObjectName("botonLateral_1")
        self.botonLateral_1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.botonLateral_1.setVisible(True)

        #animacion
        self.animacionboton1 = QtCore.QPropertyAnimation(self.botonLateral_1, b'geometry')
        # Establece la duracion de la animacion
        self.animacionboton1.setDuration(400)
        # Establece la posición y tamaño donde empezará la animacion
        self.animacionboton1.setStartValue(QtCore.QRect(10, 20, 41, 41))
        # Establece la posición y tamaño donde terminará la animacion
        self.animacionboton1.setEndValue(QtCore.QRect(10, 20, 200, 41))

        # Inicia la animacion
        self.animacionboton1.start()
        self.botonLateral_1.setText("INGRESAR")
        self.botonLateral_1.clicked.connect(self.showVentanaIngresar)

        #boton 2

        self.botonLateral_2 = QtWidgets.QPushButton(self.widgetMenuLateral)
        # Establece tamaño y posicion del QpushButton
        self.botonLateral_2.setGeometry(QtCore.QRect(10, 80, 41, 41))
        # Establece el texto al QPushButton
        self.botonLateral_2.setText("")
        # creamos una variable local para el objeto QIcon
        self.botonLateral_2.setObjectName("botonLateral_2")
        self.botonLateral_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.botonLateral_2.setVisible(True)
        #animacion
        self.animacionboton2 = QtCore.QPropertyAnimation(self.botonLateral_2, b'geometry')
        # Establece la duracion de la animacion
        self.animacionboton2.setDuration(400)
        # Establece la posición y tamaño donde empezará la animacion
        self.animacionboton2.setStartValue(QtCore.QRect(10, 80, 41, 41))
        # Establece la posición y tamaño donde terminará la animacion
        self.animacionboton2.setEndValue(QtCore.QRect(10, 80, 200, 41))

        # Inicia la animacion
        self.animacionboton2.start()
        self.botonLateral_2.setText("BORRAR")



        #boton 3

        self.botonLateral_3 = QtWidgets.QPushButton(self.widgetMenuLateral)
        # Establece tamaño y posicion del QpushButton
        self.botonLateral_3.setGeometry(QtCore.QRect(10, 140, 41, 41))
        # Establece el texto al QPushButton
        self.botonLateral_3.setText("")
        # creamos una variable local para el objeto QIcon
        self.botonLateral_3.setObjectName("botonLateral_3")
        self.botonLateral_3.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.botonLateral_3.setVisible(True)
        #animacion
        self.animacionboton3 = QtCore.QPropertyAnimation(self.botonLateral_3, b'geometry')
        # Establece la duracion de la animacion
        self.animacionboton3.setDuration(400)
        # Establece la posición y tamaño donde empezará la animacion
        self.animacionboton3.setStartValue(QtCore.QRect(10, 140, 41, 41))
        # Establece la posición y tamaño donde terminará la animacion
        self.animacionboton3.setEndValue(QtCore.QRect(10, 140, 200, 41))

        # Inicia la animacion
        self.animacionboton3.start()
        self.botonLateral_3.setText("ACTUALIZAR")
        self.botonLateral_3.clicked.connect(self.showVentanaActualizar)

        #botón 4

        self.botonLateral_4 = QtWidgets.QPushButton(self.widgetMenuLateral)
        # Establece tamaño y posicion del QpushButton
        self.botonLateral_4.setGeometry(QtCore.QRect(10, 200, 41, 41))
        # Establece el texto al QPushButton
        self.botonLateral_4.setText("")
        # creamos una variable local para el objeto QIcon
        self.botonLateral_4.setObjectName("botonLateral_4")
        self.botonLateral_4.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.botonLateral_4.setVisible(True)
        #animacion
        self.animacionboton4 = QtCore.QPropertyAnimation(self.botonLateral_4, b'geometry')
        # Establece la duracion de la animacion
        self.animacionboton4.setDuration(400)
        # Establece la posición y tamaño donde empezará la animacion
        self.animacionboton4.setStartValue(QtCore.QRect(10, 200, 41, 41))
        # Establece la posición y tamaño donde terminará la animacion
        self.animacionboton4.setEndValue(QtCore.QRect(10, 200, 200, 41))

        # Inicia la animacion
        self.animacionboton4.start()
        self.botonLateral_4.setText("CONSULTAR")


    def showVentanaIngresar(self):
        self.ingresar = ventana_ingresar(self.role)
        self.ingresar.show()

    def showVentanaBorrar(self):
        self.borrar = ventana_borrar(self.role)
        self.borrar.show()

    def showVentanaActualizar(self):
        self.update = ventana_update(self.role)
        self.update.show()

    def showVentanaConsultar(self):
        self.consulta = ventana_consulta(self.role)
        self.consulta.show()





def window():
    app =  QApplication(sys.argv)
    #app.setStyleSheet(stylesheet)
    win = ventana_super('jrincon')
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()