def format_duration(seconds):
    if seconds == 0: 
        return "now"
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    day, hour = divmod(hour, 24)
    year, day = divmod(day, 365)
    times = [year, day, hour, min, sec]
    units = ['year', 'day', 'hour', 'minute', 'second']
    to_parse = [[times[index], units[index]] for index, value in enumerate(times) if value != 0]
    result_string = ''

    if len(to_parse) == 1:
        to_parse = to_parse[0]
        result_string += f"{to_parse[0]} {to_parse[1]+'s' if to_parse[0] != 1 else to_parse[1]}" 
    else:
        for i, j in enumerate(to_parse):
            if i < len(to_parse) -1:
                result_string += f"{j[0]} {j[1]+'s' if j[0] != 1 else j[1]}, " 
            else:
                result_string = result_string[:-2]
                result_string += f" and {j[0]} {j[1]+'s' if j[0] != 1 else j[1]}" 
    return result_string