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
    
if __name__ == "__main__":
    get_connection().close()