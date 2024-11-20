"""A játékban van egy harcos és egy varázsló, akik minden körben egy 3 elemű játéktéren léphetnek véletlenszerűen egy mezőre. Amennyiben ugyanarra a mezőre lépnek, akkor harcolnak.

Kezdetben mindkét játékos életerejét véletlenszerűen határozzuk meg egy 6 oldalú kocka dobásával. A minimális életerőpont 3 lehet, ehhez adjuk a kockadobás eredményét.

A játék során minden körben váletlenszerűen változik a játékosok pozíciója ([0,2] zárt intervallumban)

A harc azt jelenti, hogy az éelterejük 0-val, vagy 1-gyel csökken."""

"""Milyen osztályok kellenek?
Jatekos()
adattagok: nev, poz, kaszt, hp - nem kivulrol kapja hanem egy belso fuggveny adja majd meg

"""

from Jatekter import Jatekter

jatekter=Jatekter()
jatekter.jatekmenet()