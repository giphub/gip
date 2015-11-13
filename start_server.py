#coding=utf-8
'''
Created on 2015-04-14

'''

import logging
import os
import sys
import time
import traceback

from ConfigParser import ConfigParser
from tornado import httpserver, process
import tornado.ioloop
import tornado.web
import torndb


from handler.main_handler import MainHandler


class App(tornado.web.Application):
    '''
    继承tornado.web.Application
    
    '''
    
    def __init__(self,config):
        start=time.time()
        handlers = [
            (r"/", MainHandler),  
        ]
    
        settings = dict(gzip=True,
                    debug=False,)
        super(App, self).__init__(handlers, **settings)

        # 创建数据库链接
        self.db_conn = {'mysql':{},'mongodb':{},'redis':{},'solr':{}}
        self.build_db_connection(config,'mysql','test')
        self.build_db_connection(config,'mysql','account')
        self.build_db_connection(config,'mysql','nbarticle')
        self.build_db_connection(config,'solr','article')

        end = time.time()
        logging.info("......启动总耗时："+str((end-start)*1000)+"毫秒")
        print("......启动总耗时："+str((end-start)*1000)+"毫秒")
    
    def build_db_connection(self,config,type,name):
        '''
        创建数据库链接
        type为数据库种类 如mysql，mongo，redis之类，name为数据库标识名称
        配置文件中的mysql数据库配置通常是由type_name_read/write组成
        形如 mysql_account_read
        '''
        if type == 'mysql':
            self.db_conn[type][name] = {}
            self.db_conn[type][name]['read'] = self.build_mysql_db_connection(config,name,'read')
            self.db_conn[type][name]['write'] = self.build_mysql_db_connection(config,name,'write')
        elif type == 'mongodb':
            pass
        elif type == 'redis':
            pass
        elif type == 'solr':
            self.db_conn[type][name] = {}
            self.db_conn[type][name]['url'] , self.db_conn[type][name]['path'] = self.build_solr_db_connection(config,name)
         
   
    def build_solr_db_connection(self,config,name):
        '''
        添加solr的链接
        '''
        section = '_'.join(['solr',name])
        host = config.get(section,'host')
        port = config.get(section,'port')
        collection = config.get(section,'collection')
        url = host + ':' + port 
        path = '/solr/' + collection  
        return url,path


    def build_mysql_db_connection(self,config,name,opr):
        '''
        添加数据库链接
        '''
        section = '_'.join(['mysql',name,opr])
        host = config.get(section,'host')
        db = config.get(section,'database')
        user = config.get(section,'user')
        pwd = config.get(section,'password')
        return torndb.Connection(host=host, database=db, user=user, password=pwd,time_zone="+8:00")

def main():
    
    '''
    读取配置，启动服务
    '''
    config = ConfigParser()
    config.read('config.cfg')
    log_path = config.get("default", "logpath")
    num_processes = int(config.get("default", "num_processes"))
    port = int(config.get("default", "port"))
    
    # 初始化日志服务
    initLog(log_path)
    
    # 服务最大线程不超过cpu核数
    cpu_count=process.cpu_count()
    if num_processes>cpu_count:
        print("This server is only "+str(cpu_count)+" cores, input value is too large.")
        num_processes = 0
    
    # 启动服务    
    app = App(config)
    http_server = httpserver.HTTPServer(app)
    http_server.bind(port)
    http_server.start(num_processes)
    tornado.ioloop.IOLoop.instance().start()


def initLog(log_path):
    '''
    初始化日志系统，定义日格式等
    '''
    try:
        if os.path.exists(log_path)==False:
            os.makedirs(log_path)
    except:
        etype, evalue, tracebackObj = sys.exc_info()[:3]
        print("Type: " , etype)
        print("Value: " , evalue)
        traceback.print_tb(tracebackObj)
        
    track_log = log_path+'/track.log'    
    
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=track_log,
                filemode='w')
    
    #logging.debug('This is debug message')
    #logging.info('This is info message')
    #logging.warning('This is warning message')
    
 
if __name__ == "__main__":
    main()    

