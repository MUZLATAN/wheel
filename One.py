# -*- coding: utf-8 -*-
import json
import matplotlib.pyplot as plt
import numpy as np

filename = "./myface.json"

# 将数据加载到列表中
with open(filename) as f:
    pop_data = json.load(f)

# #创建一个包含人口数量的字典
bluriness = []
illum = []
occl_chin = []
occl_l_contour = []
occl_l_eye = []
occl_mouth = []
occl_nose = []
occl_r_contour = []
occl_r_eye = []
for pop_dict in pop_data:
    if pop_dict['errno'] == 0:
        blus = pop_dict['data']['result']['bluriness']
        blus = float(blus)
        ill = pop_dict['data']['result']['illum']
        ill = float(ill)
        o_ch = pop_dict['data']['result']['occl_chin']
        o_ch = float(o_ch)
        o_lc = pop_dict['data']['result']['occl_l_contour']
        o_lc = float(o_lc)
        o_le = pop_dict['data']['result']['occl_l_eye']
        o_le = float(o_le)
        o_mo = pop_dict['data']['result']['occl_mouth']
        o_mo = float(o_mo)
        o_no = pop_dict['data']['result']['occl_nose']
        o_no = float(o_no)
        o_rc = pop_dict['data']['result']['occl_r_contour']
        o_rc = float(o_rc)
        o_re = pop_dict['data']['result']['occl_r_eye']
        o_re = float(o_re)
    else:
        blus = -0.3
        o_ch = -0.3
        o_lc = -0.3
        o_le = -0.3
        o_mo = -0.3
        o_no = -0.3
        o_rc = -0.3
        o_re = -0.3
    bluriness.append(blus)
    # illum.append(ill)
    occl_chin.append(o_ch)
    occl_l_contour.append(o_lc)
    occl_l_eye.append(o_le)
    occl_mouth.append(o_mo)
    occl_nose.append(o_no)
    occl_r_contour.append(o_rc)
    occl_r_eye.append(o_re)




plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# matplotlib画图中中文显示会有问题，需要这两行设置默认字体

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=2000, xmin=0)
plt.ylim(ymax=2, ymin=-0.4)
# 画两条（0-9）的坐标轴并设置轴标签x，y

x1 = np.arange(0, 1987, 1)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的x轴坐标
colors1 = '#00CED1'  # 点的颜色
colors2 = '#DC143C'
colors3 = '#FFFFFF'
colors4 = '#58B0F0'
colors5 = '#FFE05E'
colors6 = '#5DFF74'
colors7 = '#5D5DFF'
colors8 = '#FF5D5D'
colors9 = '#5DFFDB'
area = np.pi * 0.5** 2  # 点面积
# 画散点图
plt.scatter(x1, bluriness, s=area, c=colors1, alpha=0.4, label='bluriness')
# plt.scatter(x1, illum, s=area, c=colors2, alpha=0.4, label='illum')
plt.scatter(x1, occl_chin, s=area, c=colors3, alpha=0.4, label='occl_chin')
plt.scatter(x1, occl_l_contour, s=area, c=colors4, alpha=0.4, label='occl_l_contour')
plt.scatter(x1, occl_l_eye, s=area, c=colors5, alpha=0.4, label='occl_l_eye')
plt.scatter(x1, occl_mouth, s=area, c=colors6, alpha=0.4, label='occl_mouth')
plt.scatter(x1, occl_nose, s=area, c=colors7, alpha=0.4, label='occl_nose')
plt.scatter(x1, occl_r_contour, s=area, c=colors8, alpha=0.4, label='occl_r_contour')
plt.scatter(x1, occl_r_eye, s=area, c=colors9, alpha=0.4, label='occl_r_eye')



plt.plot([0, 9.5], [9.5, 0], linewidth='0.5', color='#000000')
plt.legend()
plt.savefig(r'./12345svm.png', dpi=300)
plt.show()
