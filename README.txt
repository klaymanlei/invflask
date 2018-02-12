CREATE TABLE `t_ast` (
  `dt` date NOT NULL DEFAULT '1970-01-01' COMMENT '日期',
  `portfolio` varchar(50) NOT NULL DEFAULT '-' COMMENT '组合',
  `code` varchar(50) NOT NULL DEFAULT '-' COMMENT '代码',
  `name` varchar(50) DEFAULT '-',
  `type` varchar(50) DEFAULT '-' COMMENT '品种',
  `share` decimal(20,4) DEFAULT '0.0000' COMMENT '份额',
  `prc` decimal(20,4) DEFAULT '0.0000' COMMENT '单价',
  PRIMARY KEY (`dt`,`portfolio`,`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

CREATE TABLE `t_hld` (
  `dt` date NOT NULL DEFAULT '1970-01-01' COMMENT '日期',
  `portfolio` varchar(50) NOT NULL DEFAULT '-' COMMENT '组合',
  `code` varchar(50) NOT NULL DEFAULT '-' COMMENT '代码',
  `name` varchar(50) DEFAULT '-',
  `share` decimal(20,4) DEFAULT '0.0000' COMMENT '份额',
  `cost` decimal(20,4) DEFAULT '0.0000' COMMENT '总成本',
  PRIMARY KEY (`dt`,`portfolio`,`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

CREATE TABLE `t_trd` (
  `dt` date NOT NULL DEFAULT '1970-01-01' COMMENT '日期',
  `code` varchar(50) NOT NULL DEFAULT '-' COMMENT '代码',
  `name` varchar(50) DEFAULT '-',
  `portfolio` varchar(50) NOT NULL DEFAULT '-' COMMENT '组合',
  `share` decimal(20,4) NOT NULL DEFAULT '0.0000' COMMENT '份额',
  `prc` decimal(20,4) NOT NULL DEFAULT '0.0000' COMMENT '单价',
  `cst` decimal(20,4) NOT NULL DEFAULT '0.0000' COMMENT '其他费用',
  PRIMARY KEY (`dt`,`code`,`portfolio`,`share`,`prc`,`cst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

CREATE ALGORITHM=UNDEFINED DEFINER=`leidayu`@`%` 
SQL SECURITY DEFINER VIEW `ast_overview` AS (
select `t_ast`.`dt` AS `dt`,`t_ast`.`type` AS `type`,sum((`t_ast`.`share` * `t_ast`.`prc`)) AS `value` 
from `t_ast` group by `t_ast`.`dt`,`t_ast`.`type`)

CREATE ALGORITHM=UNDEFINED DEFINER=`leidayu`@`%` 
SQL SECURITY DEFINER VIEW `ast_portfolio` AS (
select `t_ast`.`dt` AS `dt`,`t_ast`.`portfolio` AS `portfolio`,sum((`t_ast`.`share` * `t_ast`.`prc`)) AS `value` 
from `t_ast` group by `t_ast`.`dt`,`t_ast`.`portfolio`)
