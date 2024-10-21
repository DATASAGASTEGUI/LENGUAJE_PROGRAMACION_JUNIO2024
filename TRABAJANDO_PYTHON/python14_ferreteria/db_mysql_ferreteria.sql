-- (1) ELIMINAR LA BASE DATOS SI EXISTE

DROP DATABASE IF EXISTS FERRETERIA;

-- (2) CREAR LA BASE DE DATOS SI NO EXISTE

CREATE DATABASE IF NOT EXISTS FERRETERIA;

-- (3) SELECCIONARA LA BASE DE DATOS A USAR

USE FERRETERIA;

-- (4) CREAR LA TABLAS SI NO EXISTE

-- Tabla para almacenar productos
CREATE TABLE IF NOT EXISTS Producto (
    id_producto INT            NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre      VARCHAR(100)   NOT NULL,
    descripcion VARCHAR(255)   NOT NULL,
    precio      DECIMAL(10, 2) NOT NULL,
    stock       INT            NOT NULL,
    categoria   VARCHAR(50)
);

-- Tabla para registrar ventas
CREATE TABLE IF NOT EXISTS Venta (
    id_venta INT            NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fecha    DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total    DECIMAL(10, 2) NOT NULL
);

-- Tabla para detallar productos vendidos en cada venta
CREATE TABLE DetalleVentas (
    id_detalle  INT            NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_venta    INT            NOT NULL,
    id_producto INT            NOT NULL,
    cantidad    INT            NOT NULL,
    subtotal    DECIMAL(10, 2) NOT NULL,
                FOREIGN KEY (id_venta) REFERENCES Venta(id_venta) ON DELETE CASCADE,
                FOREIGN KEY (id_producto) REFERENCES Producto(id_producto) ON DELETE CASCADE
);

CREATE TABLE Usuario (
    id_usuario     INT                                        NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(50)                                NOT NULL UNIQUE,
    contrasena     VARCHAR(255)                               NOT NULL,
    rol            ENUM('Administrador', 'Cajero', 'Almacén') NOT NULL
);

-- (5) INSERTAR REGISTROS PARA LAS TABLAS

-- Insertar productos en la tabla Producto
INSERT INTO Producto (nombre, descripcion, precio, stock, categoria) VALUES
('Martillo', 'Martillo de acero con mango de madera', 15.50, 50, 'Herramientas'),
('Destornillador', 'Juego de destornilladores planos y de estrella', 12.75, 40, 'Herramientas'),
('Llave Inglesa', 'Llave ajustable de acero inoxidable', 18.20, 30, 'Herramientas'),
('Cinta Métrica', 'Cinta métrica de 5 metros con bloqueo automático', 8.50, 25, 'Medición'),
('Taladro', 'Taladro eléctrico con velocidad variable', 85.99, 10, 'Herramientas'),
('Sierra', 'Sierra manual para madera con mango ergonómico', 20.45, 15, 'Herramientas'),
('Tornillos', 'Paquete de 100 tornillos de 2 pulgadas', 5.75, 100, 'Fijaciones'),
('Clavos', 'Caja de 500 clavos de acero', 7.20, 150, 'Fijaciones'),
('Cemento', 'Saco de cemento de 50 kg', 10.00, 20, 'Construcción'),
('Arena', 'Bolsa de arena de 25 kg', 3.50, 50, 'Construcción'),
('Tubos PVC', 'Tubo de PVC de 1 pulgada, 3 metros', 4.80, 35, 'Plomería'),
('Llave de paso', 'Llave de paso de 1/2 pulgada para agua', 6.25, 40, 'Plomería'),
('Cinta aislante', 'Rollo de cinta aislante negra de alta resistencia', 2.50, 75, 'Electricidad'),
('Foco LED', 'Foco LED de 9W luz cálida', 3.20, 100, 'Electricidad'),
('Interruptor', 'Interruptor de pared blanco', 4.30, 60, 'Electricidad'),
('Cable eléctrico', 'Rollo de cable eléctrico de 10 metros', 15.00, 25, 'Electricidad'),
('Pintura blanca', 'Galón de pintura blanca mate', 18.50, 15, 'Pintura'),
('Rodillo', 'Rodillo para pintar con mango ergonómico', 9.75, 30, 'Pintura'),
('Brocha', 'Brocha de 3 pulgadas para pintura', 4.10, 50, 'Pintura'),
('Adhesivo', 'Adhesivo multiusos de alta resistencia', 6.00, 40, 'Adhesivos'),
('Pegamento PVC', 'Pegamento especial para tubos de PVC', 5.25, 30, 'Adhesivos'),
('Escalera', 'Escalera de aluminio de 6 escalones', 75.00, 5, 'Herramientas'),
('Nivel', 'Nivel de burbuja de 40 cm', 14.00, 20, 'Medición'),
('Guantes', 'Par de guantes de trabajo de cuero', 8.50, 35, 'Protección'),
('Máscara', 'Máscara de protección contra polvo', 3.50, 50, 'Protección'),
('Flexómetro', 'Flexómetro de 3 metros', 7.20, 25, 'Medición'),
('Alicates', 'Alicates universales de acero', 12.30, 20, 'Herramientas'),
('Llave de tubo', 'Llave de tubo para plomería', 22.10, 15, 'Plomería'),
('Esmeril', 'Esmeril angular de 4.5 pulgadas', 55.99, 8, 'Herramientas'),
('Carretilla', 'Carretilla de acero con neumático sólido', 95.00, 10, 'Construcción'),
('Pala', 'Pala para excavación con mango de madera', 16.20, 20, 'Construcción'),
('Alambre galvanizado', 'Rollo de alambre galvanizado de 1 mm', 12.50, 30, 'Construcción'),
('Cerradura', 'Cerradura de seguridad para puerta', 25.00, 15, 'Seguridad'),
('Candado', 'Candado de acero inoxidable con 2 llaves', 10.99, 50, 'Seguridad'),
('Tubería de cobre', 'Tubería de cobre de 1/2 pulgada, 2 metros', 25.75, 20, 'Plomería'),
('Llave Allen', 'Juego de llaves Allen, 9 piezas', 9.90, 25, 'Herramientas'),
('Disco de corte', 'Disco de corte para metal, 7 pulgadas', 6.80, 40, 'Herramientas'),
('Lija', 'Paquete de 5 hojas de lija para madera', 4.50, 50, 'Pintura'),
('Silicón', 'Silicón transparente para sellado, 280 ml', 5.00, 30, 'Adhesivos');

-- Insertar ventas en la tabla Ventas
INSERT INTO Venta (id_venta, fecha, total) VALUES
(1, '2024-11-18 10:15:00', 30.50),
(2, '2024-11-18 11:00:00', 75.25),
(3, '2024-11-18 12:30:00', 125.00),
(4, '2024-11-18 13:45:00', 55.75),
(5, '2024-11-18 14:15:00', 40.00),
(6, '2024-11-18 15:20:00', 18.00),
(7, '2024-11-18 16:10:00', 92.50),
(8, '2024-11-18 17:00:00', 60.75),
(9, '2024-11-18 17:45:00', 43.80),
(10, '2024-11-18 18:30:00', 25.00),
(11, '2024-11-19 09:00:00', 30.50),
(12, '2024-11-19 10:30:00', 90.00),
(13, '2024-11-19 12:15:00', 135.25),
(14, '2024-11-19 14:00:00', 50.00),
(15, '2024-11-19 15:45:00', 60.00),
(16, '2024-11-19 16:30:00', 80.00),
(17, '2024-11-19 17:15:00', 125.00),
(18, '2024-11-19 18:00:00', 110.50),
(19, '2024-11-19 19:30:00', 70.75),
(20, '2024-11-19 20:15:00', 20.00);

-- Insertar detalles en la tabla DetalleVentas
INSERT INTO DetalleVentas (id_detalle, id_venta, id_producto, cantidad, subtotal) VALUES
(1, 1, 1, 1, 15.50),
(2, 1, 2, 2, 15.00),
(3, 2, 3, 1, 18.20),
(4, 2, 4, 3, 57.05),
(5, 3, 5, 1, 85.99),
(6, 3, 6, 2, 40.00),
(7, 4, 7, 10, 57.50),
(8, 5, 8, 5, 35.00),
(9, 6, 9, 2, 18.00),
(10, 7, 10, 3, 92.50),
(11, 8, 11, 5, 24.00),
(12, 8, 12, 2, 36.75),
(13, 9, 13, 4, 10.00),
(14, 9, 14, 1, 33.80),
(15, 10, 15, 2, 25.00),
(16, 11, 16, 1, 15.00),
(17, 11, 17, 2, 15.50),
(18, 12, 18, 3, 90.00),
(19, 13, 19, 1, 135.25),
(20, 14, 20, 2, 50.00),
(21, 15, 21, 1, 60.00),
(22, 16, 22, 2, 80.00),
(23, 17, 23, 1, 125.00),
(24, 18, 24, 3, 110.50),
(25, 19, 25, 2, 70.75),
(26, 20, 26, 1, 20.00);






