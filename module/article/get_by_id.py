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


@module(protocol=Protocol.ARTICLE_GET_BY_ID)
class GetById(Processor):
    '''
    示例程序
  
    '''
    def __init__(self, handler):
        Processor.__init__(self, handler)
        
        
    def process(self):

        article_id = self.handler.request_body['params']['id']
        
        res = self.db.get_article(article_id)
       
        # process datatime format
        #article = self.filter_db_res(article)     
   
        response = {}
        response['data'] = {}
        response['data']['code'] = Errorcode.ERROR_NONE
        response['data']['message'] =  "article get by id 成功显示"
        response['data']['result'] = res
                                      
        return response

 

 
