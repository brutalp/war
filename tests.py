import unittest
import sqlite3
import shutil
import random
conn = sqlite3.connect('warships.db')
cursor = conn.cursor()
WEAPONS = {}
HULLS = {}
SHIPS = {}
ENGINES = {}
WEAPONS_RANDOM = {}
HULLS_RANDOM = {}
SHIPS_RANDOM = {}
ENGINES_RANDOM = {}


def make_copy_bd():
    shutil.copy(r'warships.db', r'C:\backUp')
    print('BackUp')


def exist_ship(ship):
    result = cursor.execute("""SELECT * FROM ships""")
    for var in result:
        SHIPS.setdefault('ship', []).append(var[0])
        SHIPS.setdefault('weapon', []).append(var[1])
        SHIPS.setdefault('hull', []).append(var[2])
        SHIPS.setdefault('engine', []).append(var[3])
    SHIPS_RANDOM.setdefault('ship', []).append(sorted(SHIPS['ship'], key=lambda e: random.random()))
    SHIPS_RANDOM.setdefault('weapon', []).append(sorted(SHIPS['weapon'], key=lambda e: random.random()))
    SHIPS_RANDOM.setdefault('hull', []).append(sorted(SHIPS['hull'], key=lambda e: random.random()))
    SHIPS_RANDOM.setdefault('engine', []).append(sorted(SHIPS['engine'], key=lambda e: random.random()))
    print(SHIPS)
    print(SHIPS_RANDOM)
    return ship in SHIPS['ship']


def exist_weapon(weapon):
    result = cursor.execute("""SELECT * FROM weapons""")
    for var in result:
        WEAPONS.setdefault('weapon', []).append(var[0])
        WEAPONS.setdefault('reload_speed', []).append(var[1])
        WEAPONS.setdefault('rotation_speed', []).append(var[2])
        WEAPONS.setdefault('diameter', []).append(var[3])
        WEAPONS.setdefault('power_volley', []).append(var[4])
        WEAPONS.setdefault('count', []).append(var[5])
    WEAPONS_RANDOM.setdefault('weapon', []).append(sorted(WEAPONS['weapon'], key=lambda e: random.random()))
    WEAPONS_RANDOM.setdefault('reload_speed', []).append(sorted(WEAPONS['reload_speed'], key=lambda e: random.random()))
    WEAPONS_RANDOM.setdefault('rotation_speed', []).append(sorted(WEAPONS['rotation_speed'], key=lambda e: random.random()))
    WEAPONS_RANDOM.setdefault('diameter', []).append(sorted(WEAPONS['diameter'], key=lambda e: random.random()))
    WEAPONS_RANDOM.setdefault('power_volley', []).append(sorted(WEAPONS['power_volley'], key=lambda e: random.random()))
    WEAPONS_RANDOM.setdefault('count', []).append(sorted(WEAPONS['count'], key=lambda e: random.random()))
    return weapon in WEAPONS['weapon']


def exist_hulls(hull):
    result = cursor.execute("""SELECT * FROM hulls""")
    for var in result:
        HULLS.setdefault('hull', []).append(var[0])
        HULLS.setdefault('armor', []).append(var[1])
        HULLS.setdefault('type', []).append(var[2])
        HULLS.setdefault('capacity', []).append(var[3])
    HULLS_RANDOM.setdefault('hull', []).append(sorted(HULLS['hull'], key=lambda e: random.random()))
    HULLS_RANDOM.setdefault('armor', []).append(sorted(HULLS['armor'], key=lambda e: random.random()))
    HULLS_RANDOM.setdefault('type', []).append(sorted(HULLS['type'], key=lambda e: random.random()))
    HULLS_RANDOM.setdefault('capacity', []).append(sorted(HULLS['capacity'], key=lambda e: random.random()))
    return hull in HULLS['hull']


def exist_engine(engine):
    result = cursor.execute("""SELECT * FROM engines""")
    for var in result:
        ENGINES.setdefault('engine', []).append(var[0])
        ENGINES.setdefault('power', []).append(var[1])
        ENGINES.setdefault('type', []).append(var[2])
    ENGINES_RANDOM.setdefault('engine', []).append(sorted(ENGINES['engine'], key=lambda e: random.random()))
    ENGINES_RANDOM.setdefault('power', []).append(sorted(ENGINES['power'], key=lambda e: random.random()))
    ENGINES_RANDOM.setdefault('type', []).append(sorted(ENGINES['type'], key=lambda e: random.random()))
    return engine in ENGINES['engine']


def randomize():
    print(WEAPONS)


class TestShips(unittest.TestCase):
    # def setUp(self):
    #     self.name = 'ship-22'

    def test_exist_ship(self):
        self.assertTrue(exist_ship('ship-22'), True)

    def test_exist_weapon(self):
        self.assertTrue(exist_weapon('weapon-559'), True)

    def test_exist_hull(self):
        self.assertTrue(exist_hulls('hull-377'), True)

    def test_exist_engine(self):
        self.assertTrue(exist_engine('engine-413'), True)


if __name__ == '__main__':
    # make_copy_bd()
    unittest.main()
    # randomize()
    cursor.close()
