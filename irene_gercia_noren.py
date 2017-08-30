#irene_gercia_noren.py
import requests
from bs4 import BeautifulSoup
import re
import urllib.request

def get_picture_url(url):
	res = requests.get(url)
	res.encoding = 'utf-8'
	soup = BeautifulSoup(res.text,'html.parser')
	img = str(soup.select('div.content.container img')[0])
	picture = re.compile('img src="(.*?)"x*?')
	pic = re.findall(picture,img)[0]
	return(pic)

def main():
	for i in range(1,25):
		page = '_' + str(i)
		url = 'http://www.sanzei.com/beauty/190126' + page + '.html'
		imgurl = get_picture_url(url)
		urllib.request.urlretrieve(imgurl,'/home/hjl092868/ningge_xiaozhan/%s.jpg'%i)

if __name__ == '__main__':
	main()