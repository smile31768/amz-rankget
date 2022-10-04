import re

def get_rank(asin,html):
    rank_data = re.findall(r'/dp/B.{0,10}/ref=sr_\d{1,2}_\d{1,3}', html)
    rank_data = list(set(rank_data))
    for rank in rank_data:
        if re.search(r'.*' + asin + '.*', rank) is not None:
            return re.search(r'\d{1,3}$', rank).group()
        
if __name__ == '__main__':
    # test
    asin = 'B07VJZQ9XQ'
    html = open('B07VJZQ9XQ.html').read()
    print(get_rank(asin, html))