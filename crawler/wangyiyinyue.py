import requests
import re
from multiprocessing import Pool
import time
import json

headers = {
    "Referer": "https://music.163.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89"
                  "Safari/537.36",
    }

#  从歌单列表 获取歌单,每一页最多10个
def get_page(url):
    print(url)
    res = requests.get(url, headers=headers)
    print(res.text)
    # data = re.findall('<a title="(.*?)" href="/playlist\?id=(\d+)" class="msk"></a>', res.text) #网易的不需要歌单名称
    data = re.findall('<a title=".*?" href="/playlist\?id=(.*?)" class="msk"></a>', res.text)
    print(data)
    print(len(data))
    # 线程池 总共 < 1110(30*37)  因为要下载多个歌单，一个歌单里又有很多歌曲，所以用到了multiprocessing模块的Pool方法，提高程序运行的效率。
    # pool = Pool(processes=30)
    # pool.map(get_songs, data)


    for i in range(0,1):  #len(data)   左闭右开 [ , )
        playlist_url = "https://music.163.com/#/playlist?id=%s" % data[i]
        print(playlist_url)
        get_songs(playlist_url)


# 从歌单 获取 歌名
def get_songs(url):
    res = requests.get(url, headers=headers)
    print(res.text)
    # 在Python的string前面加上‘r’， 是为了告诉编译器这个string是个raw string
    for i in re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', res.text):
        download_url = "http://music.163.com/song/media/outer/url?id= %s" % i[0]
        print(download_url)
        # try:
        #     with open('music/' + i[1] + '.mp3', 'wb') as f:
        #         f.write(requests.get(download_url, headers=headers).content)
        # except FileNotFoundError:
        #     pass
        # except OSError:
        #     pass


if __name__ == "__main__":
    # 运行
    hot_url = "https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0"
    get_page(hot_url)
    # for i in range(0,37):  # 左闭右开 [ , )
    #     url_i = "https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset="+str(i*35)
    #     print(url_i)
    #     get_page(hot_url)
    print("处理完毕!")

