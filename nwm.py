from random import randint

Namew = "wilkiem"
hp_wilk = 5
atak_wilk = randint(2,3)
wilk = [Namew,hp_wilk,atak_wilk]

Nameq = "gnomem"
hp_gnom = 3
atak_gnom = randint(1,2)  
gnom = [Nameq,hp_gnom,atak_gnom]

Namet = "trollem"
hp_troll = 10
atak_troll = randint(4,5)
troll = [Namet,hp_troll,atak_troll,]

Nameg = "golemem"
hp_golem = 15
atak_golem = randint(5,7)
golem = [Nameg,hp_gnom,atak_golem]

Namess = "assasynem"
hp_assasin = 5
atak_assasin = randint(5,10)
assain = [Namess,hp_gnom,atak_golem]

Namewoj = "wojownik"
hp_woj = 8
atak_woj = randint(3,5)
wojownik = [Namewoj,hp_woj,atak_woj]

Names = "Somkiem"
hp_smok = 20
atak_smok = randint(5,8)
smok = [Names,hp_smok,atak_smok]

def ręka():
    atak = randint(1,3)
    return atak

def nóż():
    atak = randint(2,4)
    return atak

def miecz():
    atak = randint(3,5)
    return atak

def topór():
    atak = randint(4,6)
    return atak

def buława():
    atak = randint(5,7)
    return atak

def wm():
    atak = randint(6,8)
    return atak

def wt():
    atak = randint(7,9)
    return atak

def iskry():
    global mana
    if mana > 5:
        mana -= 5
        atak = randint(3,5)
        return atak
    else:
        print("Nie masz many ")
        return 0

def sopel():
    global mana
    if mana > 10:
        mana -= 10
        atak = randint(4,6)
        return atak
    else:
        print("Nie masz many ")
        return 0

def fire_ball():
    global mana
    if mana > 20:
        mana -= 20
        atak = randint(5,7)
        return atak
    else:
        print("Nie masz many ")
        return 0

ataki =[
    {
"1 = atak w ręcz"
    },
    {
"2 = atak nożem",
    },
    {
"3 = iskry",
    },
]

def los():
    co = randint(1,7)
    if co == 1:
        pp = wilk
    elif co == 2:
        pp = gnom
    elif co == 3:
        pp = troll
    elif co == 4:
        pp = golem
    elif co == 7:
        pp = smok
    elif co == 5:
        pp = assain
    elif co == 6:
        pp = wojownik
    return pp

def wa():
    print(ataki)
    for x in ataki:
        co = int(input())
    if co == 1:
        return ręka()
    elif co == 2:
            return nóż()  
    elif co == 3:
        if mana > 5:
            return iskry()
        else:
            print("Nie masz many!!")
            return 0
    elif co == 4:
        return miecz()
    elif co == 5:
        return topór()
    elif co == 6:
        return buława()
    elif co == 7:
        return wm()
    elif co == 8:
        return wt()
    elif co == 9:
        if mana > 10:
            return sopel()
        else:
            print("Nie masz many!!")
            return 0
    elif co == 10:
        if mana > 20:
            return fire_ball()
        else:
            print("Nie masz many!!")
            return 0
    else:
        print("Nie wybrano akcji")
        return 0
        
def nagroda():
    new_dictionary = {}
    dw=int(input("""Witaj! W nagrodę za twoje czyny możesz wybrać nagrodę.
    1 = miecz
    2 = topór
    3 = buława
    4 = wielki miecz
    5 = wielki topór
    6 = sopel
    7 = fire ball
    """))
    while True:
        if dw == 1:
            miecz = "miecz"
            new_dictionary["4 = "] = miecz if miecz else "No data"
            ataki.append(new_dictionary)
            break
        elif dw == 2:
            topór = "topór"
            new_dictionary["5 = "] = topór if topór else "No data"
            ataki.append(new_dictionary)
            break
        elif dw == 3:
            buława = "buława"
            new_dictionary["6 = "] = buława if buława else "No data"
            ataki.append(new_dictionary)
            break
        elif dw == 4:
            wielkimiecz = "wielki miecz"
            new_dictionary["7 = "] = wielkimiecz if wielkimiecz else "No data"
            ataki.append(new_dictionary)
            break
        elif dw == 5:
            wielkitopór = "wielki topór"
            new_dictionary["8 = "] = wielkitopór if wielkitopór else "No data"
            ataki.append(new_dictionary)
            break
        elif dw == 6:
            sopel = "sopel"
            new_dictionary["9 = "] = sopel if sopel else "No data"
            ataki.append(new_dictionary)
            break
        elif dw == 7:
            fireball = "fire ball"
            new_dictionary["10 = "] = fireball if fireball else "No data"
            ataki.append(new_dictionary)
            break
        else:
            print("Brak proni pod danym numerem. Spróbuj ponownie.")
            return 0   
    
hp = 100
mana = 100
name = input("Podaj swoje imie:")
print(F"Witaj {name}! Twoim zadaniem będzie zyskanie chwały.Good luck!")
wynik = 0
while hp > 0:
    przeciwnik = los()
    while przeciwnik[1] > 0:
        print(f"{name} walczy teraz z {przeciwnik[0]}")
        print(f"Przeciwnik ma {przeciwnik[1]} Hp i zadaje ci {przeciwnik[2]} obrażeń")
        hp = hp - przeciwnik[2]
        if hp < 0:
            break
        print(f"Zostało ci {hp} Hp i {mana} Many")
        atak  = wa()
        przeciwnik[1] = przeciwnik[1] - atak
        print(f"Zadałeś {atak} obrażeń")
    print('Zabiłeś przeciwnika !!!')
    wynik += 1
    if wynik % 5 == 0:
        nagroda()
else:
    print("Zgineło ci się!")
print(f"Pokonałeś {wynik} przeciwników")

