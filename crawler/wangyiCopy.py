import requests
import re
from multiprocessing import Pool
import time
import json
import codecs

headers = {
    "Referer": "http://autumnfish.cn/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131"
                  "Safari/537.36",
}
resList = []
fileW = codecs.open('MusicName.txt', 'w', 'utf-8')
fileWrite = codecs.open('distinctName.txt', 'w', 'utf-8')
#  从歌单列表 获取歌单,每一页最多10个
def get_page(url):
    t = time.time()
    req_url = url + "&t=" +str(int(round(t * 1000)))
    print(req_url)
    res = requests.get(req_url)
    data = res.text

    # 这个是string,要先转json，再通过属性去获取里面的项
    array = json.loads(data)["playlists"]
    # print(array)
    print("歌单总数："+str(len(array)))
    for item in array:
        playlist_url = "https://autumnfish.cn/playlist/detail?id=%s" % item["id"]
        print(playlist_url)
        get_songs(playlist_url)
    # 线程池 总共 < 1110(30*37)  因为要下载多个歌单，一个歌单里又有很多歌曲，所以用到了multiprocessing模块的Pool方法，提高程序运行的效率。
    # pool = Pool(processes=30)
    # pool.map(get_songs, data)


# 从歌单 获取 歌名
def get_songs(url):
    res = requests.get(url, headers=headers)
    print(res.text)
    array1 = json.loads(res.text)["playlist"]
    array2 = array1["tracks"]
    # 在Python的string前面加上‘r’， 是为了告诉编译器这个string是个raw string
    for item in array2:
        musicName = item["name"]
        # print("musicName : " + musicName)
        resName = split_name(musicName)
        print(resName)
        resList.append(resName)
        fileW.write(resName+'\n')


# 获取 简洁版歌名
def split_name(name):
    res0 = name.split(" (")[0]
    res1 = res0.split("（")[0]
    res2 = res1.split("『")[0]
    res3 = res2.split("｜")[0]
    res4 = res3.split("(")[0]
    return res4


if __name__ == "__main__":
    # 运行 爬一个单子
    # hot_url = "https://autumnfish.cn/top/playlist?limit=100&offset=100&cat=%E5%85%A8%E9%83%A8&t="
    # get_page(hot_url)
    for i in range(0,13):  # 左闭右开 [ , )
        url_i = "https://autumnfish.cn/top/playlist?order=hot&cat=%E5%85%A8%E9%83%A8&limit=100&offset="+str(i*100)
        print(url_i)
        get_page(url_i)
    print("处理完毕!")
    distinct = list(set(resList))
    print(len(distinct))
    for it in distinct:
        fileWrite.write(it + "\n")
    print("去重写入完毕!")
