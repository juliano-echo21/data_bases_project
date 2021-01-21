-- PA inserción empleado
 DROP PROCEDURE if exists INSERTAR_EMPLEADO;
DELIMITER $$
CREATE PROCEDURE Insertar_Empleado (IN Emp_Doc BIGINT, IN Emp_Tipo_doc VARCHAR(45), IN Emp_Nombre VARCHAR(45),
IN Emp_Apellido VARCHAR(45), IN Emp_F_Nacim DATE, IN Emp_Correo VARCHAR(45),IN Emp_Direccion VARCHAR(45),
IN Emp_Tel BIGINT, IN Emp_Cargo VARCHAR(45), IN Emp_Profesion VARCHAR(45), IN Emp_S_Social VARCHAR(45))
BEGIN
DECLARE error INTEGER DEFAULT 0;
      SET error=1;
	INSERT INTO EMPLEADO VALUES(Emp_Doc, Emp_Tipo_doc, Emp_Nombre, Emp_Apellido,Emp_F_Nacim, 
    Emp_Correo, Emp_Direccion, Emp_Tel, Emp_Cargo, Emp_Profesion, Emp_S_Social);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;


-- PA inserción cliente ------------------------------------------------------------------------------------------
 DROP PROCEDURE if exists  INSERTAR_CLIENTE;
DELIMITER $$
CREATE PROCEDURE Insertar_Cliente (IN Cli_Doc BIGINT, IN Cli_Tipo_doc VARCHAR(45), IN Cli_Nombre VARCHAR(45),
IN Cli_Apellido VARCHAR(45), IN Cli_Tel BIGINT, IN Cli_Correo VARCHAR(45))
BEGIN
DECLARE error INTEGER DEFAULT 0;
      SET error=1;
	INSERT INTO CLIENTE VALUES(Cli_Doc,  Cli_Tipo_doc , Cli_Nombre, Cli_Apellido, Cli_Tel, Cli_Correo);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;


-- PA inserción cambio ------------------------------------------------------------------------------------------
 DROP PROCEDURE if exists  INSERTAR_CAMBIO;
DELIMITER $$
CREATE PROCEDURE Insertar_Cambio (IN Cam_Motivo VARCHAR(45), IN Cam_fecha DATE, IN Id_Fact INT)
BEGIN
DECLARE cam_id  INT;
DECLARE error INTEGER DEFAULT 0;
      SET error=1;
    SET cam_id = (SELECT max(id_cambio) FROM CAMBIO)+1;
	INSERT INTO CAMBIO VALUES(cam_id, Cam_Motivo, Cam_fecha, Id_Fact);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;



-- PA inserción Info_Cambio ------------------------------------------------------------------------------------------
 DROP PROCEDURE if exists  INSERTAR_INFO_CAMBIO;
DELIMITER $$
CREATE PROCEDURE Insertar_Info_Cambio (IN Id_Cambio INT, IN Id_Producto INT, 
IN Prod_Nombre VARCHAR(45), Prod_Cantidad INT)
BEGIN
DECLARE error INTEGER DEFAULT 0;
      SET error=1;
	INSERT INTO INFO_CAMBIO VALUES(Id_Cambio, Id_Producto, Prod_Nombre, Prod_Cantidad);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;


-- PA inserción factura_venta ------------------------------------------------------------------------------------------
 DROP PROCEDURE if exists  INSERTAR_Factura;
DELIMITER $$
CREATE PROCEDURE Insertar_Factura (IN Fact_fecha DATE, IN Pago_total INT, IN Cli_Doc BIGINT, IN Emp_Doc BIGINT)
BEGIN
DECLARE fact_id  INT;
DECLARE error INTEGER DEFAULT 0;
 
      SET error=1;
    SET fact_id = (SELECT max(id_factura_venta) FROM factura_venta)+1;
	INSERT INTO factura_venta VALUES(fact_id,Fact_fecha, Pago_total, Cli_Doc, Emp_Doc);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;

-- PA inserción  INFO_FACT------------------------------------------------------------------------------------------
 DROP PROCEDURE if exists  INSERTAR_INFO_FACT;
DELIMITER $$
CREATE PROCEDURE Insertar_Info_Fact (IN Id_Fact INT, IN Id_Producto INT, 
IN Prod_Nombre VARCHAR(45), Prod_Cantidad INT)
BEGIN
DECLARE error INTEGER DEFAULT 0;
 
      SET error=1;

	INSERT INTO info_factura_venta VALUES(Id_Fact , Id_Producto, Prod_Nombre, Prod_Cantidad);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;


-- PA inserción PRODUCTO ------------------------------------------------------------------------------------------
 DROP PROCEDURE if exists  INSERTAR_PRODUCTO;
DELIMITER $$
CREATE PROCEDURE Insertar_Producto(IN Prod_tipo VARCHAR(45), IN Prod_modelo VARCHAR(45),
 IN Prod_color VARCHAR(45), IN Prod_talla TINYINT, IN Prod_precio INT)
BEGIN
DECLARE Prod_id INT;
DECLARE error INTEGER DEFAULT 0;
      SET error=1;

    SET prod_id = (SELECT max(id_producto) FROM producto)+1;
	INSERT INTO PRODUCTO VALUES(prod_id, Prod_tipo, Prod_modelo, Prod_color, Prod_talla, Prod_precio);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;




-- PA inserción UBICACION ------------------------------------------------------------------------------------------
DROP PROCEDURE if exists Insertar_Ubicacion;
DELIMITER $$
CREATE PROCEDURE Insertar_Ubicacion(IN Ubi_ciudad VARCHAR(45), IN Ubi_region VARCHAR(45),
 IN Ubi_Direccion VARCHAR(45), IN Ubi_C_Postal SMALLINT, IN Cli_Doc BIGINT)
BEGIN
DECLARE Ubi_id INT;
DECLARE error INTEGER DEFAULT 0;

      SET error=1;

    SET Ubi_id = (SELECT max(id_ubicacion) FROM Ubicacion)+1;
	INSERT INTO UBICACION VALUES(Ubi_id, Ubi_ciudad, Ubi_region, Ubi_Direccion, Ubi_C_Postal, Cli_Doc);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;
CALL Insertar_Ubicacion('Bogotá', 'Andina', 'Carrera 98 # 26-72', 11101, 100465465);
SELECT * FROM UBICACION;


-- PA inserción Evento_Fabricacion ------------------------------------------------------------------------------------------
 DROP PROCEDURE if exists  INSERTAR_E_FAB;
DELIMITER $$
CREATE PROCEDURE Insertar_E_Fab (IN Emp_doc BIGINT, IN Id_pedido INT, Ev_Labor VARCHAR(45))
BEGIN
DECLARE E_Fab_id INT;
DECLARE error INTEGER DEFAULT 0;
 
      SET error=1;
	SET E_Fab_id = (SELECT max(id_evento_fabricacion) FROM EVENTO_FABRICACION)+1;
	INSERT INTO EVENTO_FABRICACION VALUES(E_Fab_id,Emp_Doc, Id_pedido, Ev_Labor);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;



-- PA inserción PEDIDO ------------------------------------------------------------------------------------------
 DROP PROCEDURE if exists  INSERTAR_PEDIDO;
DELIMITER $$
CREATE PROCEDURE Insertar_Pedido (IN Ped_fecha DATE, Id_fact int)
BEGIN
DECLARE id_ped INT;
DECLARE error INTEGER DEFAULT 0;
 
      SET error=1;
	SET id_ped = (SELECT max(id_pedido) FROM PEDIDO_FABRICACION)+1;
	INSERT INTO PEDIDO_FABRICACION VALUES(id_ped, Ped_fecha, Id_fact);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;



-- PA inserción PROVEEDOR ------------------------------------------------------------------------------------------
 DROP PROCEDURE if exists  INSERTAR_PROVEEDOR;
DELIMITER $$
CREATE PROCEDURE Insertar_Proveedor (IN Nombre_prov VARCHAR(45), Tel_prov BIGINT, Empresa_prov VARCHAR(45))
BEGIN
DECLARE id_prov INT;
DECLARE error INTEGER DEFAULT 0;

      SET error=1;

	SET id_prov = (SELECT max(id_proveedor) FROM PROVEEDOR)+1;
	INSERT INTO PROVEEDOR VALUES(id_prov, Nombre_prov, Tel_prov, Empresa_prov);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;

CALL Insertar_Proveedor('Carlos Ardila', 5818007, 'Cueros 1A'); 
SELECT * FROM PROVEEDOR;



-- PA inserción MATERIAL ------------------------------------------------------------------------------------------
 DROP PROCEDURE if exists  INSERTAR_MATERIAL;
DELIMITER $$
CREATE PROCEDURE Insertar_Material (IN Nombre_mat VARCHAR(45), Precio_mat INT, Id_prov INT)
BEGIN
DECLARE id_mat INT;
DECLARE error INTEGER DEFAULT 0;
 
      SET error=1;
	SET id_mat = (SELECT max(ID_Material) FROM MATERIAL)+1;
	INSERT INTO PROVEEDOR VALUES(id_mat, Nombre_mat, Precio_mat, Id_prov);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;



-- PA inserción Compra_Material------------------------------------------------------------------------------------------
 DROP PROCEDURE if exists  INSERTAR_COMPRA_M;
DELIMITER $$
CREATE PROCEDURE Insertar_Compra_M (IN Compra_fecha DATE, IN Pago_total INT, IN Emp_Doc BIGINT, IN Id_prov INT)
BEGIN
DECLARE compra_id  INT;
DECLARE error INTEGER DEFAULT 0;
 
      SET error=1;

    SET compra_id = (SELECT max(ID_Compra_Material) FROM COMPRA_MATERIAL)+1;
	INSERT INTO COMPRA_MATERIAL VALUES(compra_id, Compra_fecha, Pago_total, Emp_Doc, Id_prov);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;



-- PA inserción Info_Compra_Material ------------------------------------------------------------------------------------------
 DROP PROCEDURE if exists  INSERTAR_INFO_COMPRA;
DELIMITER $$
CREATE PROCEDURE Insertar_Info_Compra (IN Id_Compra INT, IN Id_Material INT, Cantidad_mat INT)
BEGIN
DECLARE error INTEGER DEFAULT 0;
 
      SET error=1;

	INSERT INTO Info_Compra_Material VALUES(Id_Compra, Id_Material, Cantidad_mat);
IF error=0 THEN
	ROLLBACK;
ELSE
	COMMIT;
END IF;
END;
$$
DELIMITER ;


-- -----------------------------------------------------------------------------------------------------------
-- Resto de procedimientos almacenados (por perfil)

-- Administradora

/*Procedimiento que reduce la factura de venta deseada en un porcentaje establecido
(útil para promociones)
*/
DELIMITER $$
CREATE PROCEDURE Promocion (IN Id_Factura INT, IN Descuento INT)
	BEGIN
    DECLARE error INTEGER DEFAULT 0;
	
      SET error=1;

		UPDATE FACTURA_VENTA SET Fact_Pago_Total = Fact_Pago_Total-((Fact_Pago_Total*descuento)/100)
        WHERE ID_Factura_Venta = Id_Factura;
	IF error=0
    THEN
		ROLLBACK;
	ELSE
		COMMIT;
	END IF;
	END$$
DELIMITER ;

CALL Promocion(1, 10);
SELECT * FROM FACTURA_VENTA WHERE ID_Factura_Venta = 1;


/*Procedimiento que reduce en un porcentaje dado las compras en las que se haya comprado una Sandalia Hepearl
(válido para promociones)
*/
DELIMITER $$
CREATE PROCEDURE Descuento_Heparl (IN Descuento INT)
	BEGIN
    DECLARE error INTEGER DEFAULT 0;
      SET error=1;
	
		UPDATE factura_venta SET fact_pago_total = fact_pago_total-((fact_pago_total*Descuento)/100) WHERE id_factura_venta
        IN (SELECT DISTINCT id_factura_venta FROM info_factura_venta WHERE producto_nombre LIKE '%Hepearl%');
	IF error=0 THEN
		ROLLBACK;
	ELSE
		COMMIT;
	END IF;
	END$$
DELIMITER ;


/*Procedi8miento que aumenta en 10 % el precio de los dos modelos más vendidos
*/
DELIMITER $$
CREATE PROCEDURE Aumento_Productos (IN Descuento INT)
	BEGIN
    DECLARE error INTEGER DEFAULT 0;
	
      SET error=1;
	
		UPDATE producto SET producto_precio = producto_precio *1.10 WHERE id_producto 
        IN (select id_producto FROM (select id_producto, count(*) AS total FROM info_factura_venta 
        GROUP BY id_producto ORDER BY total DESC LIMIT 2) AS mas_vendidos);
	IF error=0 THEN
		ROLLBACK;
	ELSE
		COMMIT;
	END IF;
	END$$
DELIMITER ;


-- Vendedor

/*Procedimiento que consulta las ventas hechas entre dos fechas asignadas
*/
DELIMITER $$
CREATE PROCEDURE Intervalo_ventas (IN Fecha_inicio DATE, IN Fecha_fin DATE)
	BEGIN
    DECLARE error INTEGER DEFAULT 0;
	
      SET error=1;
	
		SELECT * FROM Factura_Venta WHERE Fact_Fecha >= Fecha_inicio AND Fact_Fecha <= Fecha_fin;
	IF error=0 OR Fecha_inicio > Fecha_fin
    THEN
		ROLLBACK;
	ELSE
		COMMIT;
	END IF;
	END$$
DELIMITER ;

CALL Intervalo_ventas ('2020-02-12', '2020-02-15');

SELECT * FROM Factura_Venta;


/* Procedimiento que aplica un descuento establecido a las facturas de una región dada
*/
DELIMITER $$
CREATE PROCEDURE Descuento_region (IN Descuento INT, IN Region VARCHAR(45))
	BEGIN
    DECLARE error INTEGER DEFAULT 0;
	
      SET error=1;
	
		update factura_venta set fact_pago_total = fact_pago_total-((fact_pago_total*descuento)/100) 
        where id_factura_venta in (select id_factura_venta from (select * from factura_venta) 
        as aux where cliente_documento in (select cliente_documento from ubicacion where ubi_region =Region));
	IF error=0 THEN
		ROLLBACK;
	ELSE
		COMMIT;
	END IF;
	END$$
DELIMITER ;


/* Procedimiento que aumenta un porcentaje dado a los clientes que hayan realizado un cambio
*/
DELIMITER $$
CREATE PROCEDURE Aumento_Por_Cambio (IN Aumento INT)
	BEGIN
    DECLARE error INTEGER DEFAULT 0;
	
      SET error=1;
	
		update factura_venta set fact_pago_total = fact_pago_total+((fact_pago_total*Aumento)/100) where cliente_documento 
        in (select cliente_documento from (select * from factura_venta) as fac_ven natural join (select * from cambio) as aux);
	IF error=0 THEN
		ROLLBACK;
	ELSE
		COMMIT;
	END IF;
	END$$
DELIMITER ;


-- Supervisor de fábrica

/*Procedimiento que aumenta en un porcentaje establecido el precio de los materiales 
que se compraron entre dos fechas dadas. 
*/
DELIMITER $$
CREATE PROCEDURE Aumento_CompraM_Fechas (IN Aumento INT, IN Fecha_inicio DATE, IN Fecha_fin DATE)
	BEGIN
    DECLARE error INTEGER DEFAULT 0;
		
      SET error=1;
	
		UPDATE material SET mat_precio = mat_precio+((mat_precio*Aumento)/100) WHERE id_material IN
		(SELECT id_material FROM info_compra_material NATURAL JOIN
		(SELECT compram_fecha, id_compra_material FROM compra_material 
		WHERE compram_fecha BETWEEN Fecha_inicio AND Fecha_fin) AS entre);
	IF error=0 OR Fecha_inicio > Fecha_fin
    THEN
		ROLLBACK;
	ELSE
		COMMIT;
	END IF;
	END$$
DELIMITER ;


/* Procedimiento que aumenta en un valor dado las comporas de material que tengan un  proveedor en específico
*/
DELIMITER $$
CREATE PROCEDURE Aumento_Compra_Prov (IN Aumento INT, IN Nombre_Proveedor VARCHAR(45))
	BEGIN
    DECLARE error INTEGER DEFAULT 0;
	
      SET error=1;
		update compra_material set compram_pago_total = compram_pago_total + Aumento where id_compra_material 
        in (select id_compra_material from (select * from compra_material) as a natural join proveedor 
        where prov_empresa = Nombre_Proveedor);
	IF error=0 THEN
		ROLLBACK;
	ELSE
		COMMIT;
	END IF;
	END$$
DELIMITER ;


/* Procedimiento que elimina un evento de fabricación ingresado antes de una fecha establecida
*/
DELIMITER $$
CREATE PROCEDURE Eliminar_evento (IN Proceso_Fab VARCHAR(45), IN Fecha DATE)
	BEGIN
    DECLARE error INTEGER DEFAULT 0;
	
      SET error=1;
		DELETE FROM evento_fabricacion WHERE id_pedido IN 
        (SELECT id_pedido FROM pedido_fabricacion WHERE pedido_fecha > Fecha) 
        AND evento_labor = Proceso_Fab;
	IF error=0 THEN
		ROLLBACK;
	ELSE
		COMMIT;
	END IF;
	END$$
DELIMITER ;


