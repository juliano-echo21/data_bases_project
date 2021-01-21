use acida;  
-- TRRIGGERS PARA ADMIN
-- 1 SE CREA UNA TABLA HISTORIAL CAMBIOS QUE VA GUARDAR EL NUMERO DE VECES QUE UN 
-- PRODUCTO DE HA CAMBIADO, CADA VEZ QUE SE INSERTE EN LA TABLA INFO_CAMBIO, SE ACTUALIZA ESTA TABLA
drop table if exists historial_cambio;
create table historial_cambio(
id_producto int,
numero_cambios int
);
drop trigger if exists tr_historial_cambio;

DELIMITER $$
CREATE TRIGGER tr_historial_cambio BEFORE INSERT 
	ON info_cambio
FOR EACH ROW 
BEGIN 
declare co int;
select count(*) into co from historial_cambio 
	where id_producto = new.ID_producto;

if co = 0 
then
	INSERT INTO historial_cambio 
		values(new.ID_producto,1,new.producto_cantidad);
ELSE 
	update historial_cambio set numero_cambios = numero_cambios+1 
		where id_producto = ID_producto;
END IF;        
END $$
DELIMITER ;   

-- 2. ANTES DE QUE SE QUIERA BORRAR UNA UBICACION Y EL CLIENTE ASOCIADO NO TENGA OTRA DIRECCION
--  SE LANZARÁ UN MENSAJE QUE DIGA QUE NO HAY UNA DIRECCION DE RESPALDO PARA ESE CLIENTE
drop trigger if exists tr_mns_ubicacion;
DELIMITER $$
CREATE TRIGGER tr_mns_ubicacion BEFORE DELETE ON UBICACION
FOR EACH ROW BEGIN
declare co int;
DECLARE war VARCHAR(255);
select count(*) into co from ubicacion where Cliente_Documento = old.Cliente_Documento ;

if co = 1 then
SET war = CONCAT('EL CLIENTE CON CEDULA: ', OLD.Cliente_Documento,'NO TIENE UBICACION DE RESPALDO');
SIGNAL SQLSTATE '45000' SET message_text = war;
end if;
END $$
DELIMITER ; 

-- 3. CADA 100 FACTURAS DE VENTA SE ENVIARÁ UN MENSAJE QUE ESE CLIENTE TIENE UN DESCUENTO DEL 10%
-- EN SU FACTURA ADICIONALMENTE SE GUARDARÁ LA FECHA, EL CLIENTE Y EL PRECIO A PAGAR
--  DENTRO DE UNA TABLA HISTORIAL_DESCUENTOS
drop table if exists historial_descuento;

CREATE TABLE historial_descuento(
id_fact int,
fecha date,
documento int,
precio_total int
);

drop trigger if exists tr_descuento;
DELIMITER $$
CREATE TRIGGER tr_descuento AFTER INSERT ON factura_venta
FOR EACH ROW BEGIN 
DECLARE war VARCHAR(255);
DECLARE des int;

if new.ID_Factura_Venta%100 = 0 then
SET war = CONCAT('EL CLIENTE CON CEDULA: ', NEW.Cliente_Documento,'DEBE TENER UN DESCUENTO EN SU COMPRA');
SIGNAL SQLSTATE '45000' SET message_text = war;
set des = new.Fact_Pago_Total * 0.9;
INSERT INTO historial_descuento VALUES(new.ID_Factura_Venta,CURDATE(),NEW.Cliente_Documento,des);
end if;

end $$
delimiter ; 


-- ESTE TRIGGER REALIZA EL DESCUENTO SOBRE LA FACTURA
drop trigger if exists aux_factura;
DELIMITER $$
CREATE TRIGGER aux_factura before insert on historial_descuento
FOR EACH ROW BEGIN
UPDATE factura_venta set Fact_Pago_Total = Fact_Pago_Total* 0.9 
	where ID_Factura_Venta = new.id_fact;

END $$
DELIMITER ; 


    
-- TRIGGERS PARA VENDEDOR

-- 1 CADA VEZ QUE SE REALICE UNA COMPRA, DENTRO DE UNA NUEVA TABLA VENTA_VENDEDOR
-- SE LLEVARA UN REGISTRO DEL NUMERO DE VENTAS QUE HACE UN VENDEDOR Y EL MONTO TOTAL
-- ACUMULADO QUE HA VENDIDO
drop table if exists venta_vendedor;

CREATE TABLE venta_vendedor(
documento_empleado int,
numero_ventas int default 0,
total_vendido int
);

DELIMITER $$
drop trigger if exists tr_venta_vendedor;
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
drop table if exists acciones_vendedores;
CREATE TABLE acciones_vendedores(
usuario varchar(40),
fecha_act date,
numero_cambios int
);
drop trigger if exists tr_acciones_vendedores;
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

-- 3 CUANDO SE QUIERA INSERTAR DENTRO DE LA TABLA UBICACION UNA NUEVA UBICACION  QUE 
-- CORRESPONDA A UN CLIENTE QUE YA TIENE UNA UBICACIÓN SE LANZARÁ UN MENSAJE NOTIFICANDO
-- QUE ESE CLIENTE YA TIENE UNA UBIACION
drop trigger if exists tr_ubicacion_cliente;
DELIMITER $$
CREATE TRIGGER tr_ubicacion_cliente BEFORE INSERT ON ubicacion
FOR EACH ROW BEGIN
DECLARE war VARCHAR(255);
IF NEW.Cliente_Documento IN (SELECT Cliente_Documento from ubicacion ) THEN 

SET war = CONCAT('EL CLIENTE CON DOCUMENTO ', new.Cliente_Documento, 'YA TIENE UNA UBICACION ASOCIADA');
SIGNAL SQLSTATE '40000' SET message_text = war;
END IF;
END $$
DELIMITER ;

-- TRIGGERS PARA SUPERVISOR

-- 1 CADA VEZ QUE LLEGUE UN PEDIDO DE MATERIAL, EN UNA NUEVA TABLA historial_material
-- SE  REGISTRARÁ EN UNA NUEVA TABLA EL NUMERO DE VECES QUE A UN  PROVEEDOR SE LE 
-- HA COMPRADO MATERIAL Y EL TOTAL QUE ES LE HA COMPRADO A LO LARGO DEL TIEMPO
-- 
drop table if exists historial_compra_material;
CREATE TABLE historial_compra_material(
id_proveedor int,
numero_pedidos int,
cantidad_total int
);

drop trigger if exists tr_historial_compra_material;
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

-- 2. CADA VEZ QUE SE REGISTRE UNA NUEVA COMPRA DE MATERIAL EN LA TABLA compra_material_empleado
-- se va a insertar el documento del empleado, la fecha de facturacion, y a qué proveedor le 
-- recibió el pedido
drop table if exists compra_material_empleado;
CREATE TABLE compra_material_empleado(
documento_empleado int,
fecha_facturacion int,
id_proveedor int
);

 drop trigger if exists tr_compra_material_empleado;
DELIMITER $$
CREATE TRIGGER tr_compra_material_empleado BEFORE INSERT ON compra_material
FOR EACH ROW BEGIN
INSERT INTO compra_material_empleado 
		values(new.documento_empleado,curdate(),new.id_proveedor);
end $$        
DELIMITER ;

-- 3. CADA VEZ QUE CAMBIE EL PRECIO DE UN MATERIAL SE VA GUARDAR EN LA TABLA HISTORIAL_MATERIAL
-- EL ID DEL PROVEEDOR QUE TRAE ESE MATERIAL, EL PORCENTAJE DEL CAMBIO Y LA FECHA DE CAMBIO
drop table if exists historial_material;
CREATE TABLE historial_material(
id_proveedor int,
porcentaje_cambio float(4,2),
fecha_act date
);

drop trigger if exists tr_historial_material;
DELIMITER $$
CREATE TRIGGER tr_historial_material BEFORE UPDATE ON material
FOR EACH ROW BEGIN
DECLARE cambio float(4,1);

SET cambio = (((new.Mat_Precio-old.Mat_Precio)/old.Mat_Precio)*100);
insert into historial_material values(new.ID_Material,concat(cambio,'%'),curdate());

END $$
DELIMITER ;

