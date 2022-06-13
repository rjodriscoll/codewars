def dirReduc(arr):
    opposite = {'NORTH':'SOUTH', 'EAST':'WEST', 'SOUTH':'NORTH', 'WEST':'EAST'}
    
    new_plan = []
    
    for d in arr:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan
    
            
    