from src.data_loder import *
from src.analysis import *
import numpy as np

student_ids,student_names,student_marks,subject_names= load_student_data("data/student_marks.csv")
print("========================================")
print("STUDENT PERFORMANCE ANALYTICS")
print("========================================")
print(f"Total Students: {student_marks.shape[0]}")
print(f"Total Subjects: {student_marks.shape[1]}")
print("--------------- CLASS STATISTICS ---------------")
print(f"Class Average: {np.round(calculateOverallAverage(student_marks),2)}")
print(f"Highest Marks: {calculateHighestTotalMarks(student_marks)}")
print(f"Lowest Marks: {calculateLowestTotalMarks(student_marks)}")
print("--------------- TOPPER DETAILS -----------------")
topperIdx=findTopper(student_marks)
topperMarks,avgTopperMarks=calculateTopperMarks(student_marks,topperIdx)
difficultSubIdx=findMostDifficultSubject(student_marks)
easySubjectIdx=findEasiestSubject(student_marks)
print(f"Topper: {student_names[topperIdx]}")
print(f"Topper Marks: {topperMarks}")
print(f"Topper Average Marks: {avgTopperMarks}")
print("--------------- SUBJECT ANALYSIS ---------------")
for i in range (0,len(subject_names)):
    print(f"{subject_names[i]} Average: {np.round(np.mean(student_marks[:,i],axis=0),2)}")
print()
print(f"Most Difficult Subject: {subject_names[difficultSubIdx]}")
print(f"Easiest Subject: {subject_names[easySubjectIdx]}")
print("--------------- PERFORMANCE --------------------")
studentsAboveAvg=findAboveAverage(student_marks)
faild=findFailedInAtleastOneSubject(student_marks,35)
studentsPassed=findStudentPassedAllSubjects(student_marks)
print(f"Students Above Class Average: {studentsAboveAvg.size}")
print(f"Students Failed: {faild.size}")
print(f"Students Passed All Subjects: {studentsPassed.size}")
print("--------------- GRADE DISTRIBUTION --------------")
grade,percentage=calculateGradePercentage(student_marks)
for i in range(0,len(grade)):
    print(f"{grade[i]}: {np.round(percentage[i],2)}")
    


