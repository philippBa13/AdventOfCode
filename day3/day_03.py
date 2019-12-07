"""Day 3: Crossed Wires"""

# get input
file = open("./input.txt")
input = file.read().split("\n")
wire_str_1 = input[0]
wire_str_2 = input[1]

test_str_1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
test_str_2 = "U62,R66,U55,R34,D71,R55,D58,R83"


def get_list_from_string(string):
    string.replace(" ", "")
    result = string.split(",")
    for i in range(len(result)):
        char = str(result[i])[0]
        num = str(result[i])[1:]
        result[i] = (char, num)
    return result


def calc_intersection(wire_1, wire_2):
    points_wire_1 = get_points_set(wire_1)
    points_wire_2 = get_points_set(wire_2)
    print("points wire1: ", points_wire_1)
    print("points wire2: ", points_wire_2)
    return points_wire_1.intersection(points_wire_2)


def calc_smallest_dis_to_point(points_set):
    distance_list = []
    for val in points_set:
        distance_list.append(calc_manhatten_dis((0, 0), val))
    return min(distance_list)


def calc_manhatten_dis(point_1, point_2):
    dis = 0
    for i in range(len(point_1)):
        dis += abs(point_1[i] - point_2[i])
    return dis


def get_points_set(wire):
    points = set()
    curr_point = [0, 0]
    for i in range(len(wire)):
        direction = wire[i][0]
        for j in range(0, int(wire[i][1])):
            if direction == 'R':
                curr_point[0] += 1
            elif direction == 'L':
                curr_point[0] -= 1
            elif direction == 'U':
                curr_point[1] += 1
            elif direction == 'D':
                curr_point[1] -= 1
            points.add(tuple(curr_point.copy()))
    return points


# logic
wire_list_1 = get_list_from_string(wire_str_1)
wire_list_2 = get_list_from_string(wire_str_2)

test_list_1 = get_list_from_string(test_str_1)
test_list_2 = get_list_from_string(test_str_2)

intersections = calc_intersection(wire_list_1, wire_list_2)

# awnser part1
print("smallest manhatten distance: ", calc_smallest_dis_to_point(intersections))
