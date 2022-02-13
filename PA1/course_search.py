"""
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
"""
import schedule
import sys
from flask import Flask, render_template, request

TOP_LEVEL_MENU = '''
quit; 
reset;
term  (filter by term);
course (filter by coursenum, e.g. COSI 103a);
instructor (filter by instructor);
subject (filter by subject, e.g. COSI, or LALS);
title  (filter by phrase in title);
description (filter by phrase in description);
timeofday (filter by day and time, e.g. meets at 11 on Wed);
'''


def topmenu(command: str, filter: str, schedule: schedule.Schedule) -> str:
    terms = {c['term'] for c in schedule.courses}
    subjects = {c['subject'] for c in schedule.courses}
    ##ADD MORE HERE

    def render_list() -> list:
        """
        returns a list of classes with specified fields: (subject, coursenum, section, name, term, instructor)
        """
        res = []
        for c in schedule.courses[:10]:
            res.append((c['subject'], c['coursenum'], c['section'], c['name'], c['term'], c['instructor']))
        return res

    if command in ['q', 'quit']:
        return render_template('home.html', target=[])


    elif command in ['h', 'help']:
        return render_template('results.html', target = (TOP_LEVEL_MENU).split(';'))


    elif command in ['r', 'reset']:
        schedule.load_courses()
        schedule = schedule.enrolled(range(5, 1000))
        return render_template('home.html', target=[])


    elif command in ['t', 'term']:
        if filter!='':
            schedule = schedule.subject(filter).sort('subject') ##filter by TERMS
            filtered_terms = render_list()
            res = ['courses has {} elements \n\n'.format(len(schedule.courses)), 'here are the first ten:', filtered_terms]
            return render_template('results.html', target = res)  
        else:
            return render_template('results.html', target = ['please choose from the following list and re-enter it above with the t command:', terms])


    elif command in ['s', 'subject']:
        if filter!='':
            schedule = schedule.subject(filter).sort('subject')
            filtered_subs = render_list()
            res = ['courses has {} elements \n\n'.format(len(schedule.courses)), 'here are the first ten:', filtered_subs]
            return render_template('results.html', target = res)  
        else:
            return render_template('results.html', target = ['please choose from the following list and re-enter it above with the s command:', subjects])

    ##ADD IF STATMENTS TO HANDLE DIFFERENT COMMANDS HERE

    else:
        return render_template('results.html', target = ['{} is not supported as a command :('.format(command)])

if __name__ == '__main__':
    topmenu()
