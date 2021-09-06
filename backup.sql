-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: example
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.2

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('cf6118fe0272');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `desafios`
--

DROP TABLE IF EXISTS `desafios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `desafios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombreDesafio` varchar(80) NOT NULL,
  `descripcionDesafio` varchar(250) NOT NULL,
  `feat1` varchar(120) NOT NULL,
  `feat2` varchar(120) NOT NULL,
  `feat3` varchar(120) NOT NULL,
  `photoURL` varchar(250) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `descripcionDesafio` (`descripcionDesafio`),
  UNIQUE KEY `nombreDesafio` (`nombreDesafio`),
  UNIQUE KEY `photoURL` (`photoURL`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `desafios`
--

LOCK TABLES `desafios` WRITE;
/*!40000 ALTER TABLE `desafios` DISABLE KEYS */;
INSERT INTO `desafios` VALUES (1,'Mente Sana','Utiliza este desafio para sentar las bases en llevar una vida mas sana a traves de mantener una mente sana - bajando el nivel de estres, angustia y asi ayudar a estar zen','Deliciosas recetas saludables para preparar todos los dias, apoyando una nutricion saludable.','Lista de tareas diarias para que organices tareas basicas, despejando tu mente para bajar tu estres','Rutinas de meditacion guiadas para cada dia, apoyando tu nueva mente sana y serena','https://pbs.twimg.com/media/Dow1gZDXkAExkmH.jpg'),(2,'Activación física atletas','Ya tienes algo de experiencia ejercitándote y has perdido training? Reactiva tu físico rápidamente con este desafío intenso en ejercicios y buena nutrición!','Recetas altas en proteínas y minerales necesarios para tu rendimiento','Apoyamos una sana reactivación a través de rutinas localizadas','Comienza el día con actividades que te proveerán energía por horas!','https://assets.entrepreneur.com/content/3x2/2000/20190913172915-Atleta.jpeg');
/*!40000 ALTER TABLE `desafios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dias`
--

DROP TABLE IF EXISTS `dias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numeroDia` int NOT NULL,
  `idDesafio` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idDesafio` (`idDesafio`),
  CONSTRAINT `dias_ibfk_1` FOREIGN KEY (`idDesafio`) REFERENCES `desafios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dias`
--

LOCK TABLES `dias` WRITE;
/*!40000 ALTER TABLE `dias` DISABLE KEYS */;
INSERT INTO `dias` VALUES (1,1,1),(2,2,1),(3,3,1),(4,1,2);
/*!40000 ALTER TABLE `dias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `extras`
--

DROP TABLE IF EXISTS `extras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `extras` (
  `id` int NOT NULL AUTO_INCREMENT,
  `actividad` varchar(80) NOT NULL,
  `tipo` varchar(80) NOT NULL,
  `descripcion` varchar(250) NOT NULL,
  `urlVideo` varchar(250) NOT NULL,
  `urlFoto` varchar(250) NOT NULL,
  `dia` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dia` (`dia`),
  CONSTRAINT `extras_ibfk_1` FOREIGN KEY (`dia`) REFERENCES `dias` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `extras`
--

LOCK TABLES `extras` WRITE;
/*!40000 ALTER TABLE `extras` DISABLE KEYS */;
INSERT INTO `extras` VALUES (1,'Pollo teriyaki','receta','Para la elaboración del Pollo Teriyaki, se requieren muy pocos ingredientes, para preparar la salsa Teriyaki, solamente usaremos cuatro ingredientes: salsa de soja japonesa o \"Shoyu\", Sake, Mirin y azúcar moreno.','https://www.youtube.com/embed/cYgkfQUUwWQ','https://i0.wp.com/www.kwanhomsai.com/wp-content/uploads/2016/04/Pollo-Teriyaki-Feath1.jpg?w=669',4),(2,'Salmón al horno','receta','Sencilla manera de preparar un Salmón de una manera rápida.','https://www.youtube.com/embed/hbPfSD8EY5U','https://t1.rg.ltmcdn.com/es/images/6/2/7/salmon_marinado_al_horno_70726_orig.jpg',2),(3,'Ensalada César','receta','Las ensaladas dan mucho juego a la hora de mezclar ingredientes. Con una buena base, podremos hacer que nuestra ensalada sea diferente cada día.','https://www.youtube.com/embed/LhrapnF8Phk','https://www.recetasderechupete.com/wp-content/uploads/2020/10/Ensalada-Cesar-final_.jpg',3),(4,'Meditación 1','rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/IShkpOm63gg','https://static.eldiario.es/clip/920fe2bf-4106-43ca-8ba4-4f1492c86897_16-9-aspect-ratio_default_0.jpg',1),(5,'Meditación 2','rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/inpok4MKVLM','https://greator.com/wp-content/uploads/2021/02/morgenmeditation-01-984x540.jpg',4),(6,'Meditación 3','rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/ZToicYcHIOU','https://assets.entrepreneur.com/content/3x2/2000/20180329172450-GettyImages-604619026.jpeg',3);
/*!40000 ALTER TABLE `extras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `extrasusuarios`
--

DROP TABLE IF EXISTS `extrasusuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `extrasusuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userID` int DEFAULT NULL,
  `actividad` varchar(150) DEFAULT NULL,
  `dia` int DEFAULT NULL,
  `tipo` varchar(80) DEFAULT NULL,
  `descripcion` varchar(300) DEFAULT NULL,
  `URLVideo` varchar(200) DEFAULT NULL,
  `URLFoto` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_extrasusuarios_userID` (`userID`),
  CONSTRAINT `extrasusuarios_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `extrasusuarios`
--

LOCK TABLES `extrasusuarios` WRITE;
/*!40000 ALTER TABLE `extrasusuarios` DISABLE KEYS */;
INSERT INTO `extrasusuarios` VALUES (1,1,'Pollo teriyaki',1,'receta','Para la elaboración del Pollo Teriyaki, se requieren muy pocos ingredientes, para preparar la salsa Teriyaki, solamente usaremos cuatro ingredientes: salsa de soja japonesa o \"Shoyu\", Sake, Mirin y azúcar moreno.','https://www.youtube.com/watch?v=cYgkfQUUwWQ','https://i0.wp.com/www.kwanhomsai.com/wp-content/uploads/2016/04/Pollo-Teriyaki-Feath1.jpg?w=669'),(2,1,'Meditación 1',1,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/watch?v=IShkpOm63gg','https://static.eldiario.es/clip/920fe2bf-4106-43ca-8ba4-4f1492c86897_16-9-aspect-ratio_default_0.jpg'),(3,1,'Salmón al horno',2,'receta','Sencilla manera de preparar un Salmón de una manera rápida.','https://www.youtube.com/watch?v=hbPfSD8EY5U','https://t1.rg.ltmcdn.com/es/images/6/2/7/salmon_marinado_al_horno_70726_orig.jpg'),(4,1,'Meditación 2',2,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/watch?v=IShkpOm63gg','https://greator.com/wp-content/uploads/2021/02/morgenmeditation-01-984x540.jpg'),(5,1,'Ensalada César',3,'receta','Las ensaladas dan mucho juego a la hora de mezclar ingredientes. Con una buena base, podremos hacer que nuestra ensalada sea diferente cada día.','https://www.youtube.com/watch?v=LhrapnF8Phk','https://www.recetasderechupete.com/wp-content/uploads/2020/10/Ensalada-Cesar-final_.jpg'),(6,1,'Meditación 3',3,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/watch?v=IShkpOm63gg','https://assets.entrepreneur.com/content/3x2/2000/20180329172450-GettyImages-604619026.jpeg'),(7,2,'Pollo teriyaki',1,'receta','Para la elaboración del Pollo Teriyaki, se requieren muy pocos ingredientes, para preparar la salsa Teriyaki, solamente usaremos cuatro ingredientes: salsa de soja japonesa o \"Shoyu\", Sake, Mirin y azúcar moreno.','https://www.youtube.com/watch?v=cYgkfQUUwWQ','https://i0.wp.com/www.kwanhomsai.com/wp-content/uploads/2016/04/Pollo-Teriyaki-Feath1.jpg?w=669'),(8,2,'Meditación 1',1,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/watch?v=IShkpOm63gg','https://static.eldiario.es/clip/920fe2bf-4106-43ca-8ba4-4f1492c86897_16-9-aspect-ratio_default_0.jpg'),(9,2,'Salmón al horno',2,'receta','Sencilla manera de preparar un Salmón de una manera rápida.','https://www.youtube.com/watch?v=hbPfSD8EY5U','https://t1.rg.ltmcdn.com/es/images/6/2/7/salmon_marinado_al_horno_70726_orig.jpg'),(10,2,'Meditación 2',2,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/watch?v=IShkpOm63gg','https://greator.com/wp-content/uploads/2021/02/morgenmeditation-01-984x540.jpg'),(11,2,'Ensalada César',3,'receta','Las ensaladas dan mucho juego a la hora de mezclar ingredientes. Con una buena base, podremos hacer que nuestra ensalada sea diferente cada día.','https://www.youtube.com/watch?v=LhrapnF8Phk','https://www.recetasderechupete.com/wp-content/uploads/2020/10/Ensalada-Cesar-final_.jpg'),(12,2,'Meditación 3',3,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/watch?v=IShkpOm63gg','https://assets.entrepreneur.com/content/3x2/2000/20180329172450-GettyImages-604619026.jpeg'),(13,3,'Pollo teriyaki',1,'receta','Para la elaboración del Pollo Teriyaki, se requieren muy pocos ingredientes, para preparar la salsa Teriyaki, solamente usaremos cuatro ingredientes: salsa de soja japonesa o \"Shoyu\", Sake, Mirin y azúcar moreno.','https://www.youtube.com/embed/cYgkfQUUwWQ','https://i0.wp.com/www.kwanhomsai.com/wp-content/uploads/2016/04/Pollo-Teriyaki-Feath1.jpg?w=669'),(14,3,'Meditación 1',1,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/IShkpOm63gg','https://static.eldiario.es/clip/920fe2bf-4106-43ca-8ba4-4f1492c86897_16-9-aspect-ratio_default_0.jpg'),(15,3,'Salmón al horno',2,'receta','Sencilla manera de preparar un Salmón de una manera rápida.','https://www.youtube.com/embed/hbPfSD8EY5U','https://t1.rg.ltmcdn.com/es/images/6/2/7/salmon_marinado_al_horno_70726_orig.jpg'),(16,3,'Meditación 2',2,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/IShkpOm63gg','https://greator.com/wp-content/uploads/2021/02/morgenmeditation-01-984x540.jpg'),(17,3,'Ensalada César',3,'receta','Las ensaladas dan mucho juego a la hora de mezclar ingredientes. Con una buena base, podremos hacer que nuestra ensalada sea diferente cada día.','https://www.youtube.com/embed/LhrapnF8Phk','https://www.recetasderechupete.com/wp-content/uploads/2020/10/Ensalada-Cesar-final_.jpg'),(18,3,'Meditación 3',3,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/IShkpOm63gg','https://assets.entrepreneur.com/content/3x2/2000/20180329172450-GettyImages-604619026.jpeg'),(19,4,'Pollo teriyaki',1,'receta','Para la elaboración del Pollo Teriyaki, se requieren muy pocos ingredientes, para preparar la salsa Teriyaki, solamente usaremos cuatro ingredientes: salsa de soja japonesa o \"Shoyu\", Sake, Mirin y azúcar moreno.','https://www.youtube.com/embed/cYgkfQUUwWQ','https://i0.wp.com/www.kwanhomsai.com/wp-content/uploads/2016/04/Pollo-Teriyaki-Feath1.jpg?w=669'),(20,4,'Meditación 1',1,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/IShkpOm63gg','https://static.eldiario.es/clip/920fe2bf-4106-43ca-8ba4-4f1492c86897_16-9-aspect-ratio_default_0.jpg'),(21,4,'Salmón al horno',2,'receta','Sencilla manera de preparar un Salmón de una manera rápida.','https://www.youtube.com/embed/hbPfSD8EY5U','https://t1.rg.ltmcdn.com/es/images/6/2/7/salmon_marinado_al_horno_70726_orig.jpg'),(22,4,'Meditación 2',2,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/IShkpOm63gg','https://greator.com/wp-content/uploads/2021/02/morgenmeditation-01-984x540.jpg'),(23,4,'Ensalada César',3,'receta','Las ensaladas dan mucho juego a la hora de mezclar ingredientes. Con una buena base, podremos hacer que nuestra ensalada sea diferente cada día.','https://www.youtube.com/embed/LhrapnF8Phk','https://www.recetasderechupete.com/wp-content/uploads/2020/10/Ensalada-Cesar-final_.jpg'),(24,4,'Meditación 3',3,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/IShkpOm63gg','https://assets.entrepreneur.com/content/3x2/2000/20180329172450-GettyImages-604619026.jpeg'),(25,NULL,'Pollo teriyaki',1,'receta','Para la elaboración del Pollo Teriyaki, se requieren muy pocos ingredientes, para preparar la salsa Teriyaki, solamente usaremos cuatro ingredientes: salsa de soja japonesa o \"Shoyu\", Sake, Mirin y azúcar moreno.','https://www.youtube.com/embed/cYgkfQUUwWQ','https://i0.wp.com/www.kwanhomsai.com/wp-content/uploads/2016/04/Pollo-Teriyaki-Feath1.jpg?w=669'),(26,NULL,'Meditación 1',1,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/IShkpOm63gg','https://static.eldiario.es/clip/920fe2bf-4106-43ca-8ba4-4f1492c86897_16-9-aspect-ratio_default_0.jpg'),(27,NULL,'Salmón al horno',2,'receta','Sencilla manera de preparar un Salmón de una manera rápida.','https://www.youtube.com/embed/hbPfSD8EY5U','https://t1.rg.ltmcdn.com/es/images/6/2/7/salmon_marinado_al_horno_70726_orig.jpg'),(28,NULL,'Meditación 2',2,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/IShkpOm63gg','https://greator.com/wp-content/uploads/2021/02/morgenmeditation-01-984x540.jpg'),(29,NULL,'Ensalada César',3,'receta','Las ensaladas dan mucho juego a la hora de mezclar ingredientes. Con una buena base, podremos hacer que nuestra ensalada sea diferente cada día.','https://www.youtube.com/embed/LhrapnF8Phk','https://www.recetasderechupete.com/wp-content/uploads/2020/10/Ensalada-Cesar-final_.jpg'),(30,NULL,'Meditación 3',3,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/IShkpOm63gg','https://assets.entrepreneur.com/content/3x2/2000/20180329172450-GettyImages-604619026.jpeg'),(31,6,'Pollo teriyaki',1,'receta','Para la elaboración del Pollo Teriyaki, se requieren muy pocos ingredientes, para preparar la salsa Teriyaki, solamente usaremos cuatro ingredientes: salsa de soja japonesa o \"Shoyu\", Sake, Mirin y azúcar moreno.','https://www.youtube.com/embed/cYgkfQUUwWQ','https://i0.wp.com/www.kwanhomsai.com/wp-content/uploads/2016/04/Pollo-Teriyaki-Feath1.jpg?w=669'),(32,6,'Meditación 1',1,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/IShkpOm63gg','https://static.eldiario.es/clip/920fe2bf-4106-43ca-8ba4-4f1492c86897_16-9-aspect-ratio_default_0.jpg'),(33,6,'Salmón al horno',2,'receta','Sencilla manera de preparar un Salmón de una manera rápida.','https://www.youtube.com/embed/hbPfSD8EY5U','https://t1.rg.ltmcdn.com/es/images/6/2/7/salmon_marinado_al_horno_70726_orig.jpg'),(34,6,'Meditación 2',2,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/inpok4MKVLM','https://greator.com/wp-content/uploads/2021/02/morgenmeditation-01-984x540.jpg'),(35,6,'Ensalada César',3,'receta','Las ensaladas dan mucho juego a la hora de mezclar ingredientes. Con una buena base, podremos hacer que nuestra ensalada sea diferente cada día.','https://www.youtube.com/embed/LhrapnF8Phk','https://www.recetasderechupete.com/wp-content/uploads/2020/10/Ensalada-Cesar-final_.jpg'),(36,6,'Meditación 3',3,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/ZToicYcHIOU','https://assets.entrepreneur.com/content/3x2/2000/20180329172450-GettyImages-604619026.jpeg'),(37,8,'Pollo teriyaki',1,'receta','Para la elaboración del Pollo Teriyaki, se requieren muy pocos ingredientes, para preparar la salsa Teriyaki, solamente usaremos cuatro ingredientes: salsa de soja japonesa o \"Shoyu\", Sake, Mirin y azúcar moreno.','https://www.youtube.com/embed/cYgkfQUUwWQ','https://i0.wp.com/www.kwanhomsai.com/wp-content/uploads/2016/04/Pollo-Teriyaki-Feath1.jpg?w=669'),(38,8,'Meditación 1',1,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/IShkpOm63gg','https://static.eldiario.es/clip/920fe2bf-4106-43ca-8ba4-4f1492c86897_16-9-aspect-ratio_default_0.jpg'),(39,8,'Salmón al horno',2,'receta','Sencilla manera de preparar un Salmón de una manera rápida.','https://www.youtube.com/embed/hbPfSD8EY5U','https://t1.rg.ltmcdn.com/es/images/6/2/7/salmon_marinado_al_horno_70726_orig.jpg'),(40,8,'Meditación 2',2,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/inpok4MKVLM','https://greator.com/wp-content/uploads/2021/02/morgenmeditation-01-984x540.jpg'),(41,8,'Ensalada César',3,'receta','Las ensaladas dan mucho juego a la hora de mezclar ingredientes. Con una buena base, podremos hacer que nuestra ensalada sea diferente cada día.','https://www.youtube.com/embed/LhrapnF8Phk','https://www.recetasderechupete.com/wp-content/uploads/2020/10/Ensalada-Cesar-final_.jpg'),(42,8,'Meditación 3',3,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/ZToicYcHIOU','https://assets.entrepreneur.com/content/3x2/2000/20180329172450-GettyImages-604619026.jpeg'),(43,7,'Pollo teriyaki',1,'receta','Para la elaboración del Pollo Teriyaki, se requieren muy pocos ingredientes, para preparar la salsa Teriyaki, solamente usaremos cuatro ingredientes: salsa de soja japonesa o \"Shoyu\", Sake, Mirin y azúcar moreno.','https://www.youtube.com/embed/cYgkfQUUwWQ','https://i0.wp.com/www.kwanhomsai.com/wp-content/uploads/2016/04/Pollo-Teriyaki-Feath1.jpg?w=669'),(44,7,'Meditación 1',1,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/IShkpOm63gg','https://static.eldiario.es/clip/920fe2bf-4106-43ca-8ba4-4f1492c86897_16-9-aspect-ratio_default_0.jpg'),(45,7,'Salmón al horno',2,'receta','Sencilla manera de preparar un Salmón de una manera rápida.','https://www.youtube.com/embed/hbPfSD8EY5U','https://t1.rg.ltmcdn.com/es/images/6/2/7/salmon_marinado_al_horno_70726_orig.jpg'),(46,7,'Meditación 2',2,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/inpok4MKVLM','https://greator.com/wp-content/uploads/2021/02/morgenmeditation-01-984x540.jpg'),(47,7,'Ensalada César',3,'receta','Las ensaladas dan mucho juego a la hora de mezclar ingredientes. Con una buena base, podremos hacer que nuestra ensalada sea diferente cada día.','https://www.youtube.com/embed/LhrapnF8Phk','https://www.recetasderechupete.com/wp-content/uploads/2020/10/Ensalada-Cesar-final_.jpg'),(48,7,'Meditación 3',3,'rutina','Una meditación guiada para principiantes.','https://www.youtube.com/embed/ZToicYcHIOU','https://assets.entrepreneur.com/content/3x2/2000/20180329172450-GettyImages-604619026.jpeg');
/*!40000 ALTER TABLE `extrasusuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `templatetodo`
--

DROP TABLE IF EXISTS `templatetodo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `templatetodo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `idDia` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idDia` (`idDia`),
  CONSTRAINT `templatetodo_ibfk_1` FOREIGN KEY (`idDia`) REFERENCES `dias` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `templatetodo`
--

LOCK TABLES `templatetodo` WRITE;
/*!40000 ALTER TABLE `templatetodo` DISABLE KEYS */;
INSERT INTO `templatetodo` VALUES (1,'Organizar trabajo del dia',4),(2,'Hacer la cama y organizar el escritorio',1),(3,'Agendar espacios libres',2),(5,'No revisar social media',2),(6,'Leer un libro por 30 minutos',2),(7,'Escribir metas del dia',4),(8,'Hacer la cama y organizar habitacion',3);
/*!40000 ALTER TABLE `templatetodo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `todousuario`
--

DROP TABLE IF EXISTS `todousuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `todousuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userID` int DEFAULT NULL,
  `actividad` varchar(150) DEFAULT NULL,
  `dia` int DEFAULT NULL,
  `done` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userID` (`userID`),
  CONSTRAINT `todousuario_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `todousuario`
--

LOCK TABLES `todousuario` WRITE;
/*!40000 ALTER TABLE `todousuario` DISABLE KEYS */;
INSERT INTO `todousuario` VALUES (1,1,'Organizar trabajo del dia',1,0),(2,1,'Hacer la cama y organizar el escritorio',1,0),(3,1,'Agendar espacios libres',2,0),(4,1,'Agendar espacios libres',2,0),(5,1,'No revisar social media',2,0),(6,1,'Leer un libro por 30 minutos',2,0),(7,1,'Escribir metas del dia',3,0),(8,1,'Hacer la cama y organizar habitacion',3,0),(9,2,'Organizar trabajo del dia',1,1),(10,2,'Hacer la cama y organizar el escritorio',1,0),(11,2,'Agendar espacios libres',2,0),(12,2,'No revisar social media',2,0),(13,2,'Leer un libro por 30 minutos',2,0),(14,2,'Escribir metas del dia',3,0),(15,2,'Hacer la cama y organizar habitacion',3,0),(16,3,'Organizar trabajo del dia',1,0),(17,3,'Hacer la cama y organizar el escritorio',1,0),(18,3,'Agendar espacios libres',2,0),(19,3,'No revisar social media',2,0),(20,3,'Leer un libro por 30 minutos',2,0),(21,3,'Escribir metas del dia',3,0),(22,3,'Hacer la cama y organizar habitacion',3,0),(23,4,'Organizar trabajo del dia',1,0),(24,4,'Hacer la cama y organizar el escritorio',1,0),(25,4,'Agendar espacios libres',2,0),(26,4,'No revisar social media',2,0),(27,4,'Leer un libro por 30 minutos',2,0),(28,4,'Escribir metas del dia',3,0),(29,4,'Hacer la cama y organizar habitacion',3,0),(30,NULL,'Organizar trabajo del dia',1,0),(31,NULL,'Hacer la cama y organizar el escritorio',1,0),(32,NULL,'Agendar espacios libres',2,0),(33,NULL,'No revisar social media',2,0),(34,NULL,'Leer un libro por 30 minutos',2,0),(35,NULL,'Escribir metas del dia',3,0),(36,NULL,'Hacer la cama y organizar habitacion',3,0),(37,6,'Organizar trabajo del dia',1,1),(38,6,'Hacer la cama y organizar el escritorio',1,1),(39,6,'Agendar espacios libres',2,0),(40,6,'No revisar social media',2,0),(41,6,'Leer un libro por 30 minutos',2,0),(42,6,'Escribir metas del dia',3,0),(43,6,'Hacer la cama y organizar habitacion',3,0),(44,8,'Organizar trabajo del dia',1,1),(45,8,'Hacer la cama y organizar el escritorio',1,1),(46,8,'Agendar espacios libres',2,0),(47,8,'No revisar social media',2,0),(48,8,'Leer un libro por 30 minutos',2,0),(49,8,'Escribir metas del dia',3,0),(50,8,'Hacer la cama y organizar habitacion',3,0),(51,7,'Organizar trabajo del dia',1,0),(52,7,'Hacer la cama y organizar el escritorio',1,0),(53,7,'Agendar espacios libres',2,0),(54,7,'No revisar social media',2,0),(55,7,'Leer un libro por 30 minutos',2,0),(56,7,'Escribir metas del dia',3,0),(57,7,'Hacer la cama y organizar habitacion',3,0),(58,1,'a',1,1),(59,1,'a',2,0),(60,1,'b',1,0),(61,3,'e',1,0),(62,3,'h',1,0),(63,3,'HOLI',1,1),(64,1,'asd',1,1),(65,1,'HOLI',1,1);
/*!40000 ALTER TABLE `todousuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(80) NOT NULL,
  `password` varchar(9000) NOT NULL,
  `nombre` varchar(80) NOT NULL,
  `desafio` varchar(80) DEFAULT NULL,
  `duracion` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'a','sha256$lSHMeqr0mE0zV1kK$396e60aef2b62ebcb3db7f1eb759f852a374743bb178d28f5110b70298357c38','a','Mente Sana',3),(2,'b','sha256$JH140fwmJdbO307G$04c9d9adf4ad3260f71cf334522b0cb3313ea423f504b9899ca33ecf88c281e0','b','Mente Sana',3),(3,'c','sha256$8PKwgb5WRyJVkv1R$8bfdfc985165f09d3ca15ac8eb61224ab163805af9966881f79d03d92c1848f3','c','Mente Sana',3),(4,'apolo@gmail.com','sha256$RMtSa9q0ARvJS9ar$ca831270974977d3d9a0b011890750f87543c7af8f523deb9c603765420455e5','Apolo','Mente Sana',3),(6,'adaschuler@gmail.com','sha256$xbXODMLhMCqCdIhC$38c2afb11464ce2b1c28b2b84d25e9b0ef9d14fc0feecb00fc70ff5691b0cac8','Ada','Mente Sana',3),(7,'life.planner.web@gmail.com','sha256$nP23QjlRqD06PHgC$5a1205b991fd24f9e8f0f7ba6fab6836cd8cecc57cd0ea00fb4fea6d8cb2f900','Life Planner','Mente Sana',3),(8,'apolo.pino@gmail.com','sha256$Nq412xvzj5qnUnox$75eba0dbd8b305fae01ca8dbe428d0b67cb0c67be155866abdb7dc681a2d1a35','Apolo','Mente Sana',3),(9,'y','sha256$oGw7XXdwCorXHN64$16b6914e09cf4c503a8c9d21289c1d379c8a4b93434d1ce9476c330aa40e87aa','y',NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-06  0:05:56
