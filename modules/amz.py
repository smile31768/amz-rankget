import requests
from urllib.parse import quote

def get_html(keyword,page,cookie,user_agent):
    keyword = quote(keyword, 'utf-8')
    #cookie = "session-id=143-6578677-7135924; session-id-time=2082787201l; i18n-prefs=USD; skin=noskin; ubid-main=134-8522695-5287302; lc-main=en_US; csm-hit=tb:PBVN6JWWGZF40WEWPD5P+s-41HC8F79GH5QMGXZ1CV3|1664696562468&t:1664696562468&adb:adblk_no; session-token=Ung+R6P+t2eun4b81ysHT3AJPglTHFyfGcBTJ3sCOpGFjiAvjhR8CkauPSdKgZUBGmeKTbDjccM+0pM0v3QqHpWU4UGkBVdb+cGMy4vYy99TB99TqmDAkmpA7+RUbm5pEMnvcbKnnooTwIJsfufg322PhN30wVVXTAeS4FetwflvJrV0nDiYl8c7H9Pr/g2/ZRpiwVP0ahKZQrEt+fLLVQFE+bzmh07E"
    headers={
        'Host': 'www.amazon.com',
        'user-agent': user_agent,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'anti-csrftoken-a2z': 'gBtJDelwICZ60r+pGBgwbzjAf4Wr+LTRIoyWRyMAAAAMAAAAAGC1xeJyYXcAAAAA',
        'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        'cookie': cookie,
    }
    # get html
    url = f'https://www.amazon.com/s?k={keyword}&page={page}'
    #url = 'https://www.amazon.com/s?k=' + keyword + '&ref=nb_sb_noss'
    resp = requests.get(url=url, headers=headers)
    # return html
    return resp

if __name__ == '__main__':
    keyword = 'python'
    page = 1
    cookie = ""
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    html = get_html(keyword,page,cookie,user_agent)
    print(html.text)