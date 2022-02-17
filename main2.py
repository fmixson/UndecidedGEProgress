from easygui import fileopenbox
from Enrollment_History_Dataframe import EnrollmentHistoryDataFrame

planAList = ['Math_Proficiency', 'Writing_Proficiency', 'Reading_Proficiency', 'Health_Proficiency', 'Nat_Sci', 'Soc_Sci',
             'Beh_Sci', 'FA_Hum', 'Comp', 'Analytic,Electives']
Plan_B_list = ['Oral_Comm', 'Writ_Comm', 'Crit_Think', 'Phys_Sci', 'Bio_Sci', 'Sci_Labs', 'Math', 'Arts', 'Hum', 'Arts_Hum',
               'Amer_Hist', 'Amer_Gov', 'Institutions', 'Self_Dev']
Plan_B_list_21 = ['Oral_Comm', 'Writ_Comm', 'Crit_Think', 'Phys_Sci', 'Bio_Sci', 'Sci_Labs', 'Math', 'Arts', 'Hum', 'Arts_Hum',
               'Amer_Hist_Gov', 'Institutions', 'Self_Dev', 'Ethnic_Stds']
Plan_C_list = ['Comp', 'Crit_Think', 'Oral_Comm', 'Math', 'Arts', 'Hum', 'Arts_Hum', 'Soc_Behav1', 'Soc_Behav2', 'Soc_Behav3',
               'Phys_Sci', 'Bio_Sci', 'Sci_Labs']

enrollment_history_file = fileopenbox('Upload Ernollment Histories', filetypes='*.csv')
e = EnrollmentHistoryDataFrame(enrollment_history_file=enrollment_history_file)
enrollment_history_df = e.create_dataframe()