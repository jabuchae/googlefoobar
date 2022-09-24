def solution(entrances, exits, paths):    
    initial_bunnies = 0
    for e in entrances:
        initial_bunnies += sum(paths[e])

    def get_max_escape(exit, max, possible_exits):
        if max == 0 or exit in entrances:
            return max

        i=0
        sum = 0
        while i < len(paths) and sum < max:
            if paths[i][exit] == 0 or i in possible_exits or i == exit: 
                i += 1
                continue
            new_exits = possible_exits + [exit]
            escape = get_max_escape(i, min(max, paths[i][exit]), new_exits)
            real_escape = min(max - sum, escape)
            paths[i][exit] -= real_escape
            sum += real_escape
            i += 1
        
        return sum

    
    for exit in exits:
        get_max_escape(exit, 2000000, exits)
    sums = 0
    for entrance in entrances:
        sums += sum(paths[entrance])

    return initial_bunnies - sums


def base_sols():
    print(
        solution(
            [0],
            [3],
            [
                [0, 7, 0, 0],
                [0, 0, 6, 0],
                [0, 0, 0, 8],
                [9, 0, 0, 0]
            ]
        )
    )

    print(
        solution(
            [0, 1],
            [4, 5],
            [
                [0, 0, 4, 6, 0, 0],
                [0, 0, 5, 2, 0, 0],
                [0, 0, 0, 0, 4, 4],
                [0, 0, 0, 0, 6, 6],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]
            ]
        )
    )

def hard_sol():
    print(
        solution(
            [0, 1],
            [4, 5],
            [
                [0, 0, 1, 5, 0, 0],
                [0, 0, 2, 2, 0, 0],
                [0, 0, 0, 0, 2, 2],
                [0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]
            ]
        )
    )

def hard_sol2():
    print(
        solution(
            [0],
            [3, 4],
            [
                [0, 20, 10, 0, 0],
                [0, 0, 0, 6, 6],
                [0, 0, 0, 6, 6],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )
    )

if __name__ == '__main__':
    base_sols()
    hard_sol()
    hard_sol2()
    


    