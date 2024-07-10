def selectData(students):
    return students.loc[students["student_id"] == 101].drop("student_id", axis=1)