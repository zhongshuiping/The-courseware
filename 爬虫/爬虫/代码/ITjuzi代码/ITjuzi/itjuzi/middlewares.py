# coding:utf8



# Start your middleware class

#from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from settings import USER_AGENTS
import random
import time
import requests
import base64


# User-Agetn 下载中间件
class RandomUserAgent(object):
    def process_request(self, request, spider):
        # 这句话用于随机选择user-agent
        user_agent = random.choice(USER_AGENTS)
        date = time.strftime(u"%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
        #print user_agent
        request.headers.setdefault('User-Agent', user_agent)
        #request.headers.setdefault('If-Modified-Since', date)

class RandomProxy(object):
    def __init__(self):
        #self.proxy_list = ["121.40.108.76:80", "121.8.243.51:8888","221.204.116.169:9797","112.95.205.29:8888","183.31.254.57:9797","221.204.116.211:9797"]
        self.proxy_auth = "mr_mao_hacker:sffqry9r"
        self.proxy_api = "http://dps.kuaidaili.com/api/getdps/?orderid=958655825381063&num=50&ut=1&sep=3"
        self.proxy_list = requests.get(self.proxy_api).text.split()

    def process_request(self, request, spider):
        proxy = random.choice(self.proxy_list)
        base64_userpass = base64.b64encode(self.proxy_auth)
        #print proxy
        request.meta['proxy'] = "http://" + proxy
        #if self.proxy_auth != None:
        request.headers['Proxy-Authorization'] = "Basic " + base64_userpass


#class ProxyMiddleware(object):
    # overwrite process request
    #def process_request(self, request, spider):
        # Set the location of the proxy
    #    sql = 'select ip,port from t_proxy_ip t where t.is_valid =1'
    #    result = SqlUtil.query_all(sql)
    #    ip_port = random.choice(result)
    #    logging.info(ip_port)
    #    request.meta['proxy'] = "http://{0}:{1}".format(ip_port['ip'], ip_port['port'])
        # # Use the following lines if your proxy requires authentication
        # proxy_user_pass = "USERNAME:PASSWORD"
        # # setup basic authentication for the proxy
        # encoded_user_pass = base64.encodestring(proxy_user_pass)
        # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
