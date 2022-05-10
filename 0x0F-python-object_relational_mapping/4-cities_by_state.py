#!/usr/bin/python3
"""Get all states"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], port=3306, db=argv[3]
    )
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name\
            FROM cities INNER JOIN states ON cities.state_id=states.id\
                ORDER BY cities.state_id ASC"
    )

    for states in cur.fetchall():
        print(states)
    cur.close()
    db.close()
