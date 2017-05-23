def check_sudoku(grid):

    def sanity_check(lists):
        res = None
        if len(lists) == 9:
            res = True
            for lst in lists:
                if not len(lst) == 9:
                    res = None
                    break
        return res

    def validate_area(area):
        zeros = area.count(0)
        orig_len = len(area)
        area = set(area) - set((0,))
        # has no duplicates, except zeros
        has_no_duplicates = len(set(area) - set((0,))) == orig_len - zeros
        # no values greater than 9
        no_val_greater_nine = not bool(area - set(range(1, 10)))
        return has_no_duplicates and no_val_greater_nine

    if sanity_check(grid) is None:
        return None

    for row in grid:
        first_check = validate_area(row)
        if not first_check:
            break
    for col in zip(*grid):
        second_check = validate_area(col)
        if not second_check:
            break
    for a, b, c in (grid[:3], grid[3:6], grid[6:10]):
        third_check = (validate_area(a[:3] + b[:3] + c[:3]) and
                       validate_area(a[3:6] + b[3:6] + c[3:6]) and
                       validate_area(a[6:10] + b[6:10] + c[6:10]))
        if not third_check:
            break
    res = first_check and second_check and third_check
    return res
