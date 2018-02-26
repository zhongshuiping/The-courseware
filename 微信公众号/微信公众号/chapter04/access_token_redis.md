# coding:utf-8

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import hashlib
import xmltodict
import time
import tornado.gen
import json
import datetime
import redis

from tornado.web import RequestHandler
from tornado.options import define, options
from tornado.httpclient import AsyncHTTPClient, HTTPRequest

WECHAT_TOKEN = "itcast"
WECHAT_APPID = "wx36766f74dbfeef15"
WECHAT_APPSECRET = "aaf6dbca95a012895eb570f0ba549ee5"

define("port", default=8080, type=int)

class AccessToken(object):
    """微信接口调用Token"""

    redis = None

    @classmethod
    @tornado.gen.coroutine
    def update_access_token(cls):
        """更新access_token"""
        client = AsyncHTTPClient()
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (WECHAT_APPID, WECHAT_APPSECRET)
        resp = yield client.fetch(url)
        print resp.body
        ret = json.loads(resp.body)
        token = ret.get("access_token")
        cls.redis.setex("wx_access_token", 7000, token)
        raise tornado.gen.Return(token)

    @classmethod
    def get_access_token(cls):
        """获取access_token"""
        access_token = cls.redis.get("wx_access_token")
        if not access_token:
            access_toke = cls.update_access_token()
        return access_token

class WeChatBaseHandler(RequestHandler):
    def prepare(self):
        signature = self.get_argument("signature")
        timestamp = self.get_argument("timestamp")
        nonce = self.get_argument("nonce")
        tmp = [WECHAT_TOKEN, timestamp, nonce]
        tmp.sort()
        tmp = "".join(tmp)
        tmp = hashlib.sha1(tmp).hexdigest()
        if tmp != signature:
            self.send_error(403)

class WeChatHandler(WeChatBaseHandler):
    """微信接入接口"""
    def get(self):
        """开发者验证接口"""
        echostr = self.get_argument("echostr")
        self.write(echostr)

    def post(self):
        """收发消息接口"""
        req_xml = self.request.body
        req = xmltodict.parse(req_xml)['xml']
        msg_type = req.get("MsgType")
        if "text" == msg_type:
            resp = {
                "ToUserName":req.get("FromUserName", ""),
                "FromUserName":req.get("ToUserName", ""),
                "CreateTime":int(time.time()),
                "MsgType":"text",
                "Content":req.get("Content", "")
            }
        elif "voice" == msg_type:
            resp = {
                "ToUserName":req.get("FromUserName", ""),
                "FromUserName":req.get("ToUserName", ""),
                "CreateTime":int(time.time()),
                "MsgType":"text",
                "Content":req.get("Recognition", u"未识别")
            }
        elif "event" == msg_type:
            if "subscribe" == req.get("Event"):
                resp = {
                     "ToUserName":req.get("FromUserName", ""),
                    "FromUserName":req.get("ToUserName", ""),
                    "CreateTime":int(time.time()),
                    "MsgType":"text",
                    "Content":u"感谢您的关注！"
                }
            else:
                resp = None
        else:
            resp = {
                "ToUserName":req.get("FromUserName", ""),
                "FromUserName":req.get("ToUserName", ""),
                "CreateTime":int(time.time()),
                "MsgType":"text",
                "Content":"I love you, itcast!"
            }
        if resp:
            resp_xml = xmltodict.unparse({"xml":resp})
        else:
            resp_xml = ""
        self.write(resp_xml)

class MediaHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        access_token = AccessToken.get_access_token()
        url = "https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token=%s" % access_token
        client = AsyncHTTPClient()
        req_body = {
            "type":"video",
            "offset":0,
            "count":20
        }
        req = HTTPRequest(url, method="POST", body=json.dumps(req_body))
        resp = yield client.fetch(req)
        self.write(resp.body)


class Application(tornado.web.Application):
    def __init__(self):
        handlers =  [
            (r"/wechat", WeChatHandler),
            (r"/media", MediaHandler)
        ]
        super(Application, self).__init__(handlers)
        self.redis = redis.StrictRedis(host="127.0.0.1", port="6379") 
        AccessToken.redis = self.redis

def main():
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()