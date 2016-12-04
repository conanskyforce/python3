# -*- coding:utf-8 -*-

import requests
def download_image():
	'''demo:下载图片
	'''
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
	url = 'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1480822989&di=5cd2ec52cd7720bcf1eca1ca77850db4&src=http://b.hiphotos.baidu.com/image/pic/item/d009b3de9c82d15825ffd75c840a19d8bd3e42da.jpg'
	response = requests.get(url,headers=headers,stream=True)
	
	with open('demo1.jpg','wb') as fd:
		for chunk in response.iter_content(128):
			fd.write(chunk)

download_image()