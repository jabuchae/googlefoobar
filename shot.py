def solution(room, me, enemy, max_distance):
    max_distance_pow = max_distance * max_distance
    room_x = room[0]
    room_y = room[1]

    def out_of_range(point):
        x_dist = me[0] - point[0]
        y_dist = me[1] - point[1]
        x_dist *= x_dist
        y_dist *= y_dist
        
        return (x_dist + y_dist) > max_distance_pow

    def slope(p1, p2):
        if (p2[0]-p1[0]) == 0:
            return None
        return float((p2[1]-p1[1])) / float((p2[0]-p1[0]))

    enemy_me_slope = slope(enemy, me)

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

    def hits_me_first(room_num_x, room_num_y):
        if room_num_x == 0 and room_num_y == 0:
            return False
        
        if room_num_x == 0:
            return enemy[0] == me[0]
        
        if room_num_y == 0:
            return enemy[1] == me[1]

        if room_num_y == room_num_x:
            return slope([room_x, room_y], me) == slope(enemy, me)

        return False

    def hits(room_num_x, room_num_y):
        enemy_pos = translate(enemy, room_num_x, room_num_y)
        if hits_me_first(room_num_x, room_num_y):
            return False
        return not out_of_range(enemy_pos)

    max_rooms_x = int(max_distance/room_x)+1
    max_rooms_y = int(max_distance/room_y)+1

    shots = 0
    
    v_aligned = me[0] == enemy[0]
    h_aligned = me[1] == enemy[1]
    upper_right_aligned = slope([room_x, room_y], enemy) == slope([room_x, room_y], me)
    upper_left_aligned = slope([0, room_y], enemy) == slope([0, room_y], me)
    lower_right_aligned = slope([room_x, 0], enemy) == slope([room_x, 0], me)
    lower_left_aligned = slope([0, 0], enemy) == slope([0, 0], me)

    h_fix = 0 if h_aligned else 1
    upper_right_fix = 1 if upper_right_aligned else 0
    upper_left_fix = 1 if upper_left_aligned else 0
    lower_right_fix = 1 if lower_right_aligned else 0
    lower_left_fix = 1 if lower_left_aligned else 0

    room_num_x = 1
    while room_num_x <= max_rooms_x:
        room_num_y = max_rooms_y
        while room_num_y >= 0:
            if hits(room_num_x, room_num_y):
                shots += room_num_y + h_fix
                if room_num_y >= room_num_x:
                    shots -= upper_right_fix
                break
            room_num_y -= 1

        room_num_y = -max_rooms_y
        while room_num_y < 0:
            if hits(room_num_x, room_num_y):
                shots += -room_num_y
                if -room_num_y >= room_num_x:
                    shots -= lower_right_fix
                break
            room_num_y += 1

        room_num_x += 1
    
    room_num_x = -1
    while room_num_x >= -max_rooms_x:
        room_num_y = max_rooms_y
        while room_num_y >= 0:
            if hits(room_num_x, room_num_y):
                shots += room_num_y + h_fix
                if room_num_y >= -room_num_x:
                    shots -= upper_left_fix
                break
            room_num_y -= 1

        room_num_y = -max_rooms_y
        while room_num_y < 0:
            if hits(room_num_x, room_num_y):
                shots += -room_num_y
                if -room_num_y >= -room_num_x:
                    shots -= lower_left_fix
                break
            room_num_y += 1

        room_num_x -= 1

    if not v_aligned:
        room_num_x = 0
        room_num_y = max_rooms_y
        while room_num_y >= 0:
            if hits(room_num_x, room_num_y):
                shots += room_num_y + h_fix
                if room_num_y >= room_num_x:
                    shots -= upper_right_fix
                break
            room_num_y -= 1

        room_num_y = -max_rooms_y
        while room_num_y < 0:
            if hits(room_num_x, room_num_y):
                shots += -room_num_y
                if -room_num_y >= room_num_x:
                    shots -= lower_right_fix
                break
            room_num_y += 1

    if h_aligned and hits(0,0):
        shots += 1
    if v_aligned and hits(0,0):
        shots += 1
    return shots

if __name__=='__main__':
    print(solution([3,2], [1,1], [2,1], 4))
    print(solution([300,275], [150,150], [185,100], 500))

