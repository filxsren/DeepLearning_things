
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
import time


# 输入参数为要分析的 html 文件名，返回值为对应的 BeautifulSoup 对象
def create_doc_from_filename(filename):
	fo = open(filename, "r", encoding='utf-8')
	html_content = fo.read()
	fo.close()
	doc = BeautifulSoup(html_content, "lxml")
	return doc


url = "https://www.duitang.com/search/?kw=fufu&type=feed"




browser = webdriver.Edge()
# 通过网页地址打开网页，此时会弹出浏览器，并加载相应的网页
browser.get(url=url)

for i in range(10):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(0.5)
	
# result = download_content(url)
# save_to_file("tips3.html", result)




# doc = create_doc_from_filename("tips3.html")
sum = 0 
doc = BeautifulSoup(browser.page_source, "lxml")
images = doc.find_all("img")
for i in images:
    sum+=1
    src = i["src"]
    filename = src.split("/")[-1]
    if filename[-4:] == "webp":
        filename = filename[:-5]
    print(i["src"])
    urlretrieve(src, "tips_3/" + filename)
    print(sum)