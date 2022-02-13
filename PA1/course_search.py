"""
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
"""
import schedule
import sys
from flask import Flask, render_template, request

schedule = schedule.Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5, 1000))  # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
'''

terms = {c['term'] for c in schedule.courses}


def topmenu(command: str) -> dict:
    """
    topmenu is the top level loop of the course search app
    """
    global schedule
    while True:
        if command == 'quit':
            ## return a render of home then,
            return
        elif command in ['h', 'help']:
            ## change this to NOT return a render template
            return '{}\n' + '-' * 40 + '\n\n'
        elif command in ['r', 'reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5, 1000))
        elif command in ['t', 'term']:
            ##need to be able to get a term
            ##maybe render a replaced!! input in html in the template/rerender the template
            ##with render_template()

            # query_text = request.form["query"]
            term = input("enter a term:" + str(terms) + ":")

            schedule = schedule.term([term]).sort('subject')
        elif command in ['s', 'subject']:
            ##do the same thing as 46

            # query_text = request.form["query"]
            subject = input("enter a subject:")

            schedule = schedule.subject([subject])
        else:
            ##different render 

            print('command', command, 'is not supported')


def print_course(course):
    """
    print_course prints a brief description of the course
    """
    ##this method will probably get deleted and migrated up
    print(course['subject'], course['coursenum'], course['section'],
          course['name'], course['term'], course['instructor'])


if __name__ == '__main__':
    topmenu()
