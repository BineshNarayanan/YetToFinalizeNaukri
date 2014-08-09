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

-- Dumping structure for table dream.provider
CREATE TABLE IF NOT EXISTS `provider` (
  `Id` double NOT NULL AUTO_INCREMENT,
  `ProviderGroup_Id` double NOT NULL,
  `Name` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `ProviderType` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `RegistrationDate` date DEFAULT NULL,
  `CreateDate` date DEFAULT NULL,
  `UpdateDate` date DEFAULT NULL,
  `IsActive` bit(1) DEFAULT NULL,
  `PrimaryEmail` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `SecondaryEmail` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `Provider_FKIndex1` (`ProviderGroup_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- Dumping data for table dream.provider: ~0 rows (approximately)
/*!40000 ALTER TABLE `provider` DISABLE KEYS */;
/*!40000 ALTER TABLE `provider` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
