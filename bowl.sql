-- phpMyAdmin SQL Dump
-- version 4.1.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 12, 2016 at 12:28 PM
-- Server version: 5.5.47-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bowl`
--

-- --------------------------------------------------------

--
-- Table structure for table `m_entries`
--

CREATE TABLE IF NOT EXISTS `m_entries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mid` int(11) NOT NULL,
  `firstname` text NOT NULL,
  `lastname` text NOT NULL,
  `displayname` text NOT NULL,
  `email` text NOT NULL,
  `enrolltime` datetime NOT NULL,
  `points` int(11) NOT NULL,
  `remaining` int(11) NOT NULL,
  `possible` int(11) NOT NULL,
  `paid` int(11) NOT NULL,
  `optout` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=58 ;

--
-- Table structure for table `m_entries_data`
--

CREATE TABLE IF NOT EXISTS `m_entries_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mid` int(11) NOT NULL,
  `eid` int(11) NOT NULL,
  `tid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1211 ;

--
-- Table structure for table `m_events`
--

CREATE TABLE IF NOT EXISTS `m_events` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `round` tinyint(4) NOT NULL,
  `starttime` datetime NOT NULL,
  `endtime` datetime NOT NULL,
  `lastupdate` datetime NOT NULL,
  `currentwins` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `m_events`
--

INSERT INTO `m_events` (`id`, `name`, `round`, `starttime`, `endtime`, `lastupdate`, `currentwins`) VALUES
(1, 'March Madness Pool 2016', 0, '2016-03-17 11:59:00', '2016-04-05 03:00:00', '2016-03-17 11:59:00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `m_games`
--

CREATE TABLE IF NOT EXISTS `m_games` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mid` int(11) NOT NULL,
  `gameid` int(11) NOT NULL,
  `winner` int(11) NOT NULL,
  `loser` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=168 ;

--
-- Table structure for table `m_teams`
--

CREATE TABLE IF NOT EXISTS `m_teams` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mid` int(11) NOT NULL,
  `seed` int(11) NOT NULL,
  `lid` int(11) NOT NULL,
  `name` text NOT NULL,
  `espnid` int(11) NOT NULL,
  `wins` int(11) NOT NULL DEFAULT '0',
  `inactive` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=65 ;

--
-- Dumping data for table `m_teams`
--

INSERT INTO `m_teams` (`id`, `mid`, `seed`, `lid`, `name`, `espnid`, `wins`, `inactive`) VALUES
(1, 1, 1, 1, 'Virginia', 258, 0, 0),
(2, 1, 1, 2, 'Oregon', 2483, 0, 0),
(3, 1, 1, 3, 'North Carolina', 153, 0, 0),
(4, 1, 1, 4, 'Kansas', 2305, 0, 0),
(5, 1, 2, 1, 'Michigan State', 127, 0, 0),
(6, 1, 2, 2, 'Oklahoma', 201, 0, 0),
(7, 1, 2, 3, 'Xavier', 2752, 0, 0),
(8, 1, 2, 4, 'Villanova', 222, 0, 0),
(9, 1, 3, 1, 'Utah', 254, 0, 0),
(10, 1, 3, 2, 'Texas A&M', 245, 0, 0),
(11, 1, 3, 3, 'West Virginia', 277, 0, 0),
(12, 1, 3, 4, 'Miami', 2390, 0, 0),
(13, 1, 4, 1, 'Iowa State', 66, 0, 0),
(14, 1, 4, 2, 'Duke', 150, 0, 0),
(15, 1, 4, 3, 'Kentucky', 96, 0, 0),
(16, 1, 4, 4, 'California', 25, 0, 0),
(17, 1, 5, 1, 'Purdue', 2509, 0, 0),
(18, 1, 5, 2, 'Baylor', 239, 0, 0),
(19, 1, 5, 3, 'Indiana', 84, 0, 0),
(20, 1, 5, 4, 'Maryland', 120, 0, 0),
(21, 1, 6, 1, 'Seton Hall', 2550, 0, 0),
(22, 1, 6, 2, 'Texas', 251, 0, 0),
(23, 1, 6, 3, 'Notre Dame', 87, 0, 0),
(24, 1, 6, 4, 'Arizona', 12, 0, 0),
(25, 1, 7, 1, 'Dayton', 2168, 0, 0),
(26, 1, 7, 2, 'Oregon State', 204, 0, 0),
(27, 1, 7, 3, 'Wisconsin', 275, 0, 0),
(28, 1, 7, 4, 'Iowa', 2294, 0, 0),
(29, 1, 8, 1, 'Texas Tech', 2641, 0, 0),
(30, 1, 8, 2, 'Saint Joseph''s', 2603, 0, 0),
(31, 1, 8, 3, 'USC', 30, 0, 0),
(32, 1, 8, 4, 'Colorado', 38, 0, 0),
(33, 1, 9, 1, 'Butler', 2086, 0, 0),
(34, 1, 9, 2, 'Cincinnati', 2132, 0, 0),
(35, 1, 9, 3, 'Providence', 2507, 0, 0),
(36, 1, 9, 4, 'Connecticut', 41, 0, 0),
(37, 1, 10, 1, 'Syracuse', 183, 0, 0),
(38, 1, 10, 2, 'VCU', 2670, 0, 0),
(39, 1, 10, 3, 'Pittsburgh', 221, 0, 0),
(40, 1, 10, 4, 'Temple', 218, 0, 0),
(41, 1, 11, 1, 'Gonzaga', 2250, 0, 0),
(42, 1, 11, 2, 'Northern Iowa', 2460, 0, 0),
(43, 1, 11, 3, 'Michigan', 130, 0, 0),
(44, 1, 11, 4, 'Wichita State', 2724, 0, 0),
(45, 1, 12, 1, 'Little Rock', 2031, 0, 0),
(46, 1, 12, 2, 'Yale', 43, 0, 0),
(47, 1, 12, 3, 'Chattanooga', 236, 0, 0),
(48, 1, 12, 4, 'South Dakota State', 2571, 0, 0),
(49, 1, 13, 1, 'Iona', 314, 0, 0),
(50, 1, 13, 2, 'UNC Wilmington', 350, 0, 0),
(51, 1, 13, 3, 'Stony Brook', 2619, 0, 0),
(52, 1, 13, 4, 'Hawaii', 62, 0, 0),
(53, 1, 14, 1, 'Fresno State', 278, 0, 0),
(54, 1, 14, 2, 'Green Bay', 2739, 0, 0),
(55, 1, 14, 3, 'Stephen F. Austin SU', 2617, 0, 0),
(56, 1, 14, 4, 'Buffalo', 2084, 0, 0),
(57, 1, 15, 1, 'Middle Tennessee State', 2393, 0, 0),
(58, 1, 15, 2, 'CSU Bakersfield', 2934, 0, 0),
(59, 1, 15, 3, 'Weber State', 2692, 0, 0),
(60, 1, 15, 4, 'UNC Asheville', 2427, 0, 0),
(61, 1, 16, 1, 'Hampton', 2261, 0, 0),
(62, 1, 16, 2, 'Holy Cross', 107, 0, 0),
(63, 1, 16, 3, 'FGCU', 526, 0, 0),
(64, 1, 16, 4, 'Austin Peay', 2046, 0, 0),

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
