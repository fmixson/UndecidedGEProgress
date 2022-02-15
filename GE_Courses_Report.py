from collections import Counter

import pandas as pd

class GECompletionReport:
    columns = ['Student_ID', 'GE_Plan', 'GE_Status', 'Total_GE_Units', 'Missing_Num_GE_Courses', 'GE_Courses',
               'Missing_GE_Area(s)', 'Current_Enrollment', 'First_Term', 'All_Courses', 'Passed_Courses']
    GE_Progress_df = pd.DataFrame(columns=columns)
    total_missing = []
    flat_list = []
    def __init__(self, student_id, completed_ge_courses, missing_ge_courses, completed_ge_units, plan, current_enrollment,
                 first_term, all_count, passed_courses):
        self.student_id = student_id
        self.completed_ge_courses = completed_ge_courses
        self.missing_ge_courses = missing_ge_courses
        self.completed_ge_units = completed_ge_units
        self.plan = plan
        self.current_enrollment = current_enrollment
        self.first_term = first_term
        self.all_count = all_count
        self.passed_courses = passed_courses

    def ge_completion(self):
        length = len(GECompletionReport.GE_Progress_df)
        # print(length)
        print('missing ge', self.missing_ge_courses)
        GECompletionReport.GE_Progress_df.loc[length, 'Student_ID'] = self.student_id
        GECompletionReport.GE_Progress_df.loc[length, 'First_Term'] = self.first_term

        total_ge_units = sum(self.completed_ge_units)
        GECompletionReport.GE_Progress_df.loc[length, 'GE_Plan'] = self.plan

        GECompletionReport.GE_Progress_df.loc[length, 'Missing_Num_GE_Courses'] = len(self.missing_ge_courses)
        missing_ge = self.missing_ge_courses

        GECompletionReport.GE_Progress_df.loc[length, 'Missing_GE_Area(s)'] = missing_ge

        ge_courses_list = self.completed_ge_courses.items()
        GECompletionReport.GE_Progress_df.loc[length, 'GE_Courses'] = ge_courses_list
        GECompletionReport.GE_Progress_df.loc[length, 'Current_Enrollment'] = self.current_enrollment
        print('length', length)
        self.all_count = dict(self.all_count)

        print(GECompletionReport.GE_Progress_df)
        print('all count', self.all_count)
        all_count_list = self.all_count.items()
        GECompletionReport.GE_Progress_df.loc[length, 'All_Courses'] = all_count_list
        passed_courses_list = self.passed_courses.items()
        GECompletionReport.GE_Progress_df.loc[length, 'Passed_Courses'] = passed_courses_list

        # print(GECompletionReport.GE_Progress_df)

        return GECompletionReport.GE_Progress_df


    def total_missing_ge(self):
        GECompletionReport.total_missing.append(self.missing_ge_courses)
        print('total missing ge', GECompletionReport.total_missing)
        for item in GECompletionReport.total_missing:
            for i in item:
                GECompletionReport.flat_list.append(i)
        long_count = Counter(GECompletionReport.flat_list)
        print('longcount', long_count)

        # print('flatlist', GECompletionReport.flat_list)
