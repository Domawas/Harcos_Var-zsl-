"""adattagok: nev, poz, kaszt, hp - nem kivulrol kapja hanem egy belso fuggveny adja majd meg"""
import random
class Jatekos:
    def __init__(self,nev:str="Játékos",poz:int=0,kaszt:str="harcos",emo:str="" ):
        self.nev=nev
        self.poz=poz
        self.kaszt=kaszt
        self.emo=emo
        self.hp=3+random.randint(1,6)

    """pozició beállítása tagfügvény set_pozicio - setter"""
    def set_pozicio(self):
        self.poz=random.randint(0,2)
    
    def set_hp(self):
        self.hp=self.hp-random.randint(0,1)
    


    def __str__(self):
        return f"Név: {self.nev}, Pozíció: {self.poz}, Kaszt: {self.kaszt}, HP: {self.hp} Emo: {self.emo}"