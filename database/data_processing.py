import pymysql
db = pymysql.connect(host='localhost',
                     user='qauser',
                     password='123456',
                     database='qadata',
                     charset='utf8')
# 获取游标，目的就是要执行sql语句
cursor = db.cursor()
# 准备sql，之前在mysql客户端如何编 写sql，在python程序里面还怎么编写
sql_create_table = "CREATE TABLE student(" \
      "`id` INT(4) zerofill unsigned NOT NULL AUTO_INCREMENT COMMENT '学号',"\
 	"`name` VARCHAR(30) NOT NULL DEFAULT '匿名' COMMENT '姓名',"\
 	"`pwd` VARCHAR(20) NOT NULL DEFAULT '123456' COMMENT '密码',"\
 	"`sex` VARCHAR(2) NOT NULL DEFAULT '女' COMMENT '性别',"\
 	"`birthday` DATETIME DEFAULT NULL COMMENT '出生日期',"\
 	"`address` VARCHAR (100) DEFAULT NULL COMMENT '家庭地址',"\
 	"`email` VARCHAR(50) DEFAULT NULL COMMENT '电子邮箱',"\
 	"PRIMARY KEY(`id`)"\
    ")ENGINE=INNODB DEFAULT CHARSET=utf8;  "
sql_insert_student ="insert into student (`id`,`name`,`pwd`,`sex`,`birthday`)value(2,'李四','123456','女','19900312');"
sql_select_student ="select * from student"
sql_create_Comprehensive_data="CREATE TABLE comprehensive_Sdata(" \
                              "R_SecuCode VARCHAR(24) DEFAULT NULL COMMENT '证券代码',"\
"CompanyCode VARCHAR(8) DEFAULT NULL COMMENT '公司代码',"\
"Comcd VARCHAR(20) DEFAULT NULL COMMENT '上市公司代码',"\
"Stkcd VARCHAR(20) NOT NULL COMMENT '股票代码',"\
"Listedstate VARCHAR(20) DEFAULT NULL COMMENT '上市状态',"\
"Csrciccd1 VARCHAR(8) DEFAULT NULL COMMENT '证监会行业门类代码',"\
"Csrciccd2 VARCHAR(16) DEFAULT NULL COMMENT '证监会行业大类代码',"\
"Date DATETIME NOT NULL COMMENT '日期',"\
"PrevClPr REAL DEFAULT NULL COMMENT '前收盘价',"\
"Oppr REAL DEFAULT NULL COMMENT '开盘价',"\
"Hipr REAL DEFAULT NULL COMMENT '最高价',"\
"Lopr REAL DEFAULT NULL COMMENT '最低价',"\
"Clpr REAL DEFAULT NULL COMMENT '收盘价',"\
"AdjClpr1 REAL DEFAULT NULL COMMENT '复权价1(元)',"\
"AdjClpr2 REAL DEFAULT NULL COMMENT '复权价2(元)',"\
"Trdvol REAL DEFAULT NULL COMMENT '成交量',"\
"Trdsum REAL DEFAULT NULL COMMENT '成交金额',"\
"Dampltd REAL DEFAULT NULL COMMENT '日振幅(%)',"\
"DFulTurnR REAL DEFAULT NULL COMMENT '总股数日换手率(%)',"\
"DTrdTurnR REAL DEFAULT NULL COMMENT '流通股日换手率(%)',"\
"Capchgdt DATETIME DEFAULT NULL COMMENT '股数变动日',"\
"Comstateshr REAL DEFAULT NULL COMMENT '公司国有股',"\
"Comlpshr REAL DEFAULT NULL COMMENT '公司法人股',"\
"Fullshr REAL DEFAULT NULL COMMENT '总股数',"\
"Trdshr REAL DEFAULT NULL COMMENT '流通股',"\
"Lsttrdshr REAL DEFAULT NULL COMMENT '已上市流通股',"\
"Dret REAL DEFAULT NULL COMMENT '日收益率',"\
"Daret REAL DEFAULT NULL COMMENT '日资本收益率',"\
"PE REAL DEFAULT NULL COMMENT '市盈率',"\
"PB REAL DEFAULT NULL COMMENT '市净率',"\
"PCF REAL DEFAULT NULL COMMENT '市现率',"\
"PS REAL DEFAULT NULL COMMENT '市销率',"\
"EPS REAL DEFAULT NULL COMMENT '每股收益(摊薄)(元/股)',"\
"ROE REAL DEFAULT NULL COMMENT '净资产收益率(摊薄)',"\
"AccumFundPS REAL DEFAULT NULL COMMENT '每股公积金(元/股)',"\
"OpPrfPS REAL DEFAULT NULL COMMENT '每股营业利润(元/股)',"\
"NAPS REAL DEFAULT NULL COMMENT '每股净资产(元/股)',"\
"NAPSadj REAL DEFAULT NULL COMMENT '调整后每股净资产(元/股)',"\
"IncomePS REAL DEFAULT NULL COMMENT '每股营业收入',"\
"NCFfropePS REAL DEFAULT NULL COMMENT '每股经营活动现金流量净额(元/股)',"\
"PRIMARY KEY(`Stkcd`,`Date`)"\
")ENGINE=INNODB DEFAULT CHARSET=utf8;"
sql_select_sdata ="select * from comprehensive_Sdata"
sql_insert_sdata = "insert into comprehensive_Sdata value('90_000001', '3', 'C000001', '000001', 'Norm', 'J', 'J66', '2021-01-04', '19.3400', '19.1000', '19.1000', '18.4400', '18.6000', '1665.2372', '18.4575', '155421643', '2891682312.05', '3.4126', '0.8009', '0.8009', NULL, '0', '156145', '19405918198', '19405918198', '19405762053', '-0.0383', '-0.0383', NULL, '1.03', '20.78', '2.72', '1.15', '6.243000', '4.72', '1.49', '14.88', '3.25', '6.01', '1.58');"
sql_drop_sdata="drop table comprehensive_Sdata"
# 4. 执行sql语句

cursor.execute(sql_create_Comprehensive_data)

# 获取查询结果，返回的数据类型是一个元组：(1,张三)
res=cursor.fetchall()
print(res)
# 5.关闭游标
cursor.close()
db.commit()

# 6.关闭连接
db.close()
