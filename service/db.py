#coding=utf-8
import torndb
import datetime
import httplib
import urllib

from constants.errorcode import Errorcode
from util.gip_exception import GipException


class DB(object):
    
    def __init__(self, application):

        self.mysql_account_read = application.db_conn['mysql']['account']['read']
        self.mysql_account_write = application.db_conn['mysql']['account']['write']

        self.mysql_article_read = application.db_conn['mysql']['article']['read']
        self.mysql_article_write = application.db_conn['mysql']['article']['write']
        

        self.solr_article_url = application.db_conn['solr']['article']['url'] 
        self.solr_article_path = application.db_conn['solr']['article']['path'] 
        #self.mongo_conn = application.mongo_conn
    
    
    def sample(self):
        
        try:
            sql = ''' select count(1) from tag'''
            result = self.mysql_account_write.query(sql)
        except:
            pass
        finally:
            
            return result[0]


    def sample_solr(self):

        res = {}
        data ={
        	'q':'title:幼儿园',
                'wt':'python',
                'indent':'true'}
                

        path = self.solr_article_path + '''select?''' + urllib.urlencode(data)
        try:
            httpClient = httplib.HTTPConnection(self.solr_article_url)
            httpClient.request("GET", path, '' , {})

            response = httpClient.getresponse()

            res = response.read().decode("unicode_escape")
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()
            return res

    
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
   
