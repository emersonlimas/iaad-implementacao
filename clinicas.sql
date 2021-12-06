-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 02-Dez-2021 às 17:51
-- Versão do servidor: 5.7.36
-- versão do PHP: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `clinicas`
--

DELIMITER $$
--
-- Procedimentos
--
DROP PROCEDURE IF EXISTS `excluir_agenda`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `excluir_agenda` ()  BEGIN
DELETE FROM app_agendaconsulta;
END$$

DROP PROCEDURE IF EXISTS `excluir_clinicas`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `excluir_clinicas` ()  BEGIN
DELETE FROM app_clinica;
END$$

DROP PROCEDURE IF EXISTS `excluir_espec`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `excluir_espec` ()  BEGIN
DELETE FROM app_especialidade;
END$$

DROP PROCEDURE IF EXISTS `excluir_med`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `excluir_med` ()  BEGIN
DELETE FROM app_medico;
END$$

DROP PROCEDURE IF EXISTS `excluir_pac`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `excluir_pac` ()  BEGIN
DELETE FROM app_paciente;
END$$

CREATE TRIGGER after_med_insert
AFTER INSERT
ON app_medico FOR EACH ROW
BEGIN
    IF NEW.NomeMed IS NULL THEN
        INSERT INTO app_medico(NomeMed)
        VALUES(new.id,CONCAT('Campo Vazio'));
    END IF;
END$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `app_agendaconsulta`
--

DROP TABLE IF EXISTS `app_agendaconsulta`;
CREATE TABLE IF NOT EXISTS `app_agendaconsulta` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `CodCli` varchar(3) NOT NULL,
  `CodMed` varchar(4) NOT NULL,
  `CpfPaciente` varchar(11) NOT NULL,
  `Data` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `app_agendaconsulta`
--

INSERT INTO `app_agendaconsulta` (`id`, `CodCli`, `CodMed`, `CpfPaciente`, `Data`) VALUES
(6, '100', '1007', '10310310303', '2021-12-15');

-- --------------------------------------------------------

--
-- Estrutura da tabela `app_clinica`
--

DROP TABLE IF EXISTS `app_clinica`;
CREATE TABLE IF NOT EXISTS `app_clinica` (
  `CodCli` varchar(3) NOT NULL,
  `NomeCli` varchar(130) NOT NULL,
  `Endereco` varchar(130) NOT NULL,
  `Telefone` varchar(11) NOT NULL,
  `Email` varchar(130) NOT NULL,
  PRIMARY KEY (`CodCli`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `app_clinica`
--

INSERT INTO `app_clinica` (`CodCli`, `NomeCli`, `Endereco`, `Telefone`, `Email`) VALUES
('100', 'Clinica de Petrolina', 'Rua Madalena, 505, Petrolina, PE', '87922222222', 'clinicadepetrolina@atendimento.com');

-- --------------------------------------------------------

--
-- Estrutura da tabela `app_clinicamedico`
--

DROP TABLE IF EXISTS `app_clinicamedico`;
CREATE TABLE IF NOT EXISTS `app_clinicamedico` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `CodCli` varchar(3) NOT NULL,
  `CodMed` varchar(4) NOT NULL,
  `DataIngresso` date NOT NULL,
  `CargaHorariaSemanal` varchar(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `app_clinicamedico`
--

INSERT INTO `app_clinicamedico` (`id`, `CodCli`, `CodMed`, `DataIngresso`, `CargaHorariaSemanal`) VALUES
(2, '100', '1007', '2014-08-10', '45');

-- --------------------------------------------------------

--
-- Estrutura da tabela `app_especialidade`
--

DROP TABLE IF EXISTS `app_especialidade`;
CREATE TABLE IF NOT EXISTS `app_especialidade` (
  `CodEspec` varchar(2) NOT NULL,
  `NomeEspec` varchar(130) NOT NULL,
  `Descricao` varchar(130) NOT NULL,
  PRIMARY KEY (`CodEspec`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `app_especialidade`
--

INSERT INTO `app_especialidade` (`CodEspec`, `NomeEspec`, `Descricao`) VALUES
('10', 'Pediatria', 'MEDICOS(AS) PEDIATRAS');

-- --------------------------------------------------------

--
-- Estrutura da tabela `app_medico`
--

DROP TABLE IF EXISTS `app_medico`;
CREATE TABLE IF NOT EXISTS `app_medico` (
  `CodMed` varchar(4) NOT NULL,
  `NomeMed` varchar(130),
  `Genero` varchar(1) NOT NULL,
  `Telefone` varchar(11) NOT NULL,
  `Email` varchar(130) NOT NULL,
  `CodEspec` varchar(2) NOT NULL,
  PRIMARY KEY (`CodMed`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `app_medico`
--

INSERT INTO `app_medico` (`CodMed`, `NomeMed`, `Genero`, `Telefone`, `Email`, `CodEspec`) VALUES
('1007', 'Andre Silva Ramalho', 'M', '87977777777', 'andresr@medico.com', '10');

-- --------------------------------------------------------

--
-- Estrutura da tabela `app_paciente`
--

DROP TABLE IF EXISTS `app_paciente`;
CREATE TABLE IF NOT EXISTS `app_paciente` (
  `CpfPaciente` varchar(11) NOT NULL,
  `NomePac` varchar(130) NOT NULL,
  `DataNascimento` date NOT NULL,
  `Genero` varchar(1) NOT NULL,
  `Telefone` varchar(11) NOT NULL,
  `Email` varchar(130) NOT NULL,
  PRIMARY KEY (`CpfPaciente`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `app_paciente`
--

INSERT INTO `app_paciente` (`CpfPaciente`, `NomePac`, `DataNascimento`, `Genero`, `Telefone`, `Email`) VALUES
('10310310303', 'Thiago Orlando Diaz', '2000-01-03', 'M', '87965656565', 'thiago@paciente.com');

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add agendaconsulta', 7, 'add_agendaconsulta'),
(26, 'Can change agendaconsulta', 7, 'change_agendaconsulta'),
(27, 'Can delete agendaconsulta', 7, 'delete_agendaconsulta'),
(28, 'Can view agendaconsulta', 7, 'view_agendaconsulta'),
(29, 'Can add clinica', 8, 'add_clinica'),
(30, 'Can change clinica', 8, 'change_clinica'),
(31, 'Can delete clinica', 8, 'delete_clinica'),
(32, 'Can view clinica', 8, 'view_clinica'),
(33, 'Can add clinicamedico', 9, 'add_clinicamedico'),
(34, 'Can change clinicamedico', 9, 'change_clinicamedico'),
(35, 'Can delete clinicamedico', 9, 'delete_clinicamedico'),
(36, 'Can view clinicamedico', 9, 'view_clinicamedico'),
(37, 'Can add especialidade', 10, 'add_especialidade'),
(38, 'Can change especialidade', 10, 'change_especialidade'),
(39, 'Can delete especialidade', 10, 'delete_especialidade'),
(40, 'Can view especialidade', 10, 'view_especialidade'),
(41, 'Can add medico', 11, 'add_medico'),
(42, 'Can change medico', 11, 'change_medico'),
(43, 'Can delete medico', 11, 'delete_medico'),
(44, 'Can view medico', 11, 'view_medico'),
(45, 'Can add paciente', 12, 'add_paciente'),
(46, 'Can change paciente', 12, 'change_paciente'),
(47, 'Can delete paciente', 12, 'delete_paciente'),
(48, 'Can view paciente', 12, 'view_paciente');

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'app', 'agendaconsulta'),
(8, 'app', 'clinica'),
(9, 'app', 'clinicamedico'),
(10, 'app', 'especialidade'),
(11, 'app', 'medico'),
(12, 'app', 'paciente');

-- --------------------------------------------------------

--
-- Estrutura da tabela `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-11-30 18:57:10.954216'),
(2, 'auth', '0001_initial', '2021-11-30 18:57:12.407334'),
(3, 'admin', '0001_initial', '2021-11-30 18:57:12.741274'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-11-30 18:57:12.758266'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-11-30 18:57:12.771203'),
(6, 'app', '0001_initial', '2021-11-30 18:57:13.163668'),
(7, 'contenttypes', '0002_remove_content_type_name', '2021-11-30 18:57:13.309692'),
(8, 'auth', '0002_alter_permission_name_max_length', '2021-11-30 18:57:13.379535'),
(9, 'auth', '0003_alter_user_email_max_length', '2021-11-30 18:57:13.446234'),
(10, 'auth', '0004_alter_user_username_opts', '2021-11-30 18:57:13.459237'),
(11, 'auth', '0005_alter_user_last_login_null', '2021-11-30 18:57:13.535758'),
(12, 'auth', '0006_require_contenttypes_0002', '2021-11-30 18:57:13.548677'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2021-11-30 18:57:13.564643'),
(14, 'auth', '0008_alter_user_username_max_length', '2021-11-30 18:57:13.639110'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2021-11-30 18:57:13.707755'),
(16, 'auth', '0010_alter_group_name_max_length', '2021-11-30 18:57:13.777978'),
(17, 'auth', '0011_update_proxy_permissions', '2021-11-30 18:57:13.799906'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2021-11-30 18:57:13.859314'),
(19, 'sessions', '0001_initial', '2021-11-30 18:57:14.034428');

-- --------------------------------------------------------

--
-- Estrutura da tabela `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
COMMIT;

-- STORED PROCEDURES --
DELIMITER $$
CREATE PROCEDURE excluir_clinicas ()
BEGIN
DELETE FROM app_clinica;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE excluir_espec ()
BEGIN
DELETE FROM app_especialidade;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE excluir_climed ()
BEGIN
DELETE FROM app_clinicamedico;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE excluir_med ()
BEGIN
DELETE FROM app_medico;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE excluir_pac ()
BEGIN
DELETE FROM app_paciente;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE excluir_agenda ()
BEGIN
DELETE FROM app_agendaconsulta;
END $$
DELIMITER ;

-- FIM DOS STOREDS PROCEDURES --

-- CRIAÇÃO DO TRIGGER --

DELIMITER $$
CREATE TRIGGER before_med_insert BEFORE INSERT
on app_medico FOR EACH ROW
BEGIN
    DECLARE CodMed INT;
select count(*) INTO CodMed 
from app_medico
where app_medico.CodMed = new.CodMed;

IF CodMed>0 
    THEN SET NEW.CodMed = CodMed * 2 ;
    END IF;
END$$
DELIMITER ;

-- FIM DO STORED PROCEDURES --

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
