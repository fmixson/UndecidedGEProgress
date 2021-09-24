import pandas
import pandas as pd
# from PlanA_Process import sorting_PlanA_majors
# from PlanB_Process import sorting_PlanB_majors
from PlanC_Process import sorting_PlanC_majors
from Degree_Completion_Report import DegreeCompletionReport
# from Major_Courses_Report import MajorCompletionReport
from GE_Courses_Report import GECompletionReport

pd.set_option('display.max_columns', None)
student_id_and_major = pd.read_csv(
    "C:/Users/fmixson/Desktop/Programming/Major/Exploratory and Discovery LCP High Unit Counts.csv")
print('Student ID and Major', student_id_and_major)

id_and_major_dict = {}

for i in range(len(student_id_and_major)):
    id_and_major_dict[student_id_and_major.loc[i, "ID"]] = student_id_and_major.loc[i, "Major"]


enrollment_history = pd.read_csv(
    "C:/Users/fmixson/Desktop/Programming/Enrollment_Histories/Enrollment History_20210913_ExpDisc.csv")
enrollment_history.sort_values(['ID'], inplace=True)
enrollment_history.replace(to_replace="SPCH",
                           value="COMM", inplace=True)
enrollment_history['Class Subject'] = enrollment_history['Class Subject'].str.strip()
enrollment_history['Class Catalog Number'] = enrollment_history['Class Catalog Number'].str.strip()
enrollment_history['Course'] = enrollment_history['Class Subject'] + " " + enrollment_history['Class Catalog Number']
enrollment_history['Class Catalog Number'] = enrollment_history['Class Catalog Number'].fillna(0)
nona_enrollment_history = enrollment_history[enrollment_history['Official Grade'].notna()]
nona_enrollment_history = nona_enrollment_history.reset_index(drop=True)
enrollment_history = nona_enrollment_history
pandas.set_option('display.max_rows', None)
# print(enrollment_history)

# enrollment_history = nona_enrollment_history
# index_W = enrollment_history[enrollment_history['Official Grade'] == 'W') & enrollment_history['Official Grade'] == 'D'].index
# enrollment_history.drop(index_W, inplace=True)
"""
Create new column then do for loop with if statement. 
if the id in dictionary matches id in dataframe then put the major in the new column.
"""

for i in range(len(enrollment_history)):
    # print(len(enrollment_history), i)
    ID = enrollment_history.loc[i, "ID"]
    if ID in id_and_major_dict.keys():

        enrollment_history.loc[i, "Major"] = id_and_major_dict[ID]
        # print(enrollment_history.loc[i, "Major"])
        if i == len(enrollment_history) - 1:
            print('equal works')
            break
        else:
            if enrollment_history.loc[i, 'ID'] != enrollment_history.loc[i + 1, 'ID']:
                print('break')
                continue


sorting_PlanC_majors(enrollment_history=enrollment_history, major_name="Undecided - AA/Transfer", plan='Plan_C')

GECompletionReport.GE_Progress_df.sort_values(by=['Missing_Num_GE_Courses'], inplace=True, ascending=True)
GECompletionReport.GE_Progress_df.to_csv('C:/Users/fmixson/Desktop/Programming/Undecided_GE.csv')













# sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="Comm Studies for Transfer-AAT",
#                      major_course_requirements='AAT_COMM.csv',
#                      major1='Core', major1_units=3, major1_disciplines=1,
#                      major2='ListA', major2_units=6, major2_disciplines=1,
#                      major3='ListB', major3_units=3, major3_disciplines=1,
#                      major4='ListC', major4_units=3, major4_disciplines=1)
# sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="English for Transfer-AAT",
#                      major_course_requirements='AAT_English.csv',
#                      major1='Core', major1_units=3, major1_disciplines=1,
#                      major2='ListA', major2_units=6, major2_disciplines=1,
#                      major3='ListB', major3_units=6, major3_disciplines=1,
#                      major4='ListC', major4_units=3, major4_disciplines=1)
# sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="Spanish for Transfer-AAT",
#                      major_course_requirements='AAT_Spanish.csv',
#                      major1='Core', major1_units=19, major1_disciplines=1,
#                      major2='ListA', major2_units=3, major2_disciplines=1)
# sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="Communications Studies-AB",
#               major_course_requirements="Comm_AA.csv",
#               major1="Core1", major1_units=3, major1_disciplines=1,
#               major2="Core2", major2_units=3, major2_disciplines=1,
#               major3="ListA", major3_units=6, major3_disciplines=1,
#               major4="ListB", major4_units=6, major4_disciplines=1)
# sorting_PlanC_majors(enrollment_history=enrollment_history, major_name="Communications Studies-AC",
#               major_course_requirements="Comm_AA.csv",
#               major1="Core1", major1_units=3, major1_disciplines=1,
#               major2="Core2", major2_units=3, major2_disciplines=1,
#               major3="ListA", major3_units=6, major3_disciplines=1,
#               major4="ListB", major4_units=6, major4_disciplines=1)
# # sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="Business Administration-AST",
# #                      major_course_requirements='AAT_BusAdmin.csv',
# #                      major1='Core', major1_units=15, major1_disciplines=1,
# #                      major2='ListA', major2_units=3, major2_disciplines=1,
# #                      major3='ListB', major3_units=6, major3_disciplines=1)
# # sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="LAS: Soc Behavioral Sci-AB",
# #                      major_course_requirements='Soc_and_Behav_Sci.csv',
# #                      major1='Core', major1_units=18, major1_disciplines=3)
# # sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="LAS: Self Dev & Soc Beh-AB",
# #                      major_course_requirements='Self_Dev_Soc_Behav.csv',
# #                      major1="Theory_Background", major1_units=6, major1_disciplines=1,
# #                      major2="Stud_Dev_App", major2_units=3, major2_disciplines=1,
# #                      major3="Stud_Vit", major3_units=3, major3_disciplines=1)
# # sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="LAS: Communications-AB",
# #                      major_course_requirements='AS_Comm.csv',
# #                      major1='Comm1', major1_units=3, major1_disciplines=1,
# #                      major2='Comm2', major2_units=3, major2_disciplines=1,
# #                      major3='Crit_Think', major3_units=3, major3_disciplines=1,
# #                      major4='Electives', major4_units=9, major4_disciplines=2)
# sorting_PlanA_majors(enrollment_history=enrollment_history, major_name="Chinese-AA",
#                major_course_requirements='Chin_AA.csv',
#                major1="Core1", major1_units=3, major1_disciplines=1,
#                major2="Core2", major2_units=18, major2_disciplines=1)
# sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="Chinese-AB",
#                major_course_requirements='Chin_AA.csv',
#                major1="Core1", major1_units=3, major1_disciplines=1,
#                major2="Core2", major2_units=18, major2_disciplines=1)
# sorting_PlanC_majors(enrollment_history=enrollment_history, major_name="Chinese-AC",
#                major_course_requirements='Chin_AA.csv',
#                major1="Core1", major1_units=3, major1_disciplines=1,
#                major2="Core2", major2_units=18, major2_disciplines=1)
# # sorting_PlanA_majors(enrollment_history=enrollment_history, major_name="LAS: Soc Behavioral Sci-AA",
# #                      major_course_requirements='Soc_and_Behav_Sci.csv',
# #                      major1='Core', major1_units=18, major1_disciplines=3)
# sorting_PlanA_majors(enrollment_history=enrollment_history, major_name="English-AA",
#                major_course_requirements='English_AA.csv',
#                major1="Core1", major1_units=4, major1_disciplines=1,
#                major2="Core2", major2_units=3, major2_disciplines=1,
#                major3="Lit", major3_units=12, major3_disciplines=1)
# sorting_PlanA_majors(enrollment_history=enrollment_history, major_name="American Sign Language-AA",
#                major_course_requirements='ASL_AA.csv',
#                major1="Core", major1_units=19, major1_disciplines=1,
#                major2="ListA", major2_units=3, major2_disciplines=1)
# sorting_PlanB_majors(enrollment_history=enrollment_history, major_name="American Sign Language-AB",
#                major_course_requirements='ASL_AA.csv',
#                major1="Core", major1_units=19, major1_disciplines=1,
#                major2="ListA", major2_units=3, major2_disciplines=1)
# sorting_PlanC_majors(enrollment_history=enrollment_history, major_name="American Sign Language-AC",
#                major_course_requirements='ASL_AA.csv',
#                major1="Core", major1_units=19, major1_disciplines=1,
#                major2="ListA", major2_units=3, major2_disciplines=1)
# sorting_PlanA_majors(enrollment_history=enrollment_history, major_name="English/Tran-AA",
#                major_course_requirements='English_AA.csv',
#                major1="Core1", major1_units=4, major1_disciplines=1,
#                major2="Core2", major2_units=3, major2_disciplines=1,
#                major3="Lit", major3_units=12, major3_disciplines=1)
# sorting_PlanA_majors(enrollment_history=enrollment_history, major_name="French-AA",
#                major_course_requirements='Fren_AA.csv',
#                major1="Core", major1_units=26, major1_disciplines=1)
# sorting_PlanA_majors(enrollment_history=enrollment_history, major_name="Communications Studies-AA",
#               major_course_requirements="Comm_AA.csv",
#               major1="Core1", major1_units=3, major1_disciplines=1,
#               major2="Core2", major2_units=3, major2_disciplines=1,
#               major3="ListA", major3_units=6, major3_disciplines=1,
#               major4="ListB", major4_units=6, major4_disciplines=1)
#
#
# # pd.set_option('display.max_columns', None)
# #
# # student_course_list = pd.read_csv(
# #     "C:/Users/fmixson/Desktop/Programming/Enrollment_Histories/EnrollmentHistory_20210817.csv")
# #
# # student_id_list = []
# #
# # for i in range(len(student_course_list)):
# #     if student_course_list.loc[i, "ID"] not in student_id_list:
# #         student_id_list.append(student_course_list.loc[i, "ID"])
# # # print(student_id_list)
# # for student_id in student_id_list:
# #
# #     AAT_degree_processing(student_id=student_id, courses=student_course_list, major='comm_major_requirements',
# #                           major_name="COMM_AAT", major_course_requirements='AAT_COMM.csv',
# #                           major1='Core', major1_units=3, major1_disciplines=1,
# #                           major2='ListA', major2_units=6, major2_disciplines=1,
# #                           major3='ListB', major3_units=3, major3_disciplines=1,
# #                           major4='ListC', major4_units=3, major4_disciplines=1)
# #
# #     AAT_degree_processing(student_id=student_id, courses=student_course_list, major='english_major_requirements',
# #                           major_name="English_AAT", major_course_requirements='AAT_English.csv',
# #                           major1='Core', major1_units=3, major1_disciplines=1,
# #                           major2='ListA', major2_units=6, major2_disciplines=1,
# #                           major3='ListB', major3_units=6, major3_disciplines=1,
# #                           major4='ListC', major4_units=3, major4_disciplines=1)
# #     #
# #     AAT_degree_processing(student_id=student_id, courses=student_course_list, major='spanish_major_requirements',
# #                           major_name="Spanish_AAT", major_course_requirements='AAT_Spanish.csv',
# #                           major1='Core', major1_units=19, major1_disciplines=1,
# #                           major2='ListA', major2_units=3, major2_disciplines=1)

