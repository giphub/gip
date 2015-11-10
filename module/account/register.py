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


@module(protocol=Protocol.ACCOUNT_REG)
class ModuleSample(Processor):
    '''
    账号注册：
	用户填写用户名（邮箱/手机号）密码进行注册。
	注册过程：1.用户名及md5加密之后的密码存入user表。
		  2.将用户的用户名及其他除密码之外的信息，以json格式写入user_info表，方便以后迁移到mongo
  
    '''
    def __init__(self, handler):
        Processor.__init__(self, handler)
        
        
    def process(self):

        #raise LTException(Errorcode.ERROR_NONE)
        account = self.handler.request_body['params'].get('account',None)       
        type = self.handler.request_body['params'].get('type',None)
        password = self.handler.request_body['params'].get('password',None)	
        uid = self.db.register(account,type,password)
        response = {}
        response['data'] = {}
        response['data']['code'] = Errorcode.ERROR_NONE
        response['data']['message'] =  "用户注册成功"
        response['data']['uid'] = uid
                                      
        return response

 

 
