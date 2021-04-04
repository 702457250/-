import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei' ##设置中文显示
plt.rcParams['axes.unicode_minus'] = False
x = weight
y = profit
plt.figure(figsize=(8,7))
plt.scatter(x,y,c = 'b', marker='D')##绘制散点图
plt.xlabel('weight')
plt.ylabel('profit')
plt.xticks(range(0,70,4),values[range(0,70,4),1],rotation=45)
print(range(0,70,4))                                                             
print(values[range(0,70,4),1])                                                                                                                          \par
plt.title('重量价值散点图')##添加图表标题
plt.show()

 