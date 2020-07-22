import unittest
import sqlite3
import shutil
import random
connection_bd = sqlite3.connect('warships.db')
connection_bd_backup = sqlite3.connect(r'C:\backUp\warships.db')
cursor_bd = connection_bd.cursor()
cursor_bd_backup = connection_bd_backup.cursor()


def shuffle_ships(i):
    while i > 0:
        cursor_bd.execute("""SELECT weapon FROM weapons""")
        weapons = cursor_bd.fetchall()
        cursor_bd.execute("""SELECT hull FROM hulls""")
        hulls = cursor_bd.fetchall()
        cursor_bd.execute("""SELECT engine FROM engines""")
        engines = cursor_bd.fetchall()
        cursor_bd.execute("""SELECT ship FROM ships""")
        ships = cursor_bd.fetchall()
        # Возможно здесь будет ошибка с получением длины, ошибка вне диапазона
        ship_random = str(ships[random.randrange(0, len(ships), 1)])[2:-3]
        cursor_bd.execute("DELETE FROM ships WHERE ship=?", (ship_random,))
        print(ship_random)
        cursor_bd.execute("""INSERT INTO ships (ship, weapon, hull, engine)
                                VALUES (?, ?, ?, ?)""", (ship_random,
                                                         str(weapons[random.randrange(0, len(weapons), 1)])[2:-3],
                                                         str(hulls[random.randrange(0, len(hulls), 1)])[2:-3],
                                                         str(engines[random.randrange(0, len(engines), 1)])[2:-3]))
        connection_bd.commit()
        i = i - 1


def ship_weapon(ship):
    result = cursor_bd.execute("SELECT weapon FROM ships WHERE ship=?", (ship,))
    for var in result:
        weapon_bd = var[0]
    result = cursor_bd.execute("SELECT * FROM weapons WHERE weapon=?", (weapon_bd,))
    for var in result:
        reload_speed_bd = var[1]
    return reload_speed_bd


def ship_hull_type(ship):
    result = cursor_bd.execute("SELECT hull FROM ships WHERE ship=?", (ship,))
    for var in result:
        hull_bd = var[0]
    result = cursor_bd.execute("SELECT type FROM hulls WHERE hull=?", (hull_bd,))
    for var in result:
        type_bd = var[0]
    return type_bd


def ship_engine_power(ship):
    result = cursor_bd.execute("SELECT engine FROM ships WHERE ship=?", (ship,))
    for var in result:
        engine_bd = var[0]
    result = cursor_bd.execute("SELECT power FROM engines WHERE engine=?", (engine_bd,))
    for var in result:
        power_bd = var[0]
    return power_bd


def ship_engine(ship):
    result = cursor_bd.execute("SELECT engine FROM ships WHERE ship=?", (ship,))
    for var in result:
        engine_bd = var[0]
    return engine_bd


def make_copy_bd():
    shutil.copy(r'warships.db', r'C:\backUp')
    print('BackUp')


def exist_diameter(arg):
    exist = False
    result = cursor_bd.execute("""SELECT diameter FROM weapons""")
    for var in result:
        if var[0] == arg:
            exist = True
    return exist


def exist_ship_bd(ship):
    result = cursor_bd.execute("""SELECT ship FROM ships""")
    exist = False
    for var in result:
        if var[0] == ship:
            exist = True
    return exist


def exist_ship_backup(ship):
    result_backup = cursor_bd_backup.execute("""SELECT ship FROM ships""")
    exist = False
    for var in result_backup:
        if var[0] == ship:
            exist = True
    return exist


def hull_capacity_for_generators():
    result = cursor_bd.execute("SELECT capacity FROM hulls")
    for var in result:
        print(var[0])


class TestShips(unittest.TestCase):
    # make_copy_bd()
    # shuffle_ships(5)
    # ship_weapon('ship-22')
    # hull_capacity_for_generators()

    def test_exist_ship_bd(self):
        self.assertTrue(exist_ship_bd('ship-22'), True)

    def test_exist_backup(self):
        self.assertTrue(exist_ship_backup('ship-22'), True)

    def test_wrong_reload_speed(self):
        self.assertEqual(ship_weapon('ship-22'), 300)

    def test_reload_speed(self):
        self.assertEqual(ship_weapon('ship-22'), 298)

    def test_ship_hull_type(self):
        self.assertEqual(ship_hull_type('ship-22'), 619)

    def test_ship_engine_power(self):
        self.assertEqual(ship_engine_power('ship-124'), 526)

    def test_ship_engine(self):
        self.assertEqual(ship_engine('ship-124'), 'engine-736')


if __name__ == '__main__':
    unittest.main()
    cursor_bd.close()
    cursor_bd_backup.close()
