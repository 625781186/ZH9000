# coding=utf8

import MySQLdb

class MySQLConnextion():
    @classmethod
    def executeSQL(self, sql, pair = None):
        connection = MySQLdb.connect(host="localhost",
                                     port=3306,
                                     user="cherry",
                                     passwd="lian",
                                     db="zh9000",
                                     charset="utf8")
        cursor = connection.cursor()
        # 查询事件无需事务
        # MMySQLdb 中默认关闭了自动提交(autocommit = 0)
        # 因此 select 与 DML 一样都会被认为是一个事务

        # startwith 对于空串也返回 true
        if str(sql).startswith('SELECT') :
            cursor.execute(sql, pair)
            rst = cursor.fetchall()
            for row in rst:
                print(row)
            print '\n'
            return rst

        sql_insert = "insert into `student` (name, age) VALUES ('H', '99')"
        sql_update = "update `student` set age = 100 WHERE NAME = 'C'"
        sql_delete = "delete from `student` WHERE age < 30"

        try:
            cursor.execute(sql, pair)
            print cursor.rowcount
            connection.commit()
        except Exception as exp:
            print(exp)
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
