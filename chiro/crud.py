# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 20:18:40 2025

@author: maxime
"""

import db.database as database  



def toon_alle_leden() -> None:
    leden = database.get_all_leden()
    if len(leden) == 0:
        print("Er zijn nog geen leden.")
        return
    for lid in leden:
        print(lid)


def toon_lid_op_id() -> None:
    try:
        lid_id = int(input("Geef het id: "))
    except ValueError:
        print("Ongeldig id (geef een geheel getal).")
        return

    lid = database.get_lid_by_id(lid_id)
    if lid is None:
        print("Geen lid gevonden met dit id.")
    else:
        print(lid)


def zoek_leden_op_naam() -> None:
    naam = input("Geef voornaam, achternaam of voornaam & achternaam in: ").strip()
    if naam == "":
        print("Zoekterm mag niet leeg zijn.")
        return

    leden = database.get_leden_by_naam(naam)
    if len(leden) == 0:
        print("Geen leden gevonden.")
        return

    for lid in leden:
        print(lid)

