import numpy as np
import cv2

def sortAsScore(point):
    point_s = []
    point_s = point[np.lexsort(-point.T)]
    return point_s

def IOU(ret1, ret2):
    '''
        Intersection(ret1, ret2)/Union(ret1, ret2)
    '''
    # calc the intersection
    x11, x12, y11, y12 = ret1[0], ret1[1], ret1[2], ret1[3]
    x21, x22, y21, y22 = ret2[0], ret2[1], ret2[2], ret2[3]

    width_u  = min(x12, x22)-max(x11, x21)
    height_u = min(y22, y12)-max(y21, y11)

    #Union
    if width_u > 0 and height_u > 0:
        union_area = width_u*height_u
    else:
        union_area = 0
    #Intersection
    intersection_area = (x11 - x12)*(y11 - y12) + (x21 - x22)*(y21 - y22) - union_area

    return union_area/intersection_area

txtfile  = open('point.txt', 'r')

strs = txtfile.readlines()

if len(strs) > 1:
    exit

boxes = strs[0].strip().split(' ')

bbx = []

for it in boxes:
    if it == ' ' or it == '':
        continue
    bbx.append(it)

bbx_float = list(map(float, bbx))

point = np.array(bbx_float, dtype=np.float32).reshape(-1, 5)

sort_point = sortAsScore(point)

print(sort_point)


for idx in range(len(sort_point)):
    for jdx in range(idx+1, len(sort_point)):
        if int(sort_point[jdx][0]) <= 0 | int(sort_point[jdx][2]) <= 0 | int(sort_point[jdx][1]) <= 0 | int(sort_point[jdx][3]) <= 0:
            continue
        iou = IOU(sort_point[idx], sort_point[jdx])
        print(iou)
        if iou > 0.1:
            sort_point[jdx][0], sort_point[jdx][1], sort_point[jdx][2], sort_point[jdx][3], sort_point[jdx][4] = 0, 0, 0, 0, 0


img = cv2.imread('./welcome.jpg')
for it in sort_point:
    if int(it[0]) <= 0 | int(it[2]) <= 0 | int(it[1]) <= 0 | int(it[3]) <= 0:
        continue
    cv2.rectangle(img, (int(it[0]), int(it[2])), (int(it[1]), int(it[3])), (225, 225, 225))

cv2.imshow(" ", img)
cv2.waitKey(10000)