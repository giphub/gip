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


@module(protocol=Protocol.ARTICLE_GETBYID)
class GetById(Processor):
    '''
    示例程序
  
    '''
    def __init__(self, handler):
        Processor.__init__(self, handler)
        
        
    def process(self):

        article_id = self.handler.request_body['params']['id']
                 
        response = {}
        response['data'] = {}
        response['data']['code'] = Errorcode.ERROR_NONE
        response['data']['message'] =  "article get by id 成功显示"
        response['data']['sample'] =self.db.get_article_by_id(article_id)['title']
                                      
        return response

 

 
