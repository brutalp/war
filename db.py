import sqlite3
import random
conn = sqlite3.connect('warships.db')
cursor = conn.cursor()


def make_random_text(text):
    return text + '-' + str(random.randrange(0, 999, 1))


def make_something(some, i):
    while i > 0:
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
                                                       random.randrange(0, 999, 10),
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
        i = i - 1


def main():
    # make random
    # make_something('engine', 5)
    # make_something('weapon', 5)
    # make_something('hull', 5)
    # make_something('engine', 5)
    # make_something('ship', 5)
    cursor.close()


if __name__ == '__main__':
    main()
