CREATE ROLE IF NOT EXISTS 'Administradora', 'Vendedor', 'Supervisor de fabrica';


-- Administradora
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.cambio TO 'Administradora';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.cliente TO 'Administradora';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.compra_material TO 'Administradora';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.empleado TO 'Administradora';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.evento_fabricacion TO 'Administradora';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.factura_venta TO 'Administradora';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.info_cambio TO 'Administradora';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.info_compra_material TO 'Administradora';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.info_factura_venta TO 'Administradora';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.material TO 'Administradora';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.pedido_fabricacion TO 'Administradora';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.producto TO 'Administradora';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.proveedor TO 'Administradora';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.ubicacion TO 'Administradora';




-- Vendedor
GRANT INSERT, SELECT ON ACIDA.Cambio TO 'Vendedor';
GRANT INSERT, SELECT ON ACIDA.Info_Cambio TO 'Vendedor';
GRANT INSERT, SELECT ON ACIDA.Cliente TO 'Vendedor';
GRANT INSERT, SELECT ON ACIDA.Factura_Venta TO 'Vendedor';
GRANT INSERT, SELECT ON ACIDA.Info_Factura_Venta TO 'Vendedor';
GRANT INSERT, SELECT, UPDATE ON ACIDA.Producto TO 'Vendedor';
GRANT INSERT, SELECT ON ACIDA.Ubicacion TO 'Vendedor';
GRANT INSERT, SELECT ON ACIDA.Pedido_Fabricacion TO 'Vendedor';
grant select on ACIDA.empleado TO 'Vendedor';
grant select on ACIDA.venta_vendedor TO 'Vendedor';

-- Supervisor de fábrica
GRANT SELECT ON ACIDA.cliente TO 'Supervisor de fabrica';
GRANT INSERT, SELECT ON ACIDA.Compra_Material TO 'Supervisor de fabrica';
GRANT INSERT, SELECT ON ACIDA.Evento_Fabricacion TO 'Supervisor de fabrica';
GRANT INSERT, SELECT ON ACIDA.Compra_Material TO 'Supervisor de fabrica';
GRANT INSERT, SELECT ON ACIDA.Info_Compra_Material TO 'Supervisor de fabrica';
GRANT INSERT, SELECT, UPDATE ON ACIDA.Material TO 'Supervisor de fabrica';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.empleado TO 'Supervisor de fabrica';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.proveedor TO 'Supervisor de fabrica';
GRANT INSERT, SELECT, UPDATE, DELETE ON ACIDA.factura_venta TO 'Supervisor de fabrica';
GRANT SELECT ON ACIDA.producto TO 'Supervisor de fabrica';
GRANT INSERT, SELECT,UPDATE ON ACIDA.info_factura_venta TO 'Supervisor de fabrica';



-- Usuarios
DROP USER IF EXISTS 'mpcalderon'@'localhost';
DROP USER IF EXISTS 'jmanosalva'@'localhost';
DROP USER IF EXISTS 'jrincon'@'localhost';
CREATE USER 'mpcalderon'@'localhost' IDENTIFIED BY '12345678';
CREATE USER 'jmanosalva'@'localhost' IDENTIFIED BY '7654321';
CREATE USER 'jrincon'@'localhost' IDENTIFIED BY '3333333';



-- Permisos
GRANT 'Administradora' TO 'mpcalderon'@'localhost';
GRANT 'Vendedor' TO 'jmanosalva'@'localhost';
GRANT 'Supervisor de fabrica' TO 'jrincon'@'localhost';

SET DEFAULT ROLE 'Administradora' TO 'mpcalderon'@'localhost';
SET DEFAULT ROLE 'Vendedor' TO 'jmanosalva'@'localhost';
SET DEFAULT ROLE 'Supervisor de fabrica' TO 'jrincon'@'localhost';

-- Permisos funciones 

GRANT EXECUTE ON FUNCTION ACIDA.f_producto_mas_vendido TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON FUNCTION ACIDA.f_producto_mas_cambiado TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON FUNCTION ACIDA.f_promedio_ganancias TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON FUNCTION ACIDA.f_empleado_ventas TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON FUNCTION ACIDA.f_color_menos_vendido TO 'mpcalderon'@'localhost';


-- Permisos procedimientos almacenados

-- Administradora
GRANT EXECUTE ON PROCEDURE ACIDA.Promocion TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Descuento_Heparl TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Aumento_Productos TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Empleado TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Cliente TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Cambio TO 'mpcalderon'@'localhost'; 
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Info_Cambio TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Factura TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Info_Fact TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Producto TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Ubicacion TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_E_Fab TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Pedido TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Proveedor TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Material TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Compra_M TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Info_Compra TO 'mpcalderon'@'localhost';
GRANT EXECUTE ON ACIDA.* TO 'mpcalderon'@'localhost';

-- Vendedor
GRANT EXECUTE ON PROCEDURE ACIDA.Intervalo_ventas TO 'jmanosalva'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Descuento_region TO 'jmanosalva'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Aumento_Por_Cambio TO 'jmanosalva'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Cliente TO 'jmanosalva'@'localhost'; 
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Cambio TO 'jmanosalva'@'localhost'; 
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Info_Cambio TO 'jmanosalva'@'localhost'; 
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Factura TO 'jmanosalva'@'localhost'; 
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Info_Fact TO 'jmanosalva'@'localhost'; 
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Producto TO 'jmanosalva'@'localhost'; 
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Ubicacion TO 'jmanosalva'@'localhost'; 
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_E_Fab TO 'jmanosalva'@'localhost'; 
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Pedido TO 'jmanosalva'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Pedido TO 'jmanosalva'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Clientes_Cambio TO 'jmanosalva'@'localhost'; 
GRANT EXECUTE ON PROCEDURE ACIDA.Ganancias_Producto TO 'jmanosalva'@'localhost'; 
GRANT EXECUTE ON PROCEDURE ACIDA.Pedidos_Con_Cantidad TO 'jmanosalva'@'localhost'; 


-- Supervisor de fábrica
GRANT EXECUTE ON PROCEDURE ACIDA.Aumento_CompraM_Fechas TO 'jrincon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Aumento_Compra_Prov TO 'jrincon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Eliminar_evento TO 'jrincon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Proveedor TO 'jrincon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Material TO 'jrincon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Compra_M TO 'jrincon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Info_Compra TO 'jrincon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Empleado TO 'jrincon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Factura TO 'jrincon'@'localhost';
GRANT EXECUTE ON PROCEDURE ACIDA.Insertar_Info_Fact TO 'jrincon'@'localhost';





