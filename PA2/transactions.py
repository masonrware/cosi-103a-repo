#! usr/bin/python3

#transactions.py
#Version 1.0.0
#3-22-22

import sqlite3

def to_trans_dict(cat_tuple):
    ''' cat is a transaction tuple (rowid, name, desc)'''
    cat = {'rowid':cat_tuple[0], 'item':cat_tuple[1],'amount':cat_tuple[2],
    'transaction':cat_tuple[3], 'date':cat_tuple[4], 'desc':cat_tuple[5]}
    return cat

def to_trans_dict_list(cat_tuples):
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [to_trans_dict(cat) for cat in cat_tuples]

class Transaction:
    def __init__(self, dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item INT, amount INT, category text, date text, desc text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    def select_one(self,rowid):
        ''' return a transaction with a specified rowid '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where rowid=(?)",(rowid,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict(tuples[0])

    def add(self,item):
        ''' add a transaction to the transactions table.
            this returns the rowid of the inserted element '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        ##below needs changing of the fields
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",
        (item['item'], item['amount'], item['category'], item['date'], item['desc']))

        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def update(self,rowid,item):
        ''' update a transaction in the transactions table.  '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''UPDATE transactions
                        SET item=(?), amount=(?),category=(?),date=(?),desc=(?)
                        WHERE rowid=(?);
        ''',(item['item'],item['amount'],item['category'],item['date'], item['desc'], rowid))

        con.commit()
        con.close()

    def delete(self,rowid):
        ''' delete a transaction from the transactions table. '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()

        cur.execute('''DELETE FROM transactions
                       WHERE rowid=(?);
        ''',(rowid,))

        con.commit()
        con.close()

    #mason
    def select_date(self,date):
        '''select a transaction by date'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,* from transactions
                    where SUBSTR(date, 4, 2)=(?)''',(date,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    #Kayla
    def select_month(self, month):
        '''select a transaction by month'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,* from transactions
                    where SUBSTR(date, 1, 2)=(?)''',(month,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    #Kayla
    def select_year(self, year):
        '''select a transaction by year'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,* from transactions
                    where SUBSTR(date, 7, 2)=(?)''',(year,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)
    
    #jason
    def select_category(self,category):
        '''select a transaction by category'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,* from transactions
                    where category=(?)''',(category,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    #Ben
    def select_description(self, descrption):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,* from transactions
                    where desc LIKE (?)''',(descrption,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)
    
    #kevin
    def select_item(self, item):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,* from transactions
                    where item=(?)''',(item,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)
