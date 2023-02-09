import matplotlib.pyplot as plt
import numpy as np

"""
1.获取txt 的数据（纯数字）
2.切片获取每一列，一列就是一个属性
3.处理每一个属性
4.不同属性之间关系的散点图
5.不同属性不同权重获取最终得分
6.画得分的直方图
"""

"""  本站作者的
  :param n: 点的数量，整数
  :param s:点的大小，整数
  :return: None
  """
def draw1(n, s):

    # 加载数据：    000000_1.txt 本站作者的   ；   000000_2.txt  爬虫作者的
    data = np.loadtxt('C:/Users/jiadu218986/Documents/dataTxtToUse/000000_1.txt', encoding='utf-8', delimiter="\t")

    # 通过切片获取横坐标x1
    # 取第 1、2、3、4列数据
    # 粉丝比
    x1 = data[:, 0]
    # 更新频率 1~4
    x2 = data[:, 1]
    # 账户类型 1~4
    x3 = data[:, 2]
    # 垂直度
    x4 = data[:, 3]

    # 通过切片获取纵坐标R
    # 取第5列数据
    # 点击率
    y1 = data[:, 4]
    # 曝光比
    y2 = data[:, 5]
    # pc比
    y3 = data[:, 6]


    # 科学计数法
    x1 = [(float(x) * 200000) for x in x1]
    x1 = [np.log2(x) if x > 1 else 0 for x in x1]
    x1 = [np.log2(x) / 4.5 if x > 1 else 0 for x in x1]
    x4 = [float(x) for x in x4]
    y1 = [float(x) for x in y1]
    y2 = [(float(x) * 30000000) for x in y2]
    y3 = [float(x) for x in y3]
    # 读取科学计数法还是有问题，将至过滤了
    y1 = [0.0001 * x if x > 1 else x for x in y1]
    y3 = [0.0001 * x if x > 1 else x for x in y3]
    y1 = [0.0001 if x == 0 else x for x in y1]
    y3 = [0.0001 if x == 0 else x for x in y3]

    y2 = [np.log10(x) / 8.0 if x > 1 else 0.001 for x in y2]
    y3 = [(np.log10(x) + 5) / 5.0 if x != 1 else 1 for x in y3]

    # 类型值的处理
    x2 = [(4 - x) / 4 for x in x2]
    x3 = [(4 - x) / 4 for x in x3]

    # # 垂直度的处理(对于垂直度很低的数据有利)
    # x4 = [abs(a-0.5)*2.0 for a in x4]
    #
    # # 创建画图窗口
    # fig = plt.figure()
    # # 将画图窗口分成1行1列，选择第一块区域作子图
    # ax1 = fig.add_subplot(1, 1, 1)
    # # 设置标题
    # ax1.set_title('benzhan')
    # # 设置横坐标名称
    # ax1.set_xlabel('fans freq type ppd')
    # # 设置纵坐标名称
    # ax1.set_ylabel("ctr expose pc")

    # # 画散点图
    # ax1.scatter(x1, y1, s=s, c='k', marker='.')
    # ax1.scatter(x4, y1, s=s, c='g', marker='.')
    #
    # ax1.scatter(x2, y1, s=s, c='b', marker='.')
    # ax1.scatter(x3, y1, s=s, c='r', marker='.')
    #
    # ax1.scatter(y2, y1, s=s, c='y', marker='.')
    # ax1.scatter(y3, y1, s=s, c='m', marker='.')

    # 通过基础信息 分析 消费信息
    # ax1.scatter(x1, y3, s=s, c='k', marker='.')
    # ax1.scatter(x2, y3, s=s, c='b', marker='.')
    # ax1.scatter(x4, y3, s=s, c='g', marker='.')

    # 用np.array()将此数组变为numpy下的数组
    ar1 = np.array(y1)
    ar2 = np.array(y2)
    ar3 = np.array(y3)
    br1 = np.array(x1)
    br2 = np.array(x2)
    br3 = np.array(x3)
    br4 = np.array(x4)

    # 消费 内部分析
    # ax1.scatter( sigmoid(ar3/ar2), y1, s=s, c='y', marker='.')
    # ax1.scatter(ar3 / ar2, y1, s=s, c='m', marker='.')

    # ax1.scatter( sigmoid(ar3*ar2), y1, s=s, c='y', marker='.')
    # ax1.scatter(ar3 * ar2, y1, s=s, c='m', marker='.')

    # # # 画直线图
    # ax1.plot(x4, y1, c='b', ls='--')
    # 调整横坐标的上下界
    # plt.xlim(xmax=1, xmin=0)
    # plt.ylim(ymax=1, ymin=0)

    res = 0.2 * br1 + 0.7 * br2 + 0.05 * br3 + 0.18 * br4 + 0.8 * ar1 + 0.7 * ar2 + 0.5 * ar3

    plt.figure("lena")  # 定义了画板
    img = np.array(res)
    # hist函数可以直接绘制 直方图 [一维]
    # 参数有四个，第一个必选
    # arr: 需要计算直方图的一维数组
    # bins: 直方图的柱数，可选项，默认为10
    # density: 是否将得到的直方图向量归一化(默认为0),还需要 stacked=True 属性，是将直方图归一
    # facecolor: 直方图颜色
    # alpha: 透明度
    # 返回值为n: 直方图向量，是否归一化由参数设定；bins: 返回各个bin的区间范围；patches: 返回每个bin里面包含的数据，是一个list
    # n, bins, patches = \
    plt.hist(img, bins=30, facecolor='green', alpha=0.75, rwidth=0.9, log =1 )  # , log =1, density=1,, stacked=True)

    # 显示
    plt.show()
    sortArr = np.sort(res, axis=0)
    alen = len(sortArr)
    alen1 = int(alen / 20)
    print(sortArr[alen1 * 10])
    print(sortArr[alen1 * 12])
    print(sortArr[alen1 * 14])
    print(sortArr[alen1 * 16])
    print(sortArr[alen1 * 17])
    print(sortArr[alen1 * 18])
    print(sortArr[int(alen1 * 19.5+0.5)])
    print(alen)
    print(alen1)
    print(alen1*20)
    print(sortArr[alen1 * 20])
    print(sortArr[alen-1])


# 爬虫作者的
def draw2(n, s):
    """
    :param n: 点的数量，整数
    :param s:点的大小，整数
    :return: None
    """
    # 加载数据：    000000_1.txt 本站作者的   ；   000000_2.txt  爬虫作者的
    data = np.loadtxt('C:/Users/jiadu218986/Documents/dataTxtToUse/000000_2.txt', encoding='utf-8', delimiter="\t")

    # 通过切片获取横坐标x1
    # 取第 1、2、3、4列数据
    # 粉丝比
    x1 = data[:, 0]
    # 更新频率 1~4
    x2 = data[:, 1]
    # 账户类型 1~4
    x3 = data[:, 2]
    # 垂直度 绝大部分没有此值，极少的数数据可以当做脏数据
    x4 = data[:, 3]

    # 通过切片获取纵坐标R
    # 取第5列数据
    # 点击率
    y1 = data[:, 4]
    # 曝光比
    y2 = data[:, 5]
    # pc比
    y3 = data[:, 6]

    # 科学计数法
    x1 = [float(x) for x in x1]
    x1 = [a * 50000000.0 for a in x1]
    x1 = [np.log10(x) if x > 1 else 0 for x in x1]
    x1 = [np.log2(a) / 3.02 if a > 1 else 0 for a in x1]

    y1 = [float(x) for x in y1]
    y2 = [(float(x) * 5000000.0) for x in y2]
    y3 = [float(x) for x in y3]
    # 读取科学计数法还是有问题，将之过滤了
    y1 = [0.0001 * x if x > 1 else x for x in y1]
    y3 = [0.0001 * x if x > 1 else x for x in y3]
    y1 = [0.0001 if x == 0 else x for x in y1]
    y3 = [0.0001 if x == 0 else x for x in y3]

    y2x1 = [np.log10(x) / 6.0 if x > 39 else 0.267 for x in y2]
    y2 = [np.log10(x) / 6.0 if x > 9 else 0.12 for x in y2]

    y3 = [(np.log10(x) + 5) / 5.0 if x != 1 else 1 for x in y3]

    # 类型值的处理
    x2 = [(4 - x) / 4 for x in x2]
    x3 = [(4 - x) / 4 for x in x3]

    # # 创建画图窗口
    # fig = plt.figure()
    # # 将画图窗口分成1行1列，选择第一块区域作子图
    # ax1 = fig.add_subplot(1, 1, 1)
    # # 设置标题
    # ax1.set_title('crawl')
    # # 设置横坐标名称
    # ax1.set_xlabel('fans freq type ppd')
    # # 设置纵坐标名称
    # ax1.set_ylabel("ctr expose pc")

    # # 画散点图
    # ax1.scatter(x1, y1, s=s, c='k', marker='.')
    # ax1.scatter(x4, y1, s=s, c='g', marker='.')
    #
    # ax1.scatter(x2, y1, s=s, c='b', marker='.')
    # ax1.scatter(x3, y1, s=s, c='r', marker='.')
    #
    # ax1.scatter(y2, y1, s=s, c='y', marker='.')
    # ax1.scatter(y3, y1, s=s, c='m', marker='.')
    #
    # # 通过基础信息 分析 消费信息
    # ax1.scatter(x1, y2, s=s, c='k', marker='.')
    # ax1.scatter(x2, y2, s=s, c='b', marker='.')

    y11 = [x for x in y1]
    y21 = [x for x in y2]
    y31 = [x for x in y3]
    x11 = [x for x in x1]
    x21 = [x for x in x2]
    x31 = [x for x in x3]
    # 用np.array()将此数组变为numpy下的数组
    ar1 = np.array(y11)
    ar2 = np.array(y21)
    ar2x1 = np.array(y2x1)
    ar3 = np.array(y31)
    br1 = np.array(x11)
    br2 = np.array(x21)
    br3 = np.array(x31)

    # # 消费 内部分析
    # ax1.scatter( sigmoid(ar3/ar2), y1, s=s, c='y', marker='.')
    # ax1.scatter(ar3 / ar2, y1, s=s, c='m', marker='.')
    #
    # ax1.scatter( sigmoid(ar3*ar2), y1, s=s, c='y', marker='.')
    # ax1.scatter(ar3 * ar2, y1, s=s, c='m', marker='.')
    #
    # # 画直线图
    # ax1.plot(x2, y2, c='b', ls='--')
    #
    # # 调整横坐标的上下界
    # plt.xlim(xmax=1, xmin=0)
    # plt.ylim(ymax=1, ymin=0)
    #

    br10 = br1/ar2x1
    res= 0.5*br10+0.6*br2 + 0.08*br3+0.7*ar1+0.8*ar2+0.15*ar3
    #
    plt.figure("lena")  # 定义了画板
    img = np.array(res)
    # hist函数可以直接绘制 直方图 [一维]
    # 参数有四个，第一个必选
    # arr: 需要计算直方图的一维数组
    # bins: 直方图的柱数，可选项，默认为10
    # density: 是否将得到的直方图向量归一化(默认为0),还需要 stacked=True 属性，是将直方图归一
    # facecolor: 直方图颜色
    # alpha: 透明度
    # 返回值为n: 直方图向量，是否归一化由参数设定；bins: 返回各个bin的区间范围；patches: 返回每个bin里面包含的数据，是一个list
    # n, bins, patches = \
    plt.hist(img, bins=30,  facecolor='green', alpha=0.75, rwidth=0.91 )# , log =1 ,density=1,, stacked=True)

    # 显示
    plt.show()

    sortArr = np.sort(res, axis=0)
    alen = len(sortArr)
    alen1 = int(alen/20)
    print(sortArr[0])
    print(sortArr[alen1 * 6])
    print(sortArr[alen1 * 6+12516])
    print(sortArr[alen1 * 7])
    print("50%")
    print(sortArr[alen1 * 10])
    print(sortArr[alen1 * 12])
    print("65%")
    print(sortArr[alen1 * 13])
    print(sortArr[alen1 * 14])
    print("90~95%")
    print(sortArr[alen1 * 18])
    print(sortArr[alen1 * 19])
    print(alen)
    print(alen1)
    print(alen1*20)
    print(sortArr[alen-1])




# 自实现 sigmod函数
def sigmoid(x):
    return 1.0 / (np.exp(-x) + 1)


if __name__ == "__main__":
    # 运行
    # draw1(n=54424, s=2)
    draw2(n=500665, s=2)
