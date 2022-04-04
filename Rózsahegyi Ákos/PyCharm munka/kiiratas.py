'''
Megnyitási módok:
r: Olvasás
w: Írás, fájlt hoz létre; ha léztezik ilyen nevű fájl már, felülírja az eredetit
x: Írás, fájlt hoz létre; ha léztezik ilyen nevű fájl már, hibát ad
a: A létező fájl végére hozzáfűz, ha még nem létezik ilyen nevű, akkor létrehozza
a+: Hozzáfűzést és olvasást is lehetővé tesz
'''

with open('kimenet.txt', 'w', encoding='utf-8') as celfajl:
    print('Ez kerül a fájlba...', file=celfajl)

with open('kimenet.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write('alma, körte, eper')
    # sztringet ír a fájlba

    # lista elemeit írja a fájlba
    celfajl.writelines(['alma\n', 'körte\n', 'eper\n'])


# Olvasás - írás
with open('gyumolcsok.txt', 'r', encoding='utf-8') as forrasfajl, \
    open('gyumolcsok_masolat.txt', 'w', encoding='utf-8') as celfajl:
    for sor in forrasfajl:
        print(sor.strip(), file=celfajl)

with open('gyumolcsok.txt', 'r', encoding='utf-8') as forrasfajl, \
    open('gyumolcsok_masolat.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write(forrasfajl.read())