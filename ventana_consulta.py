from  PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QGridLayout, QTableView
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import mysql.connector



class ventana_consulta(QMainWindow):

    def __init__(self,role):
        super(ventana_consulta,self).__init__()
        self.role = role
        self.resize(1100,700)
        self.setWindowTitle('CONSULTAR')
        #self.showMaximized() 
        self.conection()
        with open("style.css") as f:
            self.setStyleSheet(f.read())
        self.setupUi()
        #self.defineRole()
    

    def conection(self):
        if self.role == 'mpcalderon':
            self.conn =  mysql.connector.connect( 
                 host='localhost', 
                 user= 'mpcalderon', 
                 passwd='12345678', 
                db='acida' )

        elif self.role == 'jmanosalva':
            self.conn =  mysql.connector.connect( 
                 host='localhost', 
                 user= 'jmanosalva', 
                 passwd='7654321', 
                  db='acida' )
        else:
            self.conn =  mysql.connector.connect( 
                 host='localhost', 
                 user= 'jrincon', 
                 passwd='3333333', 
                  db='acida' )

    
    
    def setupUi(self):
        self.cursor = self.conn.cursor()
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        self.crearLienzo()



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
        self.animacionLateralWidgetLateral1.setStartValue(QtCore.QRect(0, 0, 0, 700))
        # Establece la posición y tamaño donde terminará la animacion
        self.animacionLateralWidgetLateral1.setEndValue(QtCore.QRect(0, 0, 250, 700))
        self.animacionLateralWidgetLateral1.start()


        self.botonLateral_1 = QtWidgets.QPushButton(self.widgetMenuLateral)
        # Establece tamaño y posicion del QpushButton
        self.botonLateral_1.setGeometry(QtCore.QRect(0, 10, 41, 60))
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
        self.animacionboton1.setStartValue(QtCore.QRect(0, 10, 41, 60))
        # Establece la posición y tamaño donde terminará la animacion
        self.animacionboton1.setEndValue(QtCore.QRect(0, 10, 250, 60))

        # Inicia la animacion
        self.animacionboton1.start()
        self.botonLateral_1.setText("VENTAS TOTALES")
        self.botonLateral_1.clicked.connect(self.primer)

        #boton 2

        self.botonLateral_2 = QtWidgets.QPushButton(self.widgetMenuLateral)
        # Establece tamaño y posicion del QpushButton
        self.botonLateral_2.setGeometry(QtCore.QRect(0, 90, 41, 60))
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
        self.animacionboton2.setStartValue(QtCore.QRect(0, 90, 41, 60))
        # Establece la posición y tamaño donde terminará la animacion
        self.animacionboton2.setEndValue(QtCore.QRect(0, 90, 250, 60))

        # Inicia la animacion
        self.animacionboton2.start()
        self.botonLateral_2.setText("VENTAS POR EMPLEADO")
        
        self.botonLateral_2.clicked.connect(self.segundo)



        #boton 3

        self.botonLateral_3 = QtWidgets.QPushButton(self.widgetMenuLateral)
        # Establece tamaño y posicion del QpushButton
        self.botonLateral_3.setGeometry(QtCore.QRect(0, 180, 41, 60))
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
        self.animacionboton3.setStartValue(QtCore.QRect(0, 180, 41, 60))
        # Establece la posición y tamaño donde terminará la animacion
        self.animacionboton3.setEndValue(QtCore.QRect(0, 180, 250, 60))

        # Inicia la animacion
        self.animacionboton3.start()
        self.botonLateral_3.setText("GANANCIAS TOTALES")
        
        self.botonLateral_3.clicked.connect(self.tercero)

        

    def primer(self):
        self.limpiarLienzo()
        self.crearLienzo()

        self.labelPrimero = QtWidgets.QLabel(self.widgetLienzo)
        self.labelPrimero.setGeometry(QtCore.QRect(30, 30, 500, 41))
        self.labelPrimero.setObjectName("labelHasta")
        self.labelPrimero.setText('Cantidad Vendida y Productos Vendidos Desde:')
        self.labelPrimero.setVisible(True)

        self.primeroFecha = QtWidgets.QLineEdit(self.widgetLienzo)
        self.primeroFecha.setGeometry(QtCore.QRect(370, 70, 261, 31))
        self.primeroFecha.setText("")
        self.primeroFecha.setObjectName("primeroFecha")
        self.primeroFecha.setPlaceholderText("FECHA (YYYY-MM-DD)")
        self.primeroFecha.setMaxLength(20)
        self.primeroFecha.setVisible(True)


        self.bottonCommit = QtWidgets.QPushButton(self.widgetLienzo)
        # Establece tamaño y posicion del QpushButton
        self.bottonCommit.setGeometry(QtCore.QRect(680, 23, 120, 50))
        # Establece el texto al QPushButton
        self.bottonCommit.setText("Buscar")
        # creamos una variable local para el objeto QIcon
        self.bottonCommit.setObjectName("bottonCommit")
        self.bottonCommit.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.bottonCommit.setVisible(True)

        self.bottonCommit.clicked.connect(self.buscarA)

        self.vendido = QtWidgets.QLabel(self.widgetLienzo)
        self.vendido.setGeometry(QtCore.QRect(30, 120, 500, 41))
        self.vendido.setObjectName("vendido")
        self.vendido.setText('Total vendido:')
        self.vendido.setVisible(True)

        self.vendidoR = QtWidgets.QLabel(self.widgetLienzo)
        self.vendidoR.setGeometry(QtCore.QRect(240, 120, 500, 41))
        self.vendidoR.setObjectName("vendidoR")
        self.vendidoR.setText('')
        self.vendidoR.setVisible(True)


        self.nroproductos = QtWidgets.QLabel(self.widgetLienzo)
        self.nroproductos.setGeometry(QtCore.QRect(30, 200, 600, 41))
        self.nroproductos.setObjectName("nroproductos")
        self.nroproductos.setText('Total Productos Vendidos:')
        self.nroproductos.setVisible(True)


        self.nroproductosR = QtWidgets.QLabel(self.widgetLienzo)
        self.nroproductosR.setGeometry(QtCore.QRect(350, 200, 500, 41))
        self.nroproductosR.setObjectName("nroproductosR")
        self.nroproductosR.setText('')
        self.nroproductosR.setVisible(True)



    def segundo(self):
        self.limpiarLienzo()
        self.crearLienzo()

        self.labelPrimero = QtWidgets.QLabel(self.widgetLienzo)
        self.labelPrimero.setGeometry(QtCore.QRect(30, 30, 500, 41))
        self.labelPrimero.setObjectName("labelHasta")
        self.labelPrimero.setText('Empleado que más ventas realizó entre:')
        self.labelPrimero.setVisible(True)

        self.primeroFecha = QtWidgets.QLineEdit(self.widgetLienzo)
        self.primeroFecha.setGeometry(QtCore.QRect(30, 90, 261, 31))
        self.primeroFecha.setText("")
        self.primeroFecha.setObjectName("primeroFecha")
        self.primeroFecha.setPlaceholderText("FECHA (YYYY-MM-DD)")
        self.primeroFecha.setMaxLength(20)
        self.primeroFecha.setVisible(True)

        self.segundaFecha = QtWidgets.QLineEdit(self.widgetLienzo)
        self.segundaFecha.setGeometry(QtCore.QRect(310, 90, 261, 31))
        self.segundaFecha.setText("")
        self.segundaFecha.setObjectName("segundaFecha")
        self.segundaFecha.setPlaceholderText("FECHA (YYYY-MM-DD)")
        self.segundaFecha.setMaxLength(20)
        self.segundaFecha.setVisible(True)

        self.nombre = QtWidgets.QLabel(self.widgetLienzo)
        self.nombre.setGeometry(QtCore.QRect(30, 160, 500, 41))
        self.nombre.setObjectName("nombre")
        self.nombre.setText("")
        self.nombre.setVisible(True)


        self.bottonCommit = QtWidgets.QPushButton(self.widgetLienzo)
        # Establece tamaño y posicion del QpushButton
        self.bottonCommit.setGeometry(QtCore.QRect(680, 23, 120, 50))
        # Establece el texto al QPushButton
        self.bottonCommit.setText("Buscar")
        # creamos una variable local para el objeto QIcon
        self.bottonCommit.setObjectName("bottonCommit")
        self.bottonCommit.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.bottonCommit.setVisible(True)

        self.bottonCommit.clicked.connect(self.buscarB)

    def tercero(self):
        self.limpiarLienzo()
        self.crearLienzo() 

        self.labelPrimero = QtWidgets.QLabel(self.widgetLienzo)
        self.labelPrimero.setGeometry(QtCore.QRect(30, 30, 900, 50))
        self.labelPrimero.setObjectName("labelPrimero")
        self.labelPrimero.setText('Número de sandalias y Zapatillas vendidas y promedio de ganancia rebicidas en :')
        self.labelPrimero.wordWrap()
        self.labelPrimero.setVisible(True)

        self.ciudad = QtWidgets.QComboBox(self.widgetLienzo)
        self.ciudad.setGeometry(QtCore.QRect(630, 70, 140, 30))
        self.ciudad.setObjectName("ciudad")
        self.ciudad.setObjectName("comboBox")

        self.ciudad.addItem('')
        self.ciudad.addItem('Bogotá')
        self.ciudad.addItem('Medellín')
        self.ciudad.addItem('Barranquilla')
        self.ciudad.addItem('Cúcuta')
        self.ciudad.addItem('Cali')
        self.ciudad.addItem('Bucaramanga')
        self.ciudad.addItem('Santa Marta')
        self.ciudad.addItem('Leticia')

        self.ciudad.setVisible(True)

        self.terzapatilla = QtWidgets.QLabel(self.widgetLienzo)
        self.terzapatilla.setGeometry(QtCore.QRect(30, 90, 700, 50))
        self.terzapatilla.setObjectName("terzapatilla")
        self.terzapatilla.setText('ZAPATILLAS')
        self.terzapatilla.wordWrap()
        self.terzapatilla.setVisible(True)

        self.terGanancia = QtWidgets.QLabel(self.widgetLienzo)
        self.terGanancia.setGeometry(QtCore.QRect(210, 90, 700, 50))
        self.terGanancia.setObjectName("terGanancia")
        self.terGanancia.setText('GANANCIA')
        self.terGanancia.wordWrap()
        self.terGanancia.setVisible(True)

        self.terGananciaR = QtWidgets.QLabel(self.widgetLienzo)
        self.terGananciaR.setGeometry(QtCore.QRect(210, 150, 700, 50))
        self.terGananciaR.setObjectName("terGananciaR")
        self.terGananciaR.setText('')
        self.terGananciaR.wordWrap()
        self.terGananciaR.setVisible(True)




        self.tercantidad = QtWidgets.QLabel(self.widgetLienzo)
        self.tercantidad.setGeometry(QtCore.QRect(390, 90, 700, 50))
        self.tercantidad.setObjectName("tercantidad")
        self.tercantidad.setText('CANTIDAD')
        self.tercantidad.wordWrap()
        self.tercantidad.setVisible(True)

        self.tercantidadR = QtWidgets.QLabel(self.widgetLienzo)
        self.tercantidadR.setGeometry(QtCore.QRect(390, 150, 700, 50))
        self.tercantidadR.setObjectName("tercantidadR")
        self.tercantidadR.setText('')
        self.tercantidadR.wordWrap()
        self.tercantidadR.setVisible(True)


        #sandlias
        self.sandalia = QtWidgets.QLabel(self.widgetLienzo)
        self.sandalia.setGeometry(QtCore.QRect(30, 250, 700, 50))
        self.sandalia.setObjectName("sandalia")
        self.sandalia.setText('SANDALIAS')
        self.sandalia.wordWrap()
        self.sandalia.setVisible(True)


        self.sanGanancia = QtWidgets.QLabel(self.widgetLienzo)
        self.sanGanancia.setGeometry(QtCore.QRect(210, 250, 700, 50))
        self.sanGanancia.setObjectName("sanGanancia")
        self.sanGanancia.setText('GANANCIA')
        self.sanGanancia.wordWrap()
        self.sanGanancia.setVisible(True)

        self.sanGananciaR = QtWidgets.QLabel(self.widgetLienzo)
        self.sanGananciaR.setGeometry(QtCore.QRect(210, 310, 700, 50))
        self.sanGananciaR.setObjectName("sanGananciaR")
        self.sanGananciaR.setText('')
        self.sanGananciaR.wordWrap()
        self.sanGananciaR.setVisible(True)

        self.sancantidad = QtWidgets.QLabel(self.widgetLienzo)
        self.sancantidad.setGeometry(QtCore.QRect(390, 250, 700, 50))
        self.sancantidad.setObjectName("sancantidad")
        self.sancantidad.setText('CANTIDAD')
        self.sancantidad.wordWrap()
        self.sancantidad.setVisible(True)

        self.sancantidadR = QtWidgets.QLabel(self.widgetLienzo)
        self.sancantidadR.setGeometry(QtCore.QRect(390, 310, 700, 50))
        self.sancantidadR.setObjectName("tercantidadR")
        self.sancantidadR.setText('')
        self.sancantidadR.wordWrap()
        self.sancantidadR.setVisible(True)



        self.bottonCommit = QtWidgets.QPushButton(self.widgetLienzo)
        # Establece tamaño y posicion del QpushButton
        self.bottonCommit.setGeometry(QtCore.QRect(630, 500, 120, 50))
        # Establece el texto al QPushButton
        self.bottonCommit.setText("Buscar")
        # creamos una variable local para el objeto QIcon
        self.bottonCommit.setObjectName("bottonCommit")
        self.bottonCommit.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.bottonCommit.setVisible(True)

        self.bottonCommit.clicked.connect(self.buscarC)









    def buscarA(self): 
        self.table = None
        fecha = self.primeroFecha.text()
        print(fecha)
        self.cursor.callproc('Ventas_Desde_Mes',[fecha])
        for result in self.cursor.stored_results():
            l = result.fetchall()

        self.vendidoR.setText(str(l[0][0]))         
        self.nroproductosR.setText(str(l[0][1]))

    def buscarB(self):
        self.table = None   
        fecha = self.primeroFecha.text()
        fecha2 = self.segundaFecha.text()
        print(fecha)
        print(fecha2)
        self.cursor.callproc('Empleado_Ventas',[fecha,fecha2])
        for result in self.cursor.stored_results():
            l = result.fetchall()
            print(l)
        
        try:
            nombre = l[0][0]+ ' ' + l[0][1]
            self.nombre.setText(nombre)
        
        except :
            self.nombre.setText('No se realizaron ventas en esta fecha')


    def buscarC(self):
        c = self.ciudad.currentText()
        self.cursor.callproc('Total_En_Ciudad',[c])
        
        for result in self.cursor.stored_results():
            l = result.fetchall()
        print(l)
        if len(l)==1:
            self.sancantidadR.setText(str(int(l[0][1])))
            self.sanGananciaR.setText(str(int(l[0][2])))

            self.terGananciaR.setText('No hubo ventas')
            self.tercantidadR.setText('No hubo ventas')

        else:
            self.sancantidadR.setText(str(int(l[0][1])))
            self.sanGananciaR.setText(str(int(l[0][2])))

            self.terGananciaR.setText(str(int(l[1][2])))
            self.tercantidadR.setText(str(int(l[1][1])))
            


        



                  


    def limpiarLienzo(self):   
        self.widgetLienzo.setParent(None)
        self.widgetLienzo.deleteLater()
        self.widgetLienzo = None

    def crearLienzo(self):
        
        self.widgetLienzo = QtWidgets.QWidget(self.centralwidget)
        self.widgetLienzo.setGeometry(QtCore.QRect(250, 40, 1100, 600))
        self.widgetLienzo.setAutoFillBackground(False)
        self.widgetLienzo.setObjectName("widgetLienzo")
        self.widgetLienzo.setVisible(True)

    def crearTabla(self):
          self.table = QTableWidget(self.widgetLienzo)
          self.table.setGeometry(QtCore.QRect(30,80,1700,800))
          self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
          self.table.resizeColumnsToContents()
          self.table.setColumnCount(1)
          self.table.setRowCount(1)
          self.table.setVisible(True)
          self.table.setAlternatingRowColors(True) 
          self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)







def window():
    app =  QApplication(sys.argv)
    #app.setStyleSheet(stylesheet)
    win = ventana_consulta('mpcalderon')
    win.show()
    sys.exit(app.exec_())
#se ejecuta solo si se ejecuta desde esta ventana
if __name__ == "__main__":
    window()