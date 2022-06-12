
def zero(f = None):
    if not f: 
        return 0 
    else: 
        return int(f(0))

def one(f = None):
    if not f: 
        return 1 
    else: 
        return int(f(1))
def two(f = None):
    if not f: 
        return 2
    else: 
        return int(f(2))

def three(f = None): 
    if not f: 
        return 3
    else: 
        return int(f(3))

def four(f = None): 
    if not f: 
        return 4
    else: 
        return int(f(4))

def five(f = None):
    if not f: 
        return 5
    else: 
        return int(f(5))
def six(f = None):
    if not f: 
        return 6
    else: 
        return int(f(6))

def seven(f = None): 
    if not f: 
        return 7
    else: 
        return int(f(7))
        
def eight(f = None):
    if not f: 
        return 8
    else: 
        return int(f(8))
def nine(f = None): 
    if not f: 
        return 9
    else: 
        return int(f(9))


def plus(input):
    return lambda x: x + input
def minus(input): 
    return lambda x: x - input
def times(input):
    return lambda x: x * input
def divided_by(input): 
    return lambda x: x / input 