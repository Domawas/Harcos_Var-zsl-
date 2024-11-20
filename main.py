"""A játékban van egy harcos és egy varázsló, akik minden körben egy 3 elemű játéktéren léphetnek véletlenszerűen egy mezőre. Amennyiben ugyanarra a mezőre lépnek, akkor harcolnak.

Kezdetben mindkét játékos életerejét véletlenszerűen határozzuk meg egy 6 oldalú kocka dobásával. A minimális életerőpont 3 lehet, ehhez adjuk a kockadobás eredményét.

A játék során minden körben váletlenszerűen változik a játékosok pozíciója ([0,2] zárt intervallumban)

A harc azt jelenti, hogy az éelterejük 0-val, vagy 1-gyel csökken."""

"""Milyen osztályok kellenek?
Jatekos()
adattagok: nev, poz, kaszt, hp - nem kivulrol kapja hanem egy belso fuggveny adja majd meg

"""

from Jatekos import Jatekos
harcos=Jatekos("Tubamtolog",0,"támogató","🕵️‍♂️")
varazslo=Jatekos("Waar'Ash Low",2,"támogató","🧙‍♂️")

lista=["_","_","_"]
lista[harcos.poz]=harcos.emo                #igy tudjuk elérni az adattagokat
lista[varazslo.poz]=varazslo.emo


def kiir(kor:int=0):
    print(f"{kor}.kör")
    print("-"*110)
    print(f"{lista} *[    {harcos.nev} Életereje: {harcos.hp}     ]*[       {varazslo.nev} Életereje: {varazslo.hp}     ]*")
    print("-"*110)

n=1 # Kör
kiir(n)

""" Játék

dobunk kockával, az új poziciót. ez a játékos osztály feladata
"""
while(harcos.hp>0 and varazslo.hp>0):
    harcos.set_pozicio() #lép a harcos
    varazslo.set_pozicio() # lép a varázsló
    lista=["_","_","_"]
    lista[harcos.poz]=harcos.emo                #igy tudjuk elérni az adattagokat
    lista[varazslo.poz]=varazslo.emo
    if(harcos.poz==varazslo.poz):
        lista[varazslo.poz]="⚔"
        """Itt harcolnak """
        harcos.set_hp()
        varazslo.set_hp()
    n+=1
    kiir(n)
    input()