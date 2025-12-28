# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 22:45:24 2025

@author: maxime
"""

Afdelingen = {
    1: "Pimpel",
    2: "Speelclub",
    3: "Rakwi",
    4: "Tito",
    5: "Keti",
    6: "Aspi",
}

class Afdeling:
    def __init__(self, id: int = 0):
        try:
            id = int(id) if id is not None else 0
        except (TypeError, ValueError):
            id = 0

        if id not in Afdelingen:
            self.id = 0
            self.naam = ""
            print(f"AfdelingID {id} is ongeldig. Kies uit: {', '.join(str(k) for k in Afdelingen.keys())}")
            print("Als afdelingID werd er ipv een foute afdelingID niets ingegeven")
        else:
            self.id = id
            self.naam = Afdelingen[id]

    def __str__(self) -> str:
        if self.id == 0:
            return ""
        return f"{self.id} - {self.naam}"