'''
破解有道词典
'''
from urllib import parse
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

data = {
    "i": "girl",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "15444134838310",
    "sign": "e54dc032b685279dae1590dca9ca959e",
    "ts": "1544413483831",
    "bv": "652e7a11d3f7ccf6ac9350133b8efe77",
    "doctype": "json",
    "from": "AUTO",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTIME",
    "typoResult":" false"
}

# 参数data需要是bytes格式
data = parse.urlencode(data).encode()

headers = {
    Accept: application/json, text/javascript, */*; q=0.01
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: no-cache
    Connection: keep-alive
    Content-Length: 254
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    Cookie: P_INFO=chensunxu@163.com|1537322517|0|other|00&99|fuj&1535709308&urs#fuj&350200#10#0#0|&0||chensunxu@163.com; OUTFOX_SEARCH_USER_ID=-961420222@120.36.144.199; OUTFOX_SEARCH_USER_ID_NCOO=1819876408.684289; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abc9iPYfbahhrb5XVnwEw; ___rl__test__cookies=1544413483822
    Host: fanyi.youdao.com
    Origin: http://fanyi.youdao.com
    Pragma: no-cache
    Referer: http://fanyi.youdao.com/
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36
    X-Requested-With: XMLHttpRequest
}