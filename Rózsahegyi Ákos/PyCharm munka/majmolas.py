with open("majom.jpg", "rb") as forrasfajl:
    with open("masolat.jpg", "wb") as celfajl:
        darab_meret = 2096
        darab = forrasfajl.read(darab_meret)

        while len(darab) > 0:
            celfajl.write(darab)
            darab = forrasfajl.read(darab_meret)