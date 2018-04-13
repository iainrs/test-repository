# create db object
import sqlite3

class Db():
    def __init__(self,dbname='data.db'):
        import os.path

        self.dbn=dbname
        full=os.path.abspath(self.dbn)
        self.exists = False
        if not os.path.isfile(self.dbn):
            print('Error < ',full,' > does not exist')
            return None
        print(full,' exists')
        self.exists=True
        self.opstat=False
        self.conn=None
        self.cur=None


    def open(self):
        if not self.opstat:
            self.conn = sqlite3.connect(self.dbn)
            self.cur=self.conn.cursor()
            self.opstat=True
        return self.cur

    def close(self):
        if self.opstat:
            self.commit()
            self.conn.close()
            self.opstat=False
        return

    def commit(self):
        if not self.opstat:
            return False
        else:
            self.conn.commit()
            return True




            #connection = sqlite3.connect('data.db')
            #cursor=connection.cursor()

            #query = "DELETE FROM items where name = ? "
            ##print(query)

            #cursor.execute(query, (name,) )
            #connection.commit()
            #connection.close
if __name__ == '__main__':
    db=Db()
    # db.exists property of class
    if db.exists :

        curs=db.open()

        qu='SELECT * from items'
        rows=curs.execute(qu)
        for row in rows:
            print(row)
        curs=db.open()

        db.close()
        db.close()

        curs=db.open()

        qu='SELECT * from users'
        rows=curs.execute(qu)
        for row in rows:
            print(row)
        db.close()



