# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 20:18:40 2025

@author: maxime
"""

import db.database as database  
from model.lid import Lid
import sys
import csv
from pathlib import Path



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

def voeg_lid_toe() -> None:
    voornaam = input("Voornaam: ").strip()
    achternaam = input("Achternaam: ").strip()
    afdeling = input("Afdeling: ").strip()

    if not voornaam or not achternaam or not afdeling:
        print("Voornaam, achternaam en afdeling zijn verplicht.")
        return

    nieuw_lid = Lid(id=0, voornaam=voornaam, achternaam=achternaam, afdeling=afdeling)
    new_id = database.save_lid(nieuw_lid)
    print(f"Lid toegevoegd met id={new_id}.")


def wijzig_lid() -> None:
    try:
        lid_id = int(input("Welk id wil je wijzigen? "))
    except ValueError:
        print("Ongeldig id.")
        return

    bestaandid = database.get_lid_by_id(lid_id)
    if bestaandid is None:
        print("Geen lid gevonden met dit id.")
        return

    print("Druk Enter om een veld hetzelfde te laten.")
    voornaam = input(f"Voornaam ({bestaandid.voornaam}): ").strip() or bestaandid.voornaam
    achternaam = input(f"Achternaam ({bestaandid.achternaam}): ").strip() or bestaandid.achternaam
    afdeling = input(f"Afdeling ({bestaandid.afdeling}): ").strip() or bestaandid.afdeling

    updated = Lid(id=lid_id, voornaam=voornaam, achternaam=achternaam, afdeling=afdeling)
    database.save_lid(updated)
    print("Lid aangepast.")


def verwijder_lid() -> None:
    try:
        lid_id = int(input("Welk id wil je verwijderen? "))
    except ValueError:
        print("Ongeldig id")
        return

    bestaand = database.get_lid_by_id(lid_id)
    if bestaand is None:
        print("Geen lid gevonden met dit id.")
        return

    bevestigen = input(
        f"Typ 'ja' als je zeker bent dat je {bestaand.voornaam} {bestaand.achternaam} wil verwijderen: "
    ).strip().lower()

    if bevestigen != "ja":
        print("Verwijderen geannuleerd")
        return

    database.delete_lid(lid_id)
    print("Lid verwijderd.")

def exporteer_leden_naar_csv() -> None:
    leden = database.get_all_leden()
    if len(leden) == 0:
        print("Geen leden om te exporteren.")
        return

    export_map = Path("exports")
    export_map.mkdir(parents=True, exist_ok=True)
    uitvoer_pad = export_map / "leden.csv"

    with uitvoer_pad.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "voornaam", "achternaam", "afdeling"])
        writer.writeheader()
        writer.writerows(
            {
                "id": l.id,
                "voornaam": l.voornaam,
                "achternaam": l.achternaam,
                "afdeling": l.afdeling,
            }
            for l in leden
        )  

    print(f"CSV geëxporteerd naar: {uitvoer_pad}")


def programma_verlaten() -> None:
    sys.exit(0)  


def menu() -> None:
    while True:
        print(
            """
1. Toon alle leden
2. Zoek lid op id
3. Zoek leden op naam
4. Voeg lid toe
5. Wijzig lid
6. Verwijder lid
7. Exporteer leden naar CSV
8. Programma afsluiten
"""
        )

        keuze = input("Kies een optie (1-8): ").strip()
        if keuze == "1":
            toon_alle_leden()
        elif keuze == "2":
            toon_lid_op_id()
        elif keuze == "3":
            zoek_leden_op_naam()
        elif keuze == "4":
            voeg_lid_toe()
        elif keuze == "5":
            wijzig_lid()
        elif keuze == "6":
            verwijder_lid()
        elif keuze == "7":
            exporteer_leden_naar_csv()
        elif keuze == "8":
            programma_verlaten()
        else:
            print("Ongeldige keuze. Kies een nummer van 1 t.e.m. 8.")

