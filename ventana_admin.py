from  PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow,QHBoxLayout, QVBoxLayout, QPushButton
import sys
import mysql.connector
from ventana_ingresar import ventana_ingresar
from ventana_update import ventana_update
from ventana_borrar import ventana_borrar
from ventana_consulta import ventana_consulta




class ventana_admin(QMainWindow):

    def __init__(self,role):
        super(ventana_admin,self).__init__()
        self.role = role
        self.resize(1500, 900)
        #self.showMaximized()
        self.setWindowTitle('ADMINISTRADORA')
        self.conectar()
        with open("style_admin.css") as f:
            self.setStyleSheet(f.read())
        self.setupUi()

    def conectar(self):
        self.conn =  mysql.connector.connect( 
                 host='localhost', 
                 user= 'mpcalderon', 
                 passwd='12345678', 
                 db='acida' )

        self.cursor = self.conn.cursor()  


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

        self.labelHasta = QtWidgets.QLabel(self.centralwidget)
        self.labelHasta.setGeometry(QtCore.QRect(300, 150, 500, 41))
        self.labelHasta.setObjectName("labelHasta")
        self.labelHasta.setText('Hasta la fecha:')

        self.ganancias = QtWidgets.QLabel(self.centralwidget)
        self.ganancias.setGeometry(QtCore.QRect(300, 150, 500, 41))
        self.ganancias.setObjectName("ganancias")
        self.ganancias.setText("")

        self.numeroVentas = QtWidgets.QLabel(self.centralwidget)
        self.numeroVentas.setGeometry(QtCore.QRect(300, 300, 500, 41))
        self.numeroVentas.setObjectName("numeroVentas")
        self.numeroVentas.setText("UNIDADES VENDIDAS")



        self.labelVendidos = QtWidgets.QPushButton(self.centralwidget)
        self.labelVendidos.setGeometry(QtCore.QRect(620, 350, 390, 41))
        self.labelVendidos.setObjectName("labelVendido")
        self.labelVendidos.setText('NUESTROS PRODUCTOS MÁS VENDIDOS:')
        self.labelVendidos.clicked.connect(self.mostrarProductos)


        self.labelSaludo = QtWidgets.QLabel(self.centralwidget)
        self.labelSaludo.setGeometry(QtCore.QRect(300, 40, 600, 80))
        self.labelSaludo.setObjectName("labelSaludo")
        self.labelSaludo.setText('Bienvenido/a Admin')


        self.botonEmpleado = QtWidgets.QPushButton(self.centralwidget)
        self.botonEmpleado.setGeometry(QtCore.QRect(550, 700, 500, 41))
        self.botonEmpleado.setObjectName("labelEmpleado")
        self.botonEmpleado.setText('NUESTRO EMPLEADO DEL MES:')

        self.nombreEmpleado = QtWidgets.QLabel(self.centralwidget)
        self.nombreEmpleado.setGeometry(QtCore.QRect(540, 780, 500, 61))
        self.nombreEmpleado.setObjectName("nombreEmpleado")
        self.nombreEmpleado.setText('')
        self.nombreEmpleado.setAlignment(QtCore.Qt.AlignCenter)
        self.botonEmpleado.clicked.connect(self.mostrarNombre)


        self.botonZapato = QtWidgets.QPushButton(self.centralwidget)
        # Establece tamaño y posicion del QpushButton
        self.botonZapato.setGeometry(QtCore.QRect(1100, 100, 300, 100))
        # Establece el texto al QPushButton
        self.botonZapato.setText("")
        # creamos una variable local para el objeto QIcon
        self.botonZapato.setObjectName("botonZapato")
        self.botonZapato.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.botonZapato.setVisible(True)
        self.botonZapato.setText("Zapatillas")
        self.botonZapato.clicked.connect(lambda  x: self.zapato(0))

        self.botonZapatoR = QtWidgets.QLabel(self.centralwidget)
        self.botonZapatoR.setGeometry(QtCore.QRect(1100, 215, 250, 60))
        self.botonZapatoR.setObjectName("botonZapatoR")
        self.botonZapatoR.setText('')
        self.botonZapatoR.setAlignment(QtCore.Qt.AlignCenter)






        self.botonSanda = QtWidgets.QPushButton(self.centralwidget)
        # Establece tamaño y posicion del QpushButton
        self.botonSanda.setGeometry(QtCore.QRect(1100, 300, 250, 90))
        # Establece el texto al QPushButton
        self.botonSanda.setText("")
        # creamos una variable local para el objeto QIcon
        self.botonSanda.setObjectName("botonSanda")
        self.botonSanda.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.botonSanda.setVisible(True)
        self.botonSanda.setText("Sandalias")
        self.botonSanda.clicked.connect(lambda x: self.zapato(1))

        self.botonSandaR = QtWidgets.QLabel(self.centralwidget)
        self.botonSandaR.setGeometry(QtCore.QRect(1100, 420, 250, 60))
        self.botonSandaR.setObjectName("botonZapatoR")
        self.botonSandaR.setText('')
        self.botonSandaR.setAlignment(QtCore.Qt.AlignCenter)


        self.menuLateralMostrar()


    def zapato(self,n):
        
        if n ==0:
            q = """select  sum(Fact_Pago_Total) as TotalVentas from factura_venta join info_factura_venta using (id_factura_venta) join producto using (id_producto) where 
                    producto_tipo='Zapatilla' and Fact_Fecha> '2020-02-01';"""
            self.cursor.execute(q)
            t = self.cursor.fetchall()[0][0]
            print(t)
            self.botonZapatoR.setText(str(t))
            
        else:
            q =  """ select  sum(Fact_Pago_Total) as TotalVentas from factura_venta join info_factura_venta using (id_factura_venta) join producto using (id_producto) where 
                producto_tipo='Sandalia' and Fact_Fecha> '2020-02-01';"""
            self.cursor.execute(q)
            t = self.cursor.fetchall()[0][0]
            print(t)
            self.botonSandaR.setText(str(t))

    def mostrarNombre(self):
        self.cursor.callproc('Empleado_Ventas',['2020-7-01','2020-7-31'])
        for result in self.cursor.stored_results():
            l=result.fetchall()

        nombre = l[0][0]+' '+ l[0][1]

        self.nombreEmpleado.setText(nombre)







    def mostrarProductos(self):
        self.cursor.callproc('Mas_vendidos')
        for result in self.cursor.stored_results():
            l = result.fetchall()


        self.vendido1 = QtWidgets.QLabel(self.centralwidget)
        self.vendido1.setGeometry(QtCore.QRect(650, 400, 311, 41))
        self.vendido1.setObjectName("labelVendidos")
        self.vendido1.setVisible(True)
        self.vendido1.setAlignment(QtCore.Qt.AlignCenter)
        


        self.vendido2 = QtWidgets.QLabel(self.centralwidget)
        self.vendido2.setGeometry(QtCore.QRect(650, 460, 311, 41))
        self.vendido2.setObjectName("labelVendidos")
        self.vendido2.setVisible(True)
        self.vendido2.setAlignment(QtCore.Qt.AlignCenter)



        self.vendido3 = QtWidgets.QLabel(self.centralwidget)
        self.vendido3.setGeometry(QtCore.QRect(650, 520, 311, 41))
        self.vendido3.setObjectName("labelVendidos")
        self.vendido3.setVisible(True)
        self.vendido3.setAlignment(QtCore.Qt.AlignCenter)

        
        self.vendido1.setText(l[0][0])
        self.vendido2.setText(l[1][0])
        self.vendido3.setText(l[2][0])




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
        self.botonLateral_1.setText("INGRESAR ")
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
        self.botonLateral_2.clicked.connect(self.showVentanaBorrar)



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
        self.botonLateral_4.clicked.connect(self.showVentanaConsultar)



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
    win = ventana_admin('mpcalderon')
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()