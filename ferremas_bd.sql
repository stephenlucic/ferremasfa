CREATE TABLE `producto` (
  `id` integer PRIMARY KEY,
  `nombre` varchar(255),
  `descripcion` varchar(255),
  `precio` float,
  `categoria` varchar(255)
);

CREATE TABLE `orden_compra` (
  `id` integer PRIMARY KEY,
  `fecha_orden` varchar(255),
  `usuario_id` integer,
  `estado` varchar(255)
);

CREATE TABLE `ventas` (
  `id` integer PRIMARY KEY,
  `fecha_emision` varchar(255),
  `cantidad` varchar(255),
  `monto` float,
  `producto_id` integer,
  `orden_id` integer
);

CREATE TABLE `oferta` (
  `id` integer PRIMARY KEY,
  `descuento` float,
  `fecha_inicio` varchar(255),
  `fecha_fin` varchar(255),
  `sucursal_id` integer,
  `producto_id` integer
);

CREATE TABLE `usuario` (
  `id` integer PRIMARY KEY,
  `nombre` varchar(255),
  `apellidos` varchar(255),
  `email` varchar(255),
  `direccion` varchar(255)
);

CREATE TABLE `boleta_factura` (
  `id` integer PRIMARY KEY,
  `orden_id` integer,
  `fecha_emision` varchar(255),
  `monto_total` float,
  `cantidad` integer
);

CREATE TABLE `reporte` (
  `id` integer PRIMARY KEY,
  `usuario_id` integer,
  `tipo` varchar(255),
  `fecha_generada` varchar(255)
);

CREATE TABLE `inventario` (
  `id` integer PRIMARY KEY,
  `cantidad` integer,
  `sucursal_id` integer,
  `producto_id` integer
);

CREATE TABLE `sucursal` (
  `id` integer PRIMARY KEY,
  `nombre` varchar(255),
  `direccion` varchar(255)
);

ALTER TABLE `inventario` ADD FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`);

ALTER TABLE `orden_compra` ADD FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`);

ALTER TABLE `boleta_factura` ADD FOREIGN KEY (`orden_id`) REFERENCES `orden_compra` (`id`);

ALTER TABLE `oferta` ADD FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`);

ALTER TABLE `reporte` ADD FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`);

ALTER TABLE `oferta` ADD FOREIGN KEY (`sucursal_id`) REFERENCES `sucursal` (`id`);

ALTER TABLE `ventas` ADD FOREIGN KEY (`orden_id`) REFERENCES `orden_compra` (`id`);

ALTER TABLE `ventas` ADD FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`);
