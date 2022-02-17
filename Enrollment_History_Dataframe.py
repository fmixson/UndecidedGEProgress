import pandas as pd


class EnrollmentHistoryDataFrame:

    def __init__(self, enrollment_history_file):
        self.enrollment_history_file = enrollment_history_file



    def create_dataframe(self):
        pd.set_option('display.max_columns', None)
        self.enrollment_history_df = pd.read_csv(self.enrollment_history_file, encoding='Latin')
        self.enrollment_history_df.replace(to_replace="SPCH",
                                   value="COMM", inplace=True)
        self.enrollment_history_df.sort_values(['ID'], inplace=True)
        self.enrollment_history_df['Class Subject'] = self.enrollment_history_df['Class Subject'].str.strip()
        self.enrollment_history_df['Class Catalog Number'] = self.enrollment_history_df['Class Catalog Number'].str.strip()
        self.enrollment_history_df['Course'] = self.enrollment_history_df['Class Subject'] + " " + self.enrollment_history_df['Class Catalog Number']
        self.enrollment_history_df['Class Catalog Number'] = self.enrollment_history_df['Class Catalog Number'].fillna(0)
        self.enrollment_history_df['Enrollment Drop Date'] = self.enrollment_history_df['Enrollment Drop Date'].fillna(0)
        # nona_enrollment_history_df = self.enrollment_history_df[self.enrollment_history_df['Class Subject'].notna()]
        # nona_enrollment_history_df = nona_enrollment_history_df.reset_index(drop=True)
        # self.enrollment_history_df = nona_enrollment_history_df
        return self.enrollment_history_df