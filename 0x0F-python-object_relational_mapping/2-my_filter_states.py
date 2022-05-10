#!/usr/bin/python3
"""Get all states"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], port=3306, db=argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (argv[4],))

    for states in cur.fetchall():
        if states[1] == argv[4]:
            print(states)
    cur.close()
    db.close()
