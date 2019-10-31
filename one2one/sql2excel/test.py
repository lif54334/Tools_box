import numpy as np
import matplotlib.pyplot as plt


y=[130.0, 163.0, 221.0, 175.0, 145.0, 138.0, 146.0, 133.0, 102.0, 61.0, 70.0, 37.0, 71.0, 52.0, 44.0]
x=np.arange(1, len(y) + 1)
y=np.array(y)
print(len(x),len(y))

plt.plot(x, y)
plt.show()

arr_mean = np.mean(y)
#求方差
arr_var = np.var(y)
#求标准差
arr_std = np.std(y,ddof=1)
print("平均值为：%f" % arr_mean)
print("方差为：%f" % arr_var)
print("标准差为:%f" % arr_std)
print("u+_std:{} {}".format(arr_mean-arr_std,arr_mean+arr_std))