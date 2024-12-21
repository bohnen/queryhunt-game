#!/bin/env python
# -*- coding: utf-8 -*-
# Make leaderboard

import utils.utils as utils

DATABASE_NAME = "original_game_schema"
DDL = """
CREATE TABLE Leaderboard (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    date DATE,
    time_sec INT
);
"""

with utils.get_connection() as conn:
    with conn.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE {DATABASE_NAME};")
        
with utils.get_connection(database=DATABASE_NAME) as conn:
    with conn.cursor() as cursor:
        cursor.execute(DDL)
        
