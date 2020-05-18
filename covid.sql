-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 18, 2020 at 09:30 PM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `covid`
--

-- --------------------------------------------------------

--
-- Table structure for table `adhar`
--

DROP TABLE IF EXISTS `adhar`;
CREATE TABLE IF NOT EXISTS `adhar` (
  `adharno` int(11) NOT NULL,
  `adharname` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`adharno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
CREATE TABLE IF NOT EXISTS `bookings` (
  `bid` int(100) NOT NULL AUTO_INCREMENT,
  `lid` varchar(50) NOT NULL,
  `pid` varchar(50) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `contact` varchar(15) NOT NULL,
  `alloted_date` varchar(30) NOT NULL,
  `request_date` varchar(20) NOT NULL DEFAULT current_timestamp(),
  `risk` varchar(5) NOT NULL,
  `status` int(1) NOT NULL DEFAULT 0,
  `sample_status` int(1) NOT NULL DEFAULT 0,
  `result` int(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`bid`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`bid`, `lid`, `pid`, `name`, `contact`, `alloted_date`, `request_date`, `risk`, `status`, `sample_status`, `result`) VALUES
(4, 'KA2017GLB146', 'Ka7272', 'Sheshnath', '9916362578', '2020-05-20T19:00', '2020-05-19 01:25:58', '45.07', 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
CREATE TABLE IF NOT EXISTS `patient` (
  `adharname` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `adharno` varchar(13) NOT NULL,
  `father` varchar(50) DEFAULT NULL,
  `mother` varchar(50) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `contact` varchar(10) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `pincode` varchar(6) NOT NULL,
  `address` varchar(250) DEFAULT NULL,
  `pid` varchar(12) NOT NULL,
  `infection` varchar(10) NOT NULL DEFAULT '0',
  `book_stat` int(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`adharno`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`adharname`, `password`, `adharno`, `father`, `mother`, `gender`, `dob`, `email`, `contact`, `state`, `district`, `pincode`, `address`, `pid`, `infection`, `book_stat`) VALUES
('Pooja', '12345', '632099145080', 'Baburao', 'Kanchana', 'female', '2020-05-04', 'pooja@gmail.com', '9148468973', 'Karnataka', 'Kalburgi', '585104', 'New Raghavendra Colony Glb', 'Ka9513', '0', 0),
('Sheshnath', '12345', '632099146396', 'baburao', 'kanchana', 'male', '1999-07-03', 'sheshnathhadbe@gmail.com', '9916362578', 'Karnataka', 'Gulbarga', '585103', 'N R colony', 'Ka7272', '18.57', 1);

-- --------------------------------------------------------

--
-- Table structure for table `sample_collection`
--

DROP TABLE IF EXISTS `sample_collection`;
CREATE TABLE IF NOT EXISTS `sample_collection` (
  `regno` varchar(20) NOT NULL,
  `regname` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `pincode` varchar(6) NOT NULL,
  `address` varchar(250) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `contact` varchar(15) DEFAULT NULL,
  `worktstart` varchar(50) DEFAULT NULL,
  `worktend` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`regno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sample_collection`
--

INSERT INTO `sample_collection` (`regno`, `regname`, `password`, `state`, `district`, `pincode`, `address`, `email`, `contact`, `worktstart`, `worktend`) VALUES
('KA2017GLB146', 'Gulbarga Testing Center', '12345', 'Karnataka', 'Gulbarga', '585105', 'SB temple road, Kalburgi', 'gulbarga_test@gmail.com', '847252563', '08:00', '20:00');

-- --------------------------------------------------------

--
-- Table structure for table `testing_facility`
--

DROP TABLE IF EXISTS `testing_facility`;
CREATE TABLE IF NOT EXISTS `testing_facility` (
  `regno` varchar(20) NOT NULL,
  `regname` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `address` varchar(250) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `contact` varchar(15) DEFAULT NULL,
  `notest` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`regno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `testing_facility`
--

INSERT INTO `testing_facility` (`regno`, `regname`, `password`, `state`, `district`, `address`, `email`, `contact`, `notest`) VALUES
('KA2017GLB148', 'ESIC Gulbarg', '12345', 'Karnataka', 'Gulbarga', 'Kharge ptrol bunk road, kalburgi', 'esic_test@gmail.com', '8472365896', '500');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
