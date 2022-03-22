import string

def irasjel_eltavolitas(szoveg):
    irasjel_nelkuli = ""
    for karakter in szoveg:
        if karakter not in string.punctuation:
            irasjel_nelkuli += karakter
    return irasjel_nelkuli

print(irasjel_eltavolitas("Nos, én sose csináltam! - mondta Alice"))
print(irasjel_eltavolitas("Teljesen, de teljesen biztos vagy benne?"))