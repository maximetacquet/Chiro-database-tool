#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 16:02:17 2025
@author: maxime
"""
import sys
import sqlite3
import logging
from pathlib import Path
from environs import Env
from model.lid import Lid

project_root = Path(__file__).resolve().parent.parent


if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))  


env_file = project_root / ".env"
if not env_file.exists():
    raise FileNotFoundError(f".env niet gevonden op: {env_file}")

env = Env()
env.read_env(env_file)  
DATABASE_NAME = env.str("DATABASE")  


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def convert_lid_row_to_object(lid_row: tuple) -> Lid:
    return Lid(
        id=lid_row[0],
        voornaam=lid_row[1],
        achternaam=lid_row[2],
        afdeling=lid_row[3]
    )

def get_connection() -> sqlite3.Connection:
    
    db_path = project_root / DATABASE_NAME

   
    db_path.parent.mkdir(parents=True, exist_ok=True)  

    is_new_db = not db_path.exists()
    conn = sqlite3.connect(db_path)
    logger.info(f"Connecteren naar database op {db_path}")

    if is_new_db:
        logger.info(f"Database op {db_path} bestaat niet. Database creëren.")
        initialize_database(conn)

    return conn

def initialize_database(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leden (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            voornaam TEXT NOT NULL,
            achternaam TEXT NOT NULL,
            afdeling TEXT NOT NULL
        );
    """)
    conn.commit()
    
def get_all_leden() -> list[Lid]:
    leden=[]
    with get_connection() as conn:
        cursor= conn.cursor()
        cursor.execute("SELECT * FROM leden ORDER BY achternaam, voornaam")
        rows= cursor.fetchall()
        for row in rows:
            leden.append(convert_lid_row_to_object(row))
    return leden

def get_lid_by_id(lid_id: int) -> Lid | None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM leden WHERE id = ?",
        (lid_id,)
    )  
    row = cursor.fetchone()
    conn.close()
    return convert_lid_row_to_object(row) if row else None

def get_leden_by_naam(naam: str) -> list[Lid]:
    leden = []
    like = f"%{naam.strip().lower()}%"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM leden
            WHERE LOWER(voornaam) LIKE ? OR LOWER(achternaam) LIKE ?
            ORDER BY achternaam, voornaam
            """,
            (like, like)
        )
        rows = cursor.fetchall()
        leden = [convert_lid_row_to_object(r) for r in rows]
    return leden

def save_lid(lid: Lid) -> int:
    conn = get_connection()
    cursor = conn.cursor()

    lid_id = getattr(lid, "id", None)

    if lid_id in (None, 0):
        cursor.execute(
            """
            INSERT INTO leden (voornaam, achternaam, afdeling)
            VALUES (?, ?, ?)
            """,
            (lid.voornaam, lid.achternaam, lid.afdeling)
        )
        conn.commit()
        nieuwe_id = cursor.lastrowid
        conn.close()
        return int(nieuwe_id)
    else:
        cursor.execute(
            """
            UPDATE leden
            SET voornaam = ?, achternaam = ?, afdeling = ?
            WHERE id = ?
            """,
            (lid.voornaam, lid.achternaam, lid.afdeling, lid_id)
        )
        conn.commit()
        conn.close()
        return int(lid_id)