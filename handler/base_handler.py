#coding=utf-8
'''
Created on 2013-11-14

'''

# python包
import time

# 第三方库包
import tornado.web
from tornado.escape import json_decode
# 自有文件
from constants.constants import Constants
from constants.errorcode import Errorcode
from constants.protocol import Protocol
from service.db import DB

class BaseHandler(tornado.web.RequestHandler):
    '''
    处理handler中共用的服务，
    本模块主要是提供方法实现，
    并不负责请求处理的业务逻辑
    '''
    
    def __init__(self, *request, **kwargs):
        super(BaseHandler, self).__init__(request[0], request[1])

        # 初始化请求参数
        self.api_version = 1
        self.protocol = 0
        self.timestamp = time.time()
        self.request_body = {}       
  
        # 初始化数据库、缓存、日志、等数据连接
        
        self.db = DB(self.application)
        
    def get(self):
        self.write('Server is running...')
        self.finish()
    
    @tornado.web.asynchronous
    def post(self):
        '''
        main_handler中需要复写这个方法，处理协议的请求
        '''
        self.finish()
        
    def init_request(self):
        ''' 
        读取并过滤请求参数
        '''
        request_headers = self.request.headers
        self.request_body = json_decode(self.request.body)
        
        self.protocol = self.request_body['protocol']
        
    
