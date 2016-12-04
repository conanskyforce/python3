# -*- coding:utf-8 -*-
import requests


def get_key_info(response,*args,**kw):
	"""回调函数
	"""
	print (response.headers['Content-Type'])

def main():

	url="http://taobao.com"
	requests.get(url,hooks=dict(response=get_key_info))


main()