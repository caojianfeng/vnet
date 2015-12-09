#!/usr/bin/env python
# -*- coding: utf-8 -*-

# E-mail: windcao@hotmail.com
# https://github.com/caojianfeng/vnet
import os
import codecs
import urlparse

from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import shutil
import sys

__author__ = 'caojianfeng'

host_ip = '192.168.36.106'
host_port = 8880

get_base_path = "webbase/gets"


def get_file_content(file_name):
    input = codecs.open(file_name, 'r', 'utf-8')
    all_the_text = "empty"
    try:
        all_the_text = input.read()
    finally:
        input.close()
    return all_the_text


# http://192.168.36.106:8880/v3/app/android/phone/animation?argCon=0&page=XXX
# 对应的文件路径：/v3/app/android/phone/animation
class VHTTPHandle(SimpleHTTPRequestHandler):
    def do_GET(self):
        res = urlparse.urlsplit(self.path)
        self.protocal_version = "HTTP/1.1"
        self.send_response(200)
        self.send_header("Welcome", "Contect")
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        file_path = get_base_path + res.path
        if os.path.exists(file_path):
            content = get_file_content(file_path)
            print content
            print content.encode('raw_unicode_escape')
            self.wfile.write(content.encode('raw_unicode_escape'))


def start_server(port):
    # http_server = HTTPServer(('[IP]', int(port)), VHTTPHandle)
    reload(sys)
    sys.setdefaultencoding('utf-8')
    http_server = HTTPServer((host_ip, int(port)), VHTTPHandle)
    http_server.serve_forever()  # 设置一直监听并接收请求其中，IP为给localhost设定的访问地址


# -- main ---
if __name__ == '__main__':
    start_server(host_port)
