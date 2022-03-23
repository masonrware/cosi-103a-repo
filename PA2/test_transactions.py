#! usr/bin/python3

#test_transactions.py
#Version 1.0.0
#3-23-22

#Written By: Mason Ware

import pytest
from transactions import Transaction, to_trans_dict

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an category database '''
    db = Transaction(dbfile)
    yield db
    
@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    cat1 = {'item':'1','amount':100,'category':'auto','date':'03-22-22','desc':'car'}
    cat2 = {'item':'2','amount':200,'category':'flight','date':'03-23-22','desc':'plane'}
    cat3 = {'item':'3','amount':300,'category':'boat','date':'03-24-22','desc':'boat'}
    id1=empty_db.add(cat1)
    id2=empty_db.add(cat2)
    id3=empty_db.add(cat3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.fixture
def med_db(small_db):
    ''' create a database with 10 more elements than small_db'''
    rowids=[]
    # add 10 categories
    for i in range(10):
        s = str(i)
        cat ={'item':'item '+s,
               'amount': i,
               'category': 'category '+s,
               'date':'date '+s,
               'desc':'description '+s
                }
        rowid = small_db.add(cat)
        rowids.append(rowid)

    yield small_db

    # remove those 10 categories
    for j in range(10):
        small_db.delete(rowids[j])



@pytest.mark.simple
def test_to_trans_dict():
    ''' teting the to_cat_dict function '''
    a = to_trans_dict((7, 'alpha', 2, 'alpha', 'alpha', 'alpha'))
    assert a['rowid']==7
    assert a['item']=='alpha'
    assert a['desc']=='alpha'
    assert len(a.keys())==6


@pytest.mark.add
def test_add(med_db):
    ''' add a category to db, the select it, then delete it'''

    cat0 = {'item':'testing_item',
            'amount':6666.666,
            'category':'testing_cat',
            'date':'testing_date',
            'desc':'testing_description'
            }
    cats0 = med_db.select_all()
    rowid = med_db.add(cat0)
    cats1 = med_db.select_all()
    assert len(cats1) == len(cats0) + 1
    cat1 = med_db.select_one(rowid)
    assert cat1['item']==cat0['item']


@pytest.mark.delete
def test_delete(med_db):
    ''' add a category to db, delete it, and see that the size changes'''
    # first we get the initial table
    cats0 = med_db.select_all()

    # then we add this category to the table and get the new list of rows
    cat0 = {'item':'testing_item',
            'amount':6666.666,
            'category':'testing_cat',
            'date':'testing_date',
            'desc':'testing_description'
            }
    rowid = med_db.add(cat0)
    cats1 = med_db.select_all()

    # now we delete the category and again get the new list of rows
    med_db.delete(rowid)
    cats2 = med_db.select_all()

    assert len(cats0)==len(cats2)
    assert len(cats2) == len(cats1)-1

@pytest.mark.update
def test_update(med_db):
    ''' add a category to db, updates it, and see that it changes'''

    # then we add this category to the table and get the new list of rows
    cat0 = {'item':'testing_item',
            'amount':6666.666,
            'category':'testing_cat',
            'date':'testing_date',
            'desc':'testing_description'
            }
    rowid = med_db.add(cat0)

    # now we upate the category
    cat1 = {'item':'new_item',
            'amount':3333.33,
            'category':'new_cat',
            'date':'new_date',
            'desc':'new_description'
            }
    med_db.update(rowid,cat1)

    # now we retrieve the category and check that it has changed
    cat2 = med_db.select_one(rowid)
    assert cat2['item']==cat1['item']

#mason
@pytest.mark.select_date
def test_select_date(med_db):
    result_list = med_db.select_date('22')
    assert result_list == [{'rowid': 1, 
                            'item': 1, 
                            'amount': 100, 
                            'transaction': 'auto', 
                            'date': '03-22-22', 
                            'desc': 'car'}]

