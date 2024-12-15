import sqlite3

conn = sqlite3.connect("./user.db")
c = conn.cursor()

listOfTables = c.execute(
    """SELECT name FROM sqlite_master WHERE type='table'
  AND name='USER'; """
).fetchall()

if listOfTables == []:
    c.execute(
        """CREATE TABLE USER
       (ID     TEXT    NOT NULL,
       KEY     TEXT    NOT NULL);"""
    )
    conn.commit()
    try:
        c.execute(
            "INSERT INTO USER (ID,KEY) \
        VALUES ('admin', 'admin' )",
        )
        conn.commit()
    except:
        raise
else:
    pass


class checkUserKey:
    def __init__(self):
        super().__init__()

    def checking(ID, Key):
        conn = sqlite3.connect("./user.db")
        c = conn.cursor()
        c.execute(
            f"SELECT KEY FROM USER WHERE ID = '{ID}'",
        )
        answer = str(c.fetchone())[2:-3]
        if Key == answer:
            return True
        else:
            return False
