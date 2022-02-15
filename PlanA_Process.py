from Degree_Applicable_Electives import DegreeApplicableUnits
from Degree_Completion_Report import DegreeCompletionReport
from GE_Progress import GEProgress
from GE_Requirements import GeRequirements
from Student_Info import StudentInfo
from Student_Info import TermInfo
from Student_Info import CourseInfo
from Student_Info import DisciplineCount
# from Major_Progress import MajorProgress
# from Major_Requirements import MajorRequirements
# from Student_Info import StudentInfo
# from Major_Courses_Report import MajorCompletionReport
from GE_Courses_Report import GECompletionReport
# from main import enrollment_history
from Student_Info import CatalogTerm


def plana_processing(student_id, courses, major_name, plan):
    plana_ge_requirements = {'Math_Proficiency': 0, 'Writing_Proficiency': 0, 'Reading_Proficiency': 0,
                          'Health_Proficiency': 0, 'Nat_Sci': 0,
                          'Soc_Sci': 0, 'FA_Hum': 0, 'Comp': 0, 'Analytic': 0}

    student = StudentInfo(student_id, courses)
    eligible_course_list = student.eligible_course_list()
    term = TermInfo(student_id, courses)
    semester = term.first_term()
    tc = CatalogTerm(student_id, courses)
    tc.calculate_catalog_term()
    course = CourseInfo(student_id, courses)
    enrolled_courses = course.current_courses()
    c = DisciplineCount(student_id, courses, passed_courses=eligible_course_list)
    all_courses = c.all_courses()
    eligible_courses = c.completed_courses()
    ge_requirements = GeRequirements(student.degree_applicable_dict, ge_plan='PlanA_GE.csv')
    ge_dataframe = ge_requirements.dataframe()
    ge_requirements.ge_courses_completed('Math_Proficiency', ge_dataframe)
    ge_requirements.ge_courses_completed('Writing_Proficiency', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Health_Proficiency', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Reading_Proficiency', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Nat_Sci', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Soc_Sci', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Beh_Sci', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('FA_Hum', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Comp', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Analytic', ge_dataframe=ge_dataframe)
    ge_requirements.area_e_ge_requirements(ge_dataframe=ge_dataframe)
    ge_requirements.reading_proficiency()
    ge_progress = GEProgress(ge_requirements.completed_ge_courses, ge_requirements.completed_ge_units,
                                student_id, ge_plan_requirements=plana_ge_requirements)
    missing_ge_courses, completed_ge_courses, completed_ge_units = ge_progress.ge_requirements_completed()

    ge_report = GECompletionReport(student_id, completed_ge_courses=completed_ge_courses,
                                    missing_ge_courses=missing_ge_courses,completed_ge_units=completed_ge_units, plan=plan,
                                    current_enrollment=enrolled_courses,
                                    first_term=semester,
                                    all_count=all_courses,
                                   passed_courses=eligible_courses)
    GE_Progress_df = ge_report.ge_completion()
    ge_report.total_missing_ge()

    degree_completion = DegreeCompletionReport(
        completed_ge_courses=ge_requirements.completed_ge_courses,
        completed_ge_units=ge_requirements.completed_ge_units,
        student_id=student_id,
        student_major=major_name,
        missing_ge=missing_ge_courses,
        all_count=all_courses,
        passed_courses=eligible_courses)


def sorting_PlanA_majors(enrollment_history, major_name, plan):
    student_id_list = []

    for i in range(len(enrollment_history)):
        """This for loop creates a list of ids for each major identified in major name. If the id is not in the list
        and the major listed for the student in the dataframe matches the major in major_name, the the id is included
        in the list."""
        if enrollment_history.loc[i, "ID"] not in student_id_list:
            # print('major in sorting majors', major_name)
            if enrollment_history.loc[i, "Major"] == major_name:
                student_id_list.append(enrollment_history.loc[i, "ID"])

    for student_id in student_id_list:
        """This for loop takes the list of students with a particular major and runs it through the AAT program.
        """
        # print(major_name)
        plana_processing(student_id=student_id, courses=enrollment_history, major_name=major_name, plan=plan)