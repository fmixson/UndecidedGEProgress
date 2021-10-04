from Degree_Applicable_Electives import DegreeApplicableUnits
from Degree_Completion_Report import DegreeCompletionReport
from GE_Progress import GEProgress
from GE_Requirements import GeRequirements
from Major_Progress import MajorProgress
from Major_Requirements import MajorRequirements
from Student_Info import StudentInfo
from Major_Courses_Report import MajorCompletionReport
from GE_Courses_Report import GECompletionReport
# from main import enrollment_history


def planb_processing(student_id, courses, major_name, major_course_requirements, **kwargs):
    planb_ge_requirements = {'Oral_Comm': 0, 'Writ_Comm': 0, 'Crit_Think': 0, 'Phys_Sci': 0, 'Bio_Sci': 0, 'Sci_Labs': 0,
                             'Math': 0,'Arts': 0, 'Hum': 0, 'Arts_Hum': 0, 'Amer_Hist': 0, 'Amer_Gov': 0,
                             'Institutions': 0, 'Self_Dev': 0}

    student = StudentInfo(student_id, courses)
    student.eligible_course_list()
    ge_requirements = GeRequirements(student.degree_applicable_dict, ge_plan='PlanB_GE.csv')
    ge_dataframe = ge_requirements.dataframe()
    ge_requirements.ge_courses_completed('Oral_Comm', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Writ_Comm', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Crit_Think', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Phys_Sci', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Bio_Sci', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Sci_Labs', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Math', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Arts', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Hum', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Arts_Hum', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Amer_Hist', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Amer_Gov', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Institutions', ge_dataframe=ge_dataframe)
    ge_requirements.ge_courses_completed('Self_Dev', ge_dataframe=ge_dataframe)

    ge_progress = GEProgress(ge_requirements.completed_ge_courses, ge_requirements.completed_ge_units,
                                student_id, ge_plan_requirements=planb_ge_requirements)
    missing_ge_courses, completed_ge_courses, completed_ge_units = ge_progress.ge_requirements_completed()

    # ge_report = GECompletionReport(student_id, completed_ge_courses=completed_ge_courses,
    #                                missing_ge_courses=missing_ge_courses,completed_ge_units=completed_ge_units)
    # GE_Progress_df = ge_report.ge_completion()
    major = MajorRequirements(revised_course_list=student.degree_applicable_dict,
                              completed_ge_courses=ge_requirements.completed_ge_courses,
                              major_requirements=major_course_requirements,
                              major_name=major_name)

    if len(kwargs) == 15:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_courses_completed(area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])
        major.major_courses_completed(area_name=kwargs['major4'], total_units=kwargs['major4_units'],
                                      number_of_disciplines=kwargs['major4_disciplines'])
        major.major_courses_completed(area_name=kwargs['major5'], total_units=kwargs['major5_units'],
                                      number_of_disciplines=kwargs['major5_disciplines'])

    if len(kwargs) == 12:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_courses_completed(area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])
        major.major_courses_completed(area_name=kwargs['major4'], total_units=kwargs['major4_units'],
                                      number_of_disciplines=kwargs['major4_disciplines'])

    elif len(kwargs) == 9:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_courses_completed(area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])

    elif len(kwargs) == 6:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])

    elif len(kwargs) == 3:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])

    major_progress = MajorProgress(student_id=student.student_id,
                                 major_course_dict=major.major_course_dict,
                                 major_units_required=major.major_num_of_units_dict,
                                 area_units=major.area_units_dict,
                                 num_of_courses_required=major.major_num_of_courses_dict)

    missing_courses_dict = major_progress.major_num_of_courses()
    missing_units_dict = major_progress.major_num_of_units()

    # majors_report = MajorCompletionReport(student_id=student_id, major=major_name, missing_courses_dict=missing_courses_dict,
    #                                       missing_units_dict=missing_units_dict, major_course_dict=major.major_course_dict,
    #                                       major_units_dict=major.area_units_dict,
    #                                       major_units_list=major.major_units_list,
    #                                       dataframe=GE_Progress_df)
    # majors_report.major_completion()
    degree_app = DegreeApplicableUnits(student_id=student_id,
                                       degree_applicable_dict=student.degree_applicable_dict,
                                       major_courses_list=major.major_courses_list,
                                       completed_ge_courses=ge_requirements.completed_ge_courses,
                                       completed_ge_units=ge_requirements.completed_ge_units,
                                       major_units_list=major.major_units_list)
    elective_units, elective_courses, elective_dict = degree_app.elective_courses()

    degree_completion = DegreeCompletionReport(
        major_requirements_dict=major.major_num_of_units_dict,
        completed_ge_courses=ge_requirements.completed_ge_courses,
        completed_ge_units=ge_requirements.completed_ge_units,
        major_course_dict=major.major_course_dict,
        area_units_dict=major.area_units_dict,
        major_units_list=major.major_units_list,
        student_id=student_id,
        student_major=major_name,
        missing_ge=missing_ge_courses,
        missing_major_courses=missing_courses_dict,
        missing_units_dict=missing_units_dict,
        elective_units=elective_units,
        elective_courses=elective_courses)

    length, missing_major_courses = degree_completion.degree_completion()
    length = degree_completion.degree_status(length=length, missing_major_courses=missing_major_courses)
    degree_completion.unused_courses(length=length, ge_courses=ge_requirements.completed_ge_courses,
                                     major_courses=major.major_courses_list,
                                     elective_courses=degree_app.elective_course_list,
                                     student_course_list=student.degree_applicable_dict)


def sorting_PlanB_majors(enrollment_history, major_name, major_course_requirements, **kwargs):
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
        print(major_name)
        planb_processing(student_id=student_id, courses=enrollment_history, major_name=major_name,
                         major_course_requirements=major_course_requirements, **kwargs)