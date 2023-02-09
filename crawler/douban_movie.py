# -*-coding:utf8-*-
import argparse

import requests
from bs4 import BeautifulSoup
import time
import random

user_agent = [
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
"Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
"Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
"UCWEB7.0.2.37/28/999",
"NOKIA5700/ UCWEB7.0.2.37/28/999",
"Openwave/ UCWEB7.0.2.37/28/999",
"Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
]
# headers = {'User-Agent': random.choice(user_agent)}

# 本地测试，关闭代理
# proxies = {'http': 'ADSL.NO.SOHU.COM:80', 'https': 'ADSL.NO.SOHU.COM:80'}
proxies = {}
# proxies = {'https': 'https://221.122.91.61:80'}

def spider(id):
    url = "https://movie.douban.com/subject/" + str(id) + "/"
    # url = "https://movie.douban.com/subject/{douban_id}/".format(douban_id=str(id))
    print(url)
    head_random = {
        # 'User-Agent': ua.random
        'User-Agent': random.choice(user_agent)
    }
    print(head_random)

    try_num = 1
    code = "-1"
    while True:
        try:
            if try_num > 30:
                break
            r = requests.get(url, timeout=5, proxies=proxies, headers=head_random, verify=True, allow_redirects=False)
            # print(r.text)
            code = str(r.status_code)
            if r.status_code == 200 and "sec.douban.com" not in r.text:
                break
            elif r.status_code == 404:
                break
            else:
                time.sleep(random.gauss(0.3, 0.05))
                try_num += 1
        except Exception as e:
            print(code, e)
    soup = BeautifulSoup(r.text, 'html.parser')
    rating_average = '0'
    ratings_count = '0'
    reviews_count = '0'
    comments_count = '0'
    rating_1 = '0'
    rating_2 = '0'
    rating_3 = '0'
    rating_4 = '0'
    rating_5 = '0'
    try:
        comment = soup.find_all('span', 'pl')
        comment_j = 1
        for i in comment:
            if i.a and i.a.string and '条' in i.a.string:
                comments_counts = i.a.string.split(' ')
                count = comments_counts[1]
                if comment_j == 1:
                    comments_count = count
                if comment_j == 2:
                    reviews_count = count
                comment_j += 1
    except Exception as e:
        print("exception_id=" + id, e)
    if comments_count == '0':
        print(r.text)
    try:
        ratings = soup.find_all('span', 'rating_per')
        # logging.info(ratings)
        for i, j in zip(ratings, range(len(ratings))):
            value = i.string
            rate = round(float(value.strip('%')) / 100.0, 4)
            rate_str = str(rate)
            index = j + 1
            if index == 1:
                rating_1 = rate_str
            if index == 2:
                rating_2 = rate_str
            if index == 3:
                rating_3 = rate_str
            if index == 4:
                rating_4 = rate_str
            if index == 5:
                rating_5 = rate_str
    except Exception as e:
        print("exception_id=" + id, e)

    try:
        average = soup.find('strong', 'll rating_num')
        if average and average.string:
            rating_average = average.string
    except Exception as e:
        print("exception_id=" + id, e)

    try:
        ratings = soup.find('span', property='v:votes')
        if ratings and ratings.string:
            ratings_count = ratings.string
    except Exception as e:
        print("exception_id=" + id, e)

    content = str(id) + "\t" \
              + str(rating_average) + "\t" \
              + str(ratings_count) + "\t" \
              + str(reviews_count) + "\t" \
              + str(comments_count) + "\t" \
              + str(rating_1) + "\t" \
              + str(rating_2) + "\t" \
              + str(rating_3) + "\t" \
              + str(rating_4) + "\t" \
              + str(rating_5) + "\t" + str(code) + "\t" + str(try_num)
    print(content)
    return id, rating_average, ratings_count, reviews_count, comments_count, rating_1, rating_2, rating_3, rating_4, rating_5, str(
        code), str(try_num)


def process(file_input, file_output):
    tag_fo = open(file=file_output, mode='w', encoding='utf-8')
    num = 0
    with open(file=file_input, mode='r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            # if num < 280:
            #     num += 1
            #     continue
            line_contents = line.split("\t")
            vid = line_contents[0]
            title = line_contents[1]
            douban_id = line_contents[2]
            # logging.info("douban_id="+douban_id)
            id, rating_average, ratings_count, reviews_count, comments_count, rating_1, rating_2, rating_3, rating_4, rating_5, code, status_num = spider(
                int(douban_id))
            content = str(vid) + "\t" \
                      + str(title) + "\t" \
                      + str(rating_average) + "\t" \
                      + str(ratings_count) + "\t" \
                      + str(reviews_count) + "\t" \
                      + str(comments_count) + "\t" \
                      + str(rating_1) + "\t" \
                      + str(rating_2) + "\t" \
                      + str(rating_3) + "\t" \
                      + str(rating_4) + "\t" \
                      + str(rating_5) + "\t" \
                      + str(code) + "\t" \
                      + str(status_num) + "\t" \
                      + "\n"
            # logging.info(content)
            tag_fo.write(content)
            time.sleep(random.gauss(4, 1))
            # if num == 1000:
            # break
            num += 1
            print("processing num=" + str(num))
            if num % 100 == 0:
                tag_fo.flush()
    tag_fo.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='douban_movie process')
    parser.add_argument('--in-path', type=str, default='./douban_movie_info.txt')
    parser.add_argument('--out-path', type=str, default='./douban_movie.txt')
    args = parser.parse_args()
    # process(args.in_path, args.out_path)
    print(spider(24325581))
