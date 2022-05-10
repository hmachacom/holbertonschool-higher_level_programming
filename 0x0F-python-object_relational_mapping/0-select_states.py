#!/usr/bin/python3
"""Get all states"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for states in cur.fetchall():
        print(states)
    cur.close()
    db.close()
