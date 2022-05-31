import random

def nevelo():
    maganhangzok = "aáeéiíoóöőuúüű"
    if szo[0].lower() in maganhangzok:
        return "az"
    else:
        return "a"

def jelzo():
    return random.choice(["piros", "nagy", "könnyed"])

print("Adj meg három főnevet!")
for sorszam in range(1, 4):
    fonev = input(str(sorszam) + ". főnév: ")
    print(nevelo(fonev).capitalize(), "", fonev, "", jelzo(), ".")