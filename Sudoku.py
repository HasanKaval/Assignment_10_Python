# This is just a formatting exercise

sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
count_set = {0, 3, 6}
counter = 0
for i in sudoku :
    inner_count = 0
    if counter in count_set :
        print(11*"- ")
    counter += 1
    for j in i :
        if inner_count == 3 or inner_count == 6 :
            print("|", j, end = " ")
        elif inner_count == 8 :
            print(j)
        else :
            print(j, end = " ")
        inner_count += 1
print(11* "- ")
