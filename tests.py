from mysql_instance import MySQL

mysql = MySQL()

mysql.ping()

mysql.exec_sql("DROP DATABASE IF EXISTS `mysql_testing`;")
mysql.exec_sql("CREATE DATABASE `mysql_testing` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci';")
mysql.exec_sql("""
CREATE TABLE `mysql_testing`.`tmp`  (
  `id` int(0) NOT NULL,
  `name` varchar(255) NULL,
  PRIMARY KEY (`id`)
);
""")

mysql.exec_sql_list([
    "INSERT INTO `mysql_testing`.`tmp`(`id`, `name`) VALUES (2, 'one');",
    "INSERT INTO `mysql_testing`.`tmp`(`id`, `name`) VALUES (3, 'one');",
    "INSERT INTO `mysql_testing`.`tmp`(`id`, `name`) VALUES (5, 'one');",
])

print(mysql.get_record('SELECT * FROM `mysql_testing`.`tmp` LIMIT 0,1000', mysql.record_callback_fetchall))
