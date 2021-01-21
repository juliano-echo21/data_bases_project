-- OTROS PROCEDIMIENTOS
use acida;


-- ADMINISTRADORA

-- DROP PROCEDURE Mas_vendidos;
DELIMITER $$
CREATE PROCEDURE Mas_vendidos ()
BEGIN
DECLARE error INTEGER DEFAULT 0;
 BEGIN
      SET error=1;
END;
    SELECT Producto_Nombre FROM factura_venta JOIN info_factura_venta 
    USING (ID_Factura_Venta) WHERE Fact_Fecha>'2020-04-01' group by ID_Producto
	order by sum(Producto_Cantidad) desc limit 5;

IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;


-- La cantidad total de ventas y productos desde el mes de marzo 
-- (Con botón y campo para ingresar el dato)
-- DROP PROCEDURE Ventas_Desde_Mes;
DELIMITER $$
CREATE PROCEDURE Ventas_Desde_Mes (IN Fecha DATE)
BEGIN
DECLARE error INTEGER DEFAULT 0;
 BEGIN
      SET error=1;
END;
    SELECT sum(Fact_Pago_Total) as TotalVentas, sum(Producto_Cantidad) as CantidadProductos 
    FROM factura_venta join info_factura_venta using (id_factura_venta) WHERE Fact_Fecha > Fecha;
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;


-- Nombre, apellido que más ventas realizó en un lapso de tiempo.
-- (Requiere botón y dos campos para las dos fechas)
-- DROP PROCEDURE Empleado_Ventas ;
DELIMITER $$
CREATE PROCEDURE Empleado_Ventas (IN Fecha_inicio DATE, IN Fecha_fin DATE)
BEGIN
DECLARE error INTEGER DEFAULT 0;
 BEGIN
      SET error=1;
END;
    SELECT empleado.Emp_Nombre, empleado.Emp_Apellido from empleado INNER JOIN factura_venta 
    ON empleado.Documento_Empleado= factura_venta.Documento_Empleado INNER JOIN info_factura_venta 
    ON factura_venta.ID_Factura_Venta=info_factura_venta.ID_Factura_Venta 
    WHERE Fact_Fecha>= Fecha_inicio  and Fact_Fecha <= Fecha_fin 
    group by empleado.Documento_Empleado, empleado.Emp_Nombre 
    ORDER BY sum(info_factura_venta.Producto_Cantidad) desc limit 1;
IF error=0 OR Fecha_inicio > Fecha_fin
THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER 



-- Número total de sandalias y zapatillas vendidas y promedio de ganancias recibidas por la venta 
-- de estos en una ciudad
-- (Con botón y campo para ingresar el dato de la ciudad)
-- DROP PROCEDURE Total_En_Ciudad;
DELIMITER $$
CREATE PROCEDURE Total_En_Ciudad (IN ciudad VARCHAR(45))
BEGIN
DECLARE error INTEGER DEFAULT 0;
 BEGIN
      SET error=1;
END;
    SELECT producto_tipo, sum(producto_cantidad) as CantidadTotal, AVG (Fact_pago_total) AS PromedioGanancia 
FROM (SELECT producto_tipo, fact_pago_total, producto_cantidad FROM ubicacion  join 
(SELECT Producto_Tipo, Fact_Pago_Total, Cliente_Documento, producto_cantidad FROM producto 
INNER join (SELECT ID_Producto, Fact_Pago_Total, Cliente_Documento, Producto_Cantidad FROM info_factura_venta 
JOIN factura_venta USING (ID_Factura_Venta)) AS ProductosVendidos on producto.ID_Producto=ProductosVendidos.ID_Producto) 
AS tipoZapatoVendido using (Cliente_Documento) WHERE Ubi_Ciudad LIKE ciudad) 
as VentasFinales GROUP by producto_tipo order by sum(producto_cantidad) and AVG (Fact_pago_total) desc;
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;


-- VENDEDOR
-- Nombre, dirección de los clientes y tipo de zapato por el que solicitaron un cambio.
-- (Requiere botón pero no requiere campo para ingresar el parámetro)
-- DROP PROCEDURE Detalles_cambio;
DELIMITER $$
CREATE PROCEDURE Detalles_cambio ()
BEGIN
DECLARE error INTEGER DEFAULT 0;
 BEGIN
      SET error=1;
END;
    SELECT Cliente_Nombre, Cliente_Apellido, Ubi_Ciudad, Producto_Tipo, Producto_Modelo from info_cambio 
    JOIN cambio using (id_cambio) JOIN producto using (id_producto) JOIN factura_venta
    using (id_factura_venta) JOIN cliente using (cliente_documento) join ubicacion using (cliente_documento);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;



-- Fecha de pedido, fecha de facturación y nombre del producto de pedidos superiores a una cantidad dada
-- (Con botón y campo para ingresar el dato)
-- DROP PROCEDURE Pedidos_Con_Cantidad;
DELIMITER $$
CREATE PROCEDURE Pedidos_Con_Cantidad (IN Cantidad INT)
BEGIN
DECLARE error INTEGER DEFAULT 0;
 BEGIN
      SET error=1;
END;
    SELECT Pedido_Fecha, Fact_Fecha, Producto_Nombre from info_factura_venta
	inner join pedido_fabricacion on info_factura_venta.ID_Factura_Venta=pedido_fabricacion.ID_Factura_Venta 
	join factura_venta where factura_venta.ID_Factura_Venta= info_factura_venta.ID_Factura_Venta and Fact_Pago_Total>Cantidad;

IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;



-- Nombre y ciudad de los clientes que solicitaron un cambio además de los días que transcurrieron 
-- entre la fecha de facturación y la fecha en la que se realizó el cambio
-- (Requiere botón pero no requiere campo para ingresar el parámetro)
-- DROP PROCEDURE Clientes_Cambio;
DELIMITER $$
CREATE PROCEDURE Clientes_Cambio ()
BEGIN
DECLARE error INTEGER DEFAULT 0;
 BEGIN
      SET error=1;
END;
    SELECT Cliente_Nombre, Cliente_Apellido, Ubi_Ciudad, Cam_Fecha-Fact_Fecha as DiasTranscurridos 
    FROM factura_venta, cambio, cliente, ubicacion where factura_venta.ID_Factura_Venta=cambio.ID_Factura_Venta 
    and factura_venta.Cliente_Documento=cliente.Cliente_Documento 
    and ubicacion.Cliente_Documento=cliente.Cliente_Documento;

IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;


-- Ganancias recibidas por la venta de una producto ingresado
-- (Requiere botón pero no requiere campo para ingresar el parámetro)
-- DROP PROCEDURE Ganancias_Producto;
DELIMITER $$
CREATE PROCEDURE Ganancias_Producto (IN Nombre_Producto VARCHAR(45))
BEGIN
DECLARE error INTEGER DEFAULT 0;
 BEGIN
      SET error=1;
END;
    Select Producto_Nombre, sum(Fact_Pago_Total) as GananciaTotal from factura_venta join info_factura_venta 
    where factura_venta.ID_Factura_Venta=info_factura_venta.ID_Factura_Venta and info_factura_venta.Producto_Nombre 
    IN (SELECT Producto_Nombre from info_factura_venta where Producto_Nombre = Nombre_Producto) 
    group by Producto_Nombre ORDER BY sum(Fact_Pago_Total) desc; 
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;



show triggers;

-- TRIGGER BORRADO DE CLIENTE EN CASCADA
DROP TABLE IF EXISTS Historia_Delete_Cliente;
CREATE TABLE Historia_Delete_Cliente (
	Fecha DATE,
    Doc_Cliente INT,
    Accion VARCHAR(45)
);

DROP TRIGGER IF EXISTS Delete_Ubicacion;
DELIMITER |
CREATE TRIGGER Delete_Ubicacion BEFORE DELETE ON Ubicacion
	FOR EACH ROW BEGIN
	INSERT INTO Historia_Delete_Cliente(Fecha, Doc_Cliente, Accion)
    VALUES (CURDATE(), OLD.Cliente_documento,'Borrado cliente');
END;
|
DELIMITER ;

DROP TRIGGER IF EXISTS Delete_Factura;
DELIMITER |
CREATE TRIGGER Delete_Factura BEFORE DELETE ON Factura_Venta
	FOR EACH ROW BEGIN
	DELETE FROM Ubicacion WHERE ubicacion.Cliente_Documento = OLD.Cliente_Documento;
    DELETE FROM pedido_fabricacion WHERE pedido_fabricacion.ID_Factura_Venta= OLD.ID_Factura_Venta;
END;
|
DELIMITER ;

DROP TRIGGER IF EXISTS Delete_Cliente;
DELIMITER |
CREATE TRIGGER Delete_Cliente BEFORE DELETE ON Cliente
	FOR EACH ROW BEGIN
    DELETE FROM Factura_Venta WHERE Factura_Venta.Cliente_Documento = OLD.Cliente_Documento;
END;
|
DELIMITER ;

DROP TRIGGER IF EXISTS Delete_info_factura;
DELIMITER |
CREATE TRIGGER Delete_info_factura BEFORE DELETE ON Factura_Venta
	FOR EACH ROW BEGIN
    DELETE FROM info_Factura_Venta WHERE info_Factura_Venta.ID_Factura_Venta = OLD.ID_Factura_Venta;
END;
|
DELIMITER ;



DROP TRIGGER IF EXISTS Delete_evento_fa;
DELIMITER |
CREATE TRIGGER Delete_evento_fa BEFORE DELETE ON pedido_fabricacion
	FOR EACH ROW BEGIN
    DELETE FROM evento_fabricacion WHERE evento_fabricacion.ID_Pedido = OLD.ID_Pedido;
END;
|
DELIMITER ;




-- ESTOS TRIGGERS QUE VAN ACA ABAJO SON LOS QUE SE CREARON PARA LA TERCERA ENTEGA (NO ESTAN TODOS)


-- 1 CADA VEZ QUE SE REALICE UNA COMPRA, DENTRO DE UNA NUEVA TABLA VENTA_VENDEDOR
-- SE LLEVARA UN REGISTRO DEL NUMERO DE VENTAS QUE HACE UN VENDEDOR Y EL MONTO TOTAL
-- ACUMULADO QUE HA VENDIDO
DROP TABLE IF EXISTS venta_vendedor;
CREATE TABLE venta_vendedor(
documento_empleado int,
numero_ventas int default 0,
total_vendido int
);

DROP TRIGGER IF EXISTS tr_venta_vendedor;
DELIMITER $$
CREATE TRIGGER tr_venta_vendedor before insert on factura_venta
for each row
begin
declare ve int;

if new.Documento_Empleado in (select documento_empleado from venta_vendedor) then 
update  venta_vendedor set numero_ventas = numero_ventas+1 
	where documento_empleado = new.Documento_Empleado;
update venta_vendedor set total_vendido =total_vendido +  new.Fact_Pago_Total
	where documento_empleado = new.Documento_Empleado;

else
	insert into venta_vendedor values(new.Documento_Empleado,1,new.Fact_Pago_Total);
end if;
end $$
DELIMITER ;


-- 2. DESPUES DE CAMBIARLE EL PRECIO A UN PRODUCTO SE VA INGRESAR EN LA TABLA acciones_vendedores
-- EL DOCUMENTO DEL EMPLEADO, LA FECHA DE ACTUALIZACION, TAMBIEN SE GUARDARÁ EL NUMERO DE CAMBIOS 
-- QUE A LA FECHA HA HECHO ESE VENDEDOR
DROP TABLE IF EXISTS acciones_vendedores;
CREATE TABLE acciones_vendedores(
usuario varchar(40),
fecha_act date,
numero_cambios int
);

DROP TRIGGER IF EXISTS tr_acciones_vendedores;
DELIMITER $$
CREATE TRIGGER tr_acciones_vendedores BEFORE UPDATE ON producto
FOR EACH ROW BEGIN 
declare nu int;

IF CURRENT_USER() IN (select usuario from acciones_vendedores) THEN
select max(numero_cambios) INTO nu from acciones_vendedores 
	where usuario = CURRENT_USER();
INSERT INTO acciones_vendedores VALUES (CURRENT_USER(),CURDATE(),nu+1);

ELSE 
INSERT INTO acciones_vendedores VALUES (CURRENT_USER(),CURDATE(),1);
END IF;

END $$
DELIMITER ;


--  CADA VEZ QUE LLEGUE UN PEDIDO DE MATERIAL, EN UNA NUEVA TABLA historial_material
-- SE  REGISTRARÁ EN UNA NUEVA TABLA EL NUMERO DE VECES QUE A UN  PROVEEDOR SE LE 
-- HA COMPRADO MATERIAL Y EL TOTAL QUE ES LE HA COMPRADO A LO LARGO DEL TIEMPO
-- 
DROP TABLE IF EXISTS historial_compra_material;
CREATE TABLE historial_compra_material(
id_proveedor int,
numero_pedidos int,
cantidad_total int
);

DROP TRIGGER IF EXISTS tr_historial_compra_material;
DELIMITER $$
CREATE TRIGGER tr_historial_compra_material BEFORE INSERT ON compra_material
FOR EACH ROW BEGIN
if new.ID_Proveedor in (select id_proveedor from historial_compra_material) THEN
UPDATE historial_compra_material SET numero_pedidos = numero_pedidos+1
	where id_proveedor = new.ID_Proveedor;
UPDATE historial_compra_material SET cantidad_total = cantidad_total + new.CompraM_Pago_Total
	where id_proveedor = new.ID_Proveedor;

else 
insert into historial_compra_material values (new.ID_Proveedor,1,new.CompraM_Pago_Total);
end if;  

end $$
DELIMITER ; 


-- . CADA VEZ QUE SE REGISTRE UNA NUEVA COMPRA DE MATERIAL EN LA TABLA compra_material_empleado
-- se va a insertar el documento del empleado, la fecha de facturacion, y a qué proveedor le 
-- recibió el pedido
DROP TABLE IF EXISTS compra_material_empleado;
CREATE TABLE compra_material_empleado(
documento_empleado int,
fecha_facturacion int,
id_proveedor int
);

DROP TRIGGER IF EXISTS tr_compra_material_empleado;
DELIMITER $$
CREATE TRIGGER tr_compra_material_empleado BEFORE INSERT ON compra_material
FOR EACH ROW BEGIN
INSERT INTO compra_material_empleado 
		values(new.documento_empleado,curdate(),new.id_proveedor);
end $$        
DELIMITER ; 



