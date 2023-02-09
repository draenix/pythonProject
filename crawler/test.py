import requests
import json

# 获取 简洁版歌名
def split_name(name):
    res0 = name.split(" (")[0]
    res1 = res0.split("（")[0]
    res2 = res1.split("『")[0]
    res3 = res2.split("｜")[0]
    res4 = res3.split("(")[0]
    return res4

# 从歌单 获取 歌名
def get_songs(url):
    res = requests.get(url)

    array1 = json.loads(res.text)["playlist"]
    # print(array1)
    array2 = array1["tracks"]
    # 在Python的string前面加上‘r’， 是为了告诉编译器这个string是个raw string
    for item in array2:
        musicName = item["name"]
        print("musicName : "+ musicName)
        print(split_name(musicName))

if __name__ == "__main__":
    inp = "Careless Whisper(Dj Dark & MD Dj Remix)"
    print(split_name(inp))
    res = inp.split("(")
    print(res[0])

    get_songs("https://autumnfish.cn/playlist/detail?id=5454637196")

