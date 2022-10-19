def solution(w, h, tokens):        
    saved_combinations = {}
    def combinations(slots, items):
        if slots == 1:
            return [[items]]
        if items == 0:
            return [[0 for _ in range(slots)]]

        comb_key = str(slots) + '-' + str(items)
        if comb_key in saved_combinations:
            return saved_combinations[comb_key]

        res_combinations = []
        for i in range(items+1):
            for partial_value in combinations(slots-1, items-i):
                value = [i] + partial_value
                res_combinations.append(value)

        saved_combinations[comb_key] = res_combinations
        
        return res_combinations

    def key_to_row(key):
        ret = []
        for index, value in enumerate(key):
            for _ in range(value):
                ret.append(index)

        return ret

    def possibleMatrix(keys, combination):
        matrix = []
        for key_index, key_amount in enumerate(combination):
            for _ in range(key_amount):
                matrix.append(key_to_row(keys[key_index]))
        return matrix

    def recIsValidColumns(matrix, columns, usedColumns, usedSpaces, row, col):
        if row == len(matrix):
            return True
        unusedCols = [False for _ in range(len(columns))]
        val = matrix[row][col]
        for col_i, col_v in enumerate(columns):
            if usedColumns[col_i]:
                continue
            for row_i, row_v in enumerate(col_v):
                if row_v == val and usedSpaces[row_i][col_i] is False:
                    usedSpaces[row_i][col_i] = True
                    if col+1 < len(matrix[0]):
                        usedColumns[col_i] = True
                        ret = recIsValidColumns(matrix, columns, usedColumns, usedSpaces, row, col+1)
                        if ret:
                            return True
                        usedColumns[col_i] = False
                    else:
                        ret = recIsValidColumns(matrix, columns, unusedCols, usedSpaces, row+1, 0)
                        if ret:
                            return True
                    usedSpaces[row_i][col_i] = False
        
        return False
                    
    def count_tokens(matrix):
        rows = list(range(len(matrix)))
        cols = list(range(len(matrix[0])))
        
        token_arr = [0 for _ in range(tokens)]
        for r in rows:
            for c in cols:
                token_arr[matrix[r][c]] += 1
        return token_arr

                    
    def isValidColumns(matrix, columns):
        cols = list(range(len(columns)))
        usedSpaces = [[False for _ in cols] for _ in range(len(matrix))]
        return recIsValidColumns(matrix, columns, [False for _ in cols], usedSpaces, 0, 0)


    row_keys = combinations(tokens, w)
    col_keys = combinations(tokens, h)
    row_combinations = combinations(len(row_keys), h)
    col_combinations = combinations(len(col_keys), w)

    
    matrixes = []
    columns = []
    for row_schema in row_combinations:
        matrix = possibleMatrix(row_keys, row_schema)
        matrixes.append({'matrix': matrix,'tokens': count_tokens(matrix)})
    for col_schema in col_combinations:            
        matrix = possibleMatrix(col_keys, col_schema)
        columns.append({'matrix': matrix,'tokens': count_tokens(matrix)})

    count = 0
    for matrix in matrixes:
        for column in columns:
            if matrix['tokens'] == column['tokens'] and isValidColumns(matrix['matrix'], column['matrix']):
                count += 1

    return str(count)


if __name__ == '__main__':
    print(solution(2, 2, 2))
    print(solution(2, 3, 4))
