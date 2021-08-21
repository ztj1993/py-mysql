# -*- coding: utf-8 -*-
# Intro: MySQL实例模块单元测试
# Author: Ztj
# Email: ztj1993@gmail.com

import unittest

from ZtjMySQL import MySQL

__DROP_DATABASE__ = "DROP DATABASE IF EXISTS `testing`;"
__CREATE_DATABASE__ = "CREATE DATABASE `testing` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci';"
__CREATE_TABLE__ = """
CREATE TABLE `testing`.`tmp` (
  `id` int(0) NOT NULL,
  `name` varchar(255) NULL,
  PRIMARY KEY (`id`)
);
"""
__INSERT_INTO_LIST__ = [
    "INSERT INTO `testing`.`tmp`(`id`, `name`) VALUES (1, 'one');",
    "INSERT INTO `testing`.`tmp`(`id`, `name`) VALUES (2, 'two');",
    "INSERT INTO `testing`.`tmp`(`id`, `name`) VALUES (3, 'three');",
]
__SELECT_SQL__ = "SELECT * FROM `testing`.`tmp`;"
__SELECT_COUNT__ = "SELECT count(*) FROM `testing`.`tmp`;"
__SELECT_LIST__ = [
    {'id': 1, 'name': 'one'},
    {'id': 2, 'name': 'two'},
    {'id': 3, 'name': 'three'},
]


class TestMySQL(unittest.TestCase):

    def test_connection_destroy(self):
        """测试初始化"""
        mysql = MySQL(host='127.0.0.1', user='root')
        connection1 = mysql.connection()
        connection2 = mysql.connection()
        self.assertEqual(connection1, connection2)
        mysql.destroy()
        connection3 = mysql.connection()
        self.assertEqual(connection1, connection2)
        self.assertNotEqual(connection1, connection3)

    def test_ping(self):
        """测试初始化"""
        mysql = MySQL(host='127.0.0.1', user='root')
        self.assertTrue(mysql.ping())

    def test_record(self):
        """测试设置配置项"""
        mysql = MySQL(host='127.0.0.1', user='root')
        mysql.exec_sql(__DROP_DATABASE__)
        mysql.exec_sql(__CREATE_DATABASE__)
        mysql.exec_sql(__CREATE_TABLE__)
        mysql.exec_sql_list(__INSERT_INTO_LIST__)
        self.assertListEqual(
            mysql.get_record(__SELECT_SQL__, mysql.record_callback_fetch_all),
            __SELECT_LIST__
        )
        self.assertEqual(
            mysql.get_record(__SELECT_COUNT__, mysql.record_callback_fetch_value),
            len(__SELECT_LIST__)
        )


if __name__ == '__main__':
    unittest.main()
