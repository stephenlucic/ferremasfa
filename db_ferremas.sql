CREATE TABLE `usuario` (
  `id` int PRIMARY KEY,
  `nombre` varchar(255),
  `email` varchar(255)
);

CREATE TABLE `ordenes` (
  `id` int PRIMARY KEY,
  `detalle` varchar(255),
  `usuario_id` int,
  `producto_id` int
);

ALTER TABLE `ordenes` ADD FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`);
