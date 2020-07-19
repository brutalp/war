import unittest
import sqlite3
import shutil
import random
connection_bd = sqlite3.connect('warships.db')
connection_bd_backup = sqlite3.connect(r'C:\backUp\warships.db')
cursor_bd = connection_bd.cursor()
cursor_bd_backup = connection_bd_backup.cursor()


def shuffle():
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


def make_copy_bd():
    shutil.copy(r'warships.db', r'C:\backUp')
    print('BackUp')


def exist_ship(ship):
    result = cursor_bd.execute("""SELECT ship FROM ships""")
    result_backup = cursor_bd_backup.execute("""SELECT ship FROM ships""")
    exist = False
    for var in result:
        if var[0] == ship:
            exist = True
    # for var in result_backup:
    #     print(var[0])
    return exist


class TestShips(unittest.TestCase):
    shuffle()
    def test_exist_ship(self):
        self.assertTrue(exist_ship('ship-22'), True)


if __name__ == '__main__':
    # make_copy_bd()
    # unittest.main()
    cursor_bd.close()
    cursor_bd_backup.close()
