def snail(snail_map):
    result = []
    while len(snail_map) > 0:
        result += snail_map[0]
        del snail_map[0]
        if len(snail_map) == 0:
            break # covers [1,2,3]
        for r in snail_map:
            result += [r[-1]] # get the last of each row
            del r[-1]
        if len(snail_map) == 0:
            break
        result += snail_map[-1][::-1] # get the last row reverse
        del snail_map[-1]
        if len(snail_map) == 0:
            break
        for r in list(reversed(snail_map)):
            result += [r[0]]
            del r[0]
    return result