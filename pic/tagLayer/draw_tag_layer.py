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
def draw1(n):

    # 加载数据：    000000_1.txt 本站作者的   ；   000000_2.txt  爬虫作者的
    data = np.loadtxt('C:/Users/jiadu218986/Documents/dataTxtToUse/20221107.txt', encoding='utf-8', delimiter="\t")

    # 通过切片获取横坐标x1
    # 取第 1、2、3、4列数据
    # id
    x0 = data[:, 0]
    # vid_cnt
    x1 = data[:, 1]
    # ctr
    x2 = data[:, 2]
    # interval_day
    x3 = data[:, 3]
    # source
    x4 = data[:, 4]

    # 已经计算好的分层分数
    y1 = data[:, 5]

    # 用np.array()将此数组变为numpy下的数组
    br1 = np.array(x1)
    br2 = np.array(x2)
    br3 = np.array(x3)
    br4 = np.array(x4)

    cr1 = np.array(y1)

    # 消费 内部分析
    # ax1.scatter( sigmoid(br3/br2), y1, s=s, c='y', marker='.')
    # ax1.scatter(br3 / br2, y1, s=s, c='m', marker='.')

    # ax1.scatter( sigmoid(br3*br2), y1, s=s, c='y', marker='.')
    # ax1.scatter(br3 * br2, y1, s=s, c='m', marker='.')

    # # # 画直线图
    # ax1.plot(x4, y1, c='b', ls='--')
    # 调整横坐标的上下界
    # plt.xlim(xmax=1, xmin=0)
    # plt.ylim(ymax=1, ymin=0)

    res = 0.7 * br1 + 0.9 * br2 + 0.7 * br3 + 0.1 * br4

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
    # , log =1 这个参数，表示y轴的长度单位是log的指数
    plt.hist(img, bins=30, facecolor='green', alpha=0.75, rwidth=0.9 )  # , log =1, density=1,, stacked=True)

    # 显示
    plt.show()
    sortArr = np.sort(res, axis=0)
    alen = len(sortArr)
    alen1 = int(alen / 20)
    print(alen)
    print(sortArr[0])
    print("10% : " + str(sortArr[alen1 * 2]))
    print(sortArr[alen1 * 4])
    print("30% : " + str(sortArr[alen1 * 6]))
    print(sortArr[alen1 * 8])
    print("50% : " + str(sortArr[alen1 * 10]))
    print(alen1)
    print(alen1*20)
    print(sortArr[alen1 * 12])
    print("70% : " + str(sortArr[alen1 * 14]))
    print(sortArr[alen1 * 15])
    print(sortArr[alen1 * 16])
    print("90% : " + str(sortArr[alen1 * 18]))
    print(sortArr[alen1 * 19])
    print("97.5% = " + str(sortArr[int(alen1 * 19.5 + 0.5)]))
    # print(sortArr[alen1 * 20])
    print("bigest : " + str(sortArr[alen-1]))




# 自实现 sigmod函数
def sigmoid(x):
    return 1.0 / (np.exp(-x) + 1)


if __name__ == "__main__":
    # 运行
    draw1(n=1009738)