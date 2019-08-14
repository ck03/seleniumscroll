from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import json


chrome_options = Options()
# 沒有這一行會自動開啟瀏覽器
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'D:\Study\Python2\chromedriver\chromedriver.exe')
driver.get("https://sj.qq.com/myapp/category.htm?orgame=1")

ret1 = None
item = {}
result_list = []
result_dict ={}
while True:
    wait = WebDriverWait(driver, 2)
    # # VIP，内容加载完成后爬取
    wait.until(
        lambda driver: driver.find_element_by_xpath("//div[@class='category-wrapper clearfix']/div[@class='main']/ul/li"))

    ret1 = driver.find_elements_by_xpath("//div[@class='category-wrapper clearfix']/div[@class='main']/ul/li")
    print(len(ret1))
    #  用find_element(s)方法判断元素是否存在 ,判斷元素是否存在elements 要加 s
    a = driver.find_elements_by_xpath("//div[@class='category-wrapper clearfix']/div[@class='main']/div[@class='load-more']/div[@class='load-more-btn']/a")
    if len(a) == 0:
        print("加載完成已經到頁面最底部了")
        for li in ret1:
            item["url"] = li.find_element_by_xpath("./div[@class='app-info clearfix']/a").get_attribute("href")
            item["imgurl"] = li.find_element_by_xpath("./div[@class='app-info clearfix']/a/img").get_attribute("src")
            item["title"] = li.find_element_by_xpath(
                "./div[@class='app-info clearfix']/div[@class='app-info-desc']/a").text
            item["size"] = li.find_element_by_xpath(
                "./div[@class='app-info clearfix']/div[@class='app-info-desc']/span[@class='size']").text
            item["download"] = li.find_element_by_xpath(
                "./div[@class='app-info clearfix']/div[@class='app-info-desc']/span[@class='download']").text
            result_list.append(item)
            item = {}
        result_dict["result"] = result_list
        print(result_dict)
        with open("應用寶.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(result_dict, ensure_ascii=False, indent=2))
        break
    else:
        a = driver.find_element_by_xpath("//div[@class='category-wrapper clearfix']/div[@class='main']/div[@class='load-more']/div[@class='load-more-btn']/a")
        print(a.text)
        # x = ret1[0].find_element_by_xpath("./div[@class='app-info clearfix']/a")
        # print(x.get_attribute("href"))
        print("*"*100)
        # 拖動到可见的元素去, 因為它是滾動頁面往下,所以此動作是在模擬頁面往下移到目前最後一個元素,代表頁面在滾動
        driver.execute_script('arguments[0].scrollIntoView();', ret1[-1])
        time.sleep(3)

driver.quit()

