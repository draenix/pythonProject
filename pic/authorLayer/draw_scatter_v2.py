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
# pgc
def draw1(n, s):
    data = np.loadtxt('D:/Document/localFile/haveVideo/000000_1.txt', encoding='utf-8', delimiter="\t")

    # 通过切片获取横坐标x1   # 取第 1、2、3、4列数据
    # 粉丝       # 更新频率 1~4     # 账户类型 1~4           # 垂直度
    x1 = data[:, 0]
    x2 = data[:, 1]
    x3 = data[:, 2]
    x4 = data[:, 3]
    # 通过切片获取纵坐标R# 取第5列数据
    # 点击率       # 曝光比     # pc比
    y1 = data[:, 4]
    y2 = data[:, 5]
    y3 = data[:, 6]
    # 视频量
    x5 = data[:, 7]

    x1 = [2 if x < 4 else x for x in x1]
    x2 = [4 if x < 1 else x for x in x2]
    x3 = [4 if x < 0 else x for x in x3]
    x4 = [0 if x < 0 else x for x in x4]
    x5 = [2 if x < 4 else x for x in x5]
    y1 = [0.00001 if x < 0.00001 else x for x in y1]
    y2 = [2 if x < 2 else x for x in y2]
    y3 = [0.00001 if x < 0.00001 else x for x in y3]

    x1 = [float(x) for x in x1]
    x2 = [float(x) for x in x2]
    x3 = [float(x) for x in x3]
    y2 = [float(x) for x in y2]

    # # 百分位数是统计中使用的度量，表示小于这个值的观察值的百分比。   axis 表示以多维数组的第几列为准
    # arr = np.array(y3)
    # print("百分位是： " )
    # print(np.percentile(arr, 75, axis=0))
    # print(np.percentile(arr, 78, axis=0))
    # print(np.percentile(arr, 80, axis=0))
    # print(85 + np.percentile(arr, 85, axis=0))
    # print(np.percentile(arr, 90, axis=0))
    # print(np.percentile(arr, 95, axis=0))
    # print(np.percentile(arr, 99, axis=0))

    x4 = [0.48786 if x > 1 else x for x in x4]  # 异常值 ppd>1，取 78%的分位数
    y1 = [0.12266 if x > 1 else x for x in y1]  # 异常值 ctr>1，取 78%的分位数
    y3 = [0.1822671 if x > 1 else x for x in y3]  # 异常值 pc >1，取 85%的分位数

    x1 = [np.log2(x)  for x in x1]
    x1 = [np.log2(x) / 4.5  for x in x1]

    # 特殊处理低曝光的点击率计算 ctrExp,  pc 时的系数
    y1y2 = [np.log10(y + 1) / 3.9 if y < 20 else 1 for y in y2]
    y1y2 = [np.log10(y + 1) / 3.4 if 20<=y < 40 else 1 for y in y2]


    y2 = [np.log10(x) / 8.0 for x in y2]

    # y3 = [(np.log10(x) + 5) / 5.0 if x > 0.0001 else 0.2 for x in y3]
    x5= [600 if x>600 else x for x in x5]
    x5 = [x/600.0 for x in x5]

    # 类型值的处理 更新频率负相关
    x2 = [(4 - x) / 4 if x != 5 else 0.0 for x in x2]
    x2 = [(x - 2) if x < 0 else x for x in x2]
    x3 = [(4 - x) / 4 for x in x3]
    # # 垂直度的处理(对于垂直度很低的数据有利)
    x4 = [abs(a - 0.5) * 2.0 for a in x4]

    # # 1 画散点图
    # # 创建画图窗口
    # fig = plt.figure()
    # # 将画图窗口分成1行1列，选择第一块区域作子图
    # ax1 = fig.add_subplot(1, 1, 1)
    # # 设置标题
    # ax1.set_title('pgc')
    # # 设置横坐标名称
    # ax1.set_xlabel('fans freq type ppd vids')
    # # 设置纵坐标名称
    # ax1.set_ylabel("ctr expose pc")
    # # 画散点图
    # ax1.scatter(x5, y1, s=s, c='m', marker='.')
    # ax1.scatter(x1, y1, s=s, c='g', marker='.')
    # ax1.scatter(x4, y1, s=s, c='r', marker='.')
    # #
    # ax1.scatter(x2, y1, s=s, c='b', marker='.')
    # ax1.scatter(x3, y1, s=s, c='r', marker='.')
    #
    # ax1.scatter(y2, y1, s=s, c='y', marker='.')
    # ax1.scatter(y3, y1, s=s, c='m', marker='.')

    # ax1.scatter(x5, x1, s=s, c='m', marker='.')
    #
    # # # # 通过基础信息 分析 消费信息
    # ax1.scatter(x1, y3, s=s, c='k', marker='.')
    # ax1.scatter(x2, y3, s=s, c='b', marker='.')
    # ax1.scatter(x5, y3, s=s, c='g', marker='.')
    #
    # # # # 消费 内部分析
    # ar1 = np.array(y1)
    # ar2 = np.array(y2)
    # # ar3 = np.array(y3)
    # # # ax1.scatter( sigmoid(ar1/ar2), y1, s=s, c='y', marker='.')
    ## 将曝光与点击合并
    # ax1.scatter( y1, ar1 / ar2 /4, s=s, c='g', marker='.')
    # ax1.scatter( sigmoid(ar3*ar2), y1, s=s, c='y', marker='.')
    # ax1.scatter(ar3 * ar2, y1, s=s, c='g', marker='.')
    # # # # 画直线图
    # # ax1.plot(x4, y1, c='b', ls='--')
    # # 调整横坐标的上下界
    # # plt.xlim(xmax=1, xmin=0)
    # # plt.ylim(ymax=1, ymin=0)
    # 显示
    # plt.show()

    # 2 画直方图
    # # 用np.array()将此数组变为numpy下的数组
    ar1 = np.array(y1)
    ar2 = np.array(y2)
    ar3 = np.array(y3)
    # 由于expose过低，降低消费数据的 系数
    ar1y2 = np.array(y1y2)
    br1 = np.array(x1)
    br2 = np.array(x2)
    br3 = np.array(x3)
    br4 = np.array(x4)
    br5 = np.array(x5)

    # 作为 ctrExp 的分母
    ar22 = [0.267 if x < 0.268 else x for x in ar2]
    # ctrExp
    ar12 = ar1 / ar22 / 4
    ar12 = [1 if x > 1 else x for x in ar12]
    ar12 = ar12 * ar1y2
    ar32 = ar3 * ar1y2
    # ax1.scatter(ar12, y3, s=s, c='g', marker='.')
    # plt.show()
    res = 0.6 * br1 + 0.25 * br2 + 0.06 * br3 + 0.12 * br4 + 0.15 * br5 + 0.3 * ar12 + 0.2 * ar2 + 0.3 * ar32

    plt.figure("lena")  # 定义了画板
    img = np.array(res)
    # # hist函数可以直接绘制 直方图 [一维]
    # # 参数有四个，第一个必选
    # # arr: 需要计算直方图的一维数组
    # # bins: 直方图的柱数，可选项，默认为10
    # # density: 是否将得到的直方图向量归一化(默认为0),还需要 stacked=True 属性，是将直方图归一
    # # facecolor: 直方图颜色
    # # alpha: 透明度
    # # 返回值为n: 直方图向量，是否归一化由参数设定；bins: 返回各个bin的区间范围；patches: 返回每个bin里面包含的数据，是一个list
    # # n, bins, patches = \
    plt.hist(img, bins=30, facecolor='green', alpha=0.75, rwidth=0.9 ) #, log =1 ) # ) # , density=1, stacked=False)
    # 显示
    plt.show()

    print(np.percentile(res, 0, axis=0))
    print(np.percentile(res, 35, axis=0))
    print(np.percentile(res, 40, axis=0))
    print("百分位是： " )
    print(np.percentile(res, 70, axis=0))
    print(np.percentile(res, 90, axis=0))

    print("头部")
    print(np.percentile(res, 95, axis=0))
    print(np.percentile(res, 100, axis=0))
    alen = len(res)
    print(alen)
    #
    # 分布 统计
    # sortArr = np.sort(res, axis=0)
    # alen = len(sortArr)
    # alen1 = int(alen / 20)
    # print(sortArr[0])
    # print("直方图 分布数值： 20份的  ")
    # print(sortArr[alen1 * 6])
    # print(sortArr[alen1 * 7])
    # print(sortArr[int(alen1 * 7.5 + 0.5)])
    # print(sortArr[alen1 * 8])
    # print(sortArr[alen1 * 10])
    # print(sortArr[alen1 * 12])
    # print(sortArr[alen1 * 13])
    # print("70%:  ")
    # print(sortArr[alen1 * 14])
    # print(sortArr[alen1 * 16])
    # print(sortArr[alen1 * 17])
    # print(sortArr[alen1 * 18])
    # print(sortArr[alen1 * 19])
    # print(sortArr[int(alen1 * 19.5 + 0.5)])
    # print("直方图 入参的总个数  ")
    # print(alen)
    # print(alen1)
    # print(alen1 * 20)
    # print(sortArr[alen1 * 20])
    # print(sortArr[alen - 1])



# ugc
def draw2(n, s):
    data = np.loadtxt('D:/Document/localFile/haveVideo/000000_2.txt', encoding='utf-8', delimiter="\t")

    # 通过切片获取横坐标x1   # 取第 1、2、3、4列数据
    # 粉丝       # 更新频率 1~4     # 账户类型 1~4           # 垂直度
    x1 = data[:, 0]
    x2 = data[:, 1]
    x3 = data[:, 2]
    x4 = data[:, 3]
    # 通过切片获取纵坐标R# 取第5列数据
    # 点击率       # 曝光比     # pc比
    y1 = data[:, 4]
    y2 = data[:, 5]
    y3 = data[:, 6]
    # 视频量
    x5 = data[:, 7]

    x1 = [2 if x < 4 else x for x in x1]
    x2 = [4 if x < 1 else x for x in x2]
    x3 = [4 if x < 0 else x for x in x3]
    x4 = [0 if x < 0 else x for x in x4]
    x5 = [2 if x < 4 else x for x in x5]
    y1 = [0.00001 if x < 0.00001 else x for x in y1]
    y2 = [2 if x < 2 else x for x in y2]
    y3 = [0.00001 if x < 0.00001 else x for x in y3]
    # # 百分位数是统计中使用的度量，表示小于这个值的观察值的百分比。   axis 表示以多维数组的第几列为准
    # arr = np.array(y3)
    # print("百分位是： " )
    # print(np.percentile(arr, 75, axis=0))
    # print(np.percentile(arr, 78, axis=0))
    # print(np.percentile(arr, 80, axis=0))
    # print(85 + np.percentile(arr, 85, axis=0))
    # print(np.percentile(arr, 90, axis=0))
    # print(np.percentile(arr, 95, axis=0))
    # print(np.percentile(arr, 99, axis=0))
    x4 = [1.0 if x > 1 else x for x in x4]  # 异常值 ppd>1，取 20%的分位数(绝大多数都是 1.0)
    y1 = [0.22222 if x > 1 else x for x in y1]  # 异常值 ctr>1，取 78%的分位数
    y3 = [0.18494 if x > 1 else x for x in y3]  # 异常值 pc >1，取 80%的分位数

    x1 = [np.log2(x) for x in x1]
    x1 = [np.log2(x) / 4.5 for x in x1]

    # 特殊处理低曝光的点击率计算 ctrExp时的系数
    y1y2 = [np.log10(y + 1) / 1.7 if y < 40 else 1 for y in y2]

    # y2y1 = [10000 - 2500*np.log10(x) if x > 10000 else x for x in y2]
    # y2y1 = [np.log10(x) / 8.0 if x > 1 else 0.001 for x in y2y1]
    y2 = [np.log10(x) / 8.0 for x in y2]
    y3 = [float(x) for x in y3]
    # y3 = [(np.log10(x) + 5) / 5.0 if x > 0.0001 else 0.2 for x in y3]

    x5 = [np.log2(x)  for x in x5]
    x5 = [np.log2(x) / 3.99 for x in x5]

    # 类型值的处理
    x2 = [(4 - x) / 4 if x != 5 else 0.0 for x in x2]
    x3 = [(4 - x) / 4 for x in x3]
    # # 垂直度的处理(对于垂直度很低的数据有利)
    x4 = [float(x) for x in x4]
    x4 = [abs(a - 0.5) * 2.0 for a in x4]

    # # 1 画散点图
    # # 创建画图窗口
    # fig = plt.figure()
    # # 将画图窗口分成1行1列，选择第一块区域作子图
    # ax1 = fig.add_subplot(1, 1, 1)
    # # 设置标题
    # ax1.set_title('ugc')
    # # 设置横坐标名称
    # ax1.set_xlabel('fans freq type ppd vids')
    # # 设置纵坐标名称
    # ax1.set_ylabel("ctr expose pc")
    #
    # ax1.scatter(x5, y1, s=s, c='y', marker='.')
    # ax1.scatter(x1, y1, s=s, c='g', marker='.')
    # ax1.scatter(x4, y1, s=s, c='r', marker='.')
    #
    # ax1.scatter(x2, y1, s=s, c='b', marker='.')
    # ax1.scatter(x3, y1, s=s, c='r', marker='.')
    #
    # ax1.scatter(y2, y1, s=s, c='y', marker='.')
    # ax1.scatter(y3, y1, s=s, c='m', marker='.')

    # ax1.scatter(x5, x1, s=s, c='m', marker='.')
    #
    # # # # 通过基础信息 分析 消费信息
    # ax1.scatter(x1, y3, s=s, c='k', marker='.')
    # ax1.scatter(x2, y3, s=s, c='b', marker='.')
    # ax1.scatter(x5, y3, s=s, c='g', marker='.')
    #
    # # # # 消费 内部分析
    # ar1 = np.array(y1)
    # ar2 = np.array(y2)
    # # ar3 = np.array(y3)
    # # # # ax1.scatter( sigmoid(ar1/ar2), y1, s=s, c='y', marker='.')
    ### 将曝光与点击合并
    # ax1.scatter( y1, ar1 / ar2 /4, s=s, c='g', marker='.')
    # ax1.scatter( sigmoid(ar3*ar2), y1, s=s, c='y', marker='.')
    # ax1.scatter(ar3 * ar2, y1, s=s, c='g', marker='.')
    # # # # 画直线图
    # # ax1.plot(x4, y1, c='b', ls='--')
    # # 调整横坐标的上下界
    # # plt.xlim(xmax=1, xmin=0)
    # # plt.ylim(ymax=1, ymin=0)
    # # 显示
    # plt.show()

    # 2 画直方图
    # # 用np.array()将此数组变为numpy下的数组
    ar1 = np.array(y1)
    ar2 = np.array(y2)
    ar3 = np.array(y3)
    # 由于expose过低，降低消费数据的 系数
    ar1y2 = np.array(y1y2)
    br1 = np.array(x1)
    br2 = np.array(x2)
    br3 = np.array(x3)
    br4 = np.array(x4)
    br5 = np.array(x5)

    # 作为 ctrExp 的分母
    ar22 = [0.267 if x < 0.268 else x for x in ar2]
    # ctrExp
    ar12 = ar1 / ar22 / 4
    ar12 = [1 if x > 1 else x for x in ar12]
    ar12 = ar12 * ar1y2
    ar32 = ar3 * ar1y2
    # ax1.scatter(ar32, y2, s=s, c='g', marker='.')
    # plt.show()
    res = 0.24 * br1 + 0.2 * br2 + 0.04 * br3 + 0.09 * br4 + 0.36 * br5 + 0.3 * ar12 + 0.2 * ar2 + 0.18 * ar32

    plt.figure("lena")  # 定义了画板
    img = np.array(res)
    # # hist函数可以直接绘制 直方图 [一维]
    # # 参数有四个，第一个必选
    # # arr: 需要计算直方图的一维数组
    # # bins: 直方图的柱数，可选项，默认为10
    # # density: 是否将得到的直方图向量归一化(默认为0),还需要 stacked=True 属性，是将直方图归一
    # # facecolor: 直方图颜色
    # # alpha: 透明度
    # # 返回值为n: 直方图向量，是否归一化由参数设定；bins: 返回各个bin的区间范围；patches: 返回每个bin里面包含的数据，是一个list
    # # n, bins, patches = \
    plt.hist(img, bins=30, facecolor='green', alpha=0.75, rwidth=0.9, log=1 )#  )# , density=1, stacked=False)
    # 显示
    plt.show()

    # 分布 统计
    print(np.percentile(res, 0, axis=0))
    print(np.percentile(res, 40, axis=0))
    print(np.percentile(res, 45, axis=0))
    print(np.percentile(res, 70, axis=0))
    print("百分80位是： ")
    print(np.percentile(res, 80, axis=0))
    print(np.percentile(res, 90, axis=0))
    print(np.percentile(res, 92, axis=0))
    print(np.percentile(res, 100, axis=0))
    alen = len(res)
    print(alen)

# 爬虫作者的 sofa uid
def draw3(n, s):
    data = np.loadtxt('D:/Document/localFile/haveVideo/000000_3.txt', encoding='utf-8', delimiter="\t")
    # 通过切片获取横坐标x1   # 取第 1、2、3、、、8 列数据
    # 粉丝       # 更新频率 1~4     # 账户类型 1~4           # 垂直度
    x1 = data[:, 0]
    x2 = data[:, 1]
    x3 = data[:, 2]
    x4 = data[:, 3]
    # 通过切片获取纵坐标R# 取第5列数据
    # 点击率       # 曝光比     # pc比
    y1 = data[:, 4]
    y2 = data[:, 5]
    y3 = data[:, 6]
    # 视频量
    x5 = data[:, 7]

    x1 = [10 if x < 10 else x for x in x1]
    x2 = [4 if x < 1 else x for x in x2]
    x3 = [4 if x < 0 else x for x in x3]
    x4 = [0 if x < 0 else x for x in x4]
    x5 = [2 if x < 4 else x for x in x5]
    y1 = [0.00001 if x < 0.00001 else x for x in y1]
    y2 = [2 if x < 2 else x for x in y2]
    y3 = [0.00001 if x < 0.00001 else x for x in y3]

    # # # 百分位数是统计中使用的度量，表示小于这个值的观察值的百分比。  axis 表示以多维数组的第几列为准
    # arr = np.array(y1)
    # print("百分位是： " )
    # print(np.percentile(arr, 10, axis=0))
    # print(np.percentile(arr, 75, axis=0))
    # print(np.percentile(arr, 78, axis=0))
    # print(np.percentile(arr, 80, axis=0))
    # print(8500 + np.percentile(arr, 85, axis=0))
    # print(np.percentile(arr, 90, axis=0))
    # print(np.percentile(arr, 95, axis=0))
    # print(np.percentile(arr, 99, axis=0))
    # print(np.percentile(arr, 100, axis=0))

    x4 = [0.20689 if x > 1 else x for x in x4]  # 异常值 ppd>1，取 78%的分位数
    y1 = [0.63320 if x > 1 else x for x in y1]  # 异常值 ctr>1，取 78%的分位数
    y3 = [0.38464 if x > 1 else x for x in y3]  # 异常值 pc >1，取 85%的分位数
    # 特殊处理低曝光的点击率计算 ctrExp时的系数
    y1y2 = [np.log10(y + 1) / 1.7 if y < 40 else 1 for y in y2]

    # 计算处理
    x1 = [np.log10(x) for x in x1]
    x1 = [np.log2(a) / 3.02 for a in x1]

    y2 = [np.log10(x) / 6.0 for x in y2]
    # # y3 = [(np.log10(x) + 5) / 5.0  for x in y3]

    x5 = [np.log2(x) for x in x5]
    x5 = [np.log2(x) / 3.99 for x in x5]
    x5 = [1 if x > 1 else x for x in x5]

    # 类型值的处理
    x2 = [(4 - x) / 4 if x != 5 else 0.0 for x in x2]
    x3 = [(4 - x) / 4 for x in x3]
    #
    # # 创建画图窗口
    fig = plt.figure()
    # 将画图窗口分成1行1列，选择第一块区域作子图
    ax1 = fig.add_subplot(1, 1, 1)
    # 设置标题
    ax1.set_title('crawl')
    # 设置横坐标名称
    ax1.set_xlabel('fans freq type ppd')
    # 设置纵坐标名称
    ax1.set_ylabel("ctr expose pc")
    # # 画散点图
    # ax1.scatter(x1, y1, s=s, c='k', marker='.')
    # ax1.scatter(x2, y1, s=s, c='b', marker='.')
    # ax1.scatter(x3, y1, s=s, c='r', marker='.')
    # ax1.scatter(x4, y1, s=s, c='y', marker='.')
    # ax1.scatter(x5, y1, s=s, c='g', marker='.')
    #
    # ax1.scatter(y2, y1, s=s, c='y', marker='.')
    # ax1.scatter(y3, y1, s=s, c='m', marker='.')

    # ax1.scatter(x1, y2, s=s, c='k', marker='.')
    # ax1.scatter(x2, y2, s=s, c='b', marker='.')
    # ax1.scatter(x3, y2, s=s, c='r', marker='.')
    # ax1.scatter(x4, y2, s=s, c='y', marker='.')
    # ax1.scatter(x5, y2, s=s, c='g', marker='.')
    #
    # # 通过基础信息 分析 消费信息
    # ax1.scatter(x1, y3, s=s, c='g', marker='.')
    # ax1.scatter(x5, y3, s=s, c='b', marker='.')

    # 用np.array()将此数组变为numpy下的数组
    ar1 = np.array(y1)
    ar2 = np.array(y2)
    ar1y2 = np.array(y1y2)
    ar3 = np.array(y3)
    br1 = np.array(x1)
    br2 = np.array(x2)
    br3 = np.array(x3)
    br4 = np.array(x4)
    br5 = np.array(x5)

    # # # 消费 内部分析
    # # ax1.scatter( sigmoid(ar3/ar2), y1, s=s, c='y', marker='.')
    # ax1.scatter(ar1 / ar2 / 3.8, y1, s=s, c='m', marker='.')
    # #
    # # ax1.scatter( sigmoid(ar3*ar2), y1, s=s, c='y', marker='.')
    # # ax1.scatter(ar3 * ar2, y1, s=s, c='m', marker='.')
    # #
    # # # # 画直线图
    # ax1.plot(x2, y2, c='b', ls='--')
    # #
    # # # 调整横坐标的上下界
    # # plt.xlim(xmax=1, xmin=0)
    # # plt.ylim(ymax=1, ymin=0)
    # #
    # # 显示
    # plt.show()

    # 作为 ctrExp 的分母
    ar22 = [0.267 if x < 0.268 else x for x in ar2]
    # ctrExp
    ar12 = ar1 / ar22 / 3.8 * ar1y2
    ar32 = ar3 * ar1y2
    ax1.scatter(ar32, y2, s=s, c='g', marker='.')
    # plt.show()

    res = 0.3 * br1 + 0.2 * br2 + 0.05 * br3 + 0.05 * br4 + 0.3 * br5 + 0.25 * ar12 + 0.25 * ar2 + 0.2 * ar32

    # #
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
    plt.hist(img, bins=30, facecolor='green', alpha=0.75, rwidth=0.91)#, log =1 )# )# ,density=1,, stacked=True)

    # 显示
    plt.show()
    #
    sortArr = np.sort(res, axis=0)
    alen = len(sortArr)
    alen1 = int(alen / 20)
    print(sortArr[0])
    print(sortArr[alen1 * 6])
    print(sortArr[int(alen1 * 6.5)])
    print(sortArr[alen1 * 7])
    print(sortArr[alen1 * 8])
    print("50%")
    print(sortArr[alen1 * 10])
    print(sortArr[alen1 * 12])
    print("65%")
    print(sortArr[alen1 * 13])
    print(sortArr[alen1 * 14])
    print(sortArr[alen1 * 16])
    print("85~95%")
    print(sortArr[alen1 * 17])
    print(sortArr[alen1 * 18])
    print(sortArr[alen1 * 19])
    print(alen)
    print(alen1)
    print(alen1 * 20)
    print(sortArr[alen - 1])
    # 显示
    plt.show()

# 爬虫作者的 ori_author_id
def draw4(n, s):
    data = np.loadtxt('D:/Document/localFile/000000_3N.txt', encoding='utf-8', delimiter="\t")

    # 通过切片获取横坐标x1   # 取第 1、2、3、、、8 列数据
    # 粉丝       # 更新频率 1~4     # 账户类型 1~4           # 垂直度
    x1 = data[:, 0]
    x2 = data[:, 1]
    x3 = data[:, 2]
    x4 = data[:, 3]
    # 通过切片获取纵坐标R# 取第5列数据
    # 点击率       # 曝光比     # pc比
    y1 = data[:, 4]
    y2 = data[:, 5]
    y3 = data[:, 6]
    # 视频量
    x5 = data[:, 7]

    x1 = [10 if x < 10 else x for x in x1]
    x2 = [4 if x < 1 else x for x in x2]
    x3 = [4 if x < 0 else x for x in x3]
    x4 = [0 if x < 0 else x for x in x4]
    x5 = [2 if x < 4 else x for x in x5]
    y1 = [0.00001 if x < 0.00001 else x for x in y1]
    y2 = [2 if x < 2 else x for x in y2]
    y3 = [0.00001 if x < 0.00001 else x for x in y3]

    # # # 百分位数是统计中使用的度量，表示小于这个值的观察值的百分比。  axis 表示以多维数组的第几列为准
    # arr = np.array(x4)
    # print("百分位是： " )
    # print(np.percentile(arr, 5, axis=0))
    # print(np.percentile(arr, 10, axis=0))
    # print(np.percentile(arr, 15, axis=0))
    # print(np.percentile(arr, 75, axis=0))
    # print(np.percentile(arr, 80, axis=0))
    # print(8500 + np.percentile(arr, 85, axis=0))
    # print(np.percentile(arr, 90, axis=0))
    # print(np.percentile(arr, 95, axis=0))
    # print(np.percentile(arr, 99, axis=0))
    # print(np.percentile(arr, 100, axis=0))
    # print(len(data))
    x4 = [0.11328 if x > 0.999999 else x for x in x4]  # 异常值 ppd>1，取 80%的分位数
    y1 = [0.51851 if x > 0.999999 else x for x in y1]  # 异常值 ctr>1，取 78%的分位数
    y3 = [0.27219 if x > 0.999999 else x for x in y3]  # 异常值 pc >1，取 78%的分位数

    # 计算处理
    x1 = [np.log10(x) for x in x1]
    x1 = [np.log2(a) / 3.02 for a in x1]
    # 特殊处理低曝光的点击率计算 ctrExp时的系数
    y1y2 = [np.log10(y + 1) / 1.7 if y < 40 else 1 for y in y2]

    y2 = [np.log10(x) / 6.0 for x in y2]
    # # y2x1 = [np.log10(x) / 6.0 if x > 9 else 0.12 for x in y2]
    # # y3 = [(np.log10(x) + 5) / 5.0 for x in y3]

    x5 = [np.log2(x) for x in x5]
    x5 = [np.log2(x) / 3.99 for x in x5]
    x5 = [1 if x > 1 else x for x in x5]

    # 类型值的处理
    x2 = [(4 - x) / 4 if x != 5 else 0.0 for x in x2]
    x3 = [(4 - x) / 4 for x in x3]

    # # 创建画图窗口
    fig = plt.figure()
    # 将画图窗口分成1行1列，选择第一块区域作子图
    ax1 = fig.add_subplot(1, 1, 1)
    # 设置标题
    ax1.set_title('ori')
    # 设置横坐标名称
    ax1.set_xlabel('fans freq type ppd')
    # 设置纵坐标名称
    ax1.set_ylabel("ctr expose pc")
    # 画散点图
    # ax1.scatter(x1, y1, s=s, c='k', marker='.')
    # ax1.scatter(x2, y1, s=s, c='b', marker='.')
    # ax1.scatter(x3, y1, s=s, c='r', marker='.')
    # ax1.scatter(x4, y1, s=s, c='y', marker='.')
    # ax1.scatter(x5, y1, s=s, c='g', marker='.')
    #
    # ax1.scatter(y2, y1, s=s, c='y', marker='.')
    # ax1.scatter(y3, y1, s=s, c='m', marker='.')

    # ax1.scatter(x1, y2, s=s, c='k', marker='.')
    # ax1.scatter(x2, y2, s=s, c='b', marker='.')
    # ax1.scatter(x3, y2, s=s, c='r', marker='.')
    # ax1.scatter(x4, y2, s=s, c='y', marker='.')
    # ax1.scatter(x5, y2, s=s, c='g', marker='.')
    #
    # # # 通过基础信息 分析 消费信息
    # ax1.scatter(x1, y3, s=s, c='y', marker='.')
    # ax1.scatter(x5, y3, s=s, c='b', marker='.')

    # 用np.array()将此数组变为numpy下的数组
    ar1 = np.array(y1)
    ar2 = np.array(y2)
    ar1y2 = np.array(y1y2)
    ar3 = np.array(y3)
    br1 = np.array(x1)
    br2 = np.array(x2)
    br3 = np.array(x3)
    br4 = np.array(x4)
    br5 = np.array(x5)

    # # # 消费 内部分析
    # # ax1.scatter( sigmoid(ar3/ar2), y1, s=s, c='y', marker='.')
    # ax1.scatter(ar1 / ar2 / 3.8, y1, s=s, c='m', marker='.')
    # #
    # # ax1.scatter( sigmoid(ar3*ar2), y1, s=s, c='y', marker='.')
    # # ax1.scatter(ar3 * ar2, y1, s=s, c='m', marker='.')
    # #
    # # # # 画直线图
    # ax1.plot(x2, y2, c='b', ls='--')
    # #
    # # # 调整横坐标的上下界
    # # plt.xlim(xmax=1, xmin=0)
    # # plt.ylim(ymax=1, ymin=0)
    # #

    # 显示
    # plt.show()
    # 作为 ctrExp 的分母
    ar22 = [0.267 if x < 0.268 else x for x in ar2]
    # ctrExp
    ar12 = ar1 / ar22 / 3.8 * ar1y2
    ar32 = ar3 * ar1y2
    ax1.scatter(ar32, y2, s=s, c='g', marker='.')
    # plt.show()
    res = 0.3 * br1 + 0.2 * br2 + 0.06 * br3 + 0.03 * br4 + 0.3 * br5 + 0.25 * ar12 + 0.25 * ar2 + 0.2 * ar32

    # #
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
    plt.hist(img, bins=30, facecolor='green', alpha=0.75, rwidth=0.91, log=1 )# ,density=1, stacked=True)
    # 显示
    plt.show()

    sortArr = np.sort(res, axis=0)
    alen = len(sortArr)
    alen1 = int(alen / 20)
    print(sortArr[0])
    print(sortArr[alen1 * 6])
    print(sortArr[int(alen1 * 6.5)])
    print(sortArr[alen1 * 7])
    print(sortArr[alen1 * 8])
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
    print(alen1 * 20)
    print(sortArr[alen - 1])


if __name__ == "__main__":
    # 运行
    draw1(n=14263, s=2)
    # draw2(78560, 2)
    # draw3(n=935879, s=2)
    # draw4(746656, 2)


# 自实现 sigmod函数
def sigmoid(x):
    return 1.0 / (np.exp(-x) + 1)
