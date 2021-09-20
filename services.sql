-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 20, 2021 at 05:25 PM
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
-- Database: `services`
--

-- --------------------------------------------------------

--
-- Table structure for table `attachmenttranscript`
--

DROP TABLE IF EXISTS `attachmenttranscript`;
CREATE TABLE IF NOT EXISTS `attachmenttranscript` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  `postDate` datetime(6) DEFAULT NULL,
  `content_type` varchar(500) NOT NULL,
  `name` varchar(5000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attachmenttranscript`
--

INSERT INTO `attachmenttranscript` (`id`, `file`, `postDate`, `content_type`, `name`) VALUES
(1, 'docs/listing/Münster,_LVM,_Bürogebäude_--_2013_--_5149-51.jpg', '2021-06-02 13:25:41.631613', 'image/jpeg', 'k05d6-4cc2-8715-957ebff115d1.jpeg'),
(2, 'docs/listing/635435339228902500.jpg', '2021-06-02 13:25:41.631613', 'image/jpeg', 't05d6-4cc2-8715-957ebff115d1.jpeg'),
(3, 'docs/listing/635435339228902500.jpg', '2021-06-02 13:25:41.631613', 'image/jpeg', 'aw05d6-4cc2-8715-957ebff115d1.jpeg'),
(4, 'docs/listing/application-occupation-profession-job-seeker-concept.jpg', '2021-06-02 13:25:41.631613', 'image/jpeg', 'e05d6-4cc2-8715-957ebff115d1.jpeg'),
(5, 'docs/listing/encyclopedia-ما-هي-فوائد-التكنولوجيا.jpg', '2021-06-02 13:25:41.631613', 'image/jpeg', 'a05d6-4cc2-8715-957ebff115d1.jpeg'),
(6, 'docs/listing/man-with-magnifying-glass-train-station.jpg', '2021-06-02 13:25:41.631613', 'image/jpeg', 'e16840fb-05d6-4cc2-8715-957ebff115d1.jpeg'),
(7, 'docs/listing/encyclopedia-ما-هي-فوائد-التكنولوجيا.jpg', '2021-06-02 13:25:41.631613', 'image/jpeg', 'h05d6-4cc2-8715-957ebff115d1.jpeg'),
(8, 'docs/listing/1.jpg', '2021-06-02 13:25:41.631613', 'image/jpeg', 'k05d6-4cc2-8715-957ebff115d1.jpeg'),
(9, 'docs/listing/man-with-magnifying-glass-train-station.jpg', '2021-06-02 13:25:41.631613', 'image/jpeg', 'm05d6-4cc2-8715-957ebff115d1.jpeg'),
(10, 'docs/listing/aerial-background-beverage-blog-blogger-browsing-1447929-pxhere.com.jpg', '2021-06-02 13:25:41.631613', 'image/jpeg', 'i05d6-4cc2-8715-957ebff115d1.jpeg'),
(11, 'docs/listing/application-occupation-profession-job-seeker-concept.jpg', '2021-06-02 13:25:41.631613', 'image/jpeg', 'o05d6-4cc2-8715-957ebff115d1.jpeg'),
(20, 'files_to_upload/c099e44b67f64502af22f3919eaac293.jpg', '2021-09-15 22:43:29.784898', 'image/jpeg', 'diverse-friends-using-digital-devices.jpg'),
(19, 'files_to_upload/44d5eda9a89449c3b50f5962fe3020fb.jpg', '2021-09-15 22:43:29.768927', 'image/jpeg', 'application-occupation-profession-job-seeker-concept.jpg'),
(18, 'files_to_upload/e85268b8bd064752b8a7cf35142dae66.jpg', '2021-09-15 22:43:29.752790', 'image/jpeg', 'aerial-background-beverage-blog-blogger-browsing-1447929-pxhere.jpg'),
(17, 'files_to_upload/5633b060d61c417aa3bb0d7143c0c4fb.jpg', '2021-09-15 22:43:29.734754', 'image/jpeg', '635435339228902500.jpg'),
(16, 'files_to_upload/4947a0a5d6de4e7cb05cbfde06752eb1.jpg', '2021-09-15 22:34:37.319490', 'image/jpeg', 'Münster,_LVM,_Bürogebäude_--_2013_--_5149-51.jpg'),
(21, 'files_to_upload/4df6a47e26f941cca5a4b2cd57cd3b38.png', '2021-09-15 22:43:29.796479', 'image/png', 'Logo 2.png');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
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
) ENGINE=MyISAM AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
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
(25, 'Can add permission general', 7, 'add_permissiongeneral'),
(26, 'Can change permission general', 7, 'change_permissiongeneral'),
(27, 'Can delete permission general', 7, 'delete_permissiongeneral'),
(28, 'Can view permission general', 7, 'view_permissiongeneral'),
(29, 'Can add role', 8, 'add_role'),
(30, 'Can change role', 8, 'change_role'),
(31, 'Can delete role', 8, 'delete_role'),
(32, 'Can view role', 8, 'view_role'),
(33, 'Can add profile', 9, 'add_profile'),
(34, 'Can change profile', 9, 'change_profile'),
(35, 'Can delete profile', 9, 'delete_profile'),
(36, 'Can view profile', 9, 'view_profile'),
(37, 'Can add category', 10, 'add_category'),
(38, 'Can change category', 10, 'change_category'),
(39, 'Can delete category', 10, 'delete_category'),
(40, 'Can view category', 10, 'view_category'),
(41, 'Can add attachment transcript', 11, 'add_attachmenttranscript'),
(42, 'Can change attachment transcript', 11, 'change_attachmenttranscript'),
(43, 'Can delete attachment transcript', 11, 'delete_attachmenttranscript'),
(44, 'Can view attachment transcript', 11, 'view_attachmenttranscript'),
(45, 'Can add the add', 12, 'add_theadd'),
(46, 'Can change the add', 12, 'change_theadd'),
(47, 'Can delete the add', 12, 'delete_theadd'),
(48, 'Can view the add', 12, 'view_theadd'),
(49, 'Can add tag', 13, 'add_tag'),
(50, 'Can change tag', 13, 'change_tag'),
(51, 'Can delete tag', 13, 'delete_tag'),
(52, 'Can view tag', 13, 'view_tag'),
(53, 'Can add reply', 14, 'add_reply'),
(54, 'Can change reply', 14, 'change_reply'),
(55, 'Can delete reply', 14, 'delete_reply'),
(56, 'Can view reply', 14, 'view_reply'),
(57, 'Can add comment', 15, 'add_comment'),
(58, 'Can change comment', 15, 'change_comment'),
(59, 'Can delete comment', 15, 'delete_comment'),
(60, 'Can view comment', 15, 'view_comment'),
(61, 'Can add rate from person', 16, 'add_ratefromperson'),
(62, 'Can change rate from person', 16, 'change_ratefromperson'),
(63, 'Can delete rate from person', 16, 'delete_ratefromperson'),
(64, 'Can view rate from person', 16, 'view_ratefromperson'),
(65, 'Can add city', 17, 'add_city'),
(66, 'Can change city', 17, 'change_city'),
(67, 'Can delete city', 17, 'delete_city'),
(68, 'Can view city', 17, 'view_city'),
(69, 'Can add region', 18, 'add_region'),
(70, 'Can change region', 18, 'change_region'),
(71, 'Can delete region', 18, 'delete_region'),
(72, 'Can view region', 18, 'view_region');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$120000$TVeactooPqaw$dzDnoQAFE/me53I/3Bqc9LzVyYt6vgAK9kzSCcROxPg=', '2021-09-15 20:32:30.030706', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2021-08-20 09:17:45.390426'),
(2, 'pbkdf2_sha256$120000$TVeactooPqaw$dzDnoQAFE/me53I/3Bqc9LzVyYt6vgAK9kzSCcROxPg=', NULL, 0, 'babilgames', 'بابل جيمس', '', 'papel@gmail.com', 0, 1, '2021-08-20 09:17:45.390426'),
(32, 'pbkdf2_sha256$120000$wVWrHEXI1P5F$fck9AQQlZNrSX3Xrshmy3tHs5K77JLcMFcDmcRDKWoM=', '2021-09-06 22:50:12.476986', 0, 'proctoring', 'Proctoring S', '', 'ahmedsonic1993@gmail.co', 0, 1, '2021-09-06 22:50:12.334986'),
(33, 'pbkdf2_sha256$120000$jCMsi8IODBZj$F4o5Mlz7nqV+jzZjmljuKUnn8Q+2Yw3rPn9YiP7ooUw=', '2021-09-14 13:36:58.092229', 0, 'kamel', 'kamel alsayed', '', 'ahmed@gmail.com', 0, 1, '2021-09-14 13:36:57.584844'),
(27, 'pbkdf2_sha256$120000$hroBokCiqAdN$Z+246oDmtF6CgUv51qKZTmj/OgSE/651qa7f6lweQhs=', '2021-09-14 13:52:18.747737', 0, 'AhmedDakrory_fromfacebook', 'Ahmed Dakrory', 'Dakrory', 'ahmedsonic1993@gmail.com', 0, 1, '2021-09-03 18:46:15.151010'),
(28, 'pbkdf2_sha256$120000$ScY4dic22hAg$mZKT0GX3EUYwbQlJe9dgA6Au58mir6REDCFhtUeNQ4w=', '2021-09-03 18:46:44.285165', 0, 'ahmeddakrory_fromgmail', 'ahmed', 'dakrory', 'ahmedeldakrori@gmail.com', 0, 1, '2021-09-03 18:46:43.795426'),
(29, 'pbkdf2_sha256$120000$WjrPHq9HL22I$RuVYpKanye7+JNa3S0mnJ+taXsreKa0aVzVTjZw39jE=', '2021-09-03 18:46:59.051951', 0, 'AhmedMohamedEldakrory_fromgmail', 'Ahmed Mohamed ', 'Eldakrory', 'aaldakrory@zewailcity.edu.eg', 0, 1, '2021-09-03 18:46:58.625484');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
CREATE TABLE IF NOT EXISTS `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `isFirstHead` tinyint(1) NOT NULL,
  `details` varchar(500) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `parentCategory` int(11) DEFAULT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `name`, `isFirstHead`, `details`, `image`, `parentCategory`, `created`, `updated`, `deleted`) VALUES
(1, 'خدمات طبية', 1, NULL, '/media/attachments/allImages/aerial-background-beverage-blog-blogger-browsing-1447929-pxhere.com.jpg', NULL, NULL, 0, 0),
(2, 'خدمات تعليمية', 1, NULL, '/media/attachments/allImages/1.jpg', NULL, NULL, 0, 0),
(3, 'تكنولوجيا', 1, NULL, '/media/attachments/allImages/encyclopedia-ما-هي-فوائد-التكنولوجيا.jpg', NULL, NULL, 0, 0),
(4, 'انشاءات ومقاولات', 1, NULL, '/media/attachments/allImages/application-occupation-profession-job-seeker-concept.jpg', NULL, NULL, 0, 0),
(5, 'صيانة', 1, NULL, '/media/attachments/allImages/Untitled-1-01.png', NULL, NULL, 0, 0),
(6, 'محاسبة ومالية', 1, NULL, '/media/attachments/allImages/635435339228902500.jpg', NULL, NULL, 0, 0),
(7, 'خياطة', 1, NULL, '/media/attachments/allImages/encyclopedia-ما-هي-فوائد-التكنولوجيا.jpg', NULL, NULL, 0, 0),
(8, 'سياحة', 1, NULL, '/media/attachments/allImages/application-occupation-profession-job-seeker-concept.jpg', NULL, NULL, 0, 0),
(18, 'صيدلة', 0, NULL, '/media/attachments/allImages/application-occupation-profession-job-seeker-concept.jpg', 1, NULL, 0, 0),
(19, 'طب', 0, NULL, '/media/attachments/allImages/encyclopedia-ما-هي-فوائد-التكنولوجيا.jpg', 1, NULL, 0, 0),
(20, 'علاج طبيعى', 0, NULL, '/media/attachments/allImages/encyclopedia-ما-هي-فوائد-التكنولوجيا.jpg', 1, NULL, 0, 0),
(21, 'تطوير حاسب', 0, NULL, '/media/attachments/allImages/application-occupation-profession-job-seeker-concept.jpg', 3, NULL, 0, 0),
(22, 'ذكاء صناعى', 0, NULL, '/media/attachments/allImages/application-occupation-profession-job-seeker-concept.jpg', 3, NULL, 0, 0),
(23, 'برمجة', 0, NULL, '/media/attachments/allImages/application-occupation-profession-job-seeker-concept.jpg', 3, NULL, 0, 0),
(24, 'روبوتات', 0, NULL, '/media/attachments/allImages/application-occupation-profession-job-seeker-concept.jpg', 3, NULL, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
CREATE TABLE IF NOT EXISTS `city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`id`, `name`, `created`, `updated`, `deleted`) VALUES
(1, 'عمان الغربية', NULL, 0, 0),
(2, 'أربد', NULL, 0, 0),
(3, 'جرش', NULL, 0, 0),
(4, 'معان', NULL, 0, 0),
(5, 'الطفيلة', NULL, 0, 0),
(6, 'العقبة', NULL, 0, 0),
(7, 'عمان الشرقية', NULL, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
CREATE TABLE IF NOT EXISTS `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `details` longtext NOT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `fromUser_id` int(11) NOT NULL,
  `rate` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `comment_fromUser_id_bc2ba429` (`fromUser_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `comment`
--

INSERT INTO `comment` (`id`, `details`, `created`, `updated`, `deleted`, `fromUser_id`, `rate`) VALUES
(1, 'هذه الخدمة رائعة', '2021-09-03 18:46:58.986069', 0, 0, 4, 1.7),
(2, 'لا يوجد بها جديد', '2021-09-03 18:46:58.986069', 0, 0, 23, 2),
(3, 'هذه الخدمة رائعة وغير مستحدثة', '2021-09-03 18:46:58.986069', 0, 0, 10, 5),
(4, 'هذا شئ جديد\r\n', '2021-09-07 15:07:01.816105', 0, 0, 11, 4),
(5, 'هذا شئ جديد\r\n', '2021-09-07 15:07:33.383419', 0, 0, 11, 4);

-- --------------------------------------------------------

--
-- Table structure for table `comment_replies`
--

DROP TABLE IF EXISTS `comment_replies`;
CREATE TABLE IF NOT EXISTS `comment_replies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_id` int(11) NOT NULL,
  `reply_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `comment_replies_comment_id_reply_id_e7895d4d_uniq` (`comment_id`,`reply_id`),
  KEY `comment_replies_comment_id_758ed1cd` (`comment_id`),
  KEY `comment_replies_reply_id_39fe14f9` (`reply_id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `comment_replies`
--

INSERT INTO `comment_replies` (`id`, `comment_id`, `reply_id`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 1, 4),
(5, 2, 5),
(6, 3, 6),
(7, 1, 7),
(8, 2, 8),
(9, 3, 9),
(10, 1, 10),
(11, 2, 11),
(12, 3, 12),
(13, 1, 13),
(14, 2, 14),
(15, 3, 15),
(16, 1, 16),
(17, 2, 17),
(18, 1, 18),
(19, 1, 19),
(20, 1, 20),
(21, 1, 21),
(22, 1, 22),
(23, 1, 23),
(24, 3, 24),
(25, 5, 25);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'mainApp', 'permissiongeneral'),
(8, 'mainApp', 'role'),
(9, 'mainApp', 'profile'),
(10, 'mainApp', 'category'),
(11, 'mainApp', 'attachmenttranscript'),
(12, 'mainApp', 'theadd'),
(13, 'mainApp', 'tag'),
(14, 'mainApp', 'reply'),
(15, 'mainApp', 'comment'),
(16, 'mainApp', 'ratefromperson'),
(17, 'mainApp', 'city'),
(18, 'mainApp', 'region');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-08-18 09:10:46.042028'),
(2, 'auth', '0001_initial', '2021-08-18 09:10:46.271885'),
(3, 'admin', '0001_initial', '2021-08-18 09:10:46.325480'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-08-18 09:10:46.332633'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-08-18 09:10:46.337579'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-08-18 09:10:46.366987'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-08-18 09:10:46.379096'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-08-18 09:10:46.393384'),
(9, 'auth', '0004_alter_user_username_opts', '2021-08-18 09:10:46.399841'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-08-18 09:10:46.413805'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-08-18 09:10:46.415769'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-08-18 09:10:46.422782'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-08-18 09:10:46.444898'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-08-18 09:10:46.459239'),
(15, 'mainApp', '0001_initial', '2021-08-18 09:10:46.572545'),
(16, 'sessions', '0001_initial', '2021-08-18 09:10:46.590075'),
(17, 'mainApp', '0002_category', '2021-08-20 07:33:40.311857'),
(18, 'mainApp', '0003_remove_category_user', '2021-08-20 07:41:38.468658'),
(19, 'mainApp', '0004_attachmenttranscript_theadd', '2021-08-20 09:05:14.080950'),
(20, 'mainApp', '0005_theadd_mainimage', '2021-08-20 09:33:56.671317'),
(21, 'mainApp', '0006_theadd_averagerate', '2021-08-30 16:45:46.160551'),
(22, 'mainApp', '0007_auto_20210831_0622', '2021-08-31 04:22:10.712910'),
(23, 'mainApp', '0008_auto_20210831_0622', '2021-08-31 04:23:02.014857'),
(24, 'mainApp', '0009_auto_20210902_1453', '2021-09-02 12:53:43.653476'),
(25, 'mainApp', '0010_profile_typeofregisteration', '2021-09-03 18:40:14.662600'),
(26, 'mainApp', '0011_remove_profile_typeofregisteration', '2021-09-03 18:42:20.259325'),
(27, 'mainApp', '0012_profile_typeofregisteration', '2021-09-03 18:43:06.965045'),
(28, 'mainApp', '0013_auto_20210907_1337', '2021-09-07 11:37:33.613036'),
(29, 'mainApp', '0014_auto_20210907_1438', '2021-09-07 12:38:45.943072'),
(30, 'mainApp', '0015_comment_rateadd', '2021-09-07 12:50:27.320361'),
(31, 'mainApp', '0016_auto_20210907_1649', '2021-09-07 14:49:38.789010'),
(32, 'mainApp', '0017_auto_20210907_1655', '2021-09-07 14:56:00.027788'),
(33, 'mainApp', '0018_auto_20210907_2051', '2021-09-07 18:51:36.354234'),
(34, 'mainApp', '0019_theadd_videourl', '2021-09-08 20:44:56.122020'),
(35, 'mainApp', '0020_theadd_featureaddnumber', '2021-09-08 21:30:36.914317'),
(36, 'mainApp', '0021_auto_20210909_0118', '2021-09-08 23:18:06.376617'),
(37, 'mainApp', '0022_auto_20210912_2102', '2021-09-12 19:02:56.717672'),
(38, 'mainApp', '0023_auto_20210912_2103', '2021-09-12 19:03:15.808937'),
(39, 'mainApp', '0024_auto_20210912_2103', '2021-09-12 19:03:27.537274');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5giwklr1m9x7vadka05agrm1ggq002t2', 'ZjgzMmU3OTViMzgzNDdjNDBjNTZiZjQ0MzI5Y2EwMmUwZjY5MWQzMDp7Il9hdXRoX3VzZXJfaWQiOiIyNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjMxNzdlMzg0YzhkY2E3YmQ5MWVmNmMwMmM5MDI5YWFhY2ZmNjRkOCJ9', '2021-09-17 18:59:19.284295'),
('t0wr9dapga3mty04fk67rgrmyg3fbxfg', 'YTdiMjU4ZjJmODc5YjJhZjgwZjFiOWYzNTk0ZjNiYjk0N2JlYzc5Mjp7fQ==', '2021-09-20 22:41:06.100983'),
('z7vrj6yp5hui0ne45zn1hmn1trx3vtft', 'ZTUwMDBhMWJjN2FkZmNlZjU0ZmY1MDQwOGFhNThiYWYyODc1M2RhYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNDNhYjIxYjk2MjQ0ZDE4ZjBlMGRiZGNmNTVlZGU3NWNiNmFiNzA4In0=', '2021-09-29 20:32:30.032705');

-- --------------------------------------------------------

--
-- Table structure for table `permissiongeneral`
--

DROP TABLE IF EXISTS `permissiongeneral`;
CREATE TABLE IF NOT EXISTS `permissiongeneral` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

DROP TABLE IF EXISTS `profile`;
CREATE TABLE IF NOT EXISTS `profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(500) DEFAULT NULL,
  `phone` varchar(500) DEFAULT NULL,
  `mobile` varchar(500) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `role_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `typeOfRegisteration` varchar(500),
  `aboutMe` longtext DEFAULT NULL,
  `region_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `profile_role_id_9bb7f33b` (`role_id`),
  KEY `profile_user_id_2aeb6f6b` (`user_id`),
  KEY `profile_region_id_bbe54288` (`region_id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `profile`
--

INSERT INTO `profile` (`id`, `address`, `phone`, `mobile`, `image`, `created`, `updated`, `deleted`, `role_id`, `user_id`, `typeOfRegisteration`, `aboutMe`, `region_id`) VALUES
(1, 'عمان - الاردن', '96264711177', '96264711177', 'attachments/userData/encyclopedia-ما-هي-فوائد-التكنولوجيا.jpg', NULL, 0, 0, 1, 1, 'Normal', 'شركة برمجيات للخدمات التطوير والتطوير المهنى', 1),
(2, 'Amman', ' ', ' ', NULL, NULL, 0, 0, 2, 2, 'Normal', 'المبرمج السريري - المعروف أيضًا باسم مسئول الترميز السريري ، أو المبرمج التشخيصي ، أو المبرمج الطبي - هو متخصص في المعلومات الصحية تتمثل مهماته الرئيسية في تحليل البيانات السريرية وتعيين رموز قياسية باستخدام نظام التصنيف.', 2),
(4, NULL, NULL, NULL, 'attachments/userData/518d9011-0ce7-11ec-b8ec-405bd84eb990jpg', '2021-09-03 18:46:58.986069', 0, 0, 2, 29, 'Gmail', 'شركة مقاولات عامة وخدمات الانشاءات', 3),
(23, '200 S Callaghan Rd', '2104344999', '', 'attachments/userData/temp.jpg', '2021-09-06 22:50:12.408985', 0, 0, 2, 32, '0', 'اهلا بكم في موقع دائرة مراقبة الشركات ... الصناعة والتجارة بموجب أحكام قانون الشركات المعدل رقم (22) لسنة 1997 وتعديلاته، ... نبذة عن دائرة مراقبة الشركات.', 4),
(10, NULL, NULL, NULL, 'attachments/userData/48b795b3-0ce7-11ec-b9cc-405bd84eb990jpg', '2021-09-03 18:46:44.217513', 0, 0, 2, 28, 'Gmail', 'تعمل شركة الأردن الدولية للاستثمار في القطاع العقاري مع التركيز على الأنشطة العقارية المتنوعة. لديها فروع تعمل في جميع أنحاء الأردن', 5),
(11, '1 omda st from fasel talbya', '01061690939', '4078840993', 'attachments/userData/37a4d86c-0ce7-11ec-8f85-405bd84eb990jpg', '2021-09-03 18:46:15.603280', 0, 0, 2, 27, 'Facebook', 'شركة ادوية', 6),
(24, '1 omda st from fasel talbya', '01061690939', '', '', '2021-09-14 13:36:58.016025', 0, 0, 2, 33, '0', NULL, 12);

-- --------------------------------------------------------

--
-- Table structure for table `profile_tags`
--

DROP TABLE IF EXISTS `profile_tags`;
CREATE TABLE IF NOT EXISTS `profile_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profile_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `profile_tags_profile_id_tag_id_af222fac_uniq` (`profile_id`,`tag_id`),
  KEY `profile_tags_profile_id_96b21275` (`profile_id`),
  KEY `profile_tags_tag_id_d3c2dab2` (`tag_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `profile_tags`
--

INSERT INTO `profile_tags` (`id`, `profile_id`, `tag_id`) VALUES
(1, 2, 1),
(2, 2, 2),
(3, 2, 3),
(4, 2, 4),
(5, 2, 5),
(6, 2, 6),
(7, 2, 7),
(8, 23, 8),
(9, 23, 9),
(10, 1, 10);

-- --------------------------------------------------------

--
-- Table structure for table `region`
--

DROP TABLE IF EXISTS `region`;
CREATE TABLE IF NOT EXISTS `region` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `cityOfRegion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `region_cityOfRegion_id_13c7baf4` (`cityOfRegion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `region`
--

INSERT INTO `region` (`id`, `name`, `created`, `updated`, `deleted`, `cityOfRegion_id`) VALUES
(1, 'خلدا', NULL, 0, 0, 1),
(2, 'عبدون', NULL, 0, 0, 1),
(3, 'الجاردنز', NULL, 0, 0, 1),
(4, 'الجبيهة', NULL, 0, 0, 1),
(5, 'دابق', NULL, 0, 0, 1),
(6, 'القصيلة', NULL, 0, 0, 2),
(7, 'الحصن', NULL, 0, 0, 2),
(8, 'وسط البلد', NULL, 0, 0, 7),
(9, 'سحاب', NULL, 0, 0, 7),
(10, 'جبل النصر', NULL, 0, 0, 7),
(11, 'رغدان', NULL, 0, 0, 7),
(12, 'وسط البلد', NULL, 0, 0, 3),
(13, 'وسط البلد', NULL, 0, 0, 4),
(14, 'وسط البلد', NULL, 0, 0, 5),
(15, 'وسط البلد', NULL, 0, 0, 6);

-- --------------------------------------------------------

--
-- Table structure for table `reply`
--

DROP TABLE IF EXISTS `reply`;
CREATE TABLE IF NOT EXISTS `reply` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `details` longtext NOT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `fromUser_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reply_fromUser_id_5e822937` (`fromUser_id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reply`
--

INSERT INTO `reply` (`id`, `details`, `created`, `updated`, `deleted`, `fromUser_id`) VALUES
(1, 'هل يمكنك ذكر المشكلة معك', '2021-09-03 18:46:15.603280', 0, 0, 10),
(2, 'برجاء ذكر ', '2021-09-03 18:46:15.603280', 0, 0, 11),
(3, 'لا يوجد ما هو مستحدث', '2021-09-03 18:46:15.603280', 0, 0, 23),
(4, 'هل يمكنك ذكر المشكلة معك', '2021-09-03 18:46:15.603280', 0, 0, 10),
(5, 'هل يمكنك ذكر المشكلة معك', '2021-09-03 18:46:15.603280', 0, 0, 4),
(6, 'هل يمكنك ذكر المشكلة معك', '2021-09-03 18:46:15.603280', 0, 0, 2),
(7, 'هل يمكنك ذكر المشكلة معك', '2021-09-03 18:46:15.603280', 0, 0, 10),
(8, 'هل يمكنك ذكر المشكلة معك', '2021-09-03 18:46:15.603280', 0, 0, 4),
(9, 'هل يمكنك ذكر المشكلة معك', '2021-09-03 18:46:15.603280', 0, 0, 10),
(10, 'برجاء ذكر ', '2021-09-03 18:46:15.603280', 0, 0, 11),
(11, 'لا يوجد ما هو مستحدث', '2021-09-03 18:46:15.603280', 0, 0, 23),
(12, 'هل يمكنك ذكر المشكلة معك', '2021-09-03 18:46:15.603280', 0, 0, 10),
(13, 'هل يمكنك ذكر المشكلة معك', '2021-09-03 18:46:15.603280', 0, 0, 4),
(14, 'هل يمكنك ذكر المشكلة معك', '2021-09-03 18:46:15.603280', 0, 0, 2),
(15, 'هل يمكنك ذكر المشكلة معك', '2021-09-03 18:46:15.603280', 0, 0, 10),
(16, 'هل يمكنك ذكر المشكلة معك', '2021-09-03 18:46:15.603280', 0, 0, 4),
(17, 'تمام', '2021-09-03 18:46:15.603280', 0, 0, 11),
(18, 'برجاء', '2021-09-07 14:30:54.192317', 0, 0, 11),
(19, 'برجاء', '2021-09-07 14:31:28.272595', 0, 0, 11),
(20, 'شكرا', '2021-09-07 14:32:36.659750', 0, 0, 11),
(21, 'as', '2021-09-07 14:33:08.406748', 0, 0, 11),
(22, 'ahmed', '2021-09-07 14:34:51.922798', 0, 0, 11),
(23, 'hi', '2021-09-07 14:34:57.254454', 0, 0, 11),
(24, 'المشكلة ان الموضوع غير واضح', '2021-09-07 14:35:46.948390', 0, 0, 11),
(25, 'برجاء مراجعة اختيارك', '2021-09-07 15:07:49.018562', 0, 0, 11);

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
CREATE TABLE IF NOT EXISTS `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`id`, `name`, `created`, `updated`, `deleted`) VALUES
(1, 'admin', NULL, 0, 0),
(2, 'normal user', NULL, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `role_permissiongeneral`
--

DROP TABLE IF EXISTS `role_permissiongeneral`;
CREATE TABLE IF NOT EXISTS `role_permissiongeneral` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `permissiongeneral_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `role_permissiongeneral_role_id_permissiongenera_d087f167_uniq` (`role_id`,`permissiongeneral_id`),
  KEY `role_permissiongeneral_role_id_53c18e55` (`role_id`),
  KEY `role_permissiongeneral_permissiongeneral_id_77da5856` (`permissiongeneral_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
CREATE TABLE IF NOT EXISTS `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) DEFAULT NULL,
  `propertyType` int(11) DEFAULT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tag`
--

INSERT INTO `tag` (`id`, `name`, `propertyType`, `created`, `updated`, `deleted`) VALUES
(1, 'ريادة أعمال', 0, '2021-09-03 18:46:58.986069', 0, 0),
(2, 'نصايح عامة', 0, '2021-09-03 18:46:58.986069', 0, 0),
(3, 'ارشادات', 0, '2021-09-03 18:46:58.986069', 0, 0),
(4, 'هندسة', 0, '2021-09-03 18:46:58.986069', 0, 0),
(5, 'برمجة', 0, '2021-09-03 18:46:58.986069', 0, 0),
(6, 'تطوير', 0, '2021-09-03 18:46:58.986069', 0, 0),
(7, 'تصميم', 0, '2021-09-03 18:46:58.986069', 0, 0),
(8, 'فن', 0, '2021-09-03 18:46:58.986069', 0, 0),
(9, 'رسوم', 0, '2021-09-03 18:46:58.986069', 0, 0),
(10, 'محمد', 0, '2021-09-15 23:28:52.889741', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `theadd`
--

DROP TABLE IF EXISTS `theadd`;
CREATE TABLE IF NOT EXISTS `theadd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `details` longtext NOT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `category_id` int(11) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `mainImage` varchar(100) DEFAULT NULL,
  `videoUrl` longtext DEFAULT NULL,
  `featureAddNumber` int(11),
  PRIMARY KEY (`id`),
  KEY `theAdd_category_id_a4186a95` (`category_id`),
  KEY `theAdd_owner_id_572a20cb` (`owner_id`)
) ENGINE=MyISAM AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `theadd`
--

INSERT INTO `theadd` (`id`, `name`, `details`, `created`, `updated`, `deleted`, `category_id`, `owner_id`, `mainImage`, `videoUrl`, `featureAddNumber`) VALUES
(1, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 5, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', 'https://www.youtube.com/embed/watch?v=Lex4NKotiw4&list=RDLex4NKotiw4&start_radio=1', 1),
(3, '123', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 5, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', 'https://www.youtube.com/embed/watch?v=Lex4NKotiw4&list=RDLex4NKotiw4&start_radio=1', 0),
(5, '345', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 2, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', 'https://www.youtube.com/embed/watch?v=Lex4NKotiw4&list=RDLex4NKotiw4&start_radio=1', 0),
(7, '778', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 4, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', 'https://www.youtube.com/embed/watch?v=Lex4NKotiw4&list=RDLex4NKotiw4&start_radio=1', 0),
(9, 'trgrg', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 6, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', 'https://www.youtube.com/embed/watch?v=Lex4NKotiw4&list=RDLex4NKotiw4&start_radio=1', 0),
(11, 'rgt', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 4, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', 'https://www.youtube.com/embed/watch?v=Lex4NKotiw4&list=RDLex4NKotiw4&start_radio=1', 0),
(13, 'rtg', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 3, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 1),
(15, '45t', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 2, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(17, '54', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 2, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(19, 'th', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 4, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(21, '5t', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 1, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(23, 'rh', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 5, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(25, 'rth', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 1, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(27, 'th', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 3, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(28, '4', '(68 منتج)محسنات غذائية ومواد اولية للخبز2(اوستريا سبونج شكولاته(الملكة)- بكالدرين شكولاته مكس- سويس', NULL, 0, 0, 4, 11, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(29, '45', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 1, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(31, '34', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 4, 4, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(32, '34', '(68 منتج)محسنات غذائية ومواد اولية للخبز2(اوستريا سبونج شكولاته(الملكة)- بكالدرين شكولاته مكس- سويس', NULL, 0, 0, 5, 10, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(33, 'erg', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 6, 11, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(34, 'dfg', '(68 منتج)محسنات غذائية ومواد اولية للخبز2(اوستريا سبونج شكولاته(الملكة)- بكالدرين شكولاته مكس- سويس', NULL, 0, 0, 3, 10, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(35, 'drg', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 4, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(36, 'v', '(68 منتج)محسنات غذائية ومواد اولية للخبز2(اوستريا سبونج شكولاته(الملكة)- بكالدرين شكولاته مكس- سويس', NULL, 0, 0, 1, 10, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(37, 'rdg', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 3, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(38, '45g', '(68 منتج)محسنات غذائية ومواد اولية للخبز2(اوستريا سبونج شكولاته(الملكة)- بكالدرين شكولاته مكس- سويس', NULL, 0, 0, 5, 10, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(39, '45g', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 5, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(41, 'fdb', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 3, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(42, 'b', '(68 منتج)محسنات غذائية ومواد اولية للخبز2(اوستريا سبونج شكولاته(الملكة)- بكالدرين شكولاته مكس- سويس', NULL, 0, 0, 2, 10, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(43, '4tg45g', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 1, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(45, '45g', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 5, 11, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(47, 'g54', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 5, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(48, '4545g4g', '(68 منتج)محسنات غذائية ومواد اولية للخبز2(اوستريا سبونج شكولاته(الملكة)- بكالدرين شكولاته مكس- سويس', NULL, 0, 0, 6, 11, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(49, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 2, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(50, '45', '(68 منتج)محسنات غذائية ومواد اولية للخبز2(اوستريا سبونج شكولاته(الملكة)- بكالدرين شكولاته مكس- سويس', NULL, 0, 0, 3, 11, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(53, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 4, 4, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(55, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 2, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(57, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 5, 4, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(59, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 1, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(60, 'مواد غذائية', '(68 منتج)محسنات غذائية ومواد اولية للخبز2(اوستريا سبونج شكولاته(الملكة)- بكالدرين شكولاته مكس- سويس', NULL, 0, 0, 2, 4, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(61, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 3, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(63, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 5, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(64, 'مواد غذائية', '(68 منتج)محسنات غذائية ومواد اولية للخبز2(اوستريا سبونج شكولاته(الملكة)- بكالدرين شكولاته مكس- سويس', NULL, 0, 0, 1, 4, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(65, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 3, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(67, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 5, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(68, 'مواد غذائية', '(68 منتج)محسنات غذائية ومواد اولية للخبز2(اوستريا سبونج شكولاته(الملكة)- بكالدرين شكولاته مكس- سويس', NULL, 0, 0, 2, 4, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(69, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 3, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(71, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 5, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(73, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 3, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(74, 'مواد غذائية', '(68 منتج)محسنات غذائية ومواد اولية للخبز2(اوستريا سبونج شكولاته(الملكة)- بكالدرين شكولاته مكس- سويس', NULL, 0, 0, 4, 4, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(75, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 2, 10, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(76, 'مواد غذائية', '(68 منتج)محسنات غذائية ومواد اولية للخبز2(اوستريا سبونج شكولاته(الملكة)- بكالدرين شكولاته مكس- سويس', NULL, 0, 0, 2, 11, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(77, 'Game Publisher', 'Besides publishing international mobile games, WE HAVE FUN!', NULL, 0, 0, 5, 2, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(78, 'مواد غذائية', '(68 منتج)محسنات غذائية ومواد اولية للخبز2(اوستريا سبونج شكولاته(الملكة)- بكالدرين شكولاته مكس- سويس', NULL, 0, 0, 2, 4, '/attachments/mainImage/application-occupation-profession-job-seeker-concept.jpg', NULL, 0),
(80, 'خدمة مضافة', 'خدمة رجال الأعمال\r\n', '2021-09-15 20:54:47.112599', 0, 0, 22, 1, 'attachments/mainImage/diverse-friends-using-digital-devices_VaA7jAd.jpg', 'https://www.youtube.com/embed/watch?v=Lex4NKotiw4&list=RDLex4NKotiw4&start_radio=1', 0);

-- --------------------------------------------------------

--
-- Table structure for table `theadd_comments`
--

DROP TABLE IF EXISTS `theadd_comments`;
CREATE TABLE IF NOT EXISTS `theadd_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `theadd_id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `theAdd_comments_theadd_id_comment_id_29f45c45_uniq` (`theadd_id`,`comment_id`),
  KEY `theAdd_comments_theadd_id_f7955e98` (`theadd_id`),
  KEY `theAdd_comments_comment_id_91bf1acc` (`comment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `theadd_comments`
--

INSERT INTO `theadd_comments` (`id`, `theadd_id`, `comment_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 5);

-- --------------------------------------------------------

--
-- Table structure for table `theadd_images`
--

DROP TABLE IF EXISTS `theadd_images`;
CREATE TABLE IF NOT EXISTS `theadd_images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `theadd_id` int(11) NOT NULL,
  `attachmenttranscript_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `theAdd_images_theadd_id_attachmenttranscript_id_4fe19079_uniq` (`theadd_id`,`attachmenttranscript_id`),
  KEY `theAdd_images_theadd_id_3d132563` (`theadd_id`),
  KEY `theAdd_images_attachmenttranscript_id_2376a422` (`attachmenttranscript_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `theadd_images`
--

INSERT INTO `theadd_images` (`id`, `theadd_id`, `attachmenttranscript_id`) VALUES
(1, 1, 1),
(22, 80, 21),
(3, 1, 10),
(4, 1, 9),
(5, 1, 8),
(6, 1, 7),
(7, 1, 6),
(8, 2, 5),
(9, 2, 4),
(10, 2, 3),
(11, 2, 2),
(12, 2, 1),
(21, 80, 20),
(20, 80, 19),
(19, 80, 18),
(18, 80, 17),
(17, 80, 16);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
