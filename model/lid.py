# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 16:09:52 2025

@author: maxime
"""

Afdelingen = ["Pimpel","Speelclub","Rakwi","Tito","Keti","Aspi"]

class Lid:
    def __init__(self, id: int=0, voornaam:str="", achternaam:str="", afdeling:str=""):
        if id is None:
            self.id=0
        else:
            self.id=id
        if voornaam is None:
            self.voornaam=""
        else:
            self.voornaam=voornaam.title()
        if achternaam is None:
            self.achternaam=""
        else:
            self.achternaam=achternaam.title()
        if afdeling is None:
            self.afdeling=""
        elif afdeling.title() not in Afdelingen:
            self.afdeling=""
            print(f"Afdeling {afdeling} is ongeldig. Kies uit: {', '.join(Afdelingen)}")
            print("Als afdeling werd er ipv een foute afdeling niets ingegeven")
        else:
            self.afdeling= afdeling.title()
    
    def __str__(self):
        return f"{self.voornaam} {self.achternaam} {self.afdeling}"