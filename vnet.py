#!/usr/bin/env python
# -*- coding: utf-8 -*-

# E-mail: windcao@hotmail.com
import urlparse
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

__author__ = 'caojianfeng'

host_ip = '192.168.4.43'
host_port = 8880

get_base_path = "webbase/gets/"


def getFileContent(file_name):
    input = open(file_name, 'r')
    all_the_text = "empty"
    try:
        all_the_text = input.read()
    finally:
        input.close()
    return all_the_text


# http://app.u17.test/v3/app/android/phone/animation?argCon=0&page=XXX
# http://127.0.0.1:8880/v3/app/android/phone/animation?argCon=0&page=XXX
# 对应的文件路径：/v3/app/android/phone/animation
class VHTTPHandle(BaseHTTPRequestHandler):
    def do_GET(self):
        res = urlparse.urlsplit(self.path)
        self.protocal_version = "HTTP/1.1"

        self.send_response(200)

        self.send_header("Welcome", "Contect")

        self.end_headers()

        content = getFileContent(get_base_path+res.path)

        self.wfile.write(content)


def start_server(port):
    # http_server = HTTPServer(('[IP]', int(port)), VHTTPHandle)
    http_server = HTTPServer((host_ip, int(port)), VHTTPHandle)
    http_server.serve_forever()  # 设置一直监听并接收请求其中，IP为给localhost设定的访问地址


# -- main ---
if __name__ == '__main__':
    start_server(host_port)
