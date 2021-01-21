from  PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from valida import valida

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.resize(1270, 850)
        self.setWindowTitle('BASE DE DATOS ÁCIDA')
        with open("style.css") as f:
            self.setStyleSheet(f.read())
        self.initUI()
    
    def initUI(self):
        #CENTRAL WID
        self.centralwidget = QtWidgets.QWidget(self)
        # Establece el nombre al objeto
        self.centralwidget.setObjectName("centralwidget")
        # Establece el widget central
        self.setCentralWidget(self.centralwidget)
        
        #MENU BAR
        self.menubar = QtWidgets.QMenuBar(self)
        # Establece tamaño y posicion del objeto
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 31))
        # Establece el nombre del obejto
        self.menubar.setObjectName("menubar")
        # Establece el MenuBar en MainWindow
        self.setMenuBar(self.menubar)


        self.widgetMenu = QtWidgets.QWidget(self.centralwidget)
        # Establece tamaño y posicion del objeto
        self.widgetMenu.setGeometry(QtCore.QRect(100, 310, 1200, 291))
        # Establece si el fondo se llena automaticamente
        self.widgetMenu.setAutoFillBackground(False)
        # Establece el nombre del obejto
        self.widgetMenu.setObjectName("widgetMenu")
        # Da visibilidad al bojeto
        self.widgetMenu.setVisible(True)

        self.widgetLienzo = QtWidgets.QWidget(self.centralwidget)
        # Establece tamaño y posicion del objeto
        self.widgetLienzo.setGeometry(QtCore.QRect(70, 0, 1200, 300))
        # Establece si el fondo se llena automaticamente
        self.widgetLienzo.setAutoFillBackground(False)
        # Establece el nombre del obejto
        self.widgetLienzo.setObjectName("widgetLienzo")
        # Da visibilidad al bojeto
        self.widgetLienzo.setVisible(True)

        #label de entrada
        # Crea un Qlabel dentro de centralwidget
        self.label = QtWidgets.QLabel(self.widgetLienzo)
        # Establece tamaño y posicion del objeto
        self.label.setGeometry(QtCore.QRect(200, 200, 700, 90))
        # Establece alineacion al Qlabel
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        # Establece el texto al QLabel
        self.label.setText("BIENVENID@ A LA BASE DE DATOS DE ÁCIDA")
        # Establece el nombre del obejto
        self.label.setObjectName("label")

        #BOTONES DE INICIO

        self.admin_button = QtWidgets.QPushButton(self.widgetMenu)
        self.admin_button.setGeometry(QtCore.QRect(100, 30, 200, 51))
        # Establece el icono de cursor cuando se pasa el mouse sobre el boton
        self.admin_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establece el texto al QPushButton
        self.admin_button.setText("ADMINISTRADORA")
        # Establece el nombre del obejto
        self.admin_button.setObjectName("admin_button")

        self.admin_button.clicked.connect(self.admin_validation)

        
        self.super_button = QtWidgets.QPushButton(self.widgetMenu)
        self.super_button.setGeometry(QtCore.QRect(420, 30, 200, 51))
        self.super_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.super_button.setText("SUPERVISOR")
        self.super_button.setObjectName("super_button")
        self.super_button.clicked.connect(self.valida_supervisor)

        self.vendedor_button = QtWidgets.QPushButton(self.widgetMenu)
        self.vendedor_button.setGeometry(QtCore.QRect(720, 30, 200, 51))
        self.vendedor_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.vendedor_button.setText("VENDEDOR")
        self.vendedor_button.setObjectName("vendedor_button")

        self.vendedor_button.clicked.connect(self.valida_vendedor)

    def admin_validation(self):
        self.adUi = valida('mpcalderon')
        self.adUi.show()

    def valida_vendedor(self):
        self.veUi = valida('jmanosalva')
        self.veUi.show()

    def valida_supervisor(self):
        self.suUi = valida('jrincon')
        self.suUi.show()        
             



    def CrearLienzo(self):
        # Crea un objeto Widget dentro de centralwidget
        self.widgetLienzo = QtWidgets.QWidget(self.centralwidget)
        
        if self.aumenu:
            # Establece tamaño y posicion del objeto
            self.widgetLienzo.setGeometry(QtCore.QRect(70, 850, 1200, 850))
        else:
            # Establece tamaño y posicion del objeto
            self.widgetLienzo.setGeometry(QtCore.QRect(298, 850, 1200, 850))
        # Establece si el fondo se llena automaticamente
        self.widgetLienzo.setAutoFillBackground(False)
        # Establece el nombre del obejto
        self.widgetLienzo.setObjectName("widgetLienzo")
        # Da visibilidad al bojeto
        self.widgetLienzo.setVisible(True)

    #funcion para dejar limpio el lienzo

    def menuPrincipalEsconder(self, boton):
        # Usando la varibale auxiliar comprobamos si debe moverse el menu
        if self.aumenu:
            
            # Creamos el objeto de animación y establecemos el objeto que animaremos
            self.animacionwidget2 = QtCore.QPropertyAnimation(
                self.widgetMenu, b'geometry')
            # Establece la duracion de la animacion
            self.animacionwidget2.setDuration(500)
            # Establece la posición y tamaño donde empezará la animacion
            self.animacionwidget2.setStartValue(QtCore.QRect(100, 310, 1200, 291))
            # Establece la posición y tamaño donde terminará la animacion
            self.animacionwidget2.setEndValue(QtCore.QRect(100, -100, 1200, 291))
            # Inicia la animacion
            self.animacionwidget2.start()

            # Creamos el objeto de animación y establecemos el objeto que animaremos
            self.animacionbutton2_1 = QtCore.QPropertyAnimation(
                self.admin_button, b'geometry')
            # Establece la duracion de la animacion
            self.animacionbutton2_1.setDuration(500)
            # Establece la posición y tamaño donde empezará la animacion
            self.animacionbutton2_1.setStartValue(QtCore.QRect(100, 30, 200, 51))
            # Establece la posición y tamaño donde terminará la animacion
            self.animacionbutton2_1.setEndValue(QtCore.QRect(20, -90, 200, 51))
            # Inicia la animacion
            self.animacionbutton2_1.start()

            # Creamos el objeto de animación y establecemos el objeto que animaremos
            self.animacionbutton2_2 = QtCore.QPropertyAnimation(
                self.super_button, b'geometry')
            # Establece la duracion de la animacion
            self.animacionbutton2_2.setDuration(500)
            # Establece la posición y tamaño donde empezará la animacion
            self.animacionbutton2_2.setStartValue(QtCore.QRect(420, 30, 200, 51))
            # Establece la posición y tamaño donde terminará la animacion
            self.animacionbutton2_2.setEndValue(QtCore.QRect(230, -90, 200, 51))
            # Inicia la animacion
            self.animacionbutton2_2.start()

            # Creamos el objeto de animación y establecemos el objeto que animaremos
            self.animacionbutton2_3 = QtCore.QPropertyAnimation(
                self.vendedor_button, b'geometry')
            # Establece la duracion de la animacion
            self.animacionbutton2_3.setDuration(500)
            # Establece la posición y tamaño donde empezará la animacion
            self.animacionbutton2_3.setStartValue(QtCore.QRect(720, 30, 200, 51))
            # Establece la posición y tamaño donde terminará la animacion
            self.animacionbutton2_3.setEndValue(QtCore.QRect(440, -90, 200, 51))
            # Inicia la animacion
            self.animacionbutton2_3.start()

            
            # Establece el evento que prosigue cuano termine la animacion
            self.animacionbutton2_3.finished.connect(
                partial(self.menuLateralMostrar, boton))

            # Damos valor a la variable auxiliar
            self.aumenu = False
        else:
            # En caso de que el menu ya este escondido y no sea necesario moverlo se procede a mostrar el menu lateral llamando al metodo menuLateralMostrar
            self.menuLateralMostrar(boton)
            # Damos valor a la variable auxiliar
            self.aumenul = False


    def MoverLienzoAbajo(self):
        try:
            self.animacionwidgetBajar = QtCore.QPropertyAnimation(self.widgetLienzo, b'geometry')
            # Establece la duracion de la animacion
            self.animacionwidgetBajar.setDuration(500)
            # Establece la posición y tamaño donde empezará la animacion
            self.animacionwidgetBajar.setStartValue(QtCore.QRect(70, 0, 1200, 850))
            # Establece la posición y tamaño donde terminará la animacion
            self.animacionwidgetBajar.setEndValue(QtCore.QRect(70, -850, 1200, 850))
            # Inicia la animacion
            self.animacionwidgetBajar.start()
            self.animacionwidgetB.finished.connect(self.limpiarLienzo)
        except Exception as e:
            pass

        

    def MoverLienzoArriba(self):
        self.animacionwidget = QtCore.QPropertyAnimation(
                self.widgetLienzo, b'geometry')
        # Establece la duracion de la animacion
        self.animacionwidget.setDuration(500)
        # Establece la posición y tamaño donde empezará la animacion
        self.animacionwidget.setStartValue(QtCore.QRect(70, 850, 1200, 850))
        # Establece la posición y tamaño donde terminará la animacion
        if not self.aumenu:
            self.animacionwidget.setEndValue(QtCore.QRect(70, 0, 1200, 850))
        else:
            self.animacionwidget.setEndValue(QtCore.QRect(70, 0, 1200, 300))
        # Inicia la animacion
        self.animacionwidget.start()


    def limpiarLienzo(self):
        try:
            # Oculta todo el widgetLienzo
            self.widgetLienzo.setParent(None)
            self.widgetLienzo.deleteLater()
            # Re definimos el widgetLienzo
            self.widgetLienzo = None

        except Exception as e:
            pass



def window():
    app =  QApplication(sys.argv)
    #app.setStyleSheet(stylesheet)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
  