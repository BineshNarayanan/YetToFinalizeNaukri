-- --------------------------------------------------------
-- Host:                         10.90.18.100
-- Server version:               5.5.39 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             8.3.0.4694
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping structure for table dream.seeker
CREATE TABLE IF NOT EXISTS `seeker` (
  `Id` double NOT NULL AUTO_INCREMENT,
  `Gender` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `FirstName` varchar(100) COLLATE utf8_bin NOT NULL,
  `MiddleName` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `LastName` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `ContactNumber1` varchar(16) COLLATE utf8_bin NOT NULL,
  `ContactNumber2` varchar(16) COLLATE utf8_bin DEFAULT NULL,
  `ContactNumber3` varchar(16) COLLATE utf8_bin DEFAULT NULL,
  `DateOfBirth` date NOT NULL,
  `CreationDate` date DEFAULT NULL,
  `UpdateDate` date DEFAULT NULL,
  `IsActive` bit(1) DEFAULT NULL,
  `NoticePeriodStartDate` date DEFAULT NULL,
  `NoticePeriodEndDate` date DEFAULT NULL,
  `IsImmediateJoinee` bit(1) DEFAULT NULL,
  `IsWorkingCurrently` bit(1) DEFAULT NULL,
  `TentativeJoiningDate` date DEFAULT NULL,
  `HighestQualification` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `ProfileViewCount` int(10) unsigned DEFAULT NULL,
  `PrimaryEmail` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `SecondaryEmail` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `YearsOfExperience` int(10) unsigned DEFAULT NULL,
  `SkillSets` varchar(1000) COLLATE utf8_bin DEFAULT NULL,
  `IndustryCode` double DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- Dumping data for table dream.seeker: ~0 rows (approximately)
/*!40000 ALTER TABLE `seeker` DISABLE KEYS */;
/*!40000 ALTER TABLE `seeker` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
