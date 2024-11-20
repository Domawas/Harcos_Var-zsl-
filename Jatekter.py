from Jatekos import Jatekos
class Jatekter:
    def __init__(self):

        self.harcos=Jatekos("Tubamtolog",0,"támogató","🕵️‍♂️")
        self.varazslo=Jatekos("Waar'Ash Low",2,"támogató","🧙‍♂️")

        self.lista=["_","_","_"]
        self.lista[self.harcos.poz]=self.harcos.emo                #igy tudjuk elérni az adattagokat
        self.lista[self.varazslo.poz]=self.varazslo.emo
        self.kor=1
        self.kiir()


    def kiir(self):
        print(f"{self.kor}.kör")
        print("-"*110)
        print(f"{self.lista} *[    {self.harcos.nev} Életereje: {self.harcos.hp}     ]*[       {self.varazslo.nev} Életereje: {self.varazslo.hp}     ]*")
        print("-"*110)

    def jatekmenet(self):
        """ Játék
        dobunk kockával, az új poziciót. ez a játékos osztály feladata
        """
        while(self.harcos.hp>0 and self.varazslo.hp>0):
            self.harcos.set_pozicio() #lép a harcos
            self.varazslo.set_pozicio() # lép a varázsló
            self.lista=["_","_","_"]
            self.lista[self.harcos.poz]=self.harcos.emo                #igy tudjuk elérni az adattagokat
            self.lista[self.varazslo.poz]=self.varazslo.emo
            if(self.harcos.poz==self.varazslo.poz):
                self.lista[self.varazslo.poz]="⚔"
                """Itt harcolnak """
                self.harcos.set_hp()
                self.varazslo.set_hp()
            self.kor+=1
            self.kiir()
            input()