from  PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QGridLayout, QTableView
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import mysql.connector



class ventana_update(QMainWindow):

    def __init__(self,role):
        super(ventana_update,self).__init__()
        self.role = role
        self.resize(1500,900)
        self.setWindowTitle('ACTUALIZAR')
        self.showMaximized() 
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

    def defineRole(self): 
        if self.role == 'mpcalderon':
            self.combotablas.addItem('')
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
            self.combotablas.addItem('')
            self.combotablas.addItem('producto')

        if self.role == 'jrincon':
            self.combotablas.addItem('material')
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

        #cuando cambia el texto se llama a la funcion que crea las tablas
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
         "ubicacion" :None,
         "proveedor" : self. mosProveedor,
        'factura venta': None,
        'compra material': None
         }
        self.aux = self.switcher.get(self.tab_actual)
        if self.aux is not None:
            self.aux()

    #mostrar la tabla cliente cuando se oprima el botón
    def mosCliente(self):
        print('cliente')
        self.crearTabla()
        #trae el numeor de registros de la tabla
        q = 'select count(*) from cliente;'
        
        #ejecuta la consulta
        self.cursor.execute(q)
        self.rows = self.cursor.fetchall()[0][0]
        self.table.setRowCount(self.rows)

        #trae el numero de columnas de la tabla cliente
        q = "SELECT  COUNT(*)  FROM Information_Schema.Columns WHERE Table_Name = 'cliente'"
        self.cursor.execute(q)
        self.columns = self.cursor.fetchall()[0][0]
        self.table.setColumnCount(self.columns)
        print('hola')
        #pone los nombres a las columnas de la tabla
        self.table.setHorizontalHeaderLabels(['Documento','Tipo doc', 
                        'Nombre','Apellido','Telefono','Correo'
                        ])
        
        self.nombre_cols = ['Cliente_Documento','Cliente_Tipo_Documento', 
                        'Cliente_Nombre','Cliente_Apellido','Cliente_Telefono',
                        'Cliente_Correo']
    
        #traer los registros de la tabla cliente
        q = 'select * from cliente;'
        self.cursor.execute(q)
        self.resultados = self.cursor.fetchall()
        
        #llenar la tabla con los registros con 2 ciclos for
        for j in range (len(self.resultados)):
            registro = self.resultados[j]
            for i in range (len(registro)):
                self.table.setItem(j,i,QTableWidgetItem(str(registro[i])))

        self.ajustar_columnas()
        self.table.itemChanged.connect(lambda x : self.Actualizar('cliente'))


    #funcion que muestra la tabla material
    def mosMaterial(self):
        print('material')
        self.crearTabla()

        #traer todos los registros de la tabla material
        q = 'select count(*) from material;'
        #ejecutar consulta
        self.cursor.execute(q)
        self.rows = self.cursor.fetchall()[0][0]
        self.table.setRowCount(self.rows)

        #traer el numero de columnas de la tabla
        q = "SELECT  COUNT(*)  FROM Information_Schema.Columns WHERE Table_Name = 'material'"
        self.cursor.execute(q)
        self.columns = self.cursor.fetchall()[0][0]
        self.table.setColumnCount(self.columns)
        print('hola')

        #nombrar las columnas de la tabla
        self.table.setHorizontalHeaderLabels(['ID','Nombre', 
                        'Precio','Proveedor ID'
                        ])
        
        self.nombre_cols = ['ID_Material','Mat_Nombre', 
                        'Mat_Precio','ID_Proveedor']
    


        q = 'select * from material;'
        self.cursor.execute(q)
        self.resultados = self.cursor.fetchall()
        
        #llenar la tabla con 2 ciclos for
        for j in range (len(self.resultados)):
            registro = self.resultados[j]
            for i in range (len(registro)):
                self.table.setItem(j,i,QTableWidgetItem(str(registro[i])))
        
        
        #self.ajustar_columnas()
        self.table.itemChanged.connect(lambda x : self.Actualizar('material'))




    #mostrar empleado 
    def mosEmpleado(self):
        self.crearTabla()
        print('empleado')
        #traer todos los registros de la tabla
        q = 'select count(*) from empleado;'
        self.cursor.execute(q)
        self.rows = self.cursor.fetchall()[0][0]
        self.table.setRowCount(self.rows)
        #traer el numero de columnas de la tabla para así ajustar la tabla
        q = "SELECT  COUNT(*)  FROM Information_Schema.Columns WHERE Table_Name = 'Empleado'"
        self.cursor.execute(q)
        self.columns = self.cursor.fetchall()[0][0]
        self.table.setColumnCount(self.columns)
        print('hola')
        self.table.setHorizontalHeaderLabels(['Documento','Tipo doc', 
                        'Nombre','Apellido','F Nacimiento','Correo',
                        'Dirección','Teléfono','Cargo','Profesión','S Social'])
        
        self.nombre_cols =['Documento_Empleado','Emp_Tipo_Documento', 
                        'Emp_Nombre','Emp_Apellido','Emp_Fecha_Nacimiento','Emp_Correo',
                        'Emp_Direccion','Emp_Telefono','Emp_Cargo','Emp_Profesión',
                        'Emp_Seguridad_Social']
        
        q = 'select * from empleado;'

        self.cursor.execute(q)
        self.resultados = self.cursor.fetchall()
        #llenar las tablas con dos coclos for
        for j in range (len(self.resultados)):
            registro = self.resultados[j]
            for i in range (len(registro)):
                self.table.setItem(j,i,QTableWidgetItem(str(registro[i])))
        
        self.ajustar_columnas()
        self.table.itemChanged.connect(lambda x : self.Actualizar('empleado'))


    def mosProducto(self):
        print('producto')
        self.crearTabla()

        q = 'select count(*) from producto;'
        self.cursor.execute(q)
        self.rows = self.cursor.fetchall()[0][0]
        self.table.setRowCount(self.rows)
        q = "SELECT  COUNT(*)  FROM Information_Schema.Columns WHERE Table_Name = 'producto'"
        self.cursor.execute(q)
        self.columns = self.cursor.fetchall()[0][0]
        self.table.setColumnCount(self.columns)
        print('hola')
        self.table.setHorizontalHeaderLabels(['ID','Tipo', 
                        'Modelo','Color','Talla','Precio'
                        ])
        
        self.nombre_cols = ['ID_Producto','Producto_Tipo', 
                        'Producto_Modelo','Producto_Color','Producto_Talla',
                        'Producto_Precio']
    
        q = 'select * from producto;'
        self.cursor.execute(q)
        self.resultados = self.cursor.fetchall()
        
        for j in range (len(self.resultados)):
            registro = self.resultados[j]
            for i in range (len(registro)):
                self.table.setItem(j,i,QTableWidgetItem(str(registro[i])))
        
        self.ajustar_columnas()
        self.table.itemChanged.connect(lambda x : self.Actualizar('producto'))

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
                        'Teléfono','Empresa'
                        ])
        
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

        self.table.itemChanged.connect(lambda x : self.Actualizar('proveedor'))



    def ajustar_columnas(self):
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.resizeColumnsToContents()

    def Actualizar(self,tabla):
        print('cambiando ando')
        self.colActual = self.table.currentColumn()
        self.rowActual = self.table.currentRow()
        self.id = int(self.table.item(self.rowActual,0).text())
        self.valor = self.table.currentItem().text()

        if self.valor.isdigit():
            pass
        else:
            self.valor = "'"+self.valor+"'"

        q = 'UPDATE '+ tabla +' SET '+ self.nombre_cols[self.colActual] +' = '+ self.valor +' WHERE '+self.nombre_cols[0]+ ' = '+ str(self.id)+';'
        print(q)
        try:
            self.cursor.execute(q)
            self.conn.commit()
            print('ok')
        except :
            print('huy zonas')





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



def window():
    app =  QApplication(sys.argv)
   # app.setStyleSheet(stylesheet)
    win = ventana_update('jmanosalva')
    win.show()
    sys.exit(app.exec_())
#se ejecuta solo si se ejecuta desde esta ventana
if __name__ == "__main__":
    window()