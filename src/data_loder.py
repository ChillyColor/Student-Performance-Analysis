import numpy as np

def load_student_data(file_path):
    data = np.genfromtxt(
        file_path,
        delimiter=',',
        names=True,
        dtype=None,
        encoding='utf-8'
    )
    student_ids=data['StudentID']
    student_names=data['Name']
    student_marks=np.column_stack((data['Maths'],data['Physics'],data['Chemistry'],data['ComputerScience'],data['English']))
    subject_names = np.array(data.dtype.names[2:])
    return student_ids,student_names,student_marks,subject_names
    