CREATE TABLE `t_asset` (
  `dt` date NOT NULL DEFAULT '1970-01-01' COMMENT '日期',
  `portfolio` varchar(50) NOT NULL DEFAULT '-' COMMENT '组合',
  `code` varchar(50) NOT NULL DEFAULT '-' COMMENT '代码',
  `name` varchar(50) DEFAULT '-',
  `type` varchar(50) DEFAULT '-' COMMENT '品种',
  `share` decimal(20,4) DEFAULT '0.0000' COMMENT '份额',
  `price` decimal(20,4) DEFAULT '0.0000' COMMENT '单价',
  PRIMARY KEY (`dt`,`portfolio`,`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `t_holding` (
  `dt` date NOT NULL DEFAULT '1970-01-01' COMMENT '日期',
  `portfolio` varchar(50) NOT NULL DEFAULT '-' COMMENT '组合',
  `code` varchar(50) NOT NULL DEFAULT '-' COMMENT '代码',
  `sec_type` varchar(50) NOT NULL DEFAULT '-' COMMENT '证券类型',
  `quantity` decimal(20,4) DEFAULT '0.0000' COMMENT '份额',
  `amount` decimal(20,4) DEFAULT '0.0000' COMMENT '总成本',
  PRIMARY KEY (`dt`,`portfolio`,`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `t_transaction` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `dt` DATETIME NOT NULL,
  `code` VARCHAR(50) NOT NULL,
  `operation` VARCHAR(50) NOT NULL,
  `portfolio` VARCHAR(50) NOT NULL,
  `sec_type` VARCHAR(50) DEFAULT NULL,
  `quantity` FLOAT NOT NULL,
  `price` FLOAT NOT NULL,
  `tax` FLOAT DEFAULT NULL,
  `other_charges` FLOAT DEFAULT NULL,
  `amount` FLOAT DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_t_transaction` (`dt`,`code`,`operation`,`portfolio`,`price`)
) ENGINE=MYISAM AUTO_INCREMENT=568 DEFAULT CHARSET=utf8

CREATE TABLE `t_code` (
  `code` varchar(50) NOT NULL DEFAULT '-' COMMENT '维度类型2',
  `name` varchar(50) DEFAULT '-',
  `type` varchar(50) DEFAULT '-'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE VIEW `v_asset_overview` AS (
select 
  `t_asset`.`dt` AS `dt`,
  `t_asset`.`type` AS `type`,
  sum((`t_asset`.`share` * `t_asset`.`price`)) AS `value` 
from `t_asset` 
group by 
  `t_asset`.`dt`,
  `t_asset`.`type`
);

CREATE VIEW `v_asset_portfolio` AS (
select 
  `t_asset`.`dt` AS `dt`,
  `t_asset`.`portfolio` AS `portfolio`,
  sum((`t_asset`.`share` * `t_asset`.`price`)) AS `value` 
from `t_asset` 
group by 
  `t_asset`.`dt`,
  `t_asset`.`portfolio`
);
