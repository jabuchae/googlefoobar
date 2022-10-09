
# 2 <= s <= 20
# 1 <= w <= 12
# 1 <= h <= 12
def solution(w, h, s):

    saved_combinations = {}

    def combinations(sum, slots):
        if sum == 0:
            return 1
        if slots == 1:
            return 1
        
        comb_key = str(sum) + '-' + str(slots)
        if comb_key in saved_combinations:
            return saved_combinations[comb_key]
        i = 0
        combs = 0
        while i <= sum:
            combs += combinations(sum-i, slots-1)
            i += 1

        saved_combinations[comb_key] = combs
        return combs
    
    
    configs_on_col = combinations(h, s)
    
    ret = combinations(w, configs_on_col)
    print(saved_combinations)
    
    return ret



if __name__ == '__main__':
    print(solution(2, 2, 2))
    print(solution(2, 3, 4))
