/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50620
Source Host           : localhost:3306
Source Database       : xuanke_db

Target Server Type    : MYSQL
Target Server Version : 50620
File Encoding         : 65001

Date: 2020-02-25 15:54:07
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `t_admin`
-- ----------------------------
DROP TABLE IF EXISTS `t_admin`;
CREATE TABLE `t_admin` (
  `username` varchar(20) NOT NULL DEFAULT '',
  `password` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_admin
-- ----------------------------
INSERT INTO `t_admin` VALUES ('a', 'a');

-- ----------------------------
-- Table structure for `t_classinfo`
-- ----------------------------
DROP TABLE IF EXISTS `t_classinfo`;
CREATE TABLE `t_classinfo` (
  `classNumber` varchar(20) NOT NULL COMMENT 'classNumber',
  `className` varchar(20) NOT NULL COMMENT '班级名称',
  `classSpecialFieldNumber` varchar(20) NOT NULL COMMENT '所属专业',
  `classBirthDate` varchar(20) DEFAULT NULL COMMENT '成立日期',
  `classTeacherCharge` varchar(12) DEFAULT NULL COMMENT '班主任',
  `classTelephone` varchar(20) DEFAULT NULL COMMENT '联系电话',
  `classMemo` varchar(100) DEFAULT NULL COMMENT '附加信息',
  PRIMARY KEY (`classNumber`),
  KEY `classSpecialFieldNumber` (`classSpecialFieldNumber`),
  CONSTRAINT `t_classinfo_ibfk_1` FOREIGN KEY (`classSpecialFieldNumber`) REFERENCES `t_specialfieldinfo` (`specialFieldNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_classinfo
-- ----------------------------
INSERT INTO `t_classinfo` VALUES ('BJ001', '2020计算机1班', 'ZY001', '2020-02-19', '赵小刚', '13805810834', '测试');
INSERT INTO `t_classinfo` VALUES ('BJ002', '2020计算机2班', 'ZY001', '2020-02-05', '汪大东', '13980800834', '测试班级');

-- ----------------------------
-- Table structure for `t_collegeinfo`
-- ----------------------------
DROP TABLE IF EXISTS `t_collegeinfo`;
CREATE TABLE `t_collegeinfo` (
  `collegeNumber` varchar(20) NOT NULL COMMENT 'collegeNumber',
  `collegeName` varchar(20) NOT NULL COMMENT '学院名称',
  `collegeBirthDate` varchar(20) DEFAULT NULL COMMENT '成立日期',
  `collegeMan` varchar(10) DEFAULT NULL COMMENT '院长姓名',
  `collegeTelephone` varchar(20) DEFAULT NULL COMMENT '联系电话',
  `collegeMemo` varchar(100) DEFAULT NULL COMMENT '附加信息',
  PRIMARY KEY (`collegeNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_collegeinfo
-- ----------------------------
INSERT INTO `t_collegeinfo` VALUES ('XY001', '信息工程学院', '2020-02-20', '袁明涛', '028-83919324', '测试');
INSERT INTO `t_collegeinfo` VALUES ('XY002', '外国语学院', '2020-02-12', '李长秀', '028-83920912', '测试');

-- ----------------------------
-- Table structure for `t_courseinfo`
-- ----------------------------
DROP TABLE IF EXISTS `t_courseinfo`;
CREATE TABLE `t_courseinfo` (
  `courseNumber` varchar(20) NOT NULL COMMENT 'courseNumber',
  `courseName` varchar(20) NOT NULL COMMENT '课程名称',
  `coursePhoto` varchar(60) NOT NULL COMMENT '课程照片',
  `courseTeacher` varchar(20) NOT NULL COMMENT '上课老师',
  `courseTime` varchar(40) DEFAULT NULL COMMENT '上课时间',
  `coursePlace` varchar(40) DEFAULT NULL COMMENT '上课地点',
  `courseScore` float NOT NULL COMMENT '课程学分',
  `courseMemo` varchar(100) DEFAULT NULL COMMENT '附加信息',
  PRIMARY KEY (`courseNumber`),
  KEY `courseTeacher` (`courseTeacher`),
  CONSTRAINT `t_courseinfo_ibfk_1` FOREIGN KEY (`courseTeacher`) REFERENCES `t_teacher` (`teacherNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_courseinfo
-- ----------------------------
INSERT INTO `t_courseinfo` VALUES ('KC001', 'Python从入门到放弃', 'img/1.jpg', 'TH001', '每周二下午', '6A-232', '3.5', '测试');
INSERT INTO `t_courseinfo` VALUES ('KC002', 'PHP零基础项目实战', 'img/2.jpg', 'TH001', '周一上午', '6C-310', '3.5', '测试课程');

-- ----------------------------
-- Table structure for `t_news`
-- ----------------------------
DROP TABLE IF EXISTS `t_news`;
CREATE TABLE `t_news` (
  `newsId` int(11) NOT NULL AUTO_INCREMENT COMMENT '记录编号',
  `newsTitle` varchar(50) NOT NULL COMMENT '新闻标题',
  `newsContent` varchar(500) NOT NULL COMMENT '新闻内容',
  `newsDate` varchar(20) DEFAULT NULL COMMENT '发布日期',
  `newsPhoto` varchar(60) NOT NULL COMMENT '新闻图片',
  PRIMARY KEY (`newsId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_news
-- ----------------------------
INSERT INTO `t_news` VALUES ('1', '学生选课系统上线了', '同学们可以来这里，愉快的选课了哦！', '2020-02-19', 'img/NoImage.jpg');

-- ----------------------------
-- Table structure for `t_scoreinfo`
-- ----------------------------
DROP TABLE IF EXISTS `t_scoreinfo`;
CREATE TABLE `t_scoreinfo` (
  `scoreId` int(11) NOT NULL AUTO_INCREMENT COMMENT '记录编号',
  `studentNumber` varchar(30) NOT NULL COMMENT '学生',
  `courseNumber` varchar(20) NOT NULL COMMENT '课程',
  `scoreValue` float NOT NULL COMMENT '成绩得分',
  `studentEvaluate` varchar(30) DEFAULT NULL COMMENT '学生评价',
  PRIMARY KEY (`scoreId`),
  KEY `studentNumber` (`studentNumber`),
  KEY `courseNumber` (`courseNumber`),
  CONSTRAINT `t_scoreinfo_ibfk_1` FOREIGN KEY (`studentNumber`) REFERENCES `t_student` (`studentNumber`),
  CONSTRAINT `t_scoreinfo_ibfk_2` FOREIGN KEY (`courseNumber`) REFERENCES `t_courseinfo` (`courseNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_scoreinfo
-- ----------------------------
INSERT INTO `t_scoreinfo` VALUES ('1', 'STU001', 'KC001', '92.5', '成绩不错');
INSERT INTO `t_scoreinfo` VALUES ('3', 'STU002', 'KC001', '88', '还可以');
INSERT INTO `t_scoreinfo` VALUES ('4', 'STU001', 'KC002', '93', '此学生很努力');

-- ----------------------------
-- Table structure for `t_specialfieldinfo`
-- ----------------------------
DROP TABLE IF EXISTS `t_specialfieldinfo`;
CREATE TABLE `t_specialfieldinfo` (
  `specialFieldNumber` varchar(20) NOT NULL COMMENT 'specialFieldNumber',
  `specialFieldName` varchar(20) NOT NULL COMMENT '专业名称',
  `specialCollegeNumber` varchar(20) NOT NULL COMMENT '所在学院',
  `specialBirthDate` varchar(20) DEFAULT NULL COMMENT '成立日期',
  `specialMan` varchar(10) DEFAULT NULL COMMENT '联系人',
  `specialTelephone` varchar(20) DEFAULT NULL COMMENT '联系电话',
  `specialMemo` varchar(100) DEFAULT NULL COMMENT '附加信息',
  PRIMARY KEY (`specialFieldNumber`),
  KEY `specialCollegeNumber` (`specialCollegeNumber`),
  CONSTRAINT `t_specialfieldinfo_ibfk_1` FOREIGN KEY (`specialCollegeNumber`) REFERENCES `t_collegeinfo` (`collegeNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_specialfieldinfo
-- ----------------------------
INSERT INTO `t_specialfieldinfo` VALUES ('ZY001', '计算机专业', 'XY001', '2020-02-12', '王金涛', '028-83948112', '测试');
INSERT INTO `t_specialfieldinfo` VALUES ('ZY002', '电子信息技术', 'XY002', '2020-02-12', '张涛', '028-83980123', '测试');

-- ----------------------------
-- Table structure for `t_student`
-- ----------------------------
DROP TABLE IF EXISTS `t_student`;
CREATE TABLE `t_student` (
  `studentNumber` varchar(30) NOT NULL COMMENT 'studentNumber',
  `studentName` varchar(12) NOT NULL COMMENT '姓名',
  `studentPassword` varchar(30) NOT NULL COMMENT '登录密码',
  `studentSex` varchar(2) NOT NULL COMMENT '性别',
  `studentClassNumber` varchar(20) NOT NULL COMMENT '所在班级',
  `studentBirthday` varchar(20) DEFAULT NULL COMMENT '出生日期',
  `studentState` varchar(20) DEFAULT NULL COMMENT '政治面貌',
  `studentPhoto` varchar(60) NOT NULL COMMENT '学生照片',
  `studentTelephone` varchar(20) DEFAULT NULL COMMENT '联系电话',
  `studentEmail` varchar(30) DEFAULT NULL COMMENT '学生邮箱',
  `studentQQ` varchar(20) DEFAULT NULL COMMENT '联系qq',
  `studentAddress` varchar(100) DEFAULT NULL COMMENT '家庭地址',
  `studentMemo` varchar(100) DEFAULT NULL COMMENT '附加信息',
  PRIMARY KEY (`studentNumber`),
  KEY `studentClassNumber` (`studentClassNumber`),
  CONSTRAINT `t_student_ibfk_1` FOREIGN KEY (`studentClassNumber`) REFERENCES `t_classinfo` (`classNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_student
-- ----------------------------
INSERT INTO `t_student` VALUES ('STU001', '双鱼林', '123', '男', 'BJ001', '2020-02-04', '团员', 'img/8.jpg', '13898201342', 'syl@163.com', '1514151', '滨江路10号', '测试');
INSERT INTO `t_student` VALUES ('STU002', '李晓霞', '123', '女', 'BJ001', '2020-02-13', '团员', 'img/12.jpg', '13908120834', 'xiaoxia@163.com', '610841234', '四川成都红星路', '测试学生');

-- ----------------------------
-- Table structure for `t_studentselectcourseinfo`
-- ----------------------------
DROP TABLE IF EXISTS `t_studentselectcourseinfo`;
CREATE TABLE `t_studentselectcourseinfo` (
  `selectId` int(11) NOT NULL AUTO_INCREMENT COMMENT '记录编号',
  `studentNumber` varchar(30) NOT NULL COMMENT '选课学生',
  `courseNumber` varchar(20) NOT NULL COMMENT '选择课程',
  `selectTime` varchar(20) DEFAULT NULL COMMENT '选课时间',
  PRIMARY KEY (`selectId`),
  KEY `studentNumber` (`studentNumber`),
  KEY `courseNumber` (`courseNumber`),
  CONSTRAINT `t_studentselectcourseinfo_ibfk_1` FOREIGN KEY (`studentNumber`) REFERENCES `t_student` (`studentNumber`),
  CONSTRAINT `t_studentselectcourseinfo_ibfk_2` FOREIGN KEY (`courseNumber`) REFERENCES `t_courseinfo` (`courseNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_studentselectcourseinfo
-- ----------------------------
INSERT INTO `t_studentselectcourseinfo` VALUES ('2', 'STU002', 'KC001', '2020-02-25 11:32:12');
INSERT INTO `t_studentselectcourseinfo` VALUES ('4', 'STU001', 'KC001', '2020-02-25 11:42:09');
INSERT INTO `t_studentselectcourseinfo` VALUES ('5', 'STU001', 'KC002', '2020-02-25 15:43:32');

-- ----------------------------
-- Table structure for `t_teacher`
-- ----------------------------
DROP TABLE IF EXISTS `t_teacher`;
CREATE TABLE `t_teacher` (
  `teacherNumber` varchar(20) NOT NULL COMMENT 'teacherNumber',
  `teacherName` varchar(12) NOT NULL COMMENT '教师姓名',
  `teacherSex` varchar(2) NOT NULL COMMENT '性别',
  `teacherBirthday` varchar(20) DEFAULT NULL COMMENT '出生日期',
  `teacherArriveDate` varchar(20) DEFAULT NULL COMMENT '入职日期',
  `teacherCardNumber` varchar(20) DEFAULT NULL COMMENT '身份证号',
  `teacherPhone` varchar(20) DEFAULT NULL COMMENT '联系电话',
  `teacherPhoto` varchar(60) NOT NULL COMMENT '教师照片',
  `teacherAddress` varchar(100) DEFAULT NULL COMMENT '家庭地址',
  `teacherMemo` varchar(100) DEFAULT NULL COMMENT '附加信息',
  PRIMARY KEY (`teacherNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_teacher
-- ----------------------------
INSERT INTO `t_teacher` VALUES ('TH001', '张熙桐', '男', '2020-02-05', '2020-02-12', '513080199611242342', '13908130834', 'img/18.jpg', '成都春熙路', '测试');
INSERT INTO `t_teacher` VALUES ('TH002', '张德贵', '男', '2020-02-05', '2020-02-12', '513080199410242432', '13980813423', 'img/5.jpg', '南昌滨江路10号', '测试老师');
