#coding=utf-8
import torndb
import datetime
import httplib
import urllib

from tornado.escape import json_decode,json_encode

from constants.errorcode import Errorcode
from util.gip_exception import GipException
from util.solr_engine import SolrEngine

class DB(object):
    
    def __init__(self, application):

        self.mysql_test_read = application.db_conn['mysql']['test']['read']
        self.mysql_test_write = application.db_conn['mysql']['test']['write']
        
        self.mysql_account_read = application.db_conn['mysql']['account']['read']
        self.mysql_account_write = application.db_conn['mysql']['account']['write']
        
        self.mysql_article_read = application.db_conn['mysql']['nbarticle']['read']
        self.mysql_article_write = application.db_conn['mysql']['nbarticle']['write']
        
        self.solr_b = {}
        self.solr_b['article'] = application.db_conn['solr']['article']

        self.solr_article = SolrEngine('''http://%s%s'''%(application.db_conn['solr']['article']['url'],application.db_conn['solr']['article']['path']))
        #self.mongo_conn = application.mongo_conn
    
    
    def sample(self):
        
        try:
            sql = ''' select count(1) from sample'''
            result = self.mysql_test_write.query(sql)
        except:
            pass
        finally:
            
            return result[0]
    
    def sample_solr(self):
        return self.solr_article.query('*:*',start=0,rows=1) 

    def get_article_img_list(self,article_id,num):
        sql = '''select url2 as url from img where article_id = '%s' '''%article_id
        if num:
            sql = sql + 'limit %s'%num
        
        #print sql
        return self.mysql_article_read.query(sql)
        #return ['1.jpg','2.jpg']           

               
    def get_article(self,id):

        return self.solr_article.query('id:%s'%id,start=0,rows=1) 

    def search_article_by_keyword(self,keyword,start,limit):
        # 用空格给keyword分词
        kw_list = keyword.split(' ')
        q = ' and '.join(map(lambda x: 'title:%s'%x,kw_list))
        query_data = {
                'q':q.encode('utf8'),
                'wt':'json',
                'start':start,
                'rows':limit,
                'fl':'title and description and id',
                'indent':'true'}

        #print query_data
        #return self.solr_query('article',query_data)


        return self.solr_article.query(q,fields=['title','description','id'],start=start,rows=limit) 


    def register(self,account,type,password):
        
        sql = '''insert into user (email,mdn,password) value('%s','%s','%s')'''
        if type == 'email':
            sql = sql% (account,'',password)
        elif type == 'mdn':
            sql = sql% ('',account,password)
        info = json_encode({type:account})
        uid = self.mysql_account_write.execute(sql)
        #print sql	
        sql = '''insert into user_info(uid,info) value(%s,'%s')'''%(uid,info)
        info_id = self.mysql_account_write.execute(sql)
        #print sql
        return uid

       

    def check_password(self,account,type,password):
        sql = '''select id from user where `%s`='%s' and password='%s' limit 1'''%(type,account,password)
        uid = self.mysql_account_read.query(sql)[0]['id']  
        return uid


    def get_user_info(self,uid):
        sql = '''select info from user_info where uid = %s limit 1'''% uid
        info = self.mysql_account_read.query(sql)[0]['info']
        return info
 
    def solr_query(self,index,data):

        res = {}
        path = self.solr_b[index]['path'] + '''/select?''' + urllib.urlencode(data)
        try:
            httpClient = httplib.HTTPConnection(self.solr_b[index]['url'])
            httpClient.request("GET", path, '' , {})

            response = httpClient.getresponse()

            res = response.read()
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()
            return json_decode(res)
