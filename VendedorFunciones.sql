-- Funciones Vendedor 

drop function if exists  f_numero_cambios;

DELIMITER &&
CREATE FUNCTION f_numero_cambios(ciudad varchar (35)) returns int
	BEGIN
    declare numeroCambios int;
    SELECT sum(Producto_Cantidad) into numeroCambios from info_cambio JOIN cambio using (id_cambio)
	JOIN producto using (id_producto) JOIN factura_venta using (id_factura_venta)
    JOIN cliente using (cliente_documento) join ubicacion using (cliente_documento)
	where Ubi_Ciudad=ciudad group by Ubi_Ciudad order by sum(Producto_Cantidad);
    return numeroCambios;
    END &&
DELIMITER ;
select f_numero_cambios("Bogota");
-- 
drop function if exists  f_producto_ventas;
DELIMITER &&
CREATE FUNCTION f_producto_ventas(precio int) returns varchar(30)
	BEGIN
    declare productoVenta varchar(30);
    SELECT producto_nombre into productoVenta from info_factura_venta
	join factura_venta where factura_venta.ID_Factura_Venta= info_factura_venta.ID_Factura_Venta and 
	Fact_Pago_Total>precio group by Producto_Nombre order by sum(Producto_Cantidad) desc limit 1;
    return productoVenta;
    END &&
DELIMITER ;
select f_producto_ventas(300000);
-- 
drop function if exists  f_talla_mas_comprada;
DELIMITER &&
CREATE FUNCTION f_talla_mas_comprada(tipo_zapato varchar(30)) returns int
	BEGIN
    declare tallaMasComprada int;
    select Producto_Talla into tallaMasComprada from factura_venta join info_factura_venta using (id_factura_venta)
	join producto using (id_producto) where Producto_Tipo=tipo_zapato group by Producto_Talla 
	order by sum(Producto_Talla) desc limit 1;
    return tallaMasComprada;
    END &&
DELIMITER ;
select f_talla_mas_comprada("Zapatilla");
--
drop function if exists f_ganacias_productos;
DELIMITER &&
CREATE FUNCTION f_ganancias_productos(Nombre_producto varchar(30)) returns int
	BEGIN
    declare gananciaProducto int;
    Select sum(Fact_Pago_Total) as GananciaTotal into gananciaProducto from factura_venta 
	join info_factura_venta where factura_venta.ID_Factura_Venta=info_factura_venta.ID_Factura_Venta and 
	info_factura_venta.Producto_Nombre IN (SELECT Producto_Nombre from info_factura_venta 
	where Producto_Nombre like  Nombre_producto) group by Producto_Nombre ORDER BY sum(Fact_Pago_Total) desc; 
    return gananciaProducto;
    END &&
DELIMITER ;
select f_ganancias_productos("Mulan");
--
drop function if exists  f_dias_promedio;
DELIMITER &&
CREATE FUNCTION f_dias_promedio(tipo_zapato varchar(30)) returns int
	BEGIN
    declare diasPromedio int;
    select AVG(Cam_Fecha-Fact_Fecha) into diasPromedio from cambio join factura_venta using (id_factura_venta) 
	join info_cambio using (id_cambio) join producto using (id_producto) where Producto_Tipo=tipo_zapato;
    return diasPromedio;
    END &&
DELIMITER ;
select f_dias_promedio("Zapatilla");







