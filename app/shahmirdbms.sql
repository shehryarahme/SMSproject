-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 22, 2024 at 06:18 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shahmirdbms`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetAllStudents` ()   BEGIN
    SELECT * FROM students;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `user_name`, `password`) VALUES
(2, 'admin1', 'admin1');

-- --------------------------------------------------------

--
-- Table structure for table `assessment`
--

CREATE TABLE `assessment` (
  `id` int(11) NOT NULL,
  `marks_id` int(11) NOT NULL,
  `assessment_type` varchar(50) NOT NULL,
  `marks` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `assessment`
--

INSERT INTO `assessment` (`id`, `marks_id`, `assessment_type`, `marks`) VALUES
(1, 1, 'Quiz', 5),
(2, 2, 'Quiz', 5),
(3, 3, 'Quiz', 3),
(4, 4, 'Quiz', 2),
(5, 5, 'Quiz', 3),
(6, 6, 'Quiz', 3),
(7, 7, 'Quiz', 2),
(8, 8, 'Midterm', 30),
(9, 9, 'Midterm', 15),
(10, 10, 'Midterm', 23),
(11, 11, 'Midterm', 23),
(12, 12, 'Midterm', 2),
(13, 13, 'Midterm', 3),
(14, 14, 'Midterm', 12),
(15, 15, 'Final', 44),
(16, 16, 'Final', 34),
(17, 17, 'Final', 23),
(18, 18, 'Final', 34),
(19, 19, 'Final', 22),
(20, 20, 'Final', 33),
(21, 21, 'Final', 12),
(22, 22, 'Final', 50),
(23, 23, 'Final', 45),
(24, 24, 'Final', 50),
(25, 25, 'Final', 23),
(26, 26, 'Final', 50);

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `sem_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `student_sno` int(11) NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`id`, `sem_id`, `course_id`, `student_sno`, `date`, `status`) VALUES
(1, 1, 3, 87, '2024-11-25 19:00:00', 'Absent'),
(2, 1, 3, 901, '2024-11-25 19:00:00', 'Present'),
(3, 1, 3, 902, '2024-11-25 19:00:00', 'Present'),
(4, 1, 3, 903, '2024-11-25 19:00:00', 'Present'),
(5, 1, 3, 904, '2024-11-25 19:00:00', 'Present'),
(6, 1, 3, 905, '2024-11-25 19:00:00', 'Present'),
(7, 1, 3, 906, '2024-11-25 19:00:00', 'Present'),
(8, 1, 3, 87, '2024-11-10 19:00:00', 'Present'),
(9, 1, 3, 901, '2024-11-10 19:00:00', 'Absent'),
(10, 1, 3, 902, '2024-11-10 19:00:00', 'Present'),
(11, 1, 3, 903, '2024-11-10 19:00:00', 'Present'),
(12, 1, 3, 904, '2024-11-10 19:00:00', 'Present'),
(13, 1, 3, 905, '2024-11-10 19:00:00', 'Present'),
(14, 1, 3, 906, '2024-11-10 19:00:00', 'Present'),
(15, 1, 3, 87, '2024-11-11 19:00:00', 'Present'),
(16, 1, 3, 901, '2024-11-11 19:00:00', 'Present'),
(17, 1, 3, 902, '2024-11-11 19:00:00', 'Present'),
(18, 1, 3, 903, '2024-11-11 19:00:00', 'Absent'),
(19, 1, 3, 904, '2024-11-11 19:00:00', 'Present'),
(20, 1, 3, 905, '2024-11-11 19:00:00', 'Present'),
(21, 1, 3, 906, '2024-11-11 19:00:00', 'Present');

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `C_id` int(11) NOT NULL,
  `CourseName` varchar(50) NOT NULL,
  `crdHours` int(11) NOT NULL,
  `CourseCode` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`C_id`, `CourseName`, `crdHours`, `CourseCode`) VALUES
(2, 'Introduction to Programming', 3, 'CS101'),
(3, 'Calculus I', 4, 'MATH101'),
(4, 'Physics I', 3, 'PHY101'),
(5, 'History of Art', 2, 'ART101'),
(6, 'English Literature', 3, 'ENG101'),
(7, 'Biology Basics', 4, 'BIO101'),
(8, 'Database Systems', 3, 'CS201'),
(9, 'Statistics', 3, 'MATH201'),
(10, 'Chemistry I', 3, 'CHEM101'),
(11, 'Introduction to Psychology', 3, 'PSY101');

-- --------------------------------------------------------

--
-- Table structure for table `enrollment`
--

CREATE TABLE `enrollment` (
  `student_sno` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `semester_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `enrollment`
--

INSERT INTO `enrollment` (`student_sno`, `course_id`, `semester_id`) VALUES
(87, 2, 2),
(87, 3, 1),
(87, 4, 1),
(87, 4, 2),
(87, 4, 5),
(87, 6, 2),
(87, 6, 5),
(87, 7, 1),
(87, 7, 2),
(87, 7, 5),
(87, 9, 1),
(87, 10, 1),
(87, 11, 2),
(901, 3, 1),
(902, 2, 2),
(902, 3, 1),
(902, 3, 2),
(902, 7, 2),
(902, 8, 2),
(902, 9, 2),
(902, 11, 2),
(903, 3, 1),
(904, 3, 1),
(905, 3, 1),
(906, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE `faculty` (
  `sno` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `address` varchar(300) NOT NULL,
  `department` varchar(15) NOT NULL,
  `date_hired` datetime NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`sno`, `first_name`, `last_name`, `email`, `phone`, `gender`, `address`, `department`, `date_hired`, `password`) VALUES
(0, 'Shahbaz', 'Siddiqui', 'shahbaz.siddiqui@nu.edu.pk', '0300236734', 'Male', 'home,karachi', 'BSCY', '2024-11-09 10:51:13', '123'),
(90, 'Alice', 'Johnson', 'alice.johnson@example.com', '1234567890', 'Female', '123 Elm St, Springfield', 'Math', '2023-08-01 09:00:00', 'password123'),
(91, 'Bob', 'Smith', 'bob.smith@example.com', '2345678901', 'Male', '456 Oak St, Metropolis', 'Science', '2023-08-02 09:00:00', 'password123'),
(92, 'Carol', 'Williams', 'carol.williams@example.com', '3456789012', 'Female', '789 Pine St, Gotham', 'English', '2023-08-03 09:00:00', 'password123'),
(93, 'David', 'Brown', 'david.brown@example.com', '4567890123', 'Male', '101 Maple St, Star City', 'History', '2023-08-04 09:00:00', 'password123'),
(94, 'Eve', 'Davis', 'eve.davis@example.com', '5678901234', 'Female', '202 Birch St, Central City', 'Physics', '2023-08-05 09:00:00', 'password123');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `student_sno` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `semester_id` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `section` varchar(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`id`, `student_sno`, `course_id`, `semester_id`, `rating`, `section`) VALUES
(1, 87, 3, 1, 79, 'BCS-D'),
(2, 87, 7, 1, 58, 'BCS-D'),
(3, 87, 9, 1, 30, 'BCS-D'),
(4, 87, 10, 1, 50, 'BCS-D');

-- --------------------------------------------------------

--
-- Table structure for table `marks`
--

CREATE TABLE `marks` (
  `id` int(11) NOT NULL,
  `student_sno` int(11) NOT NULL,
  `course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `marks`
--

INSERT INTO `marks` (`id`, `student_sno`, `course_id`) VALUES
(1, 87, 3),
(2, 901, 3),
(3, 902, 3),
(4, 903, 3),
(5, 904, 3),
(6, 905, 3),
(7, 906, 3),
(8, 87, 3),
(9, 901, 3),
(10, 902, 3),
(11, 903, 3),
(12, 904, 3),
(13, 905, 3),
(14, 906, 3),
(15, 87, 3),
(16, 901, 3),
(17, 902, 3),
(18, 903, 3),
(19, 904, 3),
(20, 905, 3),
(21, 906, 3),
(22, 87, 7),
(23, 902, 7),
(24, 87, 9),
(25, 902, 9),
(26, 87, 10);

-- --------------------------------------------------------

--
-- Table structure for table `semester`
--

CREATE TABLE `semester` (
  `sem_id` int(11) NOT NULL,
  `semester` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `semester`
--

INSERT INTO `semester` (`sem_id`, `semester`) VALUES
(1, 'Fall 2022'),
(2, 'Spring 2023'),
(3, 'Summer 2023'),
(4, 'Fall 2023'),
(5, 'Spring 2024'),
(6, 'Summer 2024'),
(7, 'Fall 2024'),
(8, 'Spring 2025'),
(9, 'Summer 2025'),
(10, 'Fall 2025'),
(11, 'Spring 2026'),
(12, 'Summer 2026'),
(13, 'Fall 2026'),
(14, 'Spring 2027'),
(15, 'Summer 2027'),
(16, 'Fall 2027');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `sno` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `DOB` datetime NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `section` varchar(7) NOT NULL,
  `degree` varchar(10) NOT NULL,
  `campus` varchar(15) NOT NULL,
  `batch` varchar(15) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `gender` enum('male','female','other','') NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `cnic` varchar(20) DEFAULT NULL,
  `address` varchar(300) NOT NULL,
  `password` varchar(50) NOT NULL,
  `user_id` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`sno`, `first_name`, `last_name`, `DOB`, `date_created`, `section`, `degree`, `campus`, `batch`, `phone`, `gender`, `email`, `cnic`, `address`, `password`, `user_id`) VALUES
(87, 'Shahmir', 'Ahmed', '0000-00-00 00:00:00', '2024-11-09 10:38:10', 'BCS-D', 'BScs', 'karachi', 'FALL 2022', '03002675876', 'male', 'shahmir@gmail.com', '2342445', 'home,karachi', '123', '22k-0087'),
(900, 'ALI', 'AHMED', '1995-05-20 00:00:00', '2024-10-04 17:42:25', 'BCS-D', 'BS(CS)', 'KARACHI', 'FALL 2022', '0300-2875207', 'female', 'aliaaaaaa@gmail.com', '276327637263', '123 Maple Street Springfield, IL 62704 USA', 'aliahmed123', '22k-0900'),
(901, 'AHMED', 'KHAN', '1998-12-10 00:00:00', '2024-10-04 17:43:10', 'BCS-A', 'BS(SE)', 'ISLAMABAD', 'SPRING 2022', '0301-2875208', 'male', 'ahmedkhan@gmail.com', '276327637264', '456 Oak Avenue Denver, CO 80203 USA', 'ahmedkhan123', '22k-0901'),
(902, 'SARA', 'ALI', '1997-08-15 00:00:00', '2024-10-04 17:44:20', 'BCS-C', 'BS(CS)', 'LAHORE', 'FALL 2021', '0302-2875209', 'female', 'saraali@gmail.com', '276327637265', '789 Pine Road Miami, FL 33101 USA', 'saraali123', '22k-0902'),
(903, 'UMAR', 'FAROOQ', '1996-03-25 00:00:00', '2024-10-04 17:45:30', 'BCS-B', 'BS(IT)', 'KARACHI', 'FALL 2023', '0303-2875210', 'male', 'umarfarooq@gmail.com', '276327637266', '101 Cedar Lane Austin, TX 73301 USA', 'umarfarooq123', '22k-0903'),
(904, 'AAMNA', 'SHAH', '1999-11-11 00:00:00', '2024-10-04 17:46:40', 'BCS-E', 'BS(CS)', 'QUETTA', 'SPRING 2023', '0304-2875211', 'female', 'aamnashah@gmail.com', '276327637267', '202 Willow Street Seattle, WA 98101 USA', 'aamnashah123', '22k-0904'),
(905, 'KASHIF', 'ALI', '1995-07-19 00:00:00', '2024-10-04 17:47:50', 'BCS-F', 'BS(CS)', 'PESHAWAR', 'FALL 2022', '0305-2875212', 'male', 'kashifali@gmail.com', '276327637268', '303 Birch Avenue Boston, MA 02101 USA', 'kashifali123', '22k-0905'),
(906, 'ASMA', 'KHAN', '1998-04-13 00:00:00', '2024-10-04 17:48:55', 'BCS-G', 'BS(IT)', 'MULTAN', 'SPRING 2022', '0306-2875213', 'female', 'asmakhan@gmail.com', '276327637269', '404 Maple Avenue Orlando, FL 32801 USA', 'asmakhan123', '22k-0906'),
(907, 'FARHAN', 'ALI', '1996-09-23 00:00:00', '2024-10-04 17:50:10', 'BCS-H', 'BS(CS)', 'HYDERABAD', 'FALL 2023', '0307-2875214', 'male', 'farhanali@gmail.com', '276327637270', '505 Oak Drive Portland, OR 97201 USA', 'farhanali123', '22k-0907'),
(908, 'MEHWISH', 'BUTT', '1997-01-05 00:00:00', '2024-10-04 17:51:15', 'BCS-I', 'BS(CS)', 'ISLAMABAD', 'SPRING 2023', '0308-2875215', 'female', 'mehwishbutt@gmail.com', '276327637271', '606 Elm Street Dallas, TX 75201 USA', 'mehwishbutt123', '22k-0908'),
(909, 'HASSAN', 'NIAZI', '1999-10-10 00:00:00', '2024-10-04 17:52:20', 'BCS-J', 'BS(CS)', 'FAISALABAD', 'FALL 2024', '0309-2875216', 'male', 'hassanniazi@gmail.com', '276327637272', '707 Cedar Road Phoenix, AZ 85001 USA', 'hassanniazi123', '22k-0909'),
(910, 'MARIAM', 'HUSSAIN', '1995-12-20 00:00:00', '2024-10-04 17:53:25', 'BCS-K', 'BS(SE)', 'KARACHI', 'SPRING 2024', '0310-2875217', 'female', 'mariamhussain@gmail.com', '276327637273', '808 Pine Drive Detroit, MI 48201 USA', 'mariamhussain123', '22k-0910'),
(911, 'BILAL', 'SAEED', '1994-03-15 00:00:00', '2024-10-04 17:54:30', 'BCS-L', 'BS(CS)', 'LAHORE', 'FALL 2022', '0311-2875218', 'male', 'bilalsaeed@gmail.com', '276327637274', '909 Willow Street San Jose, CA 95101 USA', 'bilalsaeed123', '22k-0911'),
(912, 'NOOR', 'SHAH', '1996-08-25 00:00:00', '2024-10-04 17:55:35', 'BCS-M', 'BS(CS)', 'QUETTA', 'SPRING 2023', '0312-2875219', 'female', 'noorshah@gmail.com', '276327637275', '1010 Oak Lane Austin, TX 73301 USA', 'noorshah123', '22k-0912'),
(913, 'HAMZA', 'ALI', '1997-11-14 00:00:00', '2024-10-04 17:56:40', 'BCS-N', 'BS(IT)', 'RAWALPINDI', 'FALL 2023', '0313-2875220', 'male', 'hamzaali@gmail.com', '276327637276', '1111 Maple Street San Diego, CA 92101 USA', 'hamzaali123', '22k-0913'),
(914, 'NIDA', 'FATIMA', '1998-06-09 00:00:00', '2024-10-04 17:57:45', 'BCS-O', 'BS(CS)', 'GUJRANWALA', 'SPRING 2024', '0314-2875221', 'female', 'nidafatima@gmail.com', '276327637277', '1212 Birch Lane Nashville, TN 37201 USA', 'nidafatima123', '22k-0914'),
(923, 'Jane', 'Smith', '2001-05-15 00:00:00', NULL, 'B', 'SE', 'North', 'SPRING 2023', '0987654321', '', 'jane.smith@example.com', '9876543210987', 'Another Address', 'password456', '23k-0000'),
(924, 'John', 'Doe', '2000-01-01 00:00:00', NULL, 'A', 'CS', 'Main', 'FALL 2022', '0123456789', '', 'john@example.com', '1234567890123', 'Some Address', 'password123', '22k-0000');

--
-- Triggers `student`
--
DELIMITER $$
CREATE TRIGGER `after_insert_student` AFTER INSERT ON `student` FOR EACH ROW BEGIN
    UPDATE student
    SET user_id = CONCAT(SUBSTRING(batch, -2), 'k-', LPAD(sno, 4, '0'))
    WHERE sno = NEW.sno;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `teachercourse`
--

CREATE TABLE `teachercourse` (
  `id` int(11) NOT NULL,
  `faculty_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `section` varchar(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teachercourse`
--

INSERT INTO `teachercourse` (`id`, `faculty_id`, `course_id`, `section`) VALUES
(10, 92, 7, ''),
(11, 92, 11, ''),
(14, 94, 9, ''),
(15, 0, 2, ''),
(16, 0, 3, ''),
(17, 0, 4, ''),
(18, 0, 5, ''),
(19, 0, 6, ''),
(20, 0, 7, ''),
(21, 0, 9, ''),
(23, 0, 2, 'BCS-D'),
(24, 0, 3, 'BCS-D'),
(25, 0, 4, 'BCS-D'),
(26, 0, 7, 'BCS-D'),
(27, 0, 10, 'BCS-D'),
(28, 0, 8, 'BCS-D');

--
-- Triggers `teachercourse`
--
DELIMITER $$
CREATE TRIGGER `before_insert_teachercourse` BEFORE INSERT ON `teachercourse` FOR EACH ROW BEGIN
  
    IF NOT EXISTS (SELECT 1 FROM course WHERE C_id = NEW.course_id) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Course ID does not exist.';
    END IF;

   
    IF NOT EXISTS (SELECT 1 FROM faculty WHERE sno = NEW.faculty_id) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Faculty ID does not exist.';
    END IF;
END
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `assessment`
--
ALTER TABLE `assessment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `marks_id` (`marks_id`);

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sem_id` (`sem_id`),
  ADD KEY `course_id` (`course_id`),
  ADD KEY `student_sno` (`student_sno`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`C_id`);

--
-- Indexes for table `enrollment`
--
ALTER TABLE `enrollment`
  ADD PRIMARY KEY (`student_sno`,`course_id`,`semester_id`),
  ADD KEY `course_id` (`course_id`),
  ADD KEY `semester_id` (`semester_id`);

--
-- Indexes for table `faculty`
--
ALTER TABLE `faculty`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`),
  ADD KEY `student_sno` (`student_sno`),
  ADD KEY `course_id` (`course_id`),
  ADD KEY `semester_id` (`semester_id`);

--
-- Indexes for table `marks`
--
ALTER TABLE `marks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `student_sno` (`student_sno`),
  ADD KEY `course_id` (`course_id`);

--
-- Indexes for table `semester`
--
ALTER TABLE `semester`
  ADD PRIMARY KEY (`sem_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`sno`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `std_email` (`email`);

--
-- Indexes for table `teachercourse`
--
ALTER TABLE `teachercourse`
  ADD PRIMARY KEY (`id`),
  ADD KEY `faculty_id` (`faculty_id`),
  ADD KEY `course_id` (`course_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `assessment`
--
ALTER TABLE `assessment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `attendance`
--
ALTER TABLE `attendance`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `C_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `marks`
--
ALTER TABLE `marks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `semester`
--
ALTER TABLE `semester`
  MODIFY `sem_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=927;

--
-- AUTO_INCREMENT for table `teachercourse`
--
ALTER TABLE `teachercourse`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `assessment`
--
ALTER TABLE `assessment`
  ADD CONSTRAINT `assessment_ibfk_1` FOREIGN KEY (`marks_id`) REFERENCES `marks` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `attendance`
--
ALTER TABLE `attendance`
  ADD CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`sem_id`) REFERENCES `semester` (`sem_id`),
  ADD CONSTRAINT `attendance_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `course` (`C_id`),
  ADD CONSTRAINT `attendance_ibfk_3` FOREIGN KEY (`student_sno`) REFERENCES `student` (`sno`);

--
-- Constraints for table `enrollment`
--
ALTER TABLE `enrollment`
  ADD CONSTRAINT `enrollment_ibfk_1` FOREIGN KEY (`student_sno`) REFERENCES `student` (`sno`),
  ADD CONSTRAINT `enrollment_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `course` (`C_id`),
  ADD CONSTRAINT `enrollment_ibfk_3` FOREIGN KEY (`semester_id`) REFERENCES `semester` (`sem_id`);

--
-- Constraints for table `feedback`
--
ALTER TABLE `feedback`
  ADD CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`student_sno`) REFERENCES `student` (`sno`),
  ADD CONSTRAINT `feedback_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `course` (`C_id`),
  ADD CONSTRAINT `feedback_ibfk_3` FOREIGN KEY (`semester_id`) REFERENCES `semester` (`sem_id`);

--
-- Constraints for table `marks`
--
ALTER TABLE `marks`
  ADD CONSTRAINT `marks_ibfk_1` FOREIGN KEY (`student_sno`) REFERENCES `student` (`sno`) ON DELETE CASCADE,
  ADD CONSTRAINT `marks_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `course` (`C_id`) ON DELETE CASCADE;

--
-- Constraints for table `teachercourse`
--
ALTER TABLE `teachercourse`
  ADD CONSTRAINT `teachercourse_ibfk_1` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`sno`),
  ADD CONSTRAINT `teachercourse_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `course` (`C_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
