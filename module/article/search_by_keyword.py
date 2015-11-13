#coding=utf-8
'''
Created on 2013-10-24

'''
import datetime
from constants.errorcode import Errorcode
from constants.constants import Constants
from constants.protocol import Protocol
from module.base_processor import Processor
from module.base_processor import module
from util.gip_exception import GipException 


@module(protocol=Protocol.ARTICLE_SEARCH_BY_KEYWORD)
class SearchByKeyword(Processor):
    '''
    示例程序
  
    '''
    def __init__(self, handler):
        Processor.__init__(self, handler)
        
        
    def process(self):

        keyword = self.handler.request_body['params']['keyword']
        limit = self.handler.request_body['params'].get('limit',10)
        start = self.handler.request_body['params'].get('start',0)
        
        res = self.db.search_article_by_keyword(keyword,start,limit)
        res = self.filter_db_res(res)     
		
        res = self.add_img(res,1)
	 
        response = {}
        response['data'] = {}
        response['data']['code'] = Errorcode.ERROR_NONE
        response['data']['message'] =  "ok"
        response['data']['result'] = res
                                      
        return response

 

 
