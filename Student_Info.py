from collections import Counter
class StudentInfo:
    ineligible_courses = ['MATH 80A', 'MATH 60', 'ENGL 72', 'ENGL 52', 'ACLR 90', 'ACLR 91', 'ACLR 92', 'CHEM 95A',
                          'CHEM 95B', 'CHEM 95C', 'CHEM 95D', 'CHEM 95E', 'CHEM 95F', 'LIBR 50', 'LAW 98', 'LAW 99',
                          'BCOT 5A']
    ineligible_numbers = ['21A', '21B', '5A', '18.1', '3T', '1T', '6T', '42.07', '42.05']
    eligible_course_numbers1 = ['5L']
    eligible_course_numbers3 = ['5']
    eligible_course_numbers2 = ['40L', '50B', '50C', '51A', '51B', '51C', '52A', '52B', '52C', '62B', '71C', '60A', '62A',
                                '70A', '71A', '71B', '60L', '50A', '54A', '61A', '70C', '60B', '61B', '80B']
    eligible_grades = ['A', 'B', 'C', 'P']

    def __init__(self, student_id, courses):
        # self.major = major
        self.student_id = student_id
        self.courses = courses
        self.degree_applicable_dict = {}

    def eligible_course_list(self):
        for i in range(len(self.courses)):
            # print('course', self.courses)


            if self.student_id == self.courses.loc[i, "ID"]:
                if self.courses.loc[i, "Class Subject"] != "AED":
                    if self.courses.loc[i, "Course"] not in StudentInfo.ineligible_courses:
                        if self.courses.loc[i, "Class Catalog Number"] not in StudentInfo.ineligible_numbers:
                            course_number = self.courses.loc[i, "Class Catalog Number"]
                            if self.courses.loc[
                                i, 'Class Catalog Number'] in StudentInfo.eligible_course_numbers1:
                                course_number = course_number[0:1]
                            if self.courses.loc[
                                i, 'Class Catalog Number'] in StudentInfo.eligible_course_numbers2:
                                course_number = course_number[0:2]
                            else:
                                if len(str(course_number)) > 3:
                                    course_number = course_number[0:3]
                            if course_number == "5L" or course_number == '5':
                                self.degree_applicable_dict[self.courses.loc[i, "Course"]] = \
                                    self.courses.loc[i, "Units"]
                            else:
                                try:
                                    if int(course_number) >= 100:
                                        if self.courses.loc[i, 'Official Grade'] in StudentInfo.eligible_grades:
                                            self.degree_applicable_dict[
                                                self.courses.loc[i, "Course"]] = \
                                                self.courses.loc[i, "Units"]
                                except:
                                    continue
        return self.degree_applicable_dict

class CourseInfo(StudentInfo):

    def current_courses(self):
        current_term = 1219
        self.enrolled_courses = []

        for i in range(len(self.courses)):
            if self.student_id == self.courses.loc[i, "ID"]:
                if self.courses.loc[i, "Term"] == current_term:
                    if self.courses.loc[i, "Course"] not in self.enrolled_courses:
                        if self.courses.loc[i, 'Enrollment Drop Date'] == 0:
                            self.enrolled_courses.append(self.courses.loc[i, "Course"])
        return self.enrolled_courses

class CatalogTerm(StudentInfo):
    term_list = []
    previous_term = 0
    catalog_term = 0
    def calculate_catalog_term(self):
        for i in range(len(self.courses)):
            if self.student_id == self.courses.loc[i, 'ID']:
                if self.courses.loc[i, 'Term'] not in CatalogTerm.term_list:
                    CatalogTerm.term_list.append(self.courses.loc[i, 'Term'])
                    CatalogTerm.term_list.sort()
                    print(CatalogTerm.term_list)

        for term in CatalogTerm.term_list:
            print('prev term', CatalogTerm.previous_term)
            print('term', term)
            term_difference = term - CatalogTerm.previous_term

            print('difference', term_difference)
            if term_difference > 10:
                CatalogTerm.catalog_term = term
            CatalogTerm.previous_term = term
            print('catalog term', CatalogTerm.catalog_term)




class TermInfo(StudentInfo):

    def first_term(self):
        current_term = 1219
        semester = ''
        for i in range(len(self.courses)):
            if self.student_id == self.courses.loc[i, "ID"]:
                if self.courses.loc[i, 'Term'] != 800:
                    if self.courses.loc[i, 'Term'] <= current_term:
                        current_term = self.courses.loc[i, 'Term']
                        semester = self.courses.loc[i, 'Term Description']
        return semester



class DisciplineCount:

    def __init__(self, student_id, courses, passed_courses):
        self.student_id = student_id
        self.courses = courses
        self.passed_courses = passed_courses
        self.course_list = []
        self.trimmed_list = []
        self.trimmed_list_completed = []


    def all_courses(self):
        for i in range(len(self.courses)):
            if self.student_id == self.courses.loc[i, "ID"]:
                if self.courses.loc[i, "Course"] not in self.course_list:
                    self.course_list.append(self.courses.loc[i, 'Course'])

        for item in self.course_list:
                    splice = item.split()
                    discipline = splice[0]
                    self.trimmed_list.append(discipline)

        all_discipline_count = Counter(self.trimmed_list)
        return all_discipline_count

    def completed_courses(self):

        for item in self.passed_courses:
                    splice = item.split()
                    discipline = splice[0]
                    self.trimmed_list_completed.append(discipline)

        completed_discipline_count = Counter(self.trimmed_list_completed)
        return completed_discipline_count
