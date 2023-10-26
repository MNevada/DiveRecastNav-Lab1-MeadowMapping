import meadow_map
import numpy as np
import matplotlib.pyplot as plt
from utils.MinBinaryHeap import MinBinaryHeap

from meadow_map.basic_ops import left_on
from meadow_map.basic_ops import left
import json


def plot_poly(verts: np.ndarray, indices: np.ndarray, color="blue") -> None:
    """
    Plot the simple polygon.
    :param verts:      np.ndarray (#verts, 2)  a list of 2D-vertices position
    :param indices:    np.ndarray (#vert, )    a list of polygon vertex index (to array `verts`)
    :param color:      str                     color
    :return:
    """
    x = []
    y = []
    for i in indices:
        x.append(verts[i][0])
        y.append(verts[i][1])

    x.append(verts[indices[0]][0])
    y.append(verts[indices[0]][1])

    plt.plot(x, y, c=color, linewidth=lineWidth)


lineWidth = 0.5

# open json data
with open('MapPoint.json', 'r') as file:
    # 将JSON文件内容加载到一个变量中
    mapPointData = json.load(file)
# 输出JSON数据
out_border_points_list = []
inner_obstacle_points_list = []

max_x_value_list = []
for index, value in enumerate(mapPointData['points']):
    if index == 0:
        for item in value:
            out_border_points_list.append([item['x']/100, item['y']/100])
        # out_border_points_list.reverse()

        # test
        # value = [[550., 500.], [550., 1250.], [850., 1250.], [850., 1350.],
        #          [350., 1350.], [350., 1800.], [1450., 1800.], [1450., 1350.],
        #          [950., 1350.], [950., 1250.], [1250., 1250.], [1250., 500.]]
        # for item in value:
        #     out_border_points_list.append([item[0], item[1]])

        # test
        # value = [
        #     [750., 1290.], [750., 1500.], [1200., 1500.], [1200., 1290.],
        # ]
        # for item in value:
        #     out_border_points_list.append([item[0], item[1]])

        # test
        # value = [
        #     [350., 1250.], [350., 1800.], [1300., 1800.], [1300., 1250.],
        #     [850,1250],[850,1150],[1300,1150],[1300,1050],
        #     [350,1050],[350,1150],[750,1150],[750,1250]
        # ]
        # for item in value:
        #     out_border_points_list.append([item[0], item[1]])

        # test
        # value = [
        #     [350., 1250.], [350., 1800.], [1300., 1800.], [1300., 1250.],
        #     [850, 1250], [850, 1150], [1300, 1150], [1300, 1050],
        #     [350, 1050], [350, 1150], [750, 1150], [750, 1250]
        # ]
        # for item in value:
        #     out_border_points_list.append([item[0], item[1]])

        # test111111111111
        # value = [
        #     [350., 1250.], [350., 1800.], [1300., 1800.], [1300., 1250.],
        # ]
        # for item in value:
        #     out_border_points_list.append([item[0], item[1]])

    else:
        if index <= 0:
            inner_obstacle_point = []
            # 找到最大值x坐标
            max_x_value = None
            for item in value:
                inner_obstacle_point.append([item['x'] / 100, item['y'] / 100])
                if max_x_value is None:
                    max_x_value = item['x'] / 100
                else:
                    if item['x'] / 100 > max_x_value:
                        max_x_value = item['x'] / 100
            max_x_value_list.append(max_x_value)
            # if index == 13 :
            # inner_obstacle_point.reverse()
            inner_obstacle_points_list.append(np.array(inner_obstacle_point))



        # test1
        # if index != 13:
        #     if index == 7:
        #         inner_obstacle_point = []
        #         for item in value:
        #             inner_obstacle_point.append([item['x'] / 100, item['y'] / 100])
        #             # inner_obstacle_point.reverse()
        #         inner_obstacle_points_list.append(np.array(inner_obstacle_point))

        # test2
        # if index != 13:
        #     if index == 7 or index == 1:
        #         # if index == 1:
        #         #     value = [
        #         #         {"x": 97195, "y": 143980}, {"x": 95992, "y": 144004}, {"x": 95984, "y": 145982},
        #         #         {"x": 94805, "y": 146014},
        #         #         {"x": 94785, "y": 148029}, {"x": 97166, "y": 148004}, {"x": 97186, "y": 146006},
        #         #         {"x": 98377, "y": 145969},
        #         #         {"x": 98441, "y": 143999}, {"x": 99574, "y": 144016}, {"x": 99636, "y": 141995},
        #         #         {"x": 100796, "y": 142016},
        #         #         {"x": 100806, "y": 139985}, {"x": 98411, "y": 139993}, {"x": 98411, "y": 141978},
        #         #         {"x": 97203, "y": 141992}
        #         #     ]
        #         # if index == 7:
        #         #     value = [
        #         #         {"x": 103179, "y": 146006}, {"x": 102002, "y": 146000}, {"x": 102002, "y": 148031},
        #         #         {"x": 103155, "y": 148037},
        #         #         {"x": 103197, "y": 150015}, {"x": 104350, "y": 150045}, {"x": 104380, "y": 151986},
        #         #         {"x": 103185, "y": 152034},
        #         #         {"x": 103197, "y": 154006}, {"x": 101973, "y": 154024}, {"x": 101978, "y": 156037},
        #         #         {"x": 103149, "y": 156037},
        #         #         {"x": 103191, "y": 157991}, {"x": 105605, "y": 157967}, {"x": 105605, "y": 156031},
        #         #         {"x": 104386, "y": 155983},
        #         #         {"x": 104416, "y": 153982}, {"x": 105599, "y": 153994}, {"x": 105605, "y": 152017},
        #         #         {"x": 106806, "y": 151975},
        #         #         {"x": 106752, "y": 150033}, {"x": 105593, "y": 149973}, {"x": 105606, "y": 148027},
        #         #         {"x": 104382, "y": 147998},
        #         #         {"x": 104376, "y": 146008}, {"x": 108038, "y": 145990}, {"x": 108002, "y": 143994},
        #         #         {"x": 103169, "y": 144012}
        #         #     ]
        #
        #         #test
        #         if index == 1:
        #             value = [
        #
        #                 {"x": 100796, "y": 142016},
        #                 {"x": 100806, "y": 139985}, {"x": 98411, "y": 139993}, {"x": 98411, "y": 141978},
        #
        #             ]
        #         if index == 7:
        #             value = [
        #                         {"x": 103179, "y": 146006}, {"x": 108038, "y": 145990}, {"x": 108002, "y": 143994},
        #                         {"x": 103169, "y": 144012}
        #                     ]
        #         inner_obstacle_point = []
        #         for item in value:
        #             inner_obstacle_point.append([item['x'] / 100, item['y'] / 100])
        #             # inner_obstacle_point.reverse()
        #         inner_obstacle_points_list.append(np.array(inner_obstacle_point))

        # test11111111111111111
        # if index != 13:
        #     # if index == 2 or index == 10:
        #         inner_obstacle_point = []
        #         # 找到最大值x坐标
        #         max_x_value = None
        #         for item in value:
        #             inner_obstacle_point.append([item['x'] / 100, item['y'] / 100])
        #             if max_x_value is None:
        #                 max_x_value = item['x'] / 100
        #             else:
        #                 if item['x'] / 100 > max_x_value:
        #                     max_x_value = item['x'] / 100
        #         max_x_value_list.append(max_x_value)
        #             # inner_obstacle_point.reverse()
        #         inner_obstacle_points_list.append(np.array(inner_obstacle_point))

max_x_value_list_index = [i for i in range(len(inner_obstacle_points_list))]

def compare_index(index):
    return max_x_value_list[index]

max_x_value_list_index.sort(key=compare_index)

# out lines
verts_poly = np.array(out_border_points_list)
indices_poly = [verts_poly.shape[0] - i - 1 for i in range(verts_poly.shape[0])]  # CCW
# show lines
plot_poly(verts_poly, indices_poly, [0, 0, 1.0])
plt.scatter(verts_poly[0][0], verts_poly[0][1])

# aa = inner_obstacle_points_list[0]
# aa_indice = [(i + 2) % aa.shape[0] for i in range(aa.shape[0])]
# #start merge all lines
# verts, indices, _mergeLineSeg = meadow_map.merge_hole(verts_poly, indices_poly, aa, aa_indice)

verts = verts_poly
indices = indices_poly
diagsAll = []
mergeLineSeg = []
count = 1
for i in max_x_value_list_index:
    verts_hole = inner_obstacle_points_list[i]
    plt.scatter(verts_hole[0][0], verts_hole[0][1], linewidth=lineWidth)
    # plt.text(verts_hole[0][0], verts_hole[0][1], count, color="red")
    count += 1
    indices_hole = [(i + 2) % verts_hole.shape[0] for i in range(verts_hole.shape[0])]
    # show inner obstacle
    plot_poly(verts_hole, indices_hole, [0.0, 0.0, 0.0])
    # mergeLine
    verts, indices, _mergeLineSeg = meadow_map.merge_hole(verts, indices, verts_hole, indices_hole,inner_obstacle_points_list,i)
    if _mergeLineSeg is not None:
        mergeLineSeg.append(_mergeLineSeg)
        diagsAll.append([_mergeLineSeg[0], _mergeLineSeg[1]])

polys, diags = meadow_map.convexify(verts, indices)

# plot mergeline
for item in mergeLineSeg:
    plt.plot(
        [verts[item[0]][0], verts[item[1]][0]],
        [verts[item[0]][1], verts[item[1]][1]],
        "--", c=[0.9, 0.4, 0.8],
        linewidth=lineWidth
    )

# plot all diags. with dotted line
for d in diags:
    posA = verts[indices[d[0]]]
    posB = verts[indices[d[1]]]
    diagsAll.append([indices[d[0]], indices[d[1]]])
    plt.plot([posA[0], posB[0]], [posA[1], posB[1]], "--", c=[0.4, 0.4, 0.8], linewidth=lineWidth)

# indices for result convexy_polys
indices_res_polys = [i for i in range(len(polys))]
# indices for diagnals
indices_res_diags = [i for i in range(len(diagsAll))]

# 再对角线中心展示下标号
for diag_indice in indices_res_diags:
    _diag = diagsAll[diag_indice]
    posA = verts[_diag[0]]
    posB = verts[_diag[1]]
    # plt.text((posA[0] + posB[0]) / 2, (posA[1] + posB[1]) / 2, diag_indice, color="red")


# get the center pos of poly
def getCenterPos(verts, verts_indices):
    sumx = 0
    sumy = 0
    for indice in verts_indices:
        sumx += verts[indice][0]
        sumy += verts[indice][1]
    centX = sumx / len(verts_indices)
    centY = sumy / len(verts_indices)
    return [centX, centY]


# show the centroid of a triangle by the item number
center_of_polys = {}
for i in range(len(polys)):
    centerPos = getCenterPos(verts, polys[i])
    center_of_polys[i] = centerPos
    # plt.text(centerPos[0], centerPos[1], i, color="black")


def doAfterConvexifyAndSearch():
    # search the path

    # example 1
    startPos = [100, 100]
    # endPos = [1200., 1740]

    # example 2
    # startPos = [1000, 1500]
    # startPos = [1000, 1370]
    # endPos = [1100., 1360.]

    # example 3
    # startPos = [1000, 1500]
    # startPos = [800, 1370.]
    # endPos = [1090., 1475.]
    # endPos = [1150., 1750.]

    # example 4
    # startPos = [853, 1362]
    # startPos = [800, 1580]
    endPos = [1150., 1750.]

    plt.scatter(startPos[0], startPos[1])
    plt.scatter(endPos[0], endPos[1])

    # plt.plot([startPos[0], endPos[0]], [startPos[1], endPos[1]], "--", c=[0.4, 0.4, 0.8], linewidth=lineWidth)

    # plt.show()

    def generateLineNum(origin, target):
        return str(origin) + "_" + str(target)

    # establishing a bidirectional index for the diagonals
    biDirDignal = {}
    for diag_indice in indices_res_diags:
        _diag = diagsAll[diag_indice]
        positive_str = generateLineNum(_diag[0], _diag[1])
        negative_str = generateLineNum(_diag[1], _diag[0])
        biDirDignal[positive_str] = diag_indice
        biDirDignal[negative_str] = diag_indice

    # record ploygons connected by diagnals
    diag_poly_map = {}

    # record neighbours of polygons
    poly_neighbour = {}
    # detect which polygons contain internal diagonals.
    for i in range(len(polys)):
        poly_indices = polys[i]
        for j in range(len(poly_indices)):
            now = poly_indices[j]
            if j != len(poly_indices) - 1:
                next = poly_indices[j + 1]
            else:
                next = poly_indices[0]
            lineStr = generateLineNum(now, next)
            if lineStr in biDirDignal:
                diag_num = biDirDignal[lineStr]
                if diag_num not in diag_poly_map:
                    diag_poly_map[diag_num] = []
                if i not in poly_neighbour:
                    poly_neighbour[i] = {}
                diag_poly_map[diag_num].append(i)
                poly_neighbour[i][diag_num] = 0  # Simply providing default values and will handle the rest later

    # get distance between two pos
    def getDistance(posA, posB):
        return (posB[0] - posA[0]) ** 2 + (posB[1] - posA[1]) ** 2

    # mapping of adjacent triangles to corresponding diagonals
    poly_diag_map = {}
    #
    center_distance_map = {}
    for diag_num, poly_indices in diag_poly_map.items():
        poly_indice1 = poly_indices[0]
        poly_indice2 = poly_indices[1]
        poly_diag_map[str(poly_indice1) + "_" + str(poly_indice2)] = diag_num
        poly_diag_map[str(poly_indice2) + "_" + str(poly_indice1)] = diag_num
        center_poly1 = getCenterPos(verts, polys[poly_indice1])
        center_poly2 = getCenterPos(verts, polys[poly_indice2])
        distance = getDistance(center_poly1, center_poly2)
        center_distance_map[str(poly_indice1) + "_" + str(poly_indice2)] = distance
        center_distance_map[str(poly_indice2) + "_" + str(poly_indice1)] = distance

    # get neighbours of polygons
    for poly_indice, diag_nums in poly_neighbour.items():
        for diag_num in diag_nums:
            if diag_num in diag_poly_map:
                for _poly_indice in diag_poly_map[diag_num]:
                    if _poly_indice != poly_indice:
                        poly_neighbour[poly_indice][diag_num] = _poly_indice

    # get the polygon where the starting point and ending point are located.
    startPolyIndice = 0
    endPolyIndice = 0
    for poly_indice in indices_res_polys:
        poly = polys[poly_indice]
        count = len(poly)
        if startPolyIndice == 0 or endPolyIndice == 0:
            startFlag = True
            endFlag = True
            for i in range(count):
                ia = verts[poly[i]]
                if i != count - 1:
                    ia_next = verts[poly[i + 1]]
                else:
                    ia_next = verts[poly[0]]
                if startPolyIndice == 0:
                    if not left_on(ia, ia_next, startPos):
                        startFlag = False
                if endPolyIndice == 0:
                    if not left_on(ia, ia_next, endPos):
                        endFlag = False
            if startPolyIndice == 0 and startFlag:
                startPolyIndice = poly_indice
            if endPolyIndice == 0 and endFlag:
                endPolyIndice = poly_indice

    # if start pos and end pos in the same polygon,return the path
    # if startPolyIndice == endPolyIndice:
    #     return [startPos,endPos]

    # overloading the compare function of binaryheap
    def custom_compare(node1, node2):
        return node1['f'] - node2['f']

    # overloading the insert function of binaryheap
    def insert(self, value):
        if not hasattr(self, 'value_index_map'):
            self.value_index_map = {}
        self.heap.append(value)
        index = len(self.heap) - 1
        value['index'] = index
        self.value_index_map[value['polyIndice']] = value
        self._percolate_up(index)

    # A* algorithm
    def findPassPolys(poly_neighbour, startPoly, endPoly):
        """
        Return the pass polygon indices between start polygon and end polygon.
        :param poly_neighbour   dictionary  all the polys and their neighbours
        :param startPoly:       int         the index of start polygon
        :param endPoly:         int         the index of end polygon
        :return:                list        a list of the pass polygon indices between start polygon and end polygon.
        """
        closeList = {}  # visited poly
        initNode = {
            'g': 0,
            'f': 0,
            # 'x': startPos[0],
            # 'y': startPos[1],
            'polyIndice': startPoly
        }
        heap = MinBinaryHeap(compare_func=custom_compare, insert_func=insert)
        heap.insert(heap, initNode)
        while (len(heap.heap) > 0):
            node = heap.pop_min()
            closeList[node['polyIndice']] = True
            nodePolyIndice = node['polyIndice']
            if nodePolyIndice == endPoly:
                path = []
                path.append(nodePolyIndice)
                fatherIndice = heap.value_index_map[nodePolyIndice]['father']
                while (fatherIndice != startPolyIndice):
                    path.append(fatherIndice)
                    fatherIndice = heap.value_index_map[fatherIndice]['father']
                path.append(startPoly)
                path.reverse()
                return path
            for diag_num, neighbour_poly_indice in poly_neighbour[nodePolyIndice].items():
                if neighbour_poly_indice not in closeList:
                    g = node['g'] + center_distance_map[str(neighbour_poly_indice) + "_" + str(nodePolyIndice)]
                    if neighbour_poly_indice not in heap.value_index_map:
                        # get value H of neighbour
                        h = getDistance(center_of_polys[neighbour_poly_indice], endPos)
                        # get value G when arrive neighbour
                        neighbour_node = {
                            'g': g,
                            'f': h + g,
                            'polyIndice': neighbour_poly_indice,
                            'father': nodePolyIndice,
                        }
                        heap.insert(heap, neighbour_node)
                    else:
                        neighbour_node = heap.value_index_map[neighbour_poly_indice]
                        ng = neighbour_node['g']
                        if ng > g:
                            neighbour_node['father'] = node['polyIndice']
                            neighbour_node['g'] = g
                            neighbour_node['f'] = h + g
                            # fix heap
                            heap.update(neighbour_node['index'])

    # get the pass ploygons No. between the startpos and endpos
    path_poly = findPassPolys(poly_neighbour, startPolyIndice, endPolyIndice)

    # show the path of polys
    for i in range(len(path_poly) - 1):
        center = center_of_polys[path_poly[i]]
        next_center = center_of_polys[path_poly[i + 1]]
        plt.plot(
            [center[0], next_center[0]],
            [center[1], next_center[1]],
            "--", c='green',
            linewidth=lineWidth
        )

    pass_diagnals = []
    for i in range(len(path_poly) - 1):
        diag_num = poly_diag_map[str(path_poly[i]) + "_" + str(path_poly[i + 1])]
        center = center_of_polys[path_poly[i]]
        # Based on looking towards the next crossed diagonal from each triangle’s centroid,
        # determine the left and right of the endpoints.
        info = {
            'diag_num': diag_num,
        }
        diagPos = diagsAll[diag_num]
        if left_on(center, verts[diagPos[0]], verts[diagPos[1]]):
            info['left'] = verts[diagPos[1]]
            info['right'] = verts[diagPos[0]]
        else:
            info['left'] = verts[diagPos[0]]
            info['right'] = verts[diagPos[1]]
        pass_diagnals.append(info)

    # Treating the endpoint as an edge, with the same left and right vertices
    pass_diagnals.append({
        'left': endPos,
        'right': endPos,
    })

    # Funnel Algorithm to find final path (todo )
    apex = startPos  # representing the starting point
    # define the left and right boundry of funnel
    firstDiagInfo = pass_diagnals[0]
    lastLeft, lastRight = firstDiagInfo['left'], firstDiagInfo['right']
    lastLeftIndex = 0
    lastRightIndex = 0
    passing_point = []
    passing_point.append(startPos)

    # check if the same point
    def checkIfTheSamePoint(posA, posB):
        return posA[0] == posB[0] and posA[1] == posB[1]

    lenPassDiagnals = len(pass_diagnals)
    i = 1
    while i < lenPassDiagnals:
        diag_info = pass_diagnals[i]
        leftPoint = diag_info['left']
        rightPoint = diag_info['right']

        if not checkIfTheSamePoint(leftPoint, lastLeft):
            if checkIfTheSamePoint(lastLeft, apex):
                lastLeft = leftPoint
                lastLeftIndex = i
            else:
                if i >= lenPassDiagnals - 1:
                    if not left_on(apex, lastRight, leftPoint):
                        apex = lastRight
                        passing_point.append(apex)
                else:
                    if not left(apex, lastLeft, leftPoint):
                        if left_on(apex, lastRight, leftPoint):
                            lastLeft = leftPoint
                            lastLeftIndex = i
                        else:
                            apex = lastRight
                            passing_point.append(apex)
                            i = lastRightIndex + 1
                            _digInfo = pass_diagnals[i]
                            lastLeft, lastRight = _digInfo['left'], _digInfo['right']
                            lastLeftIndex = i
                            lastRightIndex = i

        # right
        if not checkIfTheSamePoint(rightPoint, lastRight):
            if checkIfTheSamePoint(lastRight, apex):
                lastRight = rightPoint
                lastRightIndex = i
            else:
                if i >= lenPassDiagnals - 1:
                    if left(apex, lastLeft, rightPoint):
                        apex = lastLeft
                        passing_point.append(apex)
                else:
                    if left_on(apex, lastRight, rightPoint):
                        if not left(apex, lastLeft, rightPoint):
                            lastRight = rightPoint
                            lastRightIndex = i
                        else:
                            apex = lastLeft
                            passing_point.append(apex)
                            i = lastLeftIndex + 1
                            _digInfo = pass_diagnals[i]
                            lastLeft, lastRight = _digInfo['left'], _digInfo['right']
                            lastLeftIndex = i
                            lastRightIndex = i

        i += 1

    passing_point.append(endPos)

    print(startPos, endPos)
    print(path_poly)
    print(passing_point)
    # show the final path
    for i in range(len(passing_point) - 1):
        posA = passing_point[i]
        next_posA = passing_point[i + 1]
        plt.plot(
            [posA[0], next_posA[0]],
            [posA[1], next_posA[1]],
            "-", c='red',
            linewidth=lineWidth
        )

    # export need data as json file
    res = {
        'poly_diag_map': poly_diag_map,
        'verts': verts.tolist(),
        'polys': polys,
        'diagnals_all': diagsAll,
        'poly_center': center_of_polys,
        'center_distance_map': center_distance_map,
        'poly_neighbour_diag': poly_neighbour,
    }

    jsondatar = json.dumps(res, ensure_ascii=False, indent=4)

    with open('data.json', 'w', encoding='utf-8') as f:
        f.write(jsondatar)


# doAfterConvexifyAndSearch()

plt.grid()
plt.title("Convexify with holes")
plt.show()
