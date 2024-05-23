-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: sms
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `Username` varchar(20) NOT NULL,
  `Password` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('User1',1234),('User2',5678),('User',5678);
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal_details`
--

DROP TABLE IF EXISTS `personal_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal_details` (
  `Emp_Code` varchar(5) NOT NULL,
  `Emp_Name` varchar(30) NOT NULL,
  `DOB` varchar(15) DEFAULT NULL,
  `ACC_No` varchar(10) NOT NULL,
  `Phone_No` bigint NOT NULL,
  `Gender` varchar(1) NOT NULL,
  `Age` int DEFAULT NULL,
  PRIMARY KEY (`Emp_Code`),
  UNIQUE KEY `ACC_No` (`ACC_No`),
  UNIQUE KEY `Phone_No` (`Phone_No`),
  CONSTRAINT `personal_details_chk_1` CHECK ((`Age` <= 58))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_details`
--

LOCK TABLES `personal_details` WRITE;
/*!40000 ALTER TABLE `personal_details` DISABLE KEYS */;
INSERT INTO `personal_details` VALUES ('T1','R.Shaila','1945-04-01','ICICI33551',9876543210,'F',47),('T10','K.Sathya Bhama','1972-08-12','ICICI33561',9876543219,'F',50),('T11','V.Chitra','1980-05-21','ICICI33562',9876543220,'F',42),('T15','K.Manoharan','1967-12-12','ICICI33565',9876543225,'M',55),('T16','G.Usha','1970-08-06','ICICI33566',987654326,'F',52),('T17','B.Shiyamala','1980-04-09','ICICI33567',9876543227,'F',42),('T18','S.Sujatha','1969-06-18','ICICI33568',9876543228,'F',53),('T19','N.Kamala','1974-09-09','ICICI33569',9876543229,'F',48),('T2','G.Sreedana','1945-05-01','ICICI33552',9876543211,'F',45),('T20','N.Jayanthi','1982-02-06','ICICI33570',9876543230,'F',40),('T21','S.Sudha','1985-01-01','ICICI33571',9876543231,'F',37),('T22','G.N.Yogananda','1980-10-10','ICICI33572',9876543232,'M',42),('T23','G.Shobha','1970-12-01','ICICI33573',9876543233,'F',52),('T24','S.Nanthini','1971-12-02','ICICI33574',9876543234,'F',51),('T25','B.Venkatesh','1966-12-03','ICICI33575',9876543235,'M',56),('T26','P.Renuka Devi','1969-12-04','ICICI33576',9876543236,'F',53),('T27','M.Sellan','1970-12-05','ICICI33577',9876543237,'M',52),('T28','K.Vijaya','1975-08-08','ICICI33578',9876543238,'F',47),('T29','J.Sindhuja','1980-11-23','ICICI33579',9876543239,'F',42),('T3','R.S.Ravi kumar','1945-06-01','ICICI33553',9876543212,'M',47),('T30','B.Gunapriya','1982-12-09','ICICI33580',9876543240,'F',40),('T32','K.Srevidya','1972-10-20','ICICI33582',9876543242,'F',50),('T33','Jennevie Sharma','1970-05-01','ICICI33583',9876543243,'F',52),('T34','M.Thenmozhi','1975-08-10','ICICI33584',9876543244,'F',47),('T35','S.Bindumurali','1972-08-13','ICICI33789',9876543245,'F',50),('T36','A.Bhuvaneswari','1980-07-19','ICICI33586',9876543246,'F',42),('T37','N.Jayashree','1980-10-02','ICICI33587',9876543247,'F',42),('T38','G.Bharani Shree','1967-12-18','ICICI33588',9876543248,'F',55),('T39','B.Kavitha','1981-03-27','ICICI33589',9876543249,'F',41),('T4','C.Hari Priya','1980-05-21','ICICI33554',9876543213,'F',42),('T40','K.Sujatha','1973-12-08','ICICI33590',9876543250,'F',49),('T41','P.Sangeetha','1988-08-08','ICICI33591',9876543251,'F',34),('T42','P.Santhi','1975-08-05','ICICI33592',9876543252,'F',47),('T43','M.Sharmila','1985-05-08','ICICI33593',9876543253,'F',37),('T44','P.Shanmugapriya','1985-06-08','ICICI33594',987654354,'F',37),('T45','E.Susithra','1980-06-09','ICICI33595',9876543255,'F',42),('T46','S.Vijaya','1965-09-09','ICICI33596',9876543256,'F',57),('T47','G.Rajathi','1976-05-25','ICICI33597',9876543257,'F',46),('T48','P.Chitra','1979-08-12','ICICI33598',9876543258,'F',43),('T49','G.Thiyagaraju','1974-02-06','ICICI33599',9876543259,'M',48),('T50','Y.Sheela','1980-06-09','ICICI33600',9876543260,'F',42),('T6','S.Cauvery','1975-02-08','ICICI33556',9876543215,'F',47),('T7','A.K.Shobitha','1977-06-15','ICICI33557',9876543216,'F',45),('T8','R.Sasikala','1973-05-19','ICICI33558',9876543217,'F',49),('T9','S.Radha','1982-12-09','ICICI33559',9876543218,'F',40);
/*!40000 ALTER TABLE `personal_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `s_d`
--

DROP TABLE IF EXISTS `s_d`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `s_d` (
  `Emp_Code` varchar(5) NOT NULL,
  `DOJ` varchar(15) NOT NULL,
  `DEPT` varchar(10) NOT NULL,
  `salary` int DEFAULT NULL,
  `Experience` int NOT NULL,
  `Qualification` varchar(50) NOT NULL,
  `Designation` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `s_d`
--

LOCK TABLES `s_d` WRITE;
/*!40000 ALTER TABLE `s_d` DISABLE KEYS */;
INSERT INTO `s_d` VALUES ('T1','2012-05-16','ADMIN',60202,10,'M.Sc.,M.A.,M.Phil.','PRINCIPAL'),('T10','2010-08-12','ENGLISH',38202,12,'M.A.,M.Phil.,B.Ed.','SGT'),('T11','1999-02-12','Biology',40202,23,'Msc,.M.A','SGT'),('T12','1987-04-05','English',12202,35,'M.A.','SGT'),('T13','6464','6464',64644,-4442,'45456','54564'),('T14','564564','545564',56454,-3623,'5464','65465'),('T2','2000-09-12','ADMIN',70202,22,'M.A.,B.Ed.','VP'),('T3','2008-09-25','PHYSICS',55202,14,'B.Sc.,B.Ed.','VP'),('T4','2010-06-13','BIOLOGY',45202,12,'M.A.,M.Sc.,B.Ed.','VP'),('T5','2012-08-06','SPORTS',50202,10,'M.A.,B.A.,H.P.Ed.,NIS','VP'),('T6','1998-12-01','TAMIL',65202,24,'M.A.,M.Phil.,B.Ed.','SGT'),('T7','2015-09-12','ENGLISH',40202,7,'B.Sc.,B.Ed.','SGT'),('T8','2013-08-18','SCIENCE',43202,9,'M.A.,B.Ed.','PGT'),('T9','2009-03-30','ECONOMICS',62602,13,'M.Sc.,B.Ed.','SGT');
/*!40000 ALTER TABLE `s_d` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_detail`
--

DROP TABLE IF EXISTS `staff_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_detail` (
  `Emp_Code` varchar(5) NOT NULL,
  `DOJ` varchar(15) NOT NULL,
  `DEPT` varchar(10) NOT NULL,
  `salary` int DEFAULT NULL,
  `Experience` int NOT NULL,
  `Qualification` varchar(50) NOT NULL,
  `Designation` varchar(10) NOT NULL,
  KEY `Emp_Code` (`Emp_Code`),
  CONSTRAINT `staff_detail_ibfk_1` FOREIGN KEY (`Emp_Code`) REFERENCES `personal_details` (`Emp_Code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_detail`
--

LOCK TABLES `staff_detail` WRITE;
/*!40000 ALTER TABLE `staff_detail` DISABLE KEYS */;
INSERT INTO `staff_detail` VALUES ('T1','2012-05-16','Computer',60202,15,'M.Sc.,M.A.,M.Phil.','PRINCIPAL'),('T10','2010-08-12','ENGLISH',38202,12,'M.A.,M.Phil.,B.Ed.','SGT'),('T11','1999-02-12','Biology',40202,23,'Msc,.M.A','SGT'),('T2','2000-09-12','ADMIN',70202,22,'M.A.,B.Ed.','VP'),('T3','2008-09-25','PHYSICS',55202,14,'B.Sc.,B.Ed.','VP'),('T4','2010-06-13','BIOLOGY',45202,12,'M.A.,M.Sc.,B.Ed.','VP'),('T6','1998-12-01','TAMIL',65202,24,'M.A.,M.Phil.,B.Ed.','SGT'),('T7','2015-09-12','ENGLISH',40202,7,'B.Sc.,B.Ed.','SGT'),('T8','2013-08-18','SCIENCE',43202,9,'M.A.,B.Ed.','PGT'),('T9','2009-03-30','ECONOMICS',62602,13,'M.Sc.,B.Ed.','SGT');
/*!40000 ALTER TABLE `staff_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_details`
--

DROP TABLE IF EXISTS `staff_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_details` (
  `Emp_Code` varchar(5) NOT NULL,
  `DOJ` varchar(15) NOT NULL,
  `DEPT` varchar(10) NOT NULL,
  `salary` int DEFAULT NULL,
  `Experience` int NOT NULL,
  `Qualification` varchar(50) NOT NULL,
  `Designation` varchar(10) NOT NULL,
  UNIQUE KEY `Emp_Code` (`Emp_Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_details`
--

LOCK TABLES `staff_details` WRITE;
/*!40000 ALTER TABLE `staff_details` DISABLE KEYS */;
INSERT INTO `staff_details` VALUES ('T1','2012-05-16','ADMIN',60202,10,'M.Sc.,M.A.,M.Phil.','PRINCIPAL'),('T10','2010-08-12','ENGLISH',38202,12,'M.A.,M.Phil.,B.Ed.','SGT'),('T11','1999-02-12','Biology',40202,23,'Msc,.M.A','SGT'),('T12','1987-04-05','English',12202,35,'M.A.','SGT'),('T13','6464','6464',64644,-4442,'45456','54564'),('T14','564564','545564',56454,-3623,'5464','65465'),('T2','2000-09-12','ADMIN',70202,22,'M.A.,B.Ed.','VP'),('T3','2008-09-25','PHYSICS',55202,14,'B.Sc.,B.Ed.','VP'),('T4','2010-06-13','BIOLOGY',45202,12,'M.A.,M.Sc.,B.Ed.','VP'),('T5','2012-08-06','SPORTS',50202,10,'M.A.,B.A.,H.P.Ed.,NIS','VP'),('T6','1998-12-01','TAMIL',65202,24,'M.A.,M.Phil.,B.Ed.','SGT'),('T7','2015-09-12','ENGLISH',40202,7,'B.Sc.,B.Ed.','SGT'),('T8','2013-08-18','SCIENCE',43202,9,'M.A.,B.Ed.','PGT'),('T9','2009-03-30','ECONOMICS',62602,13,'M.Sc.,B.Ed.','SGT');
/*!40000 ALTER TABLE `staff_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-29 11:50:28
