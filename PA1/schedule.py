'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json


class Schedule:
    """
    Schedule represent a list of Brandeis classes with operations for filtering
    """

    #TODO implement lower casing and normalization on the comparison
    
    def __init__(self, courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        """ load_courses reads the course data from the courses.json file"""
        print('getting archived regdata from file')
        with open("pa1_data/courses20-21.json", "r", encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = list(courses)  # making it a tuple means it is immutable

    def lastname(self, name):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in name])

    def class_start_time(self, starttime):
        ''' returns the courses by a particular course time '''
        res = []
        for course in self.courses:
            for time_frame in course['times']:
                if int(starttime)==time_frame['start']:
                    res.append(course)
        return Schedule(res)

    def get_all_start_times(self):
        res = []
        for course in self.courses:
            for time_frame in course['times']:
                res.append(time_frame['start'])
        return res

    def class_end_time(self, endtime):
        res = []
        for course in self.courses:
            for time_frame in course['times']:
                if int(endtime)==time_frame['end']:
                    res.append(course)
        
        return Schedule((res))

    def get_all_end_times(self):
        res = []
        for course in self.courses:
            for time_frame in course['times']:
                res.append(time_frame['end'])
        return res

    def class_days(self, days):
        res = []
        for course in self.courses:
            for time_frame in course['times']:
                if set(days).issubset(set(time_frame['days'])):
                    res.append(course)
        return Schedule((res))

    def compare_time_dict(self, times: list, target: list):
        ''' compares a list of time dicts against another given time dict '''
        pass

    def title(self, title):
        ''' returns the courses by a particular course title '''
        return Schedule([course for course in self.courses if course['name'] in title])

    def term(self, term):
        ''' term returns the courses in a particular term '''
        return Schedule([course for course in self.courses if course['term'] in term])

    def enrolled(self, val):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in val])

    def subject(self, subject):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subject])

    def coursenum(self, coursenum):
        ''' coursenum filters the courses by coursenum '''
        return Schedule([course for course in self.courses if course['coursenum']==coursenum])
    
    def description(self, phrase):
        ''' phrase filters the coruses by a certain searching phrase '''
        return Schedule([course for course in self.courses if phrase in course['description']])
    
    def title(set1, titles):
        ''' Returns the courses by a particular course title '''
        return Schedule([course for course in self.courses if course['name'] in titles])
    
    def sort(self, field):
        if field == 'subject':
            return Schedule(sorted(self.courses, key=lambda course: course['subject']))
        elif field == 'term':
            return Schedule(sorted(self.courses, key=lambda course: course['term']))
        elif field == 'title':
            return Schedule(sorted(self.courses, key=lambda course: course['name']))
        elif field == 'coursenum':
            return Schedule(sorted(self.courses, key=lambda course: course['coursenum']))
        #TODO:
        ##HERE IS WHERE TO ADD ADDITIONAL FILTERS FOR THE SORT
        elif field == 'description':
            return Schedule(sorted(self.courses, key=lambda course: course['description']))
        elif field == 'instructor':
            return Schedule(sorted(self.courses, key=lambda course: course['instructor']))


        else:
            raise ValueError("Cannot sort the data set using {}".format(field))
