
def add(p,q):
    return p+q

def sub(p,q):
    return p-q

def mul(p,q):
    return p*q

def divide(p,q):
    if q==0:
        raise ValueError ("you can't divide by zero")
    return p/q    