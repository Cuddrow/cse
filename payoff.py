def PayoffMatrix(player_1, player_2):
    import pandas as pd
    table = pd.DataFrame(index=player_1, columns=player_2)
    for index_1, allele_1 in enumerate(parent_1):
        for index_2, allele_2 in enumerate(parent_2):
            table.iloc[index_1, index_2] = allele_1 + allele_2

    return table

AsBs = [-1,-1]
AbBs = [0,-3]
AsBb = [-3, 0]
AbBb = [-2,-2]
matrix = [[AsBs, AsBb],[AbBs, AbBb]]
print(matrix[0])
print(matrix[1])
print(matrix[0][0][0])
