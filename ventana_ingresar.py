from  PyQt5 import QtWidgets, QtCore,QtGui, QtSql 
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtSql import QSqlQuery;
import mysql.connector
from mysql.connector import Error


class ventana_ingresar(QMainWindow):
    def __init__(self,role):
        super(ventana_ingresar,self).__init__()
        self.resize(1100,700)
        self.setWindowTitle('INGRESAR')
        with open("style.css") as f:
            self.setStyleSheet(f.read())
        self.role = role
        
        self.conection()
        self.setupUi()

    def conection(self):
        #de acuerdo con el role que se haya pasado por parámetro
        #por medio del metodo connect de la clase connector
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
        elif self.role == 'jrincon':
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
        self.combotablas = QtWidgets.QComboBox(self.centralwidget)
        self.combotablas.setGeometry(QtCore.QRect(30, 60, 200, 21))
        self.combotablas.setObjectName("comboBox")
        self.combotablas.currentIndexChanged.connect(self.cambio_tabla) 

        if self.role == 'mpcalderon':
            self.combotablas.addItem('cambio')
            self.combotablas.addItem('cliente')
            self.combotablas.addItem('empleado')
            self.combotablas.addItem('material')
            self.combotablas.addItem('producto')
            self.combotablas.addItem('ubicacion')
            self.combotablas.addItem('proveedor')
            self.combotablas.addItem('factura venta')
            self.combotablas.addItem('compra material')
        elif self.role == 'jmanosalva':
            self.combotablas.addItem('cambio')
            self.combotablas.addItem('cliente')
            self.combotablas.addItem('ubicacion')
            self.combotablas.addItem('producto')
            self.combotablas.addItem('factura venta')
        elif self.role=='jrincon':
            self.combotablas.addItem('proveedor')
            self.combotablas.addItem('empleado')
            self.combotablas.addItem('factura venta')
            self.combotablas.addItem('compra material')



        


    def cambio_tabla(self):
        self.tab_actual = self.combotablas.currentText()
        print(self.tab_actual)
        self.limpiarLienzo()
        self.crearLienzo()
        self.switcher = {  
         "cambio" : self.mosCambio,
         "cliente": self.mosCliente,
         "empleado": self.mosEmpleado,
         "material": self.mosMaterial,
         "producto" : self.mosProducto,
         "ubicacion" : self.mosUbicacion,
         "proveedor" : self. mosProveedor,
        'factura venta': self.mosf_venta,
        'compra material': self.mosco_material
         }
        self.aux = self.switcher.get(self.tab_actual)
        if self.aux is not None:
            self.aux()
        
    def limpiarLienzo(self):   
        self.widgetLienzo.setParent(None)
        self.widgetLienzo.deleteLater()
        self.widgetLienzo = None

    def crearLienzo(self):
        
        self.widgetLienzo = QtWidgets.QWidget(self.centralwidget)
        self.widgetLienzo.setGeometry(QtCore.QRect(30, 90, 1100, 600))
        self.widgetLienzo.setAutoFillBackground(False)
        self.widgetLienzo.setObjectName("widgetLienzo")
        self.widgetLienzo.setVisible(True)


    def mosCambio(self):
        self.camMotivo = QtWidgets.QComboBox(self.widgetLienzo)
        self.camMotivo.setGeometry(QtCore.QRect(40, 50, 261, 31))
        self.camMotivo.setObjectName("camMotivo")
        self.camMotivo.setPlaceholderText("Motivo")
        self.camMotivo.setVisible(True)
        self.camMotivo.addItem("Defectuoso")

        self.camFecha = QtWidgets.QLineEdit(self.widgetLienzo)
        self.camFecha.setGeometry(QtCore.QRect(350, 50, 261, 31))
        self.camFecha.setText("")
        self.camFecha.setObjectName("camFecha")
        self.camFecha.setPlaceholderText("Fecha Cambio(YYY-MM-DD)")
        self.camFecha.setMaxLength(20)
        self.camFecha.setVisible(True)

        self.id_factura_v = QtWidgets.QLineEdit(self.widgetLienzo)
        self.id_factura_v.setGeometry(QtCore.QRect(660, 50, 261, 31))
        self.id_factura_v.setText("")
        self.id_factura_v.setObjectName("id_factura_v")
        self.id_factura_v.setPlaceholderText("ID Factura")
        self.id_factura_v.setMaxLength(20)
        self.id_factura_v.setVisible(True)

        self.ingresar = QtWidgets.QPushButton(self.widgetLienzo)
        self.ingresar.setGeometry(QtCore.QRect(40, 130, 261, 31))
        # Establece el texto al QPushButton
        self.ingresar.setText("INGRESAR")
        # creamos una variable local para el objeto QIcon
        self.ingresar.setObjectName("botonLateral_3")
        self.ingresar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.ingresar.setVisible(True)
        self.ingresar.clicked.connect(lambda x : self.insert_data(0))
        


###1
    def mosCliente(self):
        self.cliDocumento = QtWidgets.QLineEdit(self.widgetLienzo)
        self.cliDocumento.setGeometry(QtCore.QRect(40, 50, 261, 31))
        self.cliDocumento.setText("")
        self.cliDocumento.setObjectName("cliDocumento")
        self.cliDocumento.setPlaceholderText("Documento Cliente")
        self.cliDocumento.setMaxLength(20)
        self.cliDocumento.setVisible(True)

        self.tipo_doc = QtWidgets.QComboBox(self.widgetLienzo)
        self.tipo_doc.setGeometry(QtCore.QRect(350, 50, 261, 31))
        self.tipo_doc.setObjectName("tipo_doc")
        self.tipo_doc.setPlaceholderText("Tipo Documento")
        self.tipo_doc.setVisible(True)
        self.tipo_doc.addItem("Cedula")
        self.tipo_doc.addItem("Cedula de extranjería")

        self.nomCliente = QtWidgets.QLineEdit(self.widgetLienzo)
        self.nomCliente.setGeometry(QtCore.QRect(660, 50, 261, 31))
        self.nomCliente.setText("")
        self.nomCliente.setObjectName("nomCliente")
        self.nomCliente.setPlaceholderText("Nombre Cliente")
        self.nomCliente.setMaxLength(20)
        self.nomCliente.setVisible(True)

        self.apeCliente = QtWidgets.QLineEdit(self.widgetLienzo)
        self.apeCliente.setGeometry(QtCore.QRect(40, 130, 261, 31))
        self.apeCliente.setText("")
        self.apeCliente.setObjectName("apeCliente")
        self.apeCliente.setPlaceholderText("Apellido Cliente")
        self.apeCliente.setMaxLength(20)
        self.apeCliente.setVisible(True)

        self.cliTelefono = QtWidgets.QLineEdit(self.widgetLienzo)
        self.cliTelefono.setGeometry(QtCore.QRect(350, 130, 261, 31))
        self.cliTelefono.setText("")
        self.cliTelefono.setObjectName("cliTelefono")
        self.cliTelefono.setPlaceholderText(" Teléfono")
        self.cliTelefono.setMaxLength(20)
        self.cliTelefono.setVisible(True)
        
        self.cliCorreo = QtWidgets.QLineEdit(self.widgetLienzo)
        self.cliCorreo.setGeometry(QtCore.QRect(660, 130, 261, 31))
        self.cliCorreo.setText("")
        self.cliCorreo.setObjectName("cliCorreo")
        self.cliCorreo.setPlaceholderText("Correo")
        self.cliCorreo.setMaxLength(60)
        self.cliCorreo.setVisible(True)
        
        

        self.ingresar = QtWidgets.QPushButton(self.widgetLienzo)
        self.ingresar.setGeometry(QtCore.QRect(660, 230, 230, 41))
        # Establece el texto al QPushButton
        self.ingresar.setText("INGRESAR")
        # creamos una variable local para el objeto QIcon
        self.ingresar.setObjectName("botonLateral_3")
        self.ingresar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.ingresar.setVisible(True)

        self.ingresar.clicked.connect(lambda x : self.insert_data(1))



       


###2        
    def mosEmpleado(self):
        self.docEmpleado = QtWidgets.QLineEdit(self.widgetLienzo)
        self.docEmpleado.setGeometry(QtCore.QRect(40, 50, 261, 31))
        self.docEmpleado.setText("")
        self.docEmpleado.setObjectName("docEmpleado")
        self.docEmpleado.setPlaceholderText("Documento Empleado")
        self.docEmpleado.setMaxLength(20)
        self.docEmpleado.setVisible(True)

        self.tipo_doc = QtWidgets.QComboBox(self.widgetLienzo)
        self.tipo_doc.setGeometry(QtCore.QRect(350, 50, 261, 31))
        self.tipo_doc.setObjectName("tipo_doc")
        self.tipo_doc.setPlaceholderText("Tipo Documento")
        self.tipo_doc.setVisible(True)
        self.tipo_doc.addItem("Cedula")
        self.tipo_doc.addItem("Cedula de extranjería")

        self.nomEmpleado = QtWidgets.QLineEdit(self.widgetLienzo)
        self.nomEmpleado.setGeometry(QtCore.QRect(660, 50, 261, 31))
        self.nomEmpleado.setText("")
        self.nomEmpleado.setObjectName("nomEmpleado")
        self.nomEmpleado.setPlaceholderText("Nombre Empleado")
        self.nomEmpleado.setMaxLength(20)
        self.nomEmpleado.setVisible(True)

        self.apeEmpleado = QtWidgets.QLineEdit(self.widgetLienzo)
        self.apeEmpleado.setGeometry(QtCore.QRect(40, 130, 261, 31))
        self.apeEmpleado.setText("")
        self.apeEmpleado.setObjectName("apeEmpleado")
        self.apeEmpleado.setPlaceholderText("Apellido Empleado")
        self.apeEmpleado.setMaxLength(20)
        self.apeEmpleado.setVisible(True)

        self.birthEmpleado = QtWidgets.QLineEdit(self.widgetLienzo)
        self.birthEmpleado.setGeometry(QtCore.QRect(350, 130, 261, 31))
        self.birthEmpleado.setText("")
        self.birthEmpleado.setObjectName("birthEmpleado")
        self.birthEmpleado.setPlaceholderText("Fecha Nacimiento(YYY-MM-DD)")
        self.birthEmpleado.setMaxLength(20)
        self.birthEmpleado.setVisible(True)
        
        self.empCorreo = QtWidgets.QLineEdit(self.widgetLienzo)
        self.empCorreo.setGeometry(QtCore.QRect(660, 130, 261, 31))
        self.empCorreo.setText("")
        self.empCorreo.setObjectName("empCorreo")
        self.empCorreo.setPlaceholderText("Correo")
        self.empCorreo.setMaxLength(60)
        self.empCorreo.setVisible(True)
        
        self.empDireccion = QtWidgets.QLineEdit(self.widgetLienzo)
        self.empDireccion.setGeometry(QtCore.QRect(40, 220, 261, 31))
        self.empDireccion.setText("")
        self.empDireccion.setObjectName("empDireccion")
        self.empDireccion.setPlaceholderText("Dirección")
        self.empDireccion.setMaxLength(60)
        self.empDireccion.setVisible(True)

        self.empTelefono = QtWidgets.QLineEdit(self.widgetLienzo)
        self.empTelefono.setGeometry(QtCore.QRect(350, 220, 261, 31))
        self.empTelefono.setText("")
        self.empTelefono.setObjectName("empTelefono")
        self.empTelefono.setPlaceholderText("Teléfono")
        self.empTelefono.setMaxLength(11)
        self.empTelefono.setVisible(True)

        #cargo
        self.empCargo = QtWidgets.QLineEdit(self.widgetLienzo)
        self.empCargo.setGeometry(QtCore.QRect(660, 220, 261, 31))
        self.empCargo.setText("")
        self.empCargo.setObjectName("empCargo")
        self.empCargo.setPlaceholderText("Cargo")
        self.empCargo.setMaxLength(11)
        self.empCargo.setVisible(True)

        #profesion
        self.empProfesion = QtWidgets.QLineEdit(self.widgetLienzo)
        self.empProfesion.setGeometry(QtCore.QRect(40, 320, 261, 31))
        self.empProfesion.setText("")
        self.empProfesion.setObjectName("empProfesion")
        self.empProfesion.setPlaceholderText("Profesión")
        self.empProfesion.setMaxLength(11)
        self.empProfesion.setVisible(True)

        #s_social
        self.empsSocial = QtWidgets.QLineEdit(self.widgetLienzo)
        self.empsSocial.setGeometry(QtCore.QRect(350, 320, 261, 31))
        self.empsSocial.setText("")
        self.empsSocial.setObjectName("empsSocial")
        self.empsSocial.setPlaceholderText("Seguridad Social")
        self.empsSocial.setMaxLength(11)
        self.empsSocial.setVisible(True)

        self.ingresar = QtWidgets.QPushButton(self.widgetLienzo)
        self.ingresar.setGeometry(QtCore.QRect(660, 320, 230, 41))
        # Establece el texto al QPushButton
        self.ingresar.setText("INGRESAR")
        # creamos una variable local para el objeto QIcon
        self.ingresar.setObjectName("botonLateral_3")
        self.ingresar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.ingresar.setVisible(True)



        
        self.ingresar.clicked.connect(lambda x : self.insert_data(2))

###3
    def mosMaterial(self):
        self.id_material = QtWidgets.QLineEdit(self.widgetLienzo)
        self.id_material.setGeometry(QtCore.QRect(40, 50, 261, 31))
        self.id_material.setText("")
        self.id_material.setObjectName("id_material")
        self.id_material.setPlaceholderText("ID material")
        self.id_material.setMaxLength(20)
        self.id_material.setVisible(True)

        self.matNombre = QtWidgets.QLineEdit(self.widgetLienzo)
        self.matNombre.setGeometry(QtCore.QRect(350, 50, 261, 31))
        self.matNombre.setObjectName("matNombre")
        self.matNombre.setPlaceholderText("Nombre ")
        self.matNombre.setMaxLength(20)
        self.matNombre.setVisible(True)

        self.matPrecio = QtWidgets.QLineEdit(self.widgetLienzo)
        self.matPrecio.setGeometry(QtCore.QRect(660, 50, 261, 31))
        self.matPrecio.setText("")
        self.matPrecio.setObjectName("matPrecio")
        self.matPrecio.setPlaceholderText("Precio")
        self.matPrecio.setMaxLength(20)
        self.matPrecio.setVisible(True)

        self.id_prove = QtWidgets.QLineEdit(self.widgetLienzo)
        self.id_prove.setGeometry(QtCore.QRect(40, 130, 261, 31))
        self.id_prove.setText("")
        self.id_prove.setObjectName("id_prove")
        self.id_prove.setPlaceholderText("ID proveedor")
        self.id_prove.setMaxLength(20)
        self.id_prove.setVisible(True)

        self.ingresar = QtWidgets.QPushButton(self.widgetLienzo)
        self.ingresar.setGeometry(QtCore.QRect(660, 210, 230, 41))
        # Establece el texto al QPushButton
        self.ingresar.setText("INGRESAR")
        # creamos una variable local para el objeto QIcon
        self.ingresar.setObjectName("botonLateral_3")
        self.ingresar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.ingresar.setVisible(True)


         #con el método callproc() se llama al procedimiento almacenado y que se crearon
            # con anterioridad desde la base de datos
        self.ingresar.clicked.connect(lambda x : self.insert_data(3))

###4     


    def mosProducto(self):
        self.prod_tipo = QtWidgets.QLineEdit(self.widgetLienzo)
        self.prod_tipo.setGeometry(QtCore.QRect(40, 50, 261, 31))
        self.prod_tipo.setText("")
        self.prod_tipo.setObjectName("id_prod")
        self.prod_tipo.setPlaceholderText("Tipo")
        self.prod_tipo.setMaxLength(20)
        self.prod_tipo.setVisible(True)

        self.prodMod = QtWidgets.QLineEdit(self.widgetLienzo)
        self.prodMod.setGeometry(QtCore.QRect(350, 50, 261, 31))
        self.prodMod.setText("")
        self.prodMod.setObjectName("prodMod")
        self.prodMod.setPlaceholderText("Modelo")
        self.prodMod.setMaxLength(20)
        self.prodMod.setVisible(True)
        

        self.prodColor = QtWidgets.QLineEdit(self.widgetLienzo)
        self.prodColor.setGeometry(QtCore.QRect(660, 50, 261, 31))
        self.prodColor.setText("")
        self.prodColor.setObjectName("prodColor")
        self.prodColor.setPlaceholderText("Color")
        self.prodColor.setMaxLength(20)
        self.prodColor.setVisible(True)

        self.prodTalla = QtWidgets.QLineEdit(self.widgetLienzo)
        self.prodTalla.setGeometry(QtCore.QRect(40, 130, 261, 31))
        self.prodTalla.setText("")
        self.prodTalla.setObjectName("prodTalla")
        self.prodTalla.setPlaceholderText("Talla")
        self.prodTalla.setMaxLength(20)
        self.prodTalla.setVisible(True)

        self.prodPrecio = QtWidgets.QLineEdit(self.widgetLienzo)
        self.prodPrecio.setGeometry(QtCore.QRect(350, 130, 261, 31))
        self.prodPrecio.setText("")
        self.prodPrecio.setObjectName("prodPrecio")
        self.prodPrecio.setPlaceholderText("Precio")
        self.prodPrecio.setMaxLength(20)
        self.prodPrecio.setVisible(True)

        self.ingresar = QtWidgets.QPushButton(self.widgetLienzo)
        self.ingresar.setGeometry(QtCore.QRect(660, 210, 230, 41))
        # Establece el texto al QPushButton
        self.ingresar.setText("INGRESAR")
        # creamos una variable local para el objeto QIcon
        self.ingresar.setObjectName("botonLateral_3")
        self.ingresar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.ingresar.setVisible(True)
        self.ingresar.clicked.connect(lambda x : self.insert_data(4))


###5    
  


    def mosUbicacion(self):
        self.ubiCiudad = QtWidgets.QLineEdit(self.widgetLienzo)
        self.ubiCiudad.setGeometry(QtCore.QRect(40, 50, 261, 31))
        self.ubiCiudad.setText("")
        self.ubiCiudad.setObjectName("ubiCiudad")
        self.ubiCiudad.setPlaceholderText("Ciudad")
        self.ubiCiudad.setMaxLength(20)
        self.ubiCiudad.setVisible(True)

        self.ubiRegion = QtWidgets.QLineEdit(self.widgetLienzo)
        self.ubiRegion.setGeometry(QtCore.QRect(350, 50, 261, 31))
        self.ubiRegion.setText("")
        self.ubiRegion.setObjectName("ubiRegion")
        self.ubiRegion.setPlaceholderText("Región")
        self.ubiRegion.setMaxLength(20)
        self.ubiRegion.setVisible(True)


        self.ubidi = QtWidgets.QLineEdit(self.widgetLienzo)
        self.ubidi.setGeometry(QtCore.QRect(660, 50, 261, 31))
        self.ubidi.setText("")
        self.ubidi.setObjectName("ubiId")
        self.ubidi.setPlaceholderText("Dirección")
        self.ubidi.setMaxLength(20)
        self.ubidi.setVisible(True)

        self.ubiCPostal = QtWidgets.QLineEdit(self.widgetLienzo)
        self.ubiCPostal.setGeometry(QtCore.QRect(40, 130, 261, 31))
        self.ubiCPostal.setText("")
        self.ubiCPostal.setObjectName("ubiCPostal")
        self.ubiCPostal.setPlaceholderText("Codigo Postal")
        self.ubiCPostal.setMaxLength(20)
        self.ubiCPostal.setVisible(True)

        self.ubiCDocumento = QtWidgets.QLineEdit(self.widgetLienzo)
        self.ubiCDocumento.setGeometry(QtCore.QRect(350, 130, 261, 31))
        self.ubiCDocumento.setText("")
        self.ubiCDocumento.setObjectName("ubiCDocumento")
        self.ubiCDocumento.setPlaceholderText("Documento Cliente")
        self.ubiCDocumento.setMaxLength(20)
        self.ubiCDocumento.setVisible(True)

        self.ingresar = QtWidgets.QPushButton(self.widgetLienzo)
        self.ingresar.setGeometry(QtCore.QRect(660, 210, 230, 41))
        # Establece el texto al QPushButton
        self.ingresar.setText("INGRESAR")
        # creamos una variable local para el objeto QIcon
        self.ingresar.setObjectName("botonLateral_3")
        self.ingresar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.ingresar.setVisible(True)
        self.ingresar.clicked.connect(lambda x : self.insert_data(5))
        

###6

    def mosProveedor(self):

        self.proNombre = QtWidgets.QLineEdit(self.widgetLienzo)
        self.proNombre.setGeometry(QtCore.QRect(40, 50, 261, 31))
        self.proNombre.setText("")
        self.proNombre.setObjectName("proNombre")
        self.proNombre.setPlaceholderText("Nombre Proveedor")
        self.proNombre.setMaxLength(20)
        self.proNombre.setVisible(True)
        

        self.proTelefono = QtWidgets.QLineEdit(self.widgetLienzo)
        self.proTelefono.setGeometry(QtCore.QRect(350, 50, 261, 31))
        self.proTelefono.setText("")
        self.proTelefono.setObjectName("proTelefono")
        self.proTelefono.setPlaceholderText("Teléfono")
        self.proTelefono.setMaxLength(20)
        self.proTelefono.setVisible(True)

        self.proEmpresa = QtWidgets.QLineEdit(self.widgetLienzo)
        self.proEmpresa.setGeometry(QtCore.QRect(660, 50, 261, 31))
        self.proEmpresa.setText("")
        self.proEmpresa.setObjectName("proEmpresa")
        self.proEmpresa.setPlaceholderText("Empresa")
        self.proEmpresa.setMaxLength(20)
        self.proEmpresa.setVisible(True)


        self.ingresar = QtWidgets.QPushButton(self.widgetLienzo)
        self.ingresar.setGeometry(QtCore.QRect(660, 210, 230, 41))
        # Establece el texto al QPushButton
        self.ingresar.setText("INGRESAR")
        # creamos una variable local para el objeto QIcon
        self.ingresar.setObjectName("botonLateral_3")
        self.ingresar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.ingresar.setVisible(True)
        self.ingresar.clicked.connect(lambda x : self.insert_data(6))

#7
    def mosco_material(self):
        self.comFecha = QtWidgets.QLineEdit(self.widgetLienzo)
        self.comFecha.setGeometry(QtCore.QRect(40, 50, 261, 31))
        self.comFecha.setText("")
        self.comFecha.setObjectName("comFecha")
        self.comFecha.setPlaceholderText("Fecha")
        self.comFecha.setMaxLength(25)
        self.comFecha.setVisible(True)

        self.comEmp = QtWidgets.QComboBox(self.widgetLienzo)
        self.comEmp.setGeometry(QtCore.QRect(350, 50, 261, 31))
        #self.factEmp.setText("")
        self.comEmp.setObjectName("comEmp")
        self.comEmp.setPlaceholderText("Documento Empleado")
        self.comEmp.setVisible(True)
        q = 'select documento_empleado from empleado;'
        self.cursor.execute(q)
        l = self.cursor.fetchall()
        for e in range (len(l)):
            self.comEmp.addItem(str(l[e][0]))

        self.factidPro = QtWidgets.QComboBox(self.widgetLienzo)
        self.factidPro.setGeometry(QtCore.QRect(660, 50, 261, 31))
        #self.factEmp.setText("")
        self.factidPro.setObjectName("factEmp")
        self.factidPro.setPlaceholderText("ID Proveedor")
        self.factidPro.setVisible(True)
        q = 'select id_proveedor from proveedor;'
        self.cursor.execute(q)
        l = self.cursor.fetchall()
        for e in range (len(l)):
            self.factidPro.addItem(str(l[e][0]))


        self.comidMat = QtWidgets.QLineEdit(self.widgetLienzo)
        self.comidMat.setGeometry(QtCore.QRect(40, 150, 261, 31))
        self.comidMat.setText("")
        self.comidMat.setObjectName("comidMat")
        self.comidMat.setPlaceholderText("ID material")
        self.comidMat.setMaxLength(25)
        self.comidMat.setVisible(True)

        self.comcanMat = QtWidgets.QLineEdit(self.widgetLienzo)
        self.comcanMat.setGeometry(QtCore.QRect(350, 150, 261, 31))
        self.comcanMat.setText("")
        self.comcanMat.setObjectName("comcanMat")
        self.comcanMat.setPlaceholderText("Cantidad")
        self.comcanMat.setMaxLength(25)
        self.comcanMat.setVisible(True)


        self.ingresar = QtWidgets.QPushButton(self.widgetLienzo)
        self.ingresar.setGeometry(QtCore.QRect(660, 210, 230, 41))
        # Establece el texto al QPushButton
        self.ingresar.setText("GENERAR COMPRA")
        # creamos una variable local para el objeto QIcon
        self.ingresar.setObjectName("botonLateral_3")
        self.ingresar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.ingresar.setVisible(True)
        self.ingresar.clicked.connect(lambda x : self.insert_data(7))
    
    
  #8  
    def mosf_venta(self):
        self.factFecha = QtWidgets.QLineEdit(self.widgetLienzo)
        self.factFecha.setGeometry(QtCore.QRect(40, 50, 261, 31))
        self.factFecha.setText("")
        self.factFecha.setObjectName("factFecha")
        self.factFecha.setPlaceholderText("Fecha")
        self.factFecha.setMaxLength(25)
        self.factFecha.setVisible(True)
        
        self.factEmp = QtWidgets.QComboBox(self.widgetLienzo)
        self.factEmp.setGeometry(QtCore.QRect(350, 50, 261, 31))
        #self.factEmp.setText("")
        self.factEmp.setObjectName("factEmp")
        self.factEmp.setPlaceholderText("Documento Empleado")
        self.factEmp.setVisible(True)
        q = 'select documento_empleado from empleado;'
        self.cursor.execute(q)
        l = self.cursor.fetchall()
        for e in range (len(l)):
            self.factEmp.addItem(str(l[e][0]))


        self.factCli = QtWidgets.QComboBox(self.widgetLienzo)
        self.factCli.setGeometry(QtCore.QRect(660, 50, 261, 31))
        #self.factEmp.setText("")
        self.factCli.setObjectName("factEmp")
        self.factCli.setPlaceholderText("Documento Cliente")
        self.factCli.setVisible(True)
        q = 'select cliente_documento from cliente;'
        self.cursor.execute(q)
        l = self.cursor.fetchall()
        for e in range (len(l)):
            self.factCli.addItem(str(l[e][0]))



        self.prod1id = QtWidgets.QLineEdit(self.widgetLienzo)
        self.prod1id.setGeometry(QtCore.QRect(40, 130, 261, 31))
        self.prod1id.setText("")
        self.prod1id.setObjectName("prod1")
        self.prod1id.setPlaceholderText("producto id")
        self.prod1id.setMaxLength(25)
        self.prod1id.setVisible(True)

        self.prod1nom = QtWidgets.QLineEdit(self.widgetLienzo)
        self.prod1nom.setGeometry(QtCore.QRect(350, 130, 261, 31))
        self.prod1nom.setText("")
        self.prod1nom.setObjectName("prod1nom")
        self.prod1nom.setPlaceholderText("producto nombre")
        self.prod1nom.setMaxLength(25)
        self.prod1nom.setVisible(True)

        self.prod1can = QtWidgets.QLineEdit(self.widgetLienzo)
        self.prod1can.setGeometry(QtCore.QRect(660, 130, 261, 31))
        self.prod1can.setText("")
        self.prod1can.setObjectName("prod1can")
        self.prod1can.setPlaceholderText("producto cantidad")
        self.prod1can.setMaxLength(25)
        self.prod1can.setVisible(True)

        ##prod 2
        self.prod2id = QtWidgets.QLineEdit(self.widgetLienzo)
        self.prod2id.setGeometry(QtCore.QRect(40, 190, 261, 31))
        self.prod2id.setText("")
        self.prod2id.setObjectName("prod2id")
        self.prod2id.setPlaceholderText("producto id")
        self.prod2id.setMaxLength(25)
        self.prod2id.setVisible(True)

        self.prod2nom = QtWidgets.QLineEdit(self.widgetLienzo)
        self.prod2nom.setGeometry(QtCore.QRect(350, 190, 261, 31))
        self.prod2nom.setText("")
        self.prod2nom.setObjectName("prod2nom")
        self.prod2nom.setPlaceholderText("producto nombre")
        self.prod2nom.setMaxLength(25)
        self.prod2nom.setVisible(True)

        self.prod2can = QtWidgets.QLineEdit(self.widgetLienzo)
        self.prod2can.setGeometry(QtCore.QRect(660, 190, 261, 31))
        self.prod2can.setText("")
        self.prod2can.setObjectName("prod2can")
        self.prod2can.setPlaceholderText("producto cantidad")
        self.prod2can.setMaxLength(25)
        self.prod2can.setVisible(True)

        self.ingresar = QtWidgets.QPushButton(self.widgetLienzo)
        self.ingresar.setGeometry(QtCore.QRect(660, 250, 230, 41))
        # Establece el texto al QPushButton
        self.ingresar.setText("GENERAR FACTURA")
        # creamos una variable local para el objeto QIcon
        self.ingresar.setObjectName("botonLateral_3")
        self.ingresar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Establecer visibilidad del Boton
        self.ingresar.setVisible(True)

        self.ingresar.clicked.connect(lambda x : self.insert_data(8))



    #funcion que inserta los datos que se hayan escrito, de acuerdo desde donde se haya llamado.

    def insert_data(self,n):
        self.cursor = self.conn.cursor()
        if n==0:
            valores = (self.camMotivo.currentText(), 
                        self.camFecha.text(),
                        int(self.id_factura_v.text()))
            print(valores)                           
            self.cursor.callproc('Insertar_Cambio',valores)   
        
        if n==1:
            valores = (int(self.cliDocumento.text()),
                            self.tipo_doc.currentText(), 
                             self.nomCliente.text(),
                           self.apeCliente.text(),
                            int(self.cliTelefono.text()),
                            self.cliCorreo.text())
            print(valores)  
             #con el método callproc() se llama al procedimiento almacenado y que se crearon
            # con anterioridad desde la base de datos                         
            self.cursor.callproc('Insertar_Cliente',valores) 


        if n==2:
            valores = (int(self.docEmpleado.text()),
            self.tipo_doc.currentText(),self.nomEmpleado.text(),
            self.apeEmpleado.text(),self.birthEmpleado.text(),self.empCorreo.text(),
            self.empDireccion.text(), int(self.empTelefono.text()),self.empCargo.text(),
            self.empProfesion.text(),self.empsSocial.text()
            )
            print(valores)                           
            self.cursor.callproc('Insertar_Empleado',valores)  


        if n==3:
            valores = ( self.matNombre.text(),
            int(self.matPrecio.text()),
            int(self.id_prove.text())
                            )
            print(valores)                           
            self.cursor.callproc('Insertar_Material',valores)  

        if n==4:
            valores = (self.prod_tipo.text(),self.prodMod.text(),
            self.prodColor.text(),int(self.prodTalla.text()),
            int(self.prodPrecio.text())
            )
            print(valores)                           
            self.cursor.callproc('Insertar_Producto',valores)  

        if n==5:
            valores = (self.ubiCiudad.text(),
            self.ubiRegion.text(),
            self.ubidi.text(),
            int(self.ubiCPostal.text()),
            int(self.ubiCDocumento.text())
            ) 
            print(valores)                           
            self.cursor.callproc('Insertar_Ubicacion',valores)   

        if n==6:
            valores = (self.proNombre.text(),
                int(self.proTelefono.text()),
                self.proEmpresa.text()
                )  

             #con el método callproc() se llama al procedimiento almacenado y que se crearon
            # con anterioridad desde la base de datos
            self.cursor.callproc('Insertar_Proveedor',valores)

        #compra material
        if n==7:
            q1 = 'select mat_precio from material where id_material=%d' % int(self.comidMat.text())
            self.cursor.execute(q1)

            total =int(self.comcanMat.text())*int(self.cursor.fetchall()[0][0])
            q = 'select max(ID_compra_material) from compra_material;'
            self.cursor.execute(q)

            self.ids = int(self.cursor.fetchall()[0][0])+1
            valoresinfo = (self.ids, 
                        int(self.comidMat.text()),
                        int(self.comcanMat.text())
            )

            valores= (
                self.comFecha.text(),
                total,
                int(self.comEmp.currentText()),
                int(self.factidPro.currentText())
            )
             #con el método callproc() se llama al procedimiento almacenado y que se crearon
            # con anterioridad desde la base de datos
            self.cursor.callproc('Insertar_Compra_M',valores)
            self.cursor.callproc('Insertar_Info_Compra',valoresinfo)

        ##fact_venta (8)
        if n==8:
            total =0
            q = 'select count(*) from factura_venta;'
            self.cursor.execute(q)
            self.ids = int(self.cursor.fetchall()[0][0])+1

            valoresinfo1 =(self.ids,
                        int(self.prod1id.text()),
                        self.prod1nom.text(),
                        int(self.prod1can.text())
            )
            valoresinfo2 =(self.ids,
                            int(self.prod2id.text()),
                            self.prod2nom.text(),
                            int(self.prod2can.text())
            )
            q1 = 'select producto_precio from producto where id_producto=%d' %int(self.prod1id.text())
            self.cursor.execute(q1)
            total+= self.cursor.fetchall()[0][0]*int(self.prod1can.text())
            q2 = 'select producto_precio from producto where id_producto=%d' %int(self.prod2id.text())
            self.cursor.execute(q2)
            total+= self.cursor.fetchall()[0][0]*int(self.prod2can.text())

            valores = (self.factFecha.text(),total,
                    int(self.factEmp.currentText()),
                    int(self.factCli.currentText())
            )
            print(valores)
            print(valoresinfo1)
            print(valoresinfo2)
            #con el método callproc() se llama al procedimiento almacenado y que se crearon
            # con anterioridad desde la base de datos
            self.cursor.callproc('Insertar_Factura',valores)
            self.cursor.callproc('Insertar_Info_Fact',valoresinfo1)
            self.cursor.callproc('Insertar_Info_Fact',valoresinfo2)




            



        


        

        
        

        
## ponerle el estilo y colores a la ventana
stylesheet  = """
#widgetLienzo{
background-color : #598567;
}

 """



def window():
    app =  QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    win = ventana_ingresar('jmanosalva')
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()


