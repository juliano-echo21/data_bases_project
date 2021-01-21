from  PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QGridLayout, QTableView, QMessageBox
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import mysql.connector



class ventana_borrar(QMainWindow):

    def __init__(self,role):
        super(ventana_borrar,self).__init__()
        self.role = role
        self.resize(1500,900)
        self.setWindowTitle('BORRAR')
        self.showMaximized() 
        self.conection()
        with open("style.css") as f:
            self.setStyleSheet(f.read())
        self.setupUi()




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


    def defineRole(self): 
        if self.role == 'mpcalderon':
            self.combotablas.addItem('cambio')
            self.combotablas.addItem('cliente')
            self.combotablas.addItem('compra Material')
            self.combotablas.addItem('empleado')
            self.combotablas.addItem('factura Venta')
            self.combotablas.addItem('material')
            self.combotablas.addItem('producto')
            self.combotablas.addItem('proveedor')
            self.combotablas.addItem('ubicación')

        if self.role=='jmanosalva':
            self.combotablas.addItem('Sin Acceso')

        if self.role == 'jrincon':
            self.combotablas.addItem('empleado')
            self.combotablas.addItem('factura Venta')
            self.combotablas.addItem('proveedor')

    
    def setupUi(self):
        self.cursor = self.conn.cursor()
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        self.crearLienzo()
           # self.table = QTableWidget(self.widgetLienzo)
            #self.table.setGeometry(QtCore.QRect(30,80,1700,800))
            #self.table.setColumnCount(1)
            #self.table.setRowCount(1)

        self.combotablas = QtWidgets.QComboBox(self.centralwidget)
        self.combotablas.setGeometry(QtCore.QRect(30, 60, 200, 21))
        self.combotablas.setObjectName("comboBox")
        self.defineRole()

        self.combotablas.currentIndexChanged.connect(self.cambio_tabla) 


    def cambio_tabla(self):
        self.table = None
        self.tab_actual = self.combotablas.currentText()
        print(self.tab_actual)
        #self.crearLienzo()
        self.switcher = {  
         "cambio" : None,
         "cliente": self.mosCliente,
         "empleado": self.mosEmpleado,
         "material": self.mosMaterial,
         "producto" : self.mosProducto,
         "ubicación" :self.mosUbicacion,
         "proveedor" : self.mosProveedor,
        'factura Venta': None,
        'compra material': None
         }
        self.aux = self.switcher.get(self.tab_actual)
        if self.aux is not None:
            self.aux()

    def mosEmpleado(self):
        pass
    def mosMaterial(self):
        pass
    def mosProducto(self):
        pass



    def mosProveedor(self):
        print('proveedor')
        self.crearTabla()

        q = 'select count(*) from proveedor;'
        self.cursor.execute(q)
        self.rows = self.cursor.fetchall()[0][0]
        self.table.setRowCount(self.rows)
        q = "SELECT  COUNT(*)  FROM Information_Schema.Columns WHERE Table_Name = 'proveedor'"
        self.cursor.execute(q)
        self.columns = self.cursor.fetchall()[0][0]
        self.table.setColumnCount(self.columns)
        print('hola')
        self.table.setHorizontalHeaderLabels(['ID','Nombre', 
                        'Teléfono','Empresa'])
        
        self.nombre_cols = ['ID_Proveedor','Prov_Nombre', 
                        'Prov_Telefono','Prov_Empresa']
    
        q = 'select * from proveedor;'
        self.cursor.execute(q)
        self.resultados = self.cursor.fetchall()
        
        for j in range (len(self.resultados)):
            registro = self.resultados[j]
            for i in range (len(registro)):
                self.table.setItem(j,i,QTableWidgetItem(str(registro[i])))

        #self.ajustar_columnas()
        #self.table.itemDoubleClicked .connect(lambda x : self.Borrar('Ubicacion'))
        

    def mosUbicacion(self):
        print('ubicacion')
        self.crearTabla()

        q = 'select count(*) from ubicacion;'
        self.cursor.execute(q)
        self.rows = self.cursor.fetchall()[0][0]
        self.table.setRowCount(self.rows)
        q = "SELECT  COUNT(*)  FROM Information_Schema.Columns WHERE Table_Name = 'ubicacion'"
        self.cursor.execute(q)
        self.columns = self.cursor.fetchall()[0][0]
        self.table.setColumnCount(self.columns)
        print('hola')
        self.table.setHorizontalHeaderLabels(['ID','Ciudad', 
                        'Región','Direccion','C. Postal','Cliente Documento'
                        ])
        
        self.nombre_cols = ['ID_Ubicacion','Ubi_Ciudad', 
                        'Ubi_Region','Ubi_Direccion','Ubi_Codigo_Postal',
                        'Cliente_Documento']
    
        q = 'select * from Ubicacion;'
        self.cursor.execute(q)
        self.resultados = self.cursor.fetchall()
        
        for j in range (len(self.resultados)):
            registro = self.resultados[j]
            for i in range (len(registro)):
                self.table.setItem(j,i,QTableWidgetItem(str(registro[i])))

        self.ajustar_columnas()
        self.table.itemDoubleClicked .connect(lambda x : self.Borrar('Ubicacion'))




    def mosCliente(self):
        print('cliente')
        self.crearTabla()

        q = 'select count(*) from cliente;'
        self.cursor.execute(q)
        self.rows = self.cursor.fetchall()[0][0]
        self.table.setRowCount(self.rows)
        q = "SELECT  COUNT(*)  FROM Information_Schema.Columns WHERE Table_Name = 'cliente'"
        self.cursor.execute(q)
        self.columns = self.cursor.fetchall()[0][0]
        self.table.setColumnCount(self.columns)
        print('hola')
        self.table.setHorizontalHeaderLabels(['Documento','Tipo doc', 
                        'Nombre','Apellido','Telefono','Correo'
                        ])
        
        self.nombre_cols = ['Cliente_Documento','Cliente_Tipo_Documento', 
                        'Cliente_Nombre','Cliente_Apellido','Cliente_Telefono',
                        'Cliente_Correo']
    
        q = 'select * from cliente;'
        self.cursor.execute(q)
        self.resultados = self.cursor.fetchall()
        
        for j in range (len(self.resultados)):
            registro = self.resultados[j]
            for i in range (len(registro)):
                self.table.setItem(j,i,QTableWidgetItem(str(registro[i])))

        self.ajustar_columnas()
        self.table.itemDoubleClicked .connect(lambda x : self.Borrar('cliente'))


    def Borrar(self,tabla):
        print('cambiando ando')
        self.colActual = self.table.currentColumn()
        self.rowActual = self.table.currentRow()
        self.id = int(self.table.item(self.rowActual,0).text())
        self.valor = self.table.currentItem().text()

        print(self.id)
        print(self.valor)
        
        q = 'DELETE FROM  '+ tabla +' WHERE '+self.nombre_cols[0]+ ' = '+ str(self.id)+';'
        try:
            self.cursor.execute(q)
            self.conn.commit()
            print('ok')
            print(q) 
        
        except mysql.connector.Error   as e:
            print(e)
            e = str(e)
            self. msg = QMessageBox()
            self.msg.setText(e)
            self.msg.exec_()

        
        
    



    def limpiarLienzo(self):   
        self.widgetLienzo.setParent(None)
        self.widgetLienzo.deleteLater()
        self.widgetLienzo = None

    def crearLienzo(self):
        
        self.widgetLienzo = QtWidgets.QWidget(self.centralwidget)
        self.widgetLienzo.setGeometry(QtCore.QRect(30, 90, 1800, 1000))
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

    def ajustar_columnas(self):
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.resizeColumnsToContents()






def window():
    app =  QApplication(sys.argv)
    #app.setStyleSheet(stylesheet)
    win = ventana_borrar('mpcalderon')
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()