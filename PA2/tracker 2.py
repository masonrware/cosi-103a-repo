#!usr/bin/python3

#tracker.py
#Version 1.5.0
#3-23-22

#Written By: Mason Ware


'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it
could be replaced with PostgreSQL or Pandas or straight python lists

'''
import sys
from transactions import Transaction
from category import Category

transactions = Transaction('tracker.db')
category = Category('tracker.db')

MENU = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
12. summarize transactions by description
'''

#given
def process_choice(choice, item_num):
    '''This is the top level function of the program, it works to
    process the given choice and call functions with an object of
    data representation.'''
    if choice=='0':                                                           #given
        # quit program
        pass
    elif choice=='1':                                                         #given
        # show all categories
        cats = category.select_all()
        print_categories(cats)
    elif choice=='2':                                                         #given
        # add a category
        cat_name = input("category name: ")
        cat_desc = input("category description: ")
        cat = {'name':cat_name, 'desc':cat_desc}
        category.add(cat)
    elif choice=='3':                                                         #given
        # modify a given category
        rowid = int(input("rowid: "))
        new_name = input("new category name: ")
        new_desc = input("new category description: ")
        cat = {'name':new_name, 'desc':new_desc}
        category.update(rowid,cat)
    elif choice=='4':                                                         #mason
        # show all transactions
        trans = transactions.select_all()
        print_transactions(trans)
    elif choice=='5':                                                         #mason
        # add a transaction
        trans_amount = float(input('transaction amount: '))
        trans_category = input('transaction category: ')
        trans_date = input('transaction date (MM-DD-YY): ')
        trans_desc = input('transaction description: ')
        item_num+=1
        new_trans = {'item': item_num,
                     'amount': trans_amount,
                     'category': trans_category,
                     'date': trans_date,
                     'desc': trans_desc
                     }
        transactions.add(new_trans)
    elif choice=='6':                                                         #name
        # delete a given transaction
        del_rowid = input('rowid > ')
        transactions.delete(del_rowid)
        print('Transaction deleted successfully!')
    elif choice=='7':                                                         #mason
        # summarize transactions by day
        input_date = input('Filter Date > ')
        trans = transactions.select_date(input_date)
        print_transactions(trans)
    elif choice=='8':                                                         #Kayla
        # summarize transactions by month
        input_month = input('Filter Month > ')
        trans = transactions.select_month(input_month)
        print_transactions(trans)
    elif choice=='9':                                                         #Kayla
        # summarize transactions by year
        input_year = input('Filter Year > ')
        trans = transactions.select_year(input_year)
        print_transactions(trans)
    elif choice=='10':                                                        #jason
        # summarize transactions by category
        input_category = input('Filter Category > ')
        trans = transactions.select_category(input_category)
        print_transactions(trans)
    elif choice=='11':                                                        #mason
        # print menu
        print(MENU)
    #Ben
    elif choice=='12':
        input_description=input("Filter Description > ")
        trans=transactions.select_description(input_description)
        print_transactions(trans)
    elif choice=='13':                                                        #kevin
        input_item=input("Filter Item > ")
        trans=transactions.select_item(input_item)
        print_transactions(trans)

    choice = input("> ")
    return (choice, item_num)

#given
def toplevel():
    ''' handle the user's choice
        read the command args and process them (psuedo)'''
    print(MENU)
    choice = input("> ")
    item_num = 0
    while choice != '0':
        # tuple of item_num and choice to keep track
        choice, item_num = process_choice(choice=choice, item_num=item_num)
    print('='*50 + '\nBye! :)\n\n')
    sys.exit(0)




##HELPER FUNCTIONS

#given
def print_transactions(items):
    ''' print the transactions '''
    if len(items)==0:
        print('no items to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-30s"%(
        'item','amount','category','date','description'))
    print('-'*40)
    for item in items:
        values = tuple(item.values())
        print("%-10s %-10d %-10s %-10s %-30s"%values[1:])

#given
def print_category(cat):
    '''prints a single category'''
    print("%-3d %-10s %-30s"%(cat['rowid'],cat['name'],cat['desc']))

#given
def print_categories(cats):
    '''prints all categories'''
    print("%-3s %-10s %-30s"%("id","name","description"))
    print('-'*45)
    for cat in cats:
        print_category(cat)




##DRIVER

if __name__ == '__main__':
    toplevel()
