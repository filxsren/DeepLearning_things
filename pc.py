
import urllib3

# 第一个函数，用来下载网页，返回网页内容
# 参数 url 代表所要下载的网页网址。
# 整体代码和之前类似
def download_content(url):
	http = urllib3.PoolManager()
	response = http.request("GET", url)
	response_data = response.data
	html_content = response_data.decode()
	return html_content
# 第二个函数，将字符串内容保存到文件中
# 第一个参数为所要保存的文件名，第二个参数为要保存的字符串内容的变量

def save_to_file(filename, content):
	fo = open(filename, "w", encoding="utf-8")
	fo.write(content)
	fo.close()


from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

import time
from PIL import Image
import torchvision.transforms as transforms


# 输入参数为要分析的 html 文件名，返回值为对应的 BeautifulSoup 对象
def create_doc_from_filename(filename):
	fo = open(filename, "r", encoding='utf-8')
	html_content = fo.read()
	fo.close()
	doc = BeautifulSoup(html_content, "lxml")
	return doc


url = "https://www.duitang.com/search/?kw=miku&type=feed"

browser = webdriver.Edge()

# opt = ChromeOptions()            # 创建Chrome参数对象
# opt.headless = True              # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
# driver = webdriver.Chrome()
# driver.get("网站")
# a1 = driver.find_element(By.CSS_SELECTOR,'#livenews-id-1-202301272620081211 > div.media-content > h2 > a').text
# print(a1)

# 通过网页地址打开网页，此时会弹出浏览器，并加载相应的网页
browser.get(url=url)

for i in range(10):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(0.5)

browser.find_element(By.CLASS_NAME,'woo-nxt').click()

# browser.find_elements().click()
# result = download_content(url)
# save_to_file("tips3.html", result)




# doc = create_doc_from_filename("tips3.html")
sum = 0 
doc = BeautifulSoup(browser.page_source, "lxml")
images = doc.find_all("img")
for i in images:
	sum+=1
	try:
		src = i["src"]
		if int(i["height"])>30:
			filename = src.split("/")[-1]
			if filename[-4:] == "webp":
				filename = filename[:-5]
			print(i["src"])
			if("png" in filename):
				n=-3
			if("gif" in filename):
				n=-3
			if("jpg" in filename):
				n=-3
			if("jpeg" in filename):
				n=-4
			urlretrieve(src, "tips/" + str(sum) +"."+ filename[n:])
			print(sum)
			time.sleep(0.3)
		if sum == 100:
			break
	except:
		print("feild")
	# src = i["src"]
	# if int(i["height"])>30:
	# 	filename = src.split("/")[-1]
	# 	if filename[-4:] == "webp":
	# 		filename = filename[:-5]
	# 	print(i["src"])
	# 	if("png" in filename):
	# 		n=-3
	# 	if("gif" in filename):
	# 		n=-3
	# 	if("jpg" in filename):
	# 		n=-3
	# 	if("jpeg" in filename):
	# 		n=-4
	# 	urlretrieve(src, "tips/" + str(sum) +"."+ filename[n:])
	# 	print(sum)
	# 	time.sleep(0.3)
	if sum == 100:
		break

