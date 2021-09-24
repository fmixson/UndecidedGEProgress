import pandas as pd


class GEProgress:
    """This class determines what ge areas are not completed.
    """
    def __init__(self, completed_ge_courses, completed_ge_units, student_id, ge_plan_requirements):
        self.student_id = student_id
        self.completed_ge_units = completed_ge_units
        self.completed_ge_courses = completed_ge_courses
        self.ge_plan_requirements = ge_plan_requirements
        self.missing_ge_courses = []

    def ge_requirements_completed(self):
        for ge_key in self.ge_plan_requirements:
            if ge_key not in self.completed_ge_courses:
                self.missing_ge_courses.append(ge_key)
        return self.missing_ge_courses, self.completed_ge_courses, self.completed_ge_units# print('missing ge', self.missing_ge_courses)

    # def area_e_requirements_completed(self):
    #     if len(self.completed_ge_courses) == 10:
    #         if sum(self.completed_ge_units) < 18:
    #             self.missing_ge_courses.append('AreaE')
    #     print('missing ge area e', self.missing_ge_courses)
    #     return self.missing_ge_courses


