#coding=utf-8
import torndb
import datetime
from constants.errorcode import Errorcode
from util.gip_exception import GipException


class DB(object):
    
    def __init__(self, application):

        self.mysql_account_read = application.db_conn['mysql']['account']['read']
        self.mysql_account_write = application.db_conn['mysql']['account']['write']

        self.mysql_article_read = application.db_conn['mysql']['article']['read']
        self.mysql_article_write = application.db_conn['mysql']['article']['write']
        


        #self.mongo_conn = application.mongo_conn
    
    
    def sample(self):
        
        try:
            sql = ''' select count(1) from tag'''
            result = self.mysql_account_write.query(sql)
        except:
            pass
        finally:
            
            return result[0]

    
    def get_article_by_id(self,id):
        
        try:
            sql = ''' select * from article where id =%s limit 1'''%(id)
            result = self.mysql_article_read.query(sql)
        except:
            pass
        finally:
            
            return result[0]

    def get_article_summary_by_keyword_in_title(self,keyword,start_id,limit_size):

        try:
            sql = ''' select id,title,description,category,create_time,keywords from article where title like'%%%%%s%%%%' limit %s,%s'''%(keyword,start_id,limit_size)
            result = self.mysql_article_read.query(sql)
        except:
            pass
        finally:
            
            return result
   
