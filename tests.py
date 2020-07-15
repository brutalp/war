from db import *


class Ships:
    pass


def check_ships():
    pass


def main():
    write_weapons()
    write_hulls()
    write_ships()
    write_engines()
    cursor.close()
    print(ENGINES)
    print(WEAPONS)
    print(HULLS)
    print(SHIPS)


if __name__ == '__main__':
    main()
