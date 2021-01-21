-- Funciones administradora:

SET GLOBAL log_bin_trust_function_creators = 1;

drop function if exists  f_producto_mas_vendido;
DELIMITER %%
CREATE FUNCTION f_producto_mas_vendido (ciudad varchar (25)) returns varchar (35)
	BEGIN 
    DECLARE nombre_producto varchar(35);
	SELECT producto_nombre into nombre_producto FROM factura_venta
	JOIN info_factura_venta USING (ID_Factura_Venta) join ubicacion using (cliente_documento)
	where ubi_ciudad=ciudad group by ID_Producto
	order by sum(Producto_Cantidad) desc limit 1;
    return nombre_producto;
	END%%
DELIMITER ; 
select f_producto_mas_vendido('Bogota');

drop function if exists  f_producto_mas_cambiado;
DELIMITER %%
CREATE FUNCTION f_producto_mas_cambiado (ciudad varchar (25)) returns varchar (35)
	BEGIN 
    DECLARE nombre_producto varchar(35);
	select producto_nombre into nombre_producto from info_cambio join cambio using (ID_Cambio)
	join factura_venta using (id_factura_venta) join ubicacion 
    where factura_venta.Cliente_Documento=ubicacion.Cliente_Documento and Ubi_Ciudad=ciudad
	group by Producto_Nombre order by sum(Producto_Cantidad) desc limit 1;
    return nombre_producto;
	END%%
DELIMITER ; 
select f_producto_mas_cambiado('Medellin');

drop function if exists f_promedio_ganancias;
DELIMITER %%
CREATE FUNCTION f_promedio_ganancias (fecha date) returns decimal (9,4)
	BEGIN 
    DECLARE promedioGanancias decimal (9,4);
	SELECT AVG(Fact_Pago_Total)-PromedioCompras as PromedioGanacias into promedioGanancias FROM factura_venta, 
	(SELECT AVG(CompraM_Pago_Total) as PromedioCompras FROM compra_material 
	WHERE CompraM_Fecha> fecha) AS PromedioPagos
	WHERE Fact_Fecha> fecha;
    return promedioGanancias;
	END%%
DELIMITER ; 
select f_promedio_ganancias('2020-03-01');

drop function if exists  f_empleado_ventas;
DELIMITER %%
CREATE FUNCTION f_empleado_ventas (documento int) returns int
	BEGIN 
    DECLARE cantidadVendida int;
	select sum(Producto_Cantidad) into cantidadVendida from empleado INNER JOIN factura_venta 
    ON empleado.Documento_Empleado= factura_venta.Documento_Empleado
	INNER JOIN info_factura_venta ON factura_venta.ID_Factura_Venta=info_factura_venta.ID_Factura_Venta
	WHERE Fact_Fecha>= '2020-01-01' and Fact_Fecha<='2020-06-30' and empleado.Documento_Empleado=documento;
    return cantidadVendida;
	END%%
DELIMITER ; 
select f_empleado_ventas(19467875);

drop function if exists  f_color_menos_vendido;
DELIMITER %%
CREATE FUNCTION f_color_menos_vendido (tipo_zapato varchar(20)) returns varchar(35)
	BEGIN 
    DECLARE colorMenosVendido varchar(35);
	select Producto_Color into colorMenosVendido from factura_venta, info_factura_venta, producto 
    where factura_venta.ID_Factura_Venta=info_factura_venta.ID_Factura_Venta and 
	info_factura_venta.ID_Producto=producto.ID_Producto and Producto_Tipo=tipo_zapato and 
    Fact_Fecha>'2020-02-01' and Fact_Fecha<'2020-05-31' group by  info_factura_venta.ID_Producto
	order by sum(Producto_Cantidad) asc limit 1;
    return colorMenosVendido;
	END%%
DELIMITER ; 
select f_color_menos_vendido("Sandalia");





