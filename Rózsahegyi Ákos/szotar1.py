adatok = {
    "Kutya neve": None,
    "Kutya életkora": None,
    "Kutya fajtája": None,
    "Rendelkezik-e érvényes oltással veszettség ellen": None
}

# print(adatok)


kutyanev = str(input("Add meg a kutyád nevét: "))
adatok["Kutya neve"] = kutyanev

kutyaeletkor = int(input("Add meg a kutyád életkorát: "))
adatok["Kutya életkora"] = kutyaeletkor

kutyafajta = str(input("Add meg a kutyád fajtáját: "))
adatok["Kutya fajtája"] = kutyafajta

kutyaoltas = str(input("Rendelkezik-e érvényes oltással veszettség ellen? (igen/nem) "))
adatok["Rendelkezik-e érvényes oltással veszettség ellen"] = kutyaoltas

print(adatok)