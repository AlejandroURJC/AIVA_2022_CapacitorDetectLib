from matplotlib import pyplot as plt
import numpy as np

def get_TP_curve_vectorizada(positive,conf):
    sorted_index = np.flip(np.argsort(conf))
    curve = np.add.accumulate((positive*1)[sorted_index])
    curve = np.concatenate(([0.0],curve))
    x_curve = np.arange(0, curve.shape[0]) / (curve.shape[0]-1)
    y_curve = curve / (curve.shape[0]-1)
    return (x_curve,y_curve)

def TP_rate(tp, fp, tn, fn):
    return tp / (tp + fp + tn + fn)

if __name__ == '__main__':
    real = np.array(
        ["1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1",
         "1", "1"])
    predict = np.array(
        ["1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1",
         "1", "1"])
    conf = np.array([TP_rate(31, 19, 0, 17), TP_rate(24, 21, 0, 24), TP_rate(29, 16, 0, 19), TP_rate(13, 23, 0, 15),
                     TP_rate(13, 29, 0, 15),
                     TP_rate(11, 19, 0, 17), TP_rate(14, 32, 0, 14), TP_rate(0, 4, 0, 0), TP_rate(0, 40, 0, 0),
                     TP_rate(0, 8, 0, 0),
                     TP_rate(0, 13, 0, 0), TP_rate(0, 6, 0, 0), TP_rate(0, 11, 0, 0), TP_rate(0, 6, 0, 0),
                     TP_rate(0, 39, 0, 0),
                     TP_rate(17, 20, 0, 73), TP_rate(24, 21, 0, 66), TP_rate(22, 15, 0, 68), TP_rate(9, 17, 0, 81),
                     TP_rate(17, 14, 0, 73),
                     TP_rate(10, 25, 0, 0), TP_rate(8, 22, 0, 2), TP_rate(8, 25, 0, 2), TP_rate(10, 24, 0, 0)])

    x_perfect, y_perfect = get_TP_curve_vectorizada(real == real, conf)
    x_curve, y_curve = get_TP_curve_vectorizada(real == predict, conf)
    plt.plot(x_perfect, y_perfect)
    plt.plot(x_curve, y_curve)
    plt.savefig('TP_curve.png')
    plt.show()