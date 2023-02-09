import re

"""
1 读取含有字符串的文本（指定编码格式）
2 每一行单独处理
3 正则匹配，筛选出第一列中 非纯数字的值 
re.match()   完全匹配：是从头匹配一个符合规则的字符串，从起始位置开始匹配，匹配成功返回一个对象；未匹配成功返回None
re.search()  截取匹配：在字符串内查找模式匹配,只要找到第一个匹配然后返回，                ， 未匹配成功返回None
"""


def draw11():
    # 指定格式
    file = open('C:/Users/jiadu218986/Documents/dataTxtToUse/000000_01.txt', "r", encoding="utf-8")
    contents = file.readlines()  # 读取全部行
    for content in contents:  # 显示一行
        uid = content.split('\t')[0]
        # print(uid)
        # 非数字匹配
        res = re.match(r"[^0-9]", uid)
        if (res != None):
            print(uid)
            print("res.group(0) is " + res.group())

    # 加载数据：    只能是 纯数字  文本的！！
    # data = np.loadtxt('C:/Users/jiadu218986/Documents/000000_02.txt', encoding='utf-8', delimiter="\t")
    # # 通过切片获取横坐标x1
    # x1 = data[:, 0]
    # ar1 = np.array(x1)


# 主模块
if __name__ == "__main__":
    # 运行
    draw11()
