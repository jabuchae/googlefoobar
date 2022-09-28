def solution(room, me, enemy, max_distance):
    max_distance_pow = max_distance * max_distance
    room_x = room[0]
    room_y = room[1]

    def distance(a, b):
        x_dist = a[0] - b[0]
        y_dist = a[1] - b[1]
        x_dist *= x_dist
        y_dist *= y_dist
        return x_dist + y_dist

    def out_of_range(point, max=max_distance_pow):        
        return distance(point, me) > max

    def slope(p1, p2):
        if p2[0]-p1[0] == 0:
            return -1000000000 if p2[1] > p1[1] else 1000000000
        return float(p2[1]-p1[1]) / float(p2[0]-p1[0]) + (-1000000000 if p2[1] > p1[1] else 1000000000 )

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

    
    def compute_obstacles(room_num_x, room_num_y):
        blockers = {}
        x_i = -room_num_x
        while x_i <= room_num_x:
            y_i = -room_num_y
            while y_i <= room_num_y:

                # corner
                corner = [room_x * x_i, room_y * y_i]
                slope_i = slope(me, corner)
                d_i = distance(corner, me)
                if slope_i in blockers:
                    if blockers[slope_i] > d_i:
                        blockers[slope_i] = d_i
                else:
                    blockers[slope_i] = d_i

                # enemies in the way
                e = translate(enemy, x_i, y_i)
                slope_i = slope(me, e)
                d_i = distance(e, me)
                if slope_i in blockers:
                    if blockers[slope_i] > d_i:
                        blockers[slope_i] = d_i
                else:
                    blockers[slope_i] = d_i
                
                if room_num_x != 0 or room_num_y != 0:
                    # me being in the way
                    e = translate(me, x_i, y_i)
                    slope_i = slope(me, e)
                    d_i = distance(e, me)
                    if slope_i in blockers:
                        if blockers[slope_i] > d_i:
                            blockers[slope_i] = d_i
                    else:
                        blockers[slope_i] = d_i

                y_i += 1
            x_i += 1
        return blockers
        
    def hits(room_num_x, room_num_y, blockers):
        if room_num_x == 0 and room_num_y ==0:
            return True

        enemy_pos = translate(enemy, room_num_x, room_num_y)
        if out_of_range(enemy_pos):
            return False
    
        enemy_slope = slope(me, enemy_pos)
        shot_length = distance(enemy_pos, me)
        
        if enemy_slope in blockers:
            return blockers[enemy_slope] >= shot_length
        
        return True

    if out_of_range(enemy):
        return 0

    max_rooms_x = int(max_distance/room_x)+4
    max_rooms_y = int(max_distance/room_y)+4

    shots = 0

    blockers = compute_obstacles(max_rooms_x, max_rooms_y)

    room_num_x = -max_rooms_x
    while room_num_x <= max_rooms_x:
        room_num_y = -max_rooms_y
        while room_num_y <= max_rooms_y:
            if hits(room_num_x, room_num_y, blockers):
                shots += 1
            room_num_y += 1
        room_num_x += 1

    return shots

if __name__=='__main__':
    print(solution([3,2], [1,1], [2,1], 4))
    print(solution([300,275], [150,150], [185,100], 500))
    print(solution([2,3], [1,1], [1,2], 4))
    print(solution([3,2], [1,1], [2,1], 500))
