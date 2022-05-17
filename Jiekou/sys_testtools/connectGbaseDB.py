"""
使用说明：
1、需安装驱动GBase8s_3.0.0_1-Win64-ODBC-Driver
2、安装DbtPy模块：pip install DbtPy
3、DbtPy接口文档地址：https://pypi.org/project/DbtPy/
4、Gbase驱动下载地址：https://gbasedbt.com/odbc/
5、Windows下Python3通过DbtPy连接到GBase 8s数据库教程：https://gbasedbt.com/index.php/archives/318/
6、需要连上公司VPN
"""
import os
print(os.path)
# if 'GBASEDBTDIR' in os.environ:
#     print('1')
#     os.add_dll_directory(os.path.join(os.environ['GBASEDBTDIR'],"bin"))
os.add_dll_directory(os.path.join(os.environ['GBASEDBTDIR'],"bin"))

import DbtPy
# import DbtPyDbi as DbtPy

class DateBase():
    def __init__(self):

        # self.conn_gbase_info = "PROTOCOL=onsoctcp;HOST=10.252.176.30;SERVICE=9088;SERVER=gbase01;DATABASE=testdb;DB_LOCALE=zh_CN.utf8;CLIENT_LOCALE=zh_CN.utf8"
        # self.conn_gbase_info = "PROTOCOL=onsoctcp;HOST=10.252.176.30;SERVICE=9088;SERVER=gbase01;DATABASE=itp_affair;DB_LOCALE=zh_CN.utf8;CLIENT_LOCALE=zh_CN.utf8"
        self.conn_gbase_info = "PROTOCOL=onsoctcp;HOST=10.252.176.86;SERVICE=9088;SERVER=gbase01;" \
                               "DATABASE=itp_affair;DB_LOCALE=zh_CN.utf8;CLIENT_LOCALE=zh_CN.utf8"
        self.user = "gbasedbt"
        self.password = "GRGbanking@2022"
        self.conn = DbtPy.connect(self.conn_gbase_info, self.user, self.password)

    #查询表数据并返回查询结果
    def search_form(self, search_sql):
        """
        功能描述：用于查询数据
        :param search_sql: SELECT 列名称 FROM 表名称
        :return:返回一个列表集
        """
        data_list = []
        stmt = DbtPy.exec_immediate(self.conn, search_sql)
        data = DbtPy.fetch_assoc(stmt)
        while data != False:
            data_list.append(data)
            data = DbtPy.fetch_assoc(stmt)
        return data_list

    def insert_data(self, insert_sql):
        """
        功能描述：插入数据
        :param insert_sql: INSERT INTO 表名称 VALUES (值1, 值2,....)
        :return:
        """
        DbtPy.exec_immediate(self.conn, insert_sql)

    def update_data(self, update_sql):
        """
        功能描述：更新数据
        :param update_sql: UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值
        :return:
        """
        DbtPy.exec_immediate(self.conn, update_sql)

    def delete_data(self, delete_sql):
        """
        功能描述：删除数据
        :param delete_sql: DELETE FROM 表名称 WHERE 列名称 = 值
        :return:
        """
        DbtPy.exec_immediate(self.conn, delete_sql)

    def close_gbase_connect(self):
        """
        功能描述：断开Gbase数据库连接
        :return:
        """
        DbtPy.close(self.conn)



if __name__=="__main__":
    #问题1：调试其它模块引入。
    db = DateBase()
    # insert_sql = "INSERT INTO mytest VALUES (3,'钟汝康',40,'深圳市龙岗区民治水尾14栋','20000.00','2022-02-22')"
    # search_sql = "select * from mytest where name = '钟汝康'"
    search_sql = "select user_id from bds_trip_info "
    # update_sql = "UPDATE mytest SET address = '深圳市龙岗区五和大发埔东村七巷' WHERE name = '钟汝康'"
    # delete_sql = "DELETE FROM mytest WHERE name = '钟汝康'"
    # db.insert_data(insert_sql)
    # db.update_data(update_sql)
    # db.delete_data(delete_sql)
    data_list = db.search_form(search_sql)
    print(data_list)
    db.close_gbase_connect()





