def paros_e(x, *args):
    talalat = False
    index = x
    while x < len(*args) and not talalat:
        if args[x] % 2 == 0:
            talalat = True
        x = x + 1
    
    if talalat:
        return True
    else:
        return False

print(paros_e(1, 20, 11, 7, 17))