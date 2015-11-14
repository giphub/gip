#coding=utf-8
'''
Created on 2015-10-24

'''
import logging
import urllib2
import tornado.web

# 引入公共服务
from constants.errorcode import Errorcode
from constants.constants import Constants
from constants.protocol import Protocol
from handler.base_handler import BaseHandler
from util.gip_exception import GipException

from tornado.escape import json_encode,json_decode


class WebHandler(BaseHandler):
    '''
           统一接收所有web页面请求，
           只负责页面显示，其内容也通过调用协议的方式实现
           
    '''

    def search(self):
        
        keyword = self.get_argument('wd',None)
        if keyword:
            start = self.get_argument('start',0)
            limit = self.get_argument('limit',10)
            body = {"protocol":Protocol.ARTICLE_SEARCH_BY_KEYWORD,"params":{"keyword":keyword,"start":start,"limit":limit}}
            response = self._api(body,{})
            search_result = response['data']['result']
        
        else:
            search_result = []
        self.render('../template/search.html',sr = search_result)

    def article(self):
        article_id = self.get_argument('aid','')
        body = {"protocol":Protocol.ARTICLE_GET_BY_ID,"params":{"id":article_id}}
        response = self._api(body,{}) 
        article = response['data']['result'][0]
        
        self.render('../template/article.html', article = article)
    
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
            

    def _api(self,body,headers):
        # 调用module处理协议
        self.request_body = body
        self.protocol = self.request_body['protocol']
        module_class = Constants.MODULE_MAPPING.get(self.protocol)
        
        if not module_class:
            raise GipException(Errorcode.MODULE_DO_NOT_EXIST)
        else:
            module = module_class(self)
            return  module.process()
            


