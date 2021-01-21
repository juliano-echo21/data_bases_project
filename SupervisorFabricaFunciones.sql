-- Funciones supervisor de fabrica 

drop function if exists f_nombre_etapa;
DELIMITER && 
CREATE FUNCTION f_nombre_etapa(nombre_empleado varchar (30)) returns varchar (35)
	BEGIN 
    DECLARE nombreEtapa varchar (35);
    SELECT distinct evento_labor into nombreEtapa FROM empleado join evento_fabricacion
    WHERE empleado.Documento_Empleado=evento_fabricacion.Documento_Empleado 
    and empleado.Emp_Nombre=nombre_empleado;
	return nombreEtapa;
	END &&
DELIMITER ;
select f_nombre_etapa('Alexander');
--
drop function if exists f_compra_unidad;
DELIMITER && 
CREATE FUNCTION f_compra_unidad(fecha date) returns int
	BEGIN 
    DECLARE compraPorUnidad int;
    select min(compraUnidad) into compraPorUnidad from (select CompraM_Pago_Total/Material_Cantidad as compraUnidad from compra_material 
	join info_compra_material using (id_compra_material) 
    where CompraM_Fecha>fecha) as compraUnidad;
	return compraPorUnidad;
	END &&
DELIMITER ;
select f_compra_unidad('2019-12-27');
--
drop function if exists  f_numero_pedidos;
DELIMITER && 
CREATE FUNCTION f_numero_pedidos(monto int) returns int
	BEGIN 
    DECLARE NumeroPedidos int;
    select count(id_pedido) into numeroPedidos from (SELECT id_pedido from pedido_fabricacion, factura_venta 
	where pedido_fabricacion.ID_Factura_Venta=factura_venta.ID_Factura_Venta
	and Pedido_Fecha IN (SELECT Pedido_Fecha FROM pedido_fabricacion where pedido_fecha<='2020-06-30') 
	and Fact_Pago_Total IN (SELECT Fact_Pago_Total FROM factura_venta WHERE Fact_Pago_Total>monto) group by
	factura_venta.ID_Factura_Venta order by sum(id_pedido)) as pedidos;
	return numeroPedidos;
	END &&
DELIMITER ;
select f_numero_pedidos(150000);
--
drop function if exists  f_mayor_proveedor;
DELIMITER && 
CREATE FUNCTION f_mayor_proveedor(fecha date) returns varchar (40)
	BEGIN 
    DECLARE mayorProveedor varchar (40);
    SELECT Prov_Nombre into mayorProveedor from compra_material join info_compra_material using (id_compra_material)
	join empleado using (documento_empleado) join proveedor WHERE proveedor.id_proveedor=compra_material.ID_Proveedor 
	and  CompraM_Fecha<=fecha group by prov_nombre order by material_cantidad desc limit 1;
	return mayorProveedor;
	END &&
DELIMITER ;
select f_mayor_proveedor('2020-02-01');
--
drop function if exists f_promedio_gastos;
DELIMITER && 
CREATE FUNCTION f_promedio_gastos(proveedor varchar(50)) returns double
	BEGIN 
    DECLARE promedioGastos double;
    SELECT avg(CompraM_Pago_Total) into promedioGastos from compra_material
	JOIN info_compra_material, proveedor where  
	compra_material.ID_Compra_Material=info_compra_material.ID_Compra_Material and compra_material.ID_Proveedor= proveedor.ID_Proveedor
	and proveedor.Prov_Empresa=proveedor
	group by compra_material.ID_Proveedor, ID_Material order by avg(CompraM_Pago_Total);
	return promedioGastos;
	END &&
DELIMITER ;
select f_promedio_gastos('Tapisantander');







