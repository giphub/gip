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
        start_id = self.handler.request_body['params']['start']
        limit_size = self.handler.request_body['params']['limit']
                
        articles = self.db.get_article_summary_by_keyword_in_title(keyword,start_id,limit_size)

        articles = self.filter_db_res(articles)     
 
        response = {}
        response['data'] = {}
        response['data']['code'] = Errorcode.ERROR_NONE
        response['data']['message'] =  "article get by keyword 成功显示"
        response['data']['article'] = articles
                                      
        return response

 

 
