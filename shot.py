def solution(room, me, enemy, max_distance):
    max_distance_pow = max_distance * max_distance
    room_x = room[0]
    room_y = room[1]

    v_aligned = me[0] == enemy[0]
    h_aligned = me[1] == enemy[1]
    def out_of_range(point):
        x_dist = me[0] - point[0]
        y_dist = me[1] - point[1]
        x_dist *= x_dist
        y_dist *= y_dist
        
        return x_dist + y_dist > max_distance_pow

    def slope(p1, p2):
        if (p2[0]-p1[0]) == 0:
            return None
        return float((p2[1]-p1[1])) / float((p2[0]-p1[0]))

    def translate(pos, room_number_x, room_number_y):
        x = pos[0] 
        x_missing = room_x - x
        x_displacement = x if room_number_x % 2 == 0 else x_missing
        new_room_x = x_displacement + room_number_x*room_x

        y = pos[1] 
        y_missing = room_y - y
        y_displacement = y if room_number_y % 2 == 0 else y_missing
        new_room_y = y_displacement + room_number_y*room_y

        return [new_room_x, new_room_y]

    def hits(room_num_x, room_num_y):
        if room_num_x == 0 and room_num_y ==0:
            return True
        enemy_pos = translate(enemy, room_num_x, room_num_y)
        enemy_slope = slope(enemy_pos, me)

        blockers = []
        x_i = 0
        x_step = 1 if room_num_x >= 0 else -1
        y_step = 1 if room_num_y >= 0 else -1
        while abs(x_i) <= abs(room_num_x):
            y_i = 0
            while abs(y_i) <= abs(room_num_y):
                corners = [
                    [room_x * x_i, room_y * y_i],
                    [room_x * x_i + room_x, room_y * y_i],
                    [room_x * x_i, room_y * y_i + room_y],
                    [room_x * x_i+ room_x, room_y * y_i + room_y],
                ]
                for corner in corners:
                    if not out_of_range(corner):
                        # corners
                        blockers.append(corner)
                if abs(x_i) < abs(room_num_x) or abs(y_i) < abs(room_num_y):
                    e = translate(enemy, x_i, y_i)
                    if not out_of_range(e):
                        # enemies in the way
                        blockers.append(e)
                
                e = translate(me, x_i, y_i)
                if not out_of_range(e):
                    # me being in the way
                    blockers.append(e)
                y_i += y_step
            x_i += x_step
        slopes = map(lambda x: slope(x, me), blockers)
        
        if enemy_slope in slopes:
            return False
        
        res = not out_of_range(enemy_pos)
        
        return res

    if out_of_range(enemy):
        return 0
    max_rooms_x = int(max_distance/room_x)+3
    max_rooms_y = int(max_distance/room_y)+3
    

    shots = 0

    room_num_x = -max_rooms_x
    while room_num_x <= max_rooms_x:
        room_num_y = -max_rooms_y
        while room_num_y <= max_rooms_y:
            if hits(room_num_x, room_num_y):
                shots += 1
            room_num_y += 1
        room_num_x += 1

    return shots

if __name__=='__main__':
    print(solution([3,2], [1,1], [2,1], 4))
    print(solution([300,275], [150,150], [185,100], 500))
    print(solution([4,4], [1,1], [3,3], 5.66))    