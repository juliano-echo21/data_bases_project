from  PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QGridLayout, QTableView
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import mysql.connector



class ventana_consulta(QMainWindow):

    def __init__(self,role):
        super(ventana_consulta,self).__init__()
        self.role = role
        self.resize(1300,700)
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
        self.botonLateral_1.setText("A")
        self.botonLateral_1.clicked.connect(self.primer)

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
        self.botonLateral_2.setText("B")
        
        self.botonLateral_2.clicked.connect(self.segundo)



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
        self.botonLateral_3.setText("C")
        
        self.botonLateral_3.clicked.connect(self.tercero)

        #botón 4

        
        

    def primer(self):
        self.limpiarLienzo()
        self.crearLienzo()
        self.crearTabla()

        self.labelPrimero = QtWidgets.QLabel(self.widgetLienzo)
        self.labelPrimero.setGeometry(QtCore.QRect(30, 30, 900, 41))
        self.labelPrimero.setObjectName("labelHasta")
        self.labelPrimero.setText('Fecha de pedido, fecha de facturación y nombre del producto de pedidos superiores a:')
        self.labelPrimero.setVisible(True)

        self.cantidad = QtWidgets.QLineEdit(self.widgetLienzo)
        self.cantidad.setGeometry(QtCore.QRect(370, 70, 261, 31))
        self.cantidad.setText("")
        self.cantidad.setObjectName("cantidad")
        self.cantidad.setPlaceholderText("Cantidad")
        self.cantidad.setMaxLength(20)
        self.cantidad.setVisible(True)


        self.bottonCommit = QtWidgets.QPushButton(self.widgetLienzo)
        # Establece tamaño y posicion del QpushButton
        self.bottonCommit.setGeometry(QtCore.QRect(790, 80, 120, 50))
        # Establece el texto al QPushButton
        self.bottonCommit.setText("Buscar")
        # creamos una variable local para el objeto QIcon
        self.bottonCommit.setObjectName("bottonCommit")
        self.bottonCommit.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.bottonCommit.setVisible(True)

        self.bottonCommit.clicked.connect(self.buscarA)


    def segundo(self):
        self.limpiarLienzo()
        self.crearLienzo()
        self.crearTabla()
        self.cursor.callproc('Clientes_Cambio')
        for result in self.cursor.stored_results():
            self.l=result.fetchall()

        self.filas = len(self.l)
        self.columnas = len(self.l[0])
        print(self.filas)
        print(self.columnas)

        self.table.setRowCount(self.filas)
        self.table.setColumnCount(self.columnas)

        self.table.setHorizontalHeaderLabels(['Nombre','Apellido', 
                        'Ciudad','# Días'
                        ])
        
        self.nombre_cols = ['Nombre','Apellido', 
                        'Ciudad','# Días']
        
        self.labelPrimero = QtWidgets.QLabel(self.widgetLienzo)
        self.labelPrimero.setGeometry(QtCore.QRect(30, 30, 700, 80))
        self.labelPrimero.setObjectName("labelHasta")
        self.labelPrimero.setWordWrap(True)
        self.labelPrimero.setText('Información de los clientes que han solicitado cambios y días transcurridos desde la compra hasta el cambio')
        self.labelPrimero.setVisible(True)

        self.bottonCommit = QtWidgets.QPushButton(self.widgetLienzo)
        # Establece tamaño y posicion del QpushButton
        self.bottonCommit.setGeometry(QtCore.QRect(800, 50, 120, 50))
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
        self.labelPrimero.setGeometry(QtCore.QRect(30, 30, 700, 41))
        self.labelPrimero.setObjectName("labelHasta")
        self.labelPrimero.setWordWrap(True)
        self.labelPrimero.setText('Ganancias recibidas por: ')
        self.labelPrimero.setVisible(True)

        self.nomPro = QtWidgets.QLineEdit(self.widgetLienzo)
        self.nomPro.setGeometry(QtCore.QRect(370, 90, 261, 31))
        self.nomPro.setText("")
        self.nomPro.setObjectName("nomPro")
        self.nomPro.setPlaceholderText("NOMBRE PRODUCTO")
        self.nomPro.setMaxLength(20)
        self.nomPro.setVisible(True)

        self.gananciasPro = QtWidgets.QLabel(self.widgetLienzo)
        self.gananciasPro.setGeometry(QtCore.QRect(30, 180, 200, 41))
        self.gananciasPro.setObjectName("gananciasPro")
        self.gananciasPro.setWordWrap(True)
        self.gananciasPro.setText('GANANCIAS:  ')
        self.gananciasPro.setVisible(True)

        self.gananciasProR = QtWidgets.QLabel(self.widgetLienzo)
        self.gananciasProR.setGeometry(QtCore.QRect(300, 180, 200, 41))
        self.gananciasProR.setObjectName("gananciasProR")
        self.gananciasProR.setWordWrap(True)
        self.gananciasProR.setText('')
        self.gananciasProR.setVisible(True)




        self.bottonCommit = QtWidgets.QPushButton(self.widgetLienzo)
        # Establece tamaño y posicion del QpushButton
        self.bottonCommit.setGeometry(QtCore.QRect(800, 50, 120, 50))
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
        print('funciona')
        self.cant = self.cantidad.text()
        try:
            self.cursor.callproc('Pedidos_Con_Cantidad',[self.cant])
            for result in self.cursor.stored_results():
                self.l = result.fetchall()
            print(self.l)

            if len(self.l)>0:
                self.columnas = len(self.l[0])
                self.filas = len(self.l)
            
                self.table.setRowCount(self.filas)
                self.table.setColumnCount(self.columnas)
                self.table.setHorizontalHeaderLabels(['Fecha Pedido','Fecha Facturacion', 
                        'Producto'
                        ])

                for i in range(len(self.l)):
                    for j in range(len(self.l[0])):
                        self.table.setItem(i,j,QTableWidgetItem(str(self.l[i][j])))


            else:
                print('cholo')
                self.table.setRowCount(1)
                self.table.setColumnCount(1)
                self.table.setItem(0,0,QTableWidgetItem('NO HAY REGISTROS'))

        except:
            print('valor muy grand')                        

        



    def limpiarLienzo(self):   
        self.widgetLienzo.setParent(None)
        self.widgetLienzo.deleteLater()
        self.widgetLienzo = None

    def crearLienzo(self):
        
        self.widgetLienzo = QtWidgets.QWidget(self.centralwidget)
        self.widgetLienzo.setGeometry(QtCore.QRect(250, 40, 1100, 900))
        self.widgetLienzo.setAutoFillBackground(False)
        self.widgetLienzo.setObjectName("widgetLienzo")
        self.widgetLienzo.setVisible(True)


    def buscarB(self):
        print('funciona')
        
        for i in range (len(self.l)):
            for j in range(len(self.l[0])):
                self.table.setItem(i,j,QTableWidgetItem(str(self.l[i][j])))


    def buscarC(self):
        print('funcionas')
        self.nomProtext = self.nomPro.text()
        
        self.cursor.callproc('Ganancias_Producto',[self.nomProtext])
        for result in self.cursor.stored_results():
            self.l = result.fetchall()
        print(self.l)
        if len(self.l)>0:
            self.gananciasProR.setText(str(int(self.l[0][1])))
        else:
             self.gananciasProR.setText('no ha generado ganancias')
        








    def crearTabla(self):
          self.table = QTableWidget(self.widgetLienzo)
          self.table.setGeometry(QtCore.QRect(30,140,900,500))
          self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
          self.table.resizeColumnsToContents()
          self.table.setColumnCount(1)
          self.table.setRowCount(1)
          self.table.setVisible(True)
          self.table.setAlternatingRowColors(True) 
          self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

def window():
    app =  QApplication(sys.argv)
   # app.setStyleSheet(stylesheet)
    win = ventana_consulta('jmanosalva')
    win.show()
    sys.exit(app.exec_())
#se ejecuta solo si se ejecuta desde esta ventana
if __name__ == "__main__":
    window()