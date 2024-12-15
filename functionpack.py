import sqlite3
import json

conn = sqlite3.connect("./test.db")
c = conn.cursor()

listOfTables = c.execute(
    """SELECT name FROM sqlite_master WHERE type='table'
  AND name='SCHOOL'; """
).fetchall()

if listOfTables == []:
    c.execute(
        """CREATE TABLE SCHOOL
       (ID INT PRIMARY KEY     NOT NULL,
       NAME            TEXT    NOT NULL,
       MARK            INT     NOT NULL,
       GENDER          TEXT    NOT NULL);"""
    )
    conn.commit()
else:
    pass


class changer:
    def __init__(self):
        super().__init__()

    def InsertNewKey(self, ID, name, mark, gender):
        try:
            conn = sqlite3.connect("./test.db")
            c = conn.cursor()
            sql = f"INSERT INTO SCHOOL (ID,NAME,MARK,GENDER) \
            VALUES ({ID}, '{name}', {mark},'{gender}' )"
            c.execute(sql)
            conn.commit()
            conn.close()
        except:
            raise

    def DeleteKey(self, ID):
        try:
            conn = sqlite3.connect("./test.db")
            c = conn.cursor()
            c.execute(
                f"DELETE from SCHOOL where ID='{ID}'",
            )
            conn.commit()
            conn.close()
        except:
            raise

    def CheckKey(self, ID):
        answer = []
        conn = sqlite3.connect("./test.db")
        c = conn.cursor()
        list = c.execute(
            f"SELECT NAME,MARK,GENDER FROM SCHOOL WHERE ID='{ID}' ",
        ).fetchall()
        for key in list:
            answer.append(key[0])
            answer.append(key[1])
            answer.append(key[2])
        return answer

    def UpdateKey(self, ID, Key, value):
        try:
            conn = sqlite3.connect("./test.db")
            c = conn.cursor()
            c.execute(
                f"UPDATE SCHOOL set {Key} = '{value}' where ID='{ID}' ",
            )
            conn.commit()
        except:
            raise

    def average(self):
        conn = sqlite3.connect("./test.db")
        c = conn.cursor()
        sumthem = 0
        i = 0
        cursor = c.execute("SELECT MARK from SCHOOL")
        for row in cursor:
            sumthem += row[0]
            i += 1
        sumthem /= i
        return sumthem

    def Excellence(self):
        conn = sqlite3.connect("./test.db")
        c = conn.cursor()
        excellen = c.execute("SELECT ID,NAME,MARK,GENDER FROM SCHOOL WHERE MARK>80")
        output = []
        for row in excellen:
            output.append([row[0], row[1]])
        return output


changer1 = changer()


class Delivery:
    def __init__(self):
        super().__init__()

    def listdisplay(self):
        listreturn = []
        conn = sqlite3.connect("./test.db")
        c = conn.cursor()
        listing = c.execute("SELECT ID,NAME,MARK,GENDER FROM SCHOOL")
        for listcontent in listing:
            listreturn.append(
                [listcontent[0], listcontent[1], listcontent[2], listcontent[3]]
            )
        conn.close()
        return listreturn

    # def listin(fileaddress="test.db"):
    def listin(self, fileaddress):
        if fileaddress:
            listreturn = []
            conn = sqlite3.connect(f"./{fileaddress}")
            c = conn.cursor()
            listing = c.execute("SELECT ID,NAME,MARK,GENDER FROM SCHOOL")
            for listcontent in listing:
                listreturn.append(
                    [listcontent[0], listcontent[1], listcontent[2], listcontent[3]]
                )
            conn.close()
            for listcontent in listreturn:
                changer1.InsertNewKey(
                    listcontent[0],
                    listcontent[1],
                    listcontent[2],
                    listcontent[3],
                )
            conn.close()
        else:
            raise


delivery = Delivery()


class Databackup:
    def __init__(self):
        pass

    def backup(self):
        conn = sqlite3.connect("./test.db")
        c = conn.cursor()
        output = c.execute("SELECT ID,NAME,MARK,GENDER FROM SCHOOL").fetchall()
        outputer = []
        for row in output:
            outputer.append([row[0], row[1], row[2], row[3]])
        with open("./output.json", mode="w", encoding="utf8") as f:
            for ID in outputer:
                json.dump(
                    {
                        "ID": ID[0],
                        "Name": ID[1],
                        "Mark": ID[2],
                        "Gender": ID[3],
                    },
                    f,
                )


databackup = Databackup()

conn.commit()
conn.close()
