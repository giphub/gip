#coding=utf-8
import torndb
import datetime
import httplib
import urllib

from tornado.escape import json_decode

from constants.errorcode import Errorcode
from util.gip_exception import GipException


class DB(object):
    
    def __init__(self, application):

        self.mysql_test_read = application.db_conn['mysql']['test']['read']
        self.mysql_test_write = application.db_conn['mysql']['test']['write']
        
        
        self.solr = {}
        self.solr['article'] = application.db_conn['solr']['article']

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
        data ={
        	'q':'title:幼儿园',
                'wt':'json',
                'start':10,
                'rows':50,
                'fl':'title',
                'indent':'true'}
        return self.solr_query('article',data)                

   
    def solr_query(self,index,data):

        res = {}
        path = self.solr[index]['path'] + '''select?''' + urllib.urlencode(data)
        try:
            httpClient = httplib.HTTPConnection(self.solr[index]['url'])
            httpClient.request("GET", path, '' , {})

            response = httpClient.getresponse()

            res = response.read()
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()
            return json_decode(res)
