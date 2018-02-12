CREATE TABLE `t_hld` (
  `dt` date NOT NULL DEFAULT '1970-01-01' COMMENT '日期',
  `code` varchar(50) NOT NULL DEFAULT '' COMMENT '维度类型2',
  `name` varchar(50) DEFAULT '-',
  `share` decimal(20,4) DEFAULT '0.0000' COMMENT '指标值',
  `cost` decimal(20,4) DEFAULT '0.0000',
  PRIMARY KEY (`dt`,`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

CREATE TABLE `t_trd` (
  `dt` date NOT NULL DEFAULT '1970-01-01' COMMENT '日期',
  `code` varchar(50) NOT NULL DEFAULT '-' COMMENT '维度类型2',
  `name` varchar(50) DEFAULT '-',
  `share` decimal(20,4) NOT NULL DEFAULT '0.0000' COMMENT '份额',
  `prc` decimal(20,4) NOT NULL DEFAULT '0.0000' COMMENT '单价',
  `cst` decimal(20,4) NOT NULL DEFAULT '0.0000' COMMENT '其他费用',
  PRIMARY KEY (`dt`,`code`,`share`,`prc`,`cst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
