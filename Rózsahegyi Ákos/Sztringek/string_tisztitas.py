irasjelek = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def irasjel_eltavolitas(szoveg):
    irasjel_nelkuli = ""
    for karakter in szoveg:
        if karakter not in irasjelek:
            irasjel_nelkuli += karakter
    return irasjel_nelkuli

print(irasjel_eltavolitas("Szia Lajos! #SWAG #YOLO"))