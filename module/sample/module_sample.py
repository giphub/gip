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


@module(protocol=Protocol.SAMPLE_MODULE_SAMPLE)
class ModuleSample(Processor):
    '''
    示例程序
  
    '''
    def __init__(self, handler):
        Processor.__init__(self, handler)
        
        
    def process(self):

        #raise LTException(Errorcode.ERROR_NONE)
       
        solr_res = self.db.sample_solr()
        #print solr_res         
        solr_res = self.filter_db_res(solr_res)
        response = {}
        response['data'] = {}
        response['data']['code'] = Errorcode.ERROR_NONE
        response['data']['message'] =  "module sample 成功显示"
        response['data']['sample'] = self.db.sample()
        response['data']['sample_solr'] =  solr_res
                                      
        return response

 

 
