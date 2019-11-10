from pylab import *
import json

filename = "./myface_angle.json"

# 将数据加载到列表中
with open(filename) as f:
    pop_data = json.load(f)

# #创建一个包含人口数量的字典
x_angles = []
y_angles = []
z_angles = []
info_scores = []

for pop_dict in pop_data:
    x_angle = pop_dict['x_angle']
    x_angle = float(x_angle)
    y_angle = pop_dict['y_angle']
    y_angle = float(y_angle)
    z_angle = pop_dict['z_angle']
    z_angle = float(z_angle)
    info_score = pop_dict['info_score']
    info_score = float(info_score)

    x_angles.append(x_angle)
    y_angles.append(y_angle)
    z_angles.append(z_angle)
    info_scores.append(info_score)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# matplotlib画图中中文显示会有问题，需要这两行设置默认字体

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=2000, xmin=0)
plt.ylim(ymax=50, ymin=-50)
# 画两条（0-9）的坐标轴并设置轴标签x，y

x1 = np.arange(0, len(x_angles), 1)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的x轴坐标
colors1 = '#00CED1'  # 点的颜色
colors2 = '#DC143C'
colors3 = '#10A70F'
colors4 = '#1712A7'
# plot中参数的含义分别是横轴值，纵轴值，颜色，透明度和标签

# 画散点图
plt.plot(x1, x_angles, '--', c=colors1, alpha=0.8, label='x_angles')
plt.plot(x1, y_angles, '--', c=colors2, alpha=0.8, label='y_angles')
plt.plot(x1, z_angles, '-', c=colors3, alpha=0.8, label='z_angles')
plt.plot(x1, info_scores, '--', c=colors4, alpha=0.8, label='info_scores')


plt.plot([0, 9.5], [9.5, 0], linewidth='0.5', color='#000000')
plt.legend()
plt.savefig(r'./angle_line.png', dpi=300)
plt.show()


