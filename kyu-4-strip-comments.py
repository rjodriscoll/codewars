def strip_comments(strng,markers):
    str_list = strng.split("\n")
    res_list = []

    for i in str_list:
        s = ""
        for c in i:
            if c in markers:
                break
            s += c
        res_list.append(s.rstrip())
    return "\n".join(res_list)