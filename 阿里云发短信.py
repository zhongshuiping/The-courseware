import sys
import urllib.request, urllib.parse, urllib.error
import base64
import hmac
from hashlib import sha1
import time
import uuid
import json
import ssl
import random


# 短信每条4分钱，可能只能发几十条了
# 代码没什么复杂的，只是用了一些大家以前没接触过的函数
# 使用别人的接口，所以只是根据别人的要求去处理Http请求

# 网址：https://dayu.aliyun.com/?utm_content=se_1057505
# 秘钥参数部分

access_key_id = 'LTAImvGW03KmxE3k';  # 自己申请的阿里云秘钥根据提示来
access_key_secret = 's41KvS5smfW2p1C629gOdCwXD036S7';  # 自己申请的阿里云秘钥，根据提示来
# server_address = 'https://sms.aliyuncs.com'
server_address = 'http://dysmsapi.aliyuncs.com/'  # 阿里云主机地址
# 定义参数   Action : SendSms发短信服务"product":"Dysmsapi"固定值 'SignName': 签名名称''TemplateCode': 短信模板编号
user_params = {'Action': 'SendSms', 'ParamString': '{"product":"Dysmsapi"}', 'SignName': 'Yangtze大学jdy',
               'TemplateCode': 'SMS_120406077'}
# Action 行为：SendSms发短信
# product : 产品接口 Dysmsapi(Dynamic send message api)动态发短信应用接口
# SignName: 签名名称（自己去阿里大于网站申请）
# TemplateCode: 短信模板编号（自己去阿里大于网站申请）


# 随机的验证码
check_code = str (random.randint (100000, 999999))
# 发送到哪个手机号码
sendto_tel = str(134xxx)


def percent_encode(encodeStr):
    """加号（+）替换成 %20、星号（*）替换成 %2A、%7E 替换回波浪号（~）"""
    encodeStr = str (encodeStr)
    # 将url进行url转码
    res = urllib.parse.quote (encodeStr.encode ('utf8'), '')
    # 阿里要求将url转码后url中的加号替换成%20，*号替换成2A%，~替换成%7E。
    res = res.replace ('+', '%20')
    res = res.replace ('*', '%2A')
    res = res.replace ('%7E', '~')
    return res


def compute_signature(parameters, access_key_secret):
    """处理签名秘钥信息"""
    # 将字典转换成列表，然后重新按字典的key对参数列表排序
    sortedParameters = sorted (list (parameters.items ()), key=lambda parameters: parameters[0])

    # 拼接参数信息
    canonicalizedQueryString = ''
    for (k, v) in sortedParameters:
        canonicalizedQueryString += '&' + percent_encode (k) + '=' + percent_encode (v)
    # 调用上面的函数，url编码并替换参数中的加号星号波浪号
    # 从第一个开始取是去掉第一个&符号。
    stringToSign = 'GET&%2F&' + percent_encode (canonicalizedQueryString[1:])
    print ("stringToSign:  " + stringToSign)

    # hmac加密算法对秘钥信息进行加密
    # 阿里要求签名采用HmacSHA1算法 + Base64,编码采用 UTF-8;
    h = hmac.new ((access_key_secret + '&').encode (encoding="utf-8"), stringToSign.encode ('utf-8'), sha1)
    signature = base64.encodestring (h.digest ()).strip ()

    return signature


def compose_url(user_params):
    """处理GET请求将参数加入，拼接url并且返回"""
    timestamp = time.strftime ("%Y-%m-%dT%H:%M:%SZ", time.gmtime (time.time ()))
    # 字典编辑参数
    parameters = { \
        'Format': 'JSON', \
        'Version': '2017-05-25', \
        'AccessKeyId': access_key_id, \
        'SignatureVersion': '1.0', \
        'SignatureMethod': 'HMAC-SHA1', \
        'SignatureNonce': str (uuid.uuid1 ()), \
        'RegionId': 'cn-hangzhou',
        'Timestamp': timestamp, \
        'PhoneNumbers': sendto_tel, \
        "TemplateParam": "{\"code\":\"" + check_code + "\"}", \
        }

    # 将自己主机相关数据和阿里秘钥接口的两部分数据都存放到一个字典里面
    for key in list (user_params.keys ()):
        parameters[key] = user_params[key]
    #处理秘钥
    signature = compute_signature (parameters, access_key_secret)
    parameters['Signature'] = signature
    # 拼接url
    url = server_address + "/?" + urllib.parse.urlencode (parameters)
    return url


def make_request(user_params, quiet=False):
    """发起请求,返回响应数据quiet参数为响应数据是否返回Json对象"""

    # 调用上面的拼接请求头函数
    url = compose_url (user_params)
    # 创建请求对象
    request = urllib.request.Request (url)
    try:
        # 创建ssl证书
        context = ssl._create_unverified_context ()
        # 使用urlib模块创建连接发送请求，带上ssl证书
        conn = urllib.request.urlopen (request, context=context)
        # 接收响应
        response = conn.read ().decode ('utf-8')
    except urllib.error.HTTPError as e:
        print ((e.read ().strip ()))
        raise SystemExit (e)
    try:
        # 将响应数据解析为json格式
        obj = json.loads (response)
        # 如果需要json对象就直接返回
        if quiet:
            return obj
    except ValueError as e:
        raise SystemExit (e)
    # json对象转换为String类型并输出到控制台
    json.dump (obj, sys.stdout, sort_keys=True, indent=2)
    print ("")


# 打印一下编码格式
print (sys.stdin.encoding)
# 调函数处理请求并发送
make_request (user_params)
