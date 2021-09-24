import pandas as pd

class GECompletionReport:
    columns = ['Student_ID', 'GE_Plan', 'GE_Status', 'Total_GE_Units', 'Missing_Num_GE_Courses', 'GE_Courses',
               'Missing_GE_Area(s)']
    GE_Progress_df = pd.DataFrame(columns=columns)

    def __init__(self, student_id, completed_ge_courses, missing_ge_courses, completed_ge_units, plan):
        self.student_id = student_id
        self.completed_ge_courses = completed_ge_courses
        self.missing_ge_courses = missing_ge_courses
        self.completed_ge_units = completed_ge_units
        self.plan = plan

    def ge_completion(self):
        length = len(GECompletionReport.GE_Progress_df)
        print(length)
        print('compl ge', self.completed_ge_courses)
        GECompletionReport.GE_Progress_df.loc[length, 'Student_ID'] = self.student_id

        total_ge_units = sum(self.completed_ge_units)
        GECompletionReport.GE_Progress_df.loc[length, 'GE_Plan'] = self.plan

        GECompletionReport.GE_Progress_df.loc[length, 'Missing_Num_GE_Courses'] = len(self.missing_ge_courses)
        missing_ge = self.missing_ge_courses

        GECompletionReport.GE_Progress_df.loc[length, 'Missing_GE_Area(s)'] = missing_ge

        ge_courses_list = self.completed_ge_courses.items()
        GECompletionReport.GE_Progress_df.loc[length, 'GE_Courses'] = ge_courses_list

        print(GECompletionReport.GE_Progress_df)

        return GECompletionReport.GE_Progress_df



