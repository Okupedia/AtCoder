N = int(input())

s_x, s_y, t_x, t_y = map(int, input().split())

s_circle = -1
t_circle = -1

x_y_r_list = []
intersected_list = []
for n in range(N):
    x, y, r = map(int, input().split())
    if (s_x - x) ** 2 + (s_y - y) ** 2 == r ** 2:
        s_circle = n
    if (t_x - x) ** 2 + (t_y - y) ** 2 == r ** 2:
        t_circle = n

    intersected_list.append([])
    for i in range(len(x_y_r_list)):
        compared_circle = x_y_r_list[i]
        center_distance = (compared_circle[0] - x) ** 2 + (compared_circle[1] - y) ** 2
        radius_diff = (compared_circle[2] - r) ** 2
        radius_sum = (compared_circle[2] + r) ** 2
        
        if radius_diff <= center_distance and center_distance <= radius_sum:
            intersected_list[n].append(i)
            intersected_list[i].append(n)


    x_y_r_list.append([x, y, r])

#print(x_y_r_list)
#print(intersected_list)
if t_circle == s_circle:
    print('Yes')
    exit()

current_circle_num_list = [t_circle]
for count in range(N):
    next_circle_num_list = []
    for current_circle_num in current_circle_num_list:
        for circle in intersected_list[current_circle_num]:
            if circle == s_circle:
                print('Yes')
                exit()
            else:
                next_circle_num_list.append(circle)
    current_circle_num_list = list(set(next_circle_num_list))

print('No')