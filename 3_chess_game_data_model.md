---
typora-copy-images-to: images
---

## 国际象棋比赛数据建模

### 一、E-R图



![](.\images\3_E-R图.drawio.png)

### 二、数据库UML图

![](.\images\3_UML图.drawio.png)

### 三、数据库表DDL

#### 俱乐部表

```mysql
CREATE TABLE `club` (
  `club_id` int NOT NULL AUTO_INCREMENT COMMENT '俱乐部ID',
  `club_name` varchar(100) NOT NULL COMMENT '俱乐部名称',
  `address` varchar(255) DEFAULT NULL COMMENT '地址',
  PRIMARY KEY (`club_id`)
) COMMENT='俱乐部表';
```

#### 锦标赛

```mysql
CREATE TABLE `championship` (
  `championship_id` int NOT NULL AUTO_INCREMENT COMMENT '锦标赛代码',
  `club_id` int NOT NULL COMMENT '关联俱乐部ID',
  `championship_name` varchar(50) NOT NULL COMMENT '名称',
  `sponsor` varchar(255) DEFAULT NULL COMMENT '赞助方',
  `start_date` date DEFAULT NULL COMMENT '开始日期',
  `end_date` date DEFAULT NULL COMMENT '结束日期',
  PRIMARY KEY (`championship_id`),
  KEY `championship_FK` (`club_id`),
  CONSTRAINT `championship_FK` FOREIGN KEY (`club_id`) REFERENCES `club` (`club_id`)
) COMMENT='锦标赛';
```

#### 棋手

```mysql
CREATE TABLE `player` (
  `player_id` int NOT NULL AUTO_INCREMENT COMMENT '棋手ID',
  `player_name` varchar(20) NOT NULL COMMENT '名称',
  `address` varchar(255) DEFAULT NULL COMMENT '地址',
  PRIMARY KEY (`player_id`)
) COMMENT='棋手表';
```

#### 比赛

```mysql
CREATE TABLE `game` (
  `game_id` int NOT NULL AUTO_INCREMENT COMMENT '比赛ID',
  `player_A_id` int DEFAULT NULL COMMENT '棋手A ID',
  `player_B_id` int DEFAULT NULL COMMENT '棋手B ID',
  `winner` int DEFAULT NULL COMMENT '赢方棋手ID',
  `championship_id` int NOT NULL,
  PRIMARY KEY (`game_id`),
  KEY `game_FK` (`player_A_id`),
  KEY `game_FK_1` (`player_B_id`),
  KEY `game_FK_2` (`winner`),
  KEY `game_FK_3` (`championship_id`),
  CONSTRAINT `game_FK` FOREIGN KEY (`player_A_id`) REFERENCES `player` (`player_id`),
  CONSTRAINT `game_FK_1` FOREIGN KEY (`player_B_id`) REFERENCES `player` (`player_id`),
  CONSTRAINT `game_FK_2` FOREIGN KEY (`winner`) REFERENCES `player` (`player_id`),
  CONSTRAINT `game_FK_3` FOREIGN KEY (`championship_id`) REFERENCES `championship` (`championship_id`)
) COMMENT='比赛表';
```

#### 会员记录

```mysql
CREATE TABLE `member` (
  `record_id` int NOT NULL AUTO_INCREMENT COMMENT '记录ID',
  `club_id` int NOT NULL COMMENT '俱乐部ID',
  `player_id` int NOT NULL COMMENT '棋手ID',
  PRIMARY KEY (`record_id`),
  UNIQUE KEY `member_un` (`club_id`,`player_id`),
  KEY `member_FK_1` (`player_id`),
  CONSTRAINT `member_FK` FOREIGN KEY (`club_id`) REFERENCES `club` (`club_id`),
  CONSTRAINT `member_FK_1` FOREIGN KEY (`player_id`) REFERENCES `player` (`player_id`)
) COMMENT='会员记录表';
```

#### 锦标赛参赛记录

```mysql
CREATE TABLE `competition_record` (
  `record_id` int NOT NULL AUTO_INCREMENT COMMENT '记录ID',
  `championship_id` int DEFAULT NULL COMMENT '锦标赛ID',
  `player_id` int DEFAULT NULL COMMENT '棋手ID',
  PRIMARY KEY (`record_id`),
  UNIQUE KEY `competition_record_un` (`championship_id`,`player_id`),
  KEY `competition_record_FK_1` (`player_id`),
  CONSTRAINT `competition_record_FK` FOREIGN KEY (`championship_id`) REFERENCES `championship` (`championship_id`),
  CONSTRAINT `competition_record_FK_1` FOREIGN KEY (`player_id`) REFERENCES `player` (`player_id`)
) COMMENT='锦标赛参赛记录';
```