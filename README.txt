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
  `dt` date NOT NULL DEFAULT '1970-01-01' COMMENT '日期',
  `code` varchar(50) NOT NULL DEFAULT '-' COMMENT '代码',
  `operation` varchar(50) NOT NULL DEFAULT '-' COMMENT '交易类型',
  `portfolio` varchar(50) NOT NULL DEFAULT '-' COMMENT '组合',
  `sec_type` varchar(50) NOT NULL DEFAULT '-' COMMENT '证券类型',
  `quantity` decimal(20,4) NOT NULL DEFAULT '0.0000' COMMENT '份额',
  `price` decimal(20,4) NOT NULL DEFAULT '0.0000' COMMENT '单价',
  `tax` decimal(20,4) NOT NULL DEFAULT '0.0000' COMMENT '税费',
  `other_charges` decimal(20,4) NOT NULL DEFAULT '0.0000' COMMENT '其他费用',
  `amount` decimal(20,4) NOT NULL DEFAULT '0.0000' COMMENT '成本',
  PRIMARY KEY (`dt`,`code`,`operation`,`portfolio`,`quantity`,`price`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
