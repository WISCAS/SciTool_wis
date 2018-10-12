# -*- coding: utf-8 -*-
# @Author : Felix Wang
# @time   : 2018/8/13 22:13

# pip3 install pycurl
import pycurl
from io import BytesIO
import os


def test_website(url):
    c = pycurl.Curl()
    buffer = BytesIO()  # 创建缓存对象
    c.setopt(c.WRITEDATA, buffer)  # 设置资源数据写入到缓存对象
    c.setopt(c.URL, url)  # 指定请求的URL
    c.setopt(c.MAXREDIRS, 5)  # 指定HTTP重定向的最大数
    c.perform()  # 执行

    http_code = c.getinfo(pycurl.HTTP_CODE)  # 返回的HTTP状态码
    dns_resolve = c.getinfo(pycurl.NAMELOOKUP_TIME)  # DNS解析所消耗的时间
    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)  # 建立连接所消耗的时间
    http_pre_trans = c.getinfo(pycurl.PRETRANSFER_TIME)  # 从建立连接到准备传输所消耗的时间
    http_start_trans = c.getinfo(pycurl.STARTTRANSFER_TIME)  # 从建立连接到传输开始消耗的时间
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)  # 传输结束所消耗的总时间
    http_size_download = c.getinfo(pycurl.SIZE_DOWNLOAD)  # 下载数据包大小
    http_size_upload = c.getinfo(pycurl.SIZE_UPLOAD)  # 上传数据包大小
    http_header_size = c.getinfo(pycurl.HEADER_SIZE)  # HTTP头部大小
    http_speed_downlaod = c.getinfo(pycurl.SPEED_DOWNLOAD)  # 平均下载速度
    http_speed_upload = c.getinfo(pycurl.SPEED_UPLOAD)  # 平均上传速度
    http_redirect_time = c.getinfo(pycurl.REDIRECT_TIME)  # 重定向所消耗的时间

    print('HTTP响应状态： %d' % http_code)
    print('DNS解析时间：%.2f ms' % (dns_resolve * 1000))
    print('建立连接时间： %.2f ms' % (http_conn_time * 1000))
    print('准备传输时间： %.2f ms' % (http_pre_trans * 1000))
    print("传输开始时间： %.2f ms" % (http_start_trans * 1000))
    print("传输结束时间： %.2f ms" % (http_total_time * 1000))
    print("重定向时间： %.2f ms" % (http_redirect_time * 1000))
    print("上传数据包大小： %d bytes/s" % http_size_upload)
    print("下载数据包大小： %d bytes/s" % http_size_download)
    print("HTTP头大小： %d bytes/s" % http_header_size)
    print("平均上传速度： %d k/s" % (http_speed_upload / 1024))
    print("平均下载速度： %d k/s" % (http_speed_downlaod / 1024))

def ping(url):
    result = os.system('ping '+ url)
    if result == 0:
        # a.status_append('网络连接正常')
        print(r'网络连接正常')
    else:
        # a.status_append('网络异常，请检查网络')
        print(r'网络连接异常')


if __name__ == '__main__':
    test_url = 'www.baidu.com'
    ping(test_url)