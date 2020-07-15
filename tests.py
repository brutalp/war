import unittest
# from db import SHIPS, WEAPONS, HULLS, ENGINES
import db


def exist_ship(ship):
    print(db.SHIPS)
    return ship in db.SHIPS.values()


class TestShips(unittest.TestCase):
    # def setUp(self):
    #     self.name = 'ship-22'

    def test_exist_ship(self):
        self.assertTrue(exist_ship('ship-22'), True)
        # assert s.exist_ship(self.name) == True


def check_ships():
    pass


# def main():
#     print(ENGINES)
#     print(WEAPONS)
#     print(HULLS)
#     print(SHIPS)


if __name__ == '__main__':
    unittest.main()
