#coding=utf-8
'''
Created on 2013-10-24

'''
import logging

import tornado.web

# 引入公共服务
from constants.errorcode import Errorcode
from constants.constants import Constants
from constants.protocol import Protocol
from handler.base_handler import BaseHandler
from util.gip_exception import GipException

class MainHandler(BaseHandler):
    '''
           统一接收所有post请求，
           按照解析的protocol分交给不同模块进行处理，
           处理结果统一在此返回结果    
    '''

    
    @tornado.web.asynchronous
    def post(self):
        try:
            # 日志记录请求参数
            logging.info('记录日志')
            # 安全过滤并，读取请求内容，验证应用授权
            self.init_request()
            #分协议调用moldule处理
       
            module_class = Constants.MODULE_MAPPING.get(self.protocol)
            
            if not module_class:
                
                raise GipException(Errorcode.MODULE_DO_NOT_EXIST) 
            else:
                # 协议执行成功后调用各自所需的服务
                module = module_class(self) 
                self.response_body = module.process()
                
        except GipException, e:
            print e.errorcode   
            self.response_body = {"error":e.errorcode}      

        except e:
            # 捕获所有抛出的错误，并作相应处理。
            print e
            self.response_body = {"error":123}
            pass
        finally:
            
            #生成返回结果       
            self.write(self.response_body)
            self.finish()
            

