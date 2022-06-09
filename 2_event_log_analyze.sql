-- event_log 建表语句

CREATE TABLE `event_log` (
  `user_id` int DEFAULT NULL,
  `event_timestamp` varchar(50) DEFAULT NULL
) COMMENT='事件记录表';

-- event_log 示例数据

INSERT INTO event_log (user_id,event_timestamp) VALUES
	 (8373613,'1603189321'),
	 (3232343,'1603189452'),
	 (1343299,'1603189498'),
	 (8372761,'1603189611'),
	 (7689821,'1603189734'),
	 (8373613,'1599062400'),
	 (8372761,'1600099200'),
	 (8373613,'1601395200');

-- 查询语句
-- 查询有多少用户在2020年9月开启关卡数大于等于1000小于2000

select count(*) as `count`
from (
	select user_id
	from event_log
	where from_unixtime(event_timestamp, '%Y-%m') = '2020-09'
	group by user_id
	having count(*) >= 1000 and count(*) < 2000
) as event_filter;


