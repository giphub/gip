#coding=utf-8
import torndb
import datetime
from constants.errorcode import Errorcode
from util.lt_exception import LTException 


class DB(object):
    
    def __init__(self, application):
        self.mysql_read = application.mysql_conn_read
        self.mysql_write = application.mysql_conn_write
        #self.mongo_conn = application.mongo_conn
    
    
    def sample(self):
        '''
        示例代码
        '''
        try:
            sql = ''' select count(1) from tag'''
            result = self.mysql_write.query(sql)
        except:
            # 抛出异常
            pass
        finally:
            
            return result[0]

    
    def get_article_by_id(self,id):
        '''
        示例代码
        '''
        try:
            sql = ''' select * from article where id =%s limit 1'''%(id)
            result = self.mysql_write.query(sql)
        except:
            # 抛出异常
            pass
        finally:
            
            return result[0]

    
