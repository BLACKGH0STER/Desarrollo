-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-11-2023 a las 16:51:14
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mydb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamos`
--

CREATE TABLE `prestamos` (
  `idprestamo` int(11) NOT NULL,
  `id` int(11) DEFAULT NULL,
  `idlibro` int(11) DEFAULT NULL,
  `fechaprestamo` date DEFAULT NULL,
  `fechadevolucion` date DEFAULT NULL,
  `estadoprestamo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `prestamos`
--

INSERT INTO `prestamos` (`idprestamo`, `id`, `idlibro`, `fechaprestamo`, `fechadevolucion`, `estadoprestamo`) VALUES
(1, 832624, 2523, '1000-01-01', '1000-01-01', 'Prestamo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbestudiantes`
--

CREATE TABLE `tbestudiantes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `edad` int(11) NOT NULL,
  `carrera` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tbestudiantes`
--

INSERT INTO `tbestudiantes` (`id`, `nombre`, `apellido`, `edad`, `carrera`) VALUES
(832624, 'Ernesto', 'Molina', 18, 'Ing. Industrial'),
(836529, 'Francisco', 'Ayala', 25, 'Ing. sistemas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tblibros`
--

CREATE TABLE `tblibros` (
  `idLibro` int(11) NOT NULL,
  `titulo` varchar(70) NOT NULL,
  `cantidad` int(8) NOT NULL,
  `autor` varchar(50) NOT NULL,
  `anio` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tblibros`
--

INSERT INTO `tblibros` (`idLibro`, `titulo`, `cantidad`, `autor`, `anio`) VALUES
(2324, 'Rayuela', 2, 'Julio Cortázar', 1963),
(2523, 'Cien años de soledad', 4, 'Gabriel Garcia Márquez', 1967);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD PRIMARY KEY (`idprestamo`),
  ADD KEY `id` (`id`),
  ADD KEY `idlibro` (`idlibro`);

--
-- Indices de la tabla `tbestudiantes`
--
ALTER TABLE `tbestudiantes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tblibros`
--
ALTER TABLE `tblibros`
  ADD PRIMARY KEY (`idLibro`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD CONSTRAINT `prestamos_ibfk_1` FOREIGN KEY (`id`) REFERENCES `tbestudiantes` (`id`),
  ADD CONSTRAINT `prestamos_ibfk_2` FOREIGN KEY (`idlibro`) REFERENCES `tblibros` (`idLibro`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
