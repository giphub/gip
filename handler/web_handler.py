#coding=utf-8
'''
Created on 2015-10-24

'''
import logging

import tornado.web

# 引入公共服务
from constants.errorcode import Errorcode
from constants.constants import Constants
from constants.protocol import Protocol
from handler.base_handler import BaseHandler
from util.gip_exception import GipException

class WebHandler(tornado.web.RequestHandler):
    '''
           统一接收所有web页面请求，
           只负责页面显示，其内容也通过调用协议的方式实现
           
    '''


    def index(self):
        self.render('../template/index.html')

    def sample(self):
        name = self.get_argument('name','World!')
        self.render('../template/sample.html',name=name)

    @tornado.web.asynchronous
    def post(self):
        self.get()
    
    @tornado.web.asynchronous
    def get(self):
        try:
            # 日志记录请求参数
            #logging.info('记录日志')
            # 获取参数
            method = self.get_argument('m','index')
            eval('self.%s()'%method)
                
        except GipException, e:
            print e.errorcode   
            response_body = {"error":e.errorcode}      
            self.write(response_body)

        except e:
            # 捕获所有抛出的错误，并作相应处理。
            print e
            response_body = {"error":123}
            self.write(response_body)
        finally:
            if not self._finished: 
                self.finish()
            

