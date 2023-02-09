import numpy as np


def test(x, y, score):
    a = np.log10(x)
    b = np.log2(a) / 3.02
    print("fans  : "+str(b))

    m = 0.12
    if (y > 9):
        m = np.log10(y) / 6.0
    print("expose: "+str(m))
    w1 = b / m * 0.15
    print("old w  : "+str(w1))


    n = 0.267
    if (y > 39):
        n = np.log10(y) / 6.0
    w2 = b / n * 0.5
    print("new w  : "+str(w2))
    print("new score is : " + str(score - w1 + w2))


if __name__ == "__main__":
    print("AHTV第一时间")
    test(5127351, 124, 0.73588478)
    print("\n w遥清水")
    test(3992315, 383, 0.77463019)

    print("\n 毒角SHOW")
    test(27298329, 364, 0.70707967)

    print("\n 正经的江叔")
    test(8989585, 0, 1.18451346)

