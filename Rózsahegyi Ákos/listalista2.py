elem = "O"
sor = [elem, elem, elem]
tarolo = [sor, sor, sor]
# print tarolo

def rajzolas():
    kord = int(input("Add meg az x és y koordinátát! "))
    for sor in tarolo:
        for elem in sor:
            if xkord < 0:
                folytatja = False
            if ykord < 0:
                folytatja = False
            if sor == xkord and tarolo == ykord:
                print('x ', end='')
            else:
                print(elem, end="")
        print()

rajzolas()