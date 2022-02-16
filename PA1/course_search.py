"""
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
"""
import schedule
import sys
from flask import Flask, render_template, request

TOP_LEVEL_MENU = '''
quit (q),; 
reset (r),;
term (t),(filte`r by term);
course (c),(filter by coursenum e.g. COSI 103a);
instructor (i),(filter by instructor);
subject (s),(filter by subject e.g. COSI or LALS);
title (ti),(filter by phrase in title);
description (d),(filter by phrase in description);
timeofday (td),(filter by day and time e.g. meets at 11 on Wed);
'''


def topmenu(command: str, filter: str, schedule: schedule.Schedule) -> str:
    terms = {c['term'] for c in schedule.courses}
    subjects = {c['subject'] for c in schedule.courses}
    titles = {c['name'] for c in schedule.courses}
    ##ADD MORE HERE
    times = [c['times'] for c in schedule.courses] ##filter out duplicates and empties


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
        msg = (TOP_LEVEL_MENU).split(';')
        cmd_fltr_dict = {}
        for command_index_pair in enumerate(msg):
            cmd_fltr_dict[command_index_pair[0]] = command_index_pair[1].split(',')
        return render_template('help.html', commands = cmd_fltr_dict)
    elif command in ['r', 'reset']:
        schedule.load_courses()
        schedule = schedule.enrolled(range(5, 1000))
        return render_template('home.html', target=[])
    elif command in ['t', 'term']:
        if filter!='':
            schedule = schedule.term(filter).sort('term')
            filtered_terms = render_list()
            if len(filtered_terms) == 0:
                res = ['{} is not a supported filter :('.format(filter)]
            else:
                res = ['There are {} {} courses \n\n'.format(len(schedule.courses), filtered_terms[0][0]), 'Here are the first 10:', filtered_terms]
            return render_template('results.html', target = res)  
        else:
            return render_template('results.html', target = ['Please choose from the following list and re-enter it above with the (term or t) command(s):', terms])
    elif command in ['s', 'subject']:
        if filter!='':
            schedule = schedule.subject(filter).sort('subject')
            filtered_subs = render_list()
            if len(filtered_subs) == 0:
                res = ['{} is not a supported filter :('.format(filter)]
            else:
                res = ['There are {} {} courses \n\n'.format(len(schedule.courses), filtered_subs[0][0]), 'Here are the first 10:', filtered_subs]
            return render_template('results.html', target = res)  
        else:
            return render_template('results.html', target = ['Please choose from the following list and re-enter it above with the (subject or s) command:', subjects])
    elif command in ['ti', 'title']:
        if filter!='':
            schedule = schedule.title(titles).sort('title')
            filtered_titles = render_list()
            if len(filtered_titles)==0:
                res = ['{} is not a supported filter :('.format(filter)]
            else:
                res = ['There are {} {} course \n\n'.format(len(schedule.courses), filtered_titles[0][0]), 'Here are the first 10:', filtered_titles]
            return render_template('results.html', target = res)  
        else:
            return render_template('results.html', target = ['Please choose from the following list and re-enter it above with the (subject or s) command:', titles])
    elif command in ['td', 'timeofday']:
        if filter!='':
            ##here is where we need to reformat
            ##INTO A LIST OF A SINGLE DICTIONARY WITH FIELDS/KEYS: ('days', 'end', 'start')
            schedule = schedule.class_time(times).sort('title')
            filtered_times = render_list()
            if len(filtered_times)==0:
                res = ['{} is not a supported filster :('.format(filter)]
            else:
                res = ['There are {} {} course \n\n'.format(len(schedule.courses), filtered_times[0][0]), 'Here are the first 10:', filtered_times]
            return render_template('results.html', target = res)
        else:
            ##create a new list of concatenated versions of each item in the gloabal terms set via list comprehension to pass in to be displayed
            ##!!!ONCE ITS PASSED BACK USER WILL ENTER PRETTY VERSION
            ##so we need to handle that as well by creating a new dictionary item to search by 
            return render_template('results.html', target = ['Please choose from the following list and re-enter it above with the (subject or s) command:', times])
    

    else:
        return render_template('results.html', target = ['{} is not supported as a command :('.format(command)])


if __name__ == '__main__':
    topmenu()
