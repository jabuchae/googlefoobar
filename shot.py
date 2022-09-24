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

    def hits_me_first(enemy_pos, room_num_x, room_num_y):
        if room_num_x == 0 and room_num_y == 0:
            return False
        
        if room_num_x == 0:
            return enemy_pos[0] == me[0]
        
        if room_num_y == 0:
            return enemy_pos[1] == me[1]

        if room_num_y == room_num_x:
            return slope([room_x, room_y], me) == slope(enemy, me)

        return False

    max_rooms_x = int(max_distance/room_x)+1
    max_rooms_y = int(max_distance/room_y)+1

    shots = 0
    
    room_num_x = -max_rooms_x
    max_room_y = max_rooms_y
    while room_num_x <= max_rooms_x:
        room_num_y = max_room_y
        while room_num_y >= -max_room_y:
            enemy_pos = translate(enemy, room_num_x, room_num_y)
            if not out_of_range(enemy_pos) and not hits_me_first(enemy_pos, room_num_x, room_num_y):
                shots += 1
            room_num_y -= 1
        room_num_x += 1
    
    return shots

if __name__=='__main__':
    print(solution([3,2], [1,1], [2,1], 4))
    print(solution([300,275], [150,150], [185,100], 500))

