-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-10-2023 a las 03:16:59
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gamesnake`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pointstable`
--

CREATE TABLE `pointstable` (
  `id` int(11) NOT NULL,
  `nickname` varchar(35) NOT NULL,
  `score` int(11) NOT NULL,
  `time` varchar(35) NOT NULL,
  `datetime` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pointstable`
--

INSERT INTO `pointstable` (`id`, `nickname`, `score`, `time`, `datetime`) VALUES
(7, 'Cristian', 90, '21', '2023-10-25 20:02:06'),
(8, 'David', 50, '16', '2023-10-25 20:04:40');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `pointstable`
--
ALTER TABLE `pointstable`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `pointstable`
--
ALTER TABLE `pointstable`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
