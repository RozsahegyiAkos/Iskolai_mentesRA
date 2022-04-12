felhasznalo = "bori99"
jelszo = "Szivecske<3"
folytatja = True

while folytatja:
    nevbekeres = str(input("Adja meg a felhasználó nevét! "))
    jelszobekeres = str(input("Adja meg a jelszavát! "))
    
    if nevbekeres == felhasznalo and jelszobekeres == jelszo:
        print("Belépés engedélyezve.")
        folytatja = False
    else:
        print("Belépés megtagadva.")
        folytatja = True