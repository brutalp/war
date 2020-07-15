import sqlite3
import random
conn = sqlite3.connect('warships.db')
cursor = conn.cursor()
WEAPONS = {}
HULLS = {}
SHIPS = {}
ENGINES = {}


def make_random_text(text):
    return text + '-' + str(random.randrange(0, 999, 1))


def make_something(some):
    try:
        if some == 'ship':
            cursor.execute("""SELECT weapon FROM weapons""")
            weapons = cursor.fetchall()
            cursor.execute("""SELECT hull FROM hulls""")
            hulls = cursor.fetchall()
            cursor.execute("""SELECT engine FROM engines""")
            engines = cursor.fetchall()
            # Возможно здесь будет ошибка с получением длины, ошибка вне диапазона
            cursor.execute("""INSERT INTO ships (ship, weapon, hull, engine)
                        VALUES (?, ?, ?, ?)""", (make_random_text(some),
                                                 str(weapons[random.randrange(0, len(weapons), 1)])[2:-3],
                                                 str(hulls[random.randrange(0, len(hulls), 1)])[2:-3],
                                                 str(engines[random.randrange(0, len(engines), 1)])[2:-3]))
            conn.commit()
        elif some == 'weapon':
            cursor.execute("""INSERT INTO weapons (weapon, reload_speed, rotation_speed, diameter, power_volley, count)
                        VALUES (?, ?, ?, ?, ?, ?)""", (make_random_text(some),
                                                       random.randrange(0, 999, 1),
                                                       random.randrange(0, 999, 1),
                                                       random.randrange(0, 999, 1),
                                                       random.randrange(0, 999, 1), random.randrange(0, 999, 1)))
            conn.commit()
            print(some)
        elif some == 'hull':
            cursor.execute("""INSERT INTO hulls (hull, armor, type, capacity)
                        VALUES (?, ?, ?, ?)""", (make_random_text(some),
                                                 random.randrange(0, 999, 1),
                                                 random.randrange(0, 999, 1),
                                                 random.randrange(0, 999, 1)))
            conn.commit()
            print(some)
        elif some == 'engine':
            cursor.execute("""INSERT INTO engines (engine, power, type)
                        VALUES (?, ?, ?)""", (make_random_text(some),
                                              random.randrange(0, 999, 1),
                                              random.randrange(0, 999, 1)))
            conn.commit()
            print(some)
        else:
            print('error')
        cursor.close()
    except:
        print()


def write_weapons():
    result = cursor.execute("""SELECT * FROM weapons""")
    for var in result:
        WEAPONS.setdefault('weapon', []).append(var[0])
        WEAPONS.setdefault('reload_speed', []).append(var[1])
        WEAPONS.setdefault('rotation_speed', []).append(var[2])
        WEAPONS.setdefault('diameter', []).append(var[3])
        WEAPONS.setdefault('power_volley', []).append(var[4])
        WEAPONS.setdefault('count', []).append(var[5])


def write_hulls():
    result = cursor.execute("""SELECT * FROM hulls""")
    for var in result:
        HULLS.setdefault('hull', []).append(var[0])
        HULLS.setdefault('armor', []).append(var[1])
        HULLS.setdefault('type', []).append(var[2])
        HULLS.setdefault('capacity', []).append(var[3])


def write_ships():
    result = cursor.execute("""SELECT * FROM ships""")
    for var in result:
        SHIPS.setdefault('ship', []).append(var[0])
        SHIPS.setdefault('weapon', []).append(var[1])
        SHIPS.setdefault('hull', []).append(var[2])
        SHIPS.setdefault('engine', []).append(var[3])


def write_engines():
    result = cursor.execute("""SELECT * FROM engines""")
    for var in result:
        ENGINES.setdefault('engine', []).append(var[0])
        ENGINES.setdefault('power', []).append(var[1])
        ENGINES.setdefault('type', []).append(var[2])


def main():
    # make random
    # make_something('engine')
    # make_something('weapon')
    # make_something('hull')
    # make_something('engine')
    # make_something('ship')

    # write in var
    write_weapons()
    write_hulls()
    write_ships()
    write_engines()
    print(SHIPS)
    cursor.close()


if __name__ == '__main__':
    main()
