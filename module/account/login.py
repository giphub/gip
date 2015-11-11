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

from tornado.escape import json_decode,json_encode

@module(protocol=Protocol.ACCOUNT_LOGIN)
class ModuleSample(Processor):
    '''
    用户登录：
	用户填写用户名（邮箱/手机号）密码进行登陆。
	登陆过程：1.验证密码是否正确
		  2.如果正确则返回用户的基本信息及token（TODO）
        
    '''
    def __init__(self, handler):
        Processor.__init__(self, handler)
        
        
    def process(self):

        #raise LTException(Errorcode.ERROR_NONE)
        account = self.handler.request_body['params'].get('account',None)       
        type = self.handler.request_body['params'].get('type',None)
        password = self.handler.request_body['params'].get('password',None)	
        try:
            uid = self.db.check_password(account,type,password)
        except:
            raise GipException(Errorcode.ACCOUNT_LOGIN_FAIL)
        user_info = self.db.get_user_info(uid) 
        
        response = {}
        response['data'] = {}
        response['data']['code'] = Errorcode.ERROR_NONE
        response['data']['message'] =  "用户登陆成功"
        response['data']['uid'] = uid
        response['data']['info'] = json_decode(user_info)                              
        return response

 

 
