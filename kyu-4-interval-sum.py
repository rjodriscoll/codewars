def sum_of_intervals(intervals):
    l = []
    for i in intervals:
        l+= [n for n in range(i[0], i[1])]
    return len(set(l))