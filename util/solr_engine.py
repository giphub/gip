#coding=utf-8

import solr

class SolrEngine(object):
    '''
        solr引擎，用于在solr cloud中添加、删除、更新、查询索引
    '''

    def __init__(self, url, timeout=30):
        '''
            初始化solr cloud的连接，默认超时时间为30秒
        '''
        self.s = solr.Solr(url, timeout=timeout)

    def close(self):
        '''
            关闭solr cloud的连接
        '''

        self.s.close()

    def add(self, doc, commit=True):
        '''
            向solr cloud添加一条索引，默认立即commit
        '''

        self.s.add(doc, commit=commit)

    def add_many(self, docs, commit=True):
        '''
            向solr cloud添加多条索引，默认立即commit
        '''

        self.s.add_many(docs, commit=commit)

    def delete(self, id=None, ids=None, commit=True):
        '''
            删除索引，根据id、id列表或者查询语句删除
        '''

        self.s.delete(id=id, ids=ids, commit=commit)

    def query(self, q, fields=None, sort=None, order='asc', start=0, rows=10):
        '''
            查询索引
        '''

        res = self.s.select(q=q, fields=fields, sort=sort, order=order, start=start, rows=rows)

        return res.results

    def commit(self):
        '''
        # 立即提交
        '''
        return self.s.commit()

if __name__ == '__main__':
    url = 'http://127.0.0.1:8983/solr/nb_article'
    engine = SolrEngine(url)
    #doc = {'rowkey': '3', 'reqtime': 123}
    #engine.add(doc)
    print engine.query('*:*', sort=['id desc'])
    #engine.delete(id=3)
