def solution(maze):
    rows = len(maze)
    cols = len(maze[0])

    def possible_new_pos(pos):
        return [
            {
                'r': pos['r'],
                'c': pos['c'] + 1
            },
            {
                'r': pos['r'],
                'c': pos['c'] - 1
            },
            {
                'r': pos['r'] + 1,
                'c': pos['c']
            }
            ,
            {
                'r': pos['r'] - 1,
                'c': pos['c']
            }
        ]

    def in_maze(pos):
        return pos['r'] >=0 and pos['c']>=0 and pos['r'] < rows and pos['c'] < cols

    class MazeStep:
        
        def __init__(self, pos, can_pass_walls, step_number):
            self.pos = pos
            self.can_pass_walls = can_pass_walls
            self.step_number = step_number

        def possible_moves(self):
            new_pos = possible_new_pos(self.pos)
            new_pos = filter(in_maze, new_pos)

            moves =[]
            for pos in new_pos:
                if maze[pos['r']][pos['c']] == 0:
                    moves.append(MazeStep(pos, self.can_pass_walls, self.step_number+1))
                else:
                    if self.can_pass_walls:
                        moves.append(MazeStep(pos, False, self.step_number+1))
            return moves

    def is_winner(step, matches):
        step_code = str(step.pos['c']) + '-' + str(step.pos['r'])
        if step_code in matches and (step.can_pass_walls or matches[step_code].can_pass_walls):
            return step.step_number + matches[step_code].step_number - 1
        return None
            
    lposes = {}
    rposes = {}
    lnext_steps = []
    rnext_steps = []

    lnext_steps.append(MazeStep({'r': 0, 'c': 0}, True, 1))
    rnext_steps.append(MazeStep({'r': rows-1, 'c': cols-1}, True, 1))
    current_step = 1
    while(len(lnext_steps)>0 or len(rnext_steps)>0):
        while len(lnext_steps)>0 and lnext_steps[0].step_number == current_step:
            lstep = lnext_steps.pop(0)
            step_code = str(lstep.pos['c']) + '-' + str(lstep.pos['r'])
            winner = is_winner(lstep, rposes)
            if winner:
                return winner
            lposes[step_code] = lstep

            for move in lstep.possible_moves():
                winner = is_winner(move, rposes)
                if winner:
                    return winner
                move_code = str(move.pos['c']) + '-' + str(move.pos['r'])
                if move_code in lposes:
                    old_move = lposes[move_code]
                    if not old_move.can_pass_walls and move.can_pass_walls:
                        lnext_steps.append(move)
                else:
                    lnext_steps.append(move)
        
        while len(rnext_steps)>0 and rnext_steps[0].step_number == current_step:
            rstep = rnext_steps.pop(0)
            step_code = str(rstep.pos['c']) + '-' + str(rstep.pos['r'])
            winner = is_winner(rstep, lposes)
            if winner:
                return winner
            
            rposes[step_code] = rstep
            for move in rstep.possible_moves():
                winner = is_winner(move, lposes)
                if winner:
                    return winner
                move_code = str(move.pos['c']) + '-' + str(move.pos['r'])
                if move_code in rposes:
                    old_move = rposes[move_code]
                    if not old_move.can_pass_walls and move.can_pass_walls:
                        rnext_steps.append(move)
                else:
                    rnext_steps.append(move)
        
        current_step += 1


if __name__ == '__main__':
    print (
        solution(
            [
                [0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 0, 0],
                [1, 1, 1, 0]
            ]
        )
    )

    print(
        solution(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0]
            ]
        )
    )

    print(
        solution(
            [
                [0, 0, 0, 0, 0, 1],
                [0, 1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 0, 0, 0],
                [1, 0, 0, 0, 1, 0]
            ]
        )
    )