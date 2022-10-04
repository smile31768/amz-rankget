from modules.amz import get_html
from modules.get_rank import get_rank
from modules.csvcreate import create_csv, write_csv
from modules.getheader import get_header
import os, time, sys
from modules.chromedrive import check_update_chromedriver

# 初始化
page=1
print('正在初始化环境...')
print("正在检查chromedriver环境...")
location=os.getcwd()+"\\modules\\"
print(check_update_chromedriver(location))
try:
    print("正在获取header...如果在此处需要停止，请按Ctrl+C")
    head = get_header(location+"chromedriver.exe")
    cookie = head['cookie']
    user_agent = head['user_agent']
    print('初始化成功！')
    time.sleep(3)
    os.system('cls')
except:
    print('初始化失败！')
    exit()
#检测keywowords.txt是否存在
if not os.path.exists('keywords.txt'):
    #不存在则创建
    with open('keywords.txt', 'w') as f:
        f.write('')
        f.close()
        print('keywords.txt创建成功，请输入关键词')
os.system('notepad keywords.txt')
keywords = open("keywords.txt").read().splitlines()
print(f"keywords: {keywords}")
asin = input('请输入asin：')
#删除已有的csv
if os.path.exists(asin+'.csv'):
    os.remove(asin+'.csv')
create_csv(['keyword', 'rank', 'page'], asin+'.csv')
while True:
    unprocessed_keywords=[]
    for keyword in keywords:
        res = get_html(keyword,page,cookie,user_agent)
        #print(f"status_code: {res.status_code}")
        rank=get_rank(asin, res.text)
        if rank is None:
            print(f'ASIN: {asin} 在{keyword}的首页中未找到自然流量位')
        else:
            print(f"ASIN: {asin} 在{keyword}中的首页自然排名是：{rank}")
        # save res.text to a file
        #with open(asin+'-'+keyword+'.html', 'w', encoding='utf-8') as f:
        #    f.write(res.text)
        #    print('搜索出来的网页已保存至'+asin+'-'+keyword+'.html')
        # save rank to csv
        if res.status_code == 503:
            write_csv([keyword,'code:503'], asin+'.csv')
            print('503错误')
        else:
            if rank is None:
                unprocessed_keywords.append(keyword)
                print('结果为空')
            else:
                write_csv([keyword, rank, page], asin+'.csv')
                print('搜索完成，结果已保存至'+asin+'.csv')
    print(f"第{page}页搜索完成")
    print(f"未找到的关键词：{unprocessed_keywords}")
    if input('是否继续搜索下一页？(y/n)') == 'y':
        page+=1
        keywords=unprocessed_keywords
    else:
        for unprocessed_keyword in unprocessed_keywords:
            write_csv([unprocessed_keyword, 'NOT FOUND'], asin+'.csv')
        break