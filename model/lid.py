# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 16:09:52 2025

@author: maxime
"""

from model.afdeling import Afdelingen


class Lid:
    def __init__(self, id: int = 0, voornaam: str = "", achternaam: str = "", afdeling_id: int = 0):
        if id is None:
            self.id = 0
        else:
            self.id = id

        if voornaam is None:
            self.voornaam = ""
        else:
            self.voornaam = voornaam.title()

        if achternaam is None:
            self.achternaam = ""
        else:
            self.achternaam = achternaam.title()

        if afdeling_id is None:
            self.afdeling_id = 0
        else:
            try:
                afdeling_id = int(afdeling_id)
            except (TypeError, ValueError):
                afdeling_id = 0

            if afdeling_id not in Afdelingen:
                self.afdeling_id = 0
                print(f"AfdelingID {afdeling_id} is ongeldig. Kies uit: {', '.join(str(k) for k in Afdelingen.keys())}")
                print("Als afdelingID werd er ipv een foute afdelingID niets ingegeven")
            else:
                self.afdeling_id = afdeling_id

    def afdeling(self) -> str:
        
        return Afdelingen.get(self.afdeling_id, "")

    def __str__(self) -> str:
        return f"{self.voornaam} {self.achternaam} {self.afdeling}"