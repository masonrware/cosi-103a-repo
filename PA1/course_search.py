"""
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
"""
from flask import render_template
import schedule

TOP_LEVEL_MENU = '''
quit (q),; 
reset (r),;
term (t),(filter by term);
course (c),(filter by coursenum e.g. COSI 103a);
instructor (i),(filter by instructor);
subject (s),(filter by subject e.g. COSI or LALS);
title (ti),(filter by phrase in title);
description (d),(filter by phrase in description);
timeofday (td),(filter by day and time e.g. meets at 11 on Wed);
help (h),(displays this page);
'''

def topmenu(command: str, filter, schedule: schedule.Schedule) -> str:
    terms = {item['term'] for item in schedule.courses}
    subjects = {item['subject'] for item in schedule.courses}
    titles = {item['name'] for item in schedule.courses}
    instructor = {item['instructor'] for item in schedule.courses}
    description = {item['description'] for item in schedule.courses}

    starttimes = set(schedule.get_all_start_times())
    endtimes = set(schedule.get_all_end_times())
    courses = set(item['coursenum'] for item in schedule.courses)

    def render_list() -> list:
        """
        returns a list of classes with specified fields:
        (subject, coursenum, section, name, term, instructor)
        """
        res = []
        for item in schedule.courses[:10]:
            res.append((item['subject'], item['coursenum'], item['section'],
            item['name'], item['term'], item['instructor']))
        return res

    #QUIT
    if command in ['q', 'quit']:
        return render_template('home.html', target=[])
    #HELP
    elif command in ['h', 'help']:
        msg = (TOP_LEVEL_MENU).split(';')
        cmd_fltr_dict = {}
        for command_index_pair in enumerate(msg):
            cmd_fltr_dict[command_index_pair[0]] = command_index_pair[1].split(',')
        return render_template('help.html', commands = cmd_fltr_dict)
    #RESET
    elif command in ['r', 'reset']:
        schedule.load_courses()
        schedule = schedule.enrolled(range(5, 1000))
        return render_template('home.html', target=[])
    #TERM
    elif command in ['t', 'term']:
        if filter!='':
            schedule = schedule.term(filter).sort('term')
            filtered_terms = render_list()
            if len(filtered_terms) == 0:
                res = ['{} is not a supported filter :('.format(filter)]
            else:
                res = ['There are {} courses in the term {} \n\n'.format(len(schedule.courses),
                 filter), 'Here are the first 10:', filtered_terms]
            return render_template('results.html', target = res)
        else:
            return render_template('results.html', target =
            ['Please choose from the following list and re-enter it above with the (term or t) command(s):', terms])
    #SUBJECT
    elif command in ['s', 'subject']:
        if filter!='':
            schedule = schedule.subject(filter).sort('subject')
            filtered_subs = render_list()
            if len(filtered_subs) == 0:
                res = ['{} is not a supported filter :('.format(filter)]
            else:
                res = ['There are {} {} courses \n\n'.format(len(schedule.courses),
                filtered_subs[0][0]), 'Here are the first 10:', filtered_subs]
            return render_template('results.html', target = res)
        else:
            return render_template('results.html', target =
            ['Please choose from the following list and re-enter it above with the (subject or s) command:', subjects])
    #TITLE
    elif command in ['ti', 'title']:
        if filter!='':
            schedule = schedule.title(filter).sort('title')
            filtered_titles = render_list()
            if len(filtered_titles)==0:
                res = ['{} is not a supported filter :('.format(filter)]
            else:
                res = ['There are {} {} courses \n\n'.format(len(schedule.courses), filter),
                'Here are the first 10:', filtered_titles]
            return render_template('results.html', target = res)
        else:
            return render_template('results.html', target =
            ['Please choose from the following list and re-enter it above with the (title or ti) command:',
            titles])
    #DATETIME
    elif command in ['td', 'timeofday']:
        if filter!='':
            if(len(filter[0])!=0 or filter[1]!='' or filter[2]!=''):
                if len(filter[0]) > 0:
                    split_up_days = filter[0].split(',')
                    split_up_days = [item.lower().strip() for item in split_up_days]
                    schedule = schedule.class_days(split_up_days)
                if filter[1] != '':
                    schedule = schedule.class_start_time(filter[1])
                if filter[2] != '':
                    schedule = schedule.class_end_time(filter[2])
                filtered_times = render_list()
                if len(filtered_times)==0:
                    res = ['No classes found for that combination :(']
                else:
                    if len(filter[0])>0:
                        if filter[1]!='' and filter[2]!='':
                            res = ['There are {} courses on {} that start at {} and end at {} \n\n'.format(len(schedule.courses),
                            filter[0], filter[1], filter[2]), 'Here are the first 10:', filtered_times]
                        elif filter[1]!='' and filter[2]=='':
                            res = ['There are {} courses on {} that start at {} \n\n'.format(len(schedule.courses),
                            filter[0], filter[1]),'Here are the first 10:', filtered_times]
                        elif filter[1]=='' and filter[2]!='':
                            res = ['There are {} courses on {} that end at {} \n\n'.format(len(schedule.courses),
                            filter[0], filter[2]), 'Here are the first 10:', filtered_times]
                        else:
                            res = ['There are {} courses on {}\n\n'.format(len(schedule.courses),
                            filter[0]), 'Here are the first 10:', filtered_times]
                    else:
                        if filter[1]!='' and filter[2]!='':
                            res = ['There are {} courses that start at {} and end at {} \n\n'.format
                            (len(schedule.courses), filter[1], filter[2]), 'Here are the first 10:', filtered_times]
                        elif filter[1]!='' and filter[2]=='':
                            res = ['There are {} courses that start at {} \n\n'.format(len(schedule.courses), filter[1]),
                            'Here are the first 10:', filtered_times]
                        elif filter[1]=='' and filter[2]!='':
                            res = ['There are {} courses that end at {} \n\n'.format(len(schedule.courses), filter[2]),
                            'Here are the first 10:', filtered_times]
                return render_template('coursetime.html', target = res)
            else:
                return render_template('coursetime.html', target =
                ['Please enter a Start Time, End Time, Days, or all above',  'start times: ',
                sorted(starttimes), 'end times:', sorted(endtimes)])
        else:
            return render_template('coursetime.html', target =
            ['Please enter a Start Time, End Time, Days, or all above', 'start times: ',
            sorted(starttimes), 'end times:', sorted(endtimes)])
    #COURSENUM
    elif command in ['c', 'course']:
        if filter!='':
            schedule = schedule.coursenum(filter).sort('coursenum')
            filtered_courses = render_list()
            if len(filtered_courses)==0:
                res = ['{} is not a supported filter :('.format(filter)]
            else:
                res = ['There are {} courses with the number {}\n\n'.format(len(schedule.courses), filter), filtered_courses]
            return render_template('results.html', target = res)
        else:
            return render_template('results.html', target=
            ['Please choose from the following list and re-enter it above with the (course or c) command:', courses])
    #INSTRUCTOR
    elif command in ['i', 'instructor']:
        if filter!='':
            schedule = schedule.instructor(filter).sort('instructor')
            filtered_instructor = render_list()
            if len(filtered_instructor) == 0:
                res = ['{} is not a supported filter :('.format(filter)]
            else:
                res = ['There are {} courses in the term {} \n\n'.format(len(schedule.courses),
                 filter), 'Here are the first 10:', filtered_instructor]
            return render_template('results.html', target = res)
        else:
            return render_template('results.html', target =
            ['Please choose from the following list and re-enter it above with the (instructor or i) command(s):', instructor])
    #DESCRIPTION
    elif command in ['d', 'description']:
        if filter!='':
            schedule = schedule.description(filter).sort('description')
            filtered_description = render_list()
            if len(filtered_description) == 0:
                res = ['{} is not a supported filter :('.format(filter)]
            else:
                res = ['There are {} courses in the term {} \n\n'.format(len(schedule.courses),
                 filter), 'Here are the first 10:', filtered_description]
            return render_template('results.html', target = res)
        else:
            return render_template('results.html', target =
            ['Please choose from the following list and re-enter it above with the (description or d) command(s):', description])

    else:
        return render_template('results.html', target = ['{} is not supported as a command :('.format(command)])

if __name__ == '__main__':
    topmenu()
