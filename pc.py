import urllib.parse
import json
import requests,re,time 
import jsonpath

#url='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1698416001888_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MTEsMCwxLDMsMiw2LDQsNSw4LDcsOQ%3D%3D&ie=utf-8&sid=&word=arduino+uno'.format(i)

#response = requests.get(url)

#print(response)

import re,requests,time#导入所需要的库



detail_urls = []#存储图片地址

for i in range(1,400,20):#20页一张
    url ='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1698416001888_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MTEsMCwxLDMsMiw2LDQsNSw4LDcsOQ%3D%3D&ie=utf-8&sid=&word=arduino+uno'.format(i)
	response = requests.get(url,timeout = (3,7))#设置请求超时时间3-7秒
	content = response.content.decode('utf-8')#使用utf-8进行解码
	detail_url = re.findall('"objURL":"(.*?)"',content,re.DOTALL)#re.DOTALL忽略格式#匹配objURL的内容,大部分为objURL或URL
	detail_urls.append(detail_url)#将获取到的图片地址保存在之前定义的列表中
	response = requests.get(url)#请求网站
	content = response.content
b = 0#图片第几张
for page in detail_urls:
	for url in page:
		try:
			print('获取到{}张图片'.format(i))
			response = requests.get(url)
			content = response.content
			if url[-3:] == 'jpg':
				with open('保存的地址{}.jpg'.format(b),'wb') as f:
				f.write(content)
			elif url[-4:] == 'jpeg':
				with open('保存的地址{}.jpeg'.format(b),'wb') as f:
				f.write(content)
			elif url[-3:] == 'png':
				with open('保存的地址{}.pon'.format(b),'wb') as f:
				f.write(content)
			else:
				continue
				
		except:
			print('超时')
		b +=1

