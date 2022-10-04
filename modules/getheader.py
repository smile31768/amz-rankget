#初始化selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def get_header(chromedriver_path):
    #无头模式
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--ignore-ssl-error')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-extensions')
    webbdriver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver_path)
    #访问亚马逊搜索页
    webbdriver.get('https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=python')
    region=webbdriver.find_element_by_id('glow-ingress-line2').text
    print(f"[get_region]Current Region: {region}")
    #region不存在则刷新
    if region == '':
        webbdriver.refresh()
        time.sleep(3)
        region=webbdriver.find_element_by_id('glow-ingress-line2').text
        print(f"[get_region]Current Region: {region}")
    #change zipcode
    print("[get_region]Change Region")
    time.sleep(2)
    webbdriver.find_element_by_id('glow-ingress-line2').click()
    time.sleep(1)
    webbdriver.find_element_by_id('GLUXZipUpdateInput').send_keys('10001')
    webbdriver.find_element_by_id('GLUXZipUpdate').click()
    time.sleep(1)
    #刷新页面
    webbdriver.refresh()
    #获取当前国家
    region=webbdriver.find_element_by_id('glow-ingress-line2').text
    print(f"[get_region]Current Region: {region}")
    time.sleep(2)
    #获取cookie
    cookie = webbdriver.execute_script("return document.cookie")
    user_agent = webbdriver.execute_script("return navigator.userAgent")
    webbdriver.quit()
    #获取user-agent
    return {'cookie':cookie,'user_agent':user_agent}

def get_norcookie():
    import requests
    url = "https://www.amazon.com/gp/bestsellers"
    headers={
        'Host': 'www.amazon.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'anti-csrftoken-a2z': 'gBtJDelwICZ60r+pGBgwbzjAf4Wr+LTRIoyWRyMAAAAMAAAAAGC1xeJyYXcAAAAA',
        'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    session = requests.session()
    response = session.get(url, headers=headers)
    cookie = response.cookies
    return cookie

if __name__ == '__main__':
    import os
    print(get_header(os.path.join(os.getcwd(),'chromedriver.exe')))